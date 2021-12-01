import argparse
from DiamondCatalogDataset import DiamondCatalogDataset
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable
from torchvision.utils import save_image
from get_latest_model import get_latest_model
# from azureml.core import Run


# command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--catalog_path', type=str, help='Path to the training data', default="../scraping/data/diamonds_catalog.csv")
parser.add_argument('--data_path', type=str, help='Path to the training data', default="../scraping/data/square")
args = parser.parse_args()
# run = Run.get_context()



# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')



# some hyperparameters
BATCH_SIZE = 64
NOISE_DIM = 64
EPOCHS = 50
LEARNING_RATE = 0.0002
loss_function = nn.BCELoss()
SNAPSHOT = 1 # save the model after every # of epochs


# load the data
# Azure can store files in the outputs/ directory
CATALOG_PATH = args.catalog_path
TRAIN_DATA_PATH = args.data_path
MODEL_BASE_PATH = "./outputs/"
SNAPSHOT_BASE_PATH = "./outputs/"
# TRANSFORM_IMG = transforms.Compose([
#     transforms.Resize(256),
#     # transforms.CenterCrop(256),
#     transforms.ToTensor(),
#     transforms.Normalize(
#         mean=[0.485, 0.456, 0.406], # TODO
#         std=[0.229, 0.224, 0.225]
#     )
# ])

train_dataset = DiamondCatalogDataset(csv_file=CATALOG_PATH, root_dir=TRAIN_DATA_PATH) #, transform=TRANSFORM_IMG)
train_data_loader = torch.utils.data.DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)




# define the Generator and Discriminator

class Generator(nn.Module):
    def __init__(self, g_input_dim:int, g_output_image_size:int, g_output_feature_dim:int):
        super(Generator, self).__init__()
        self.fc1 = nn.Linear(g_input_dim, 256)
        self.fc2 = nn.Linear(self.fc1.out_features, self.fc1.out_features*2)
        self.fc3 = nn.Linear(self.fc2.out_features, self.fc2.out_features*2)
        self.fc4 = nn.Linear(self.fc3.out_features, self.fc3.out_features)
        self.fc5 = nn.Linear(self.fc4.out_features, self.fc4.out_features//2)
        self.fc6 = nn.Linear(self.fc5.out_features, g_output_image_size + g_output_feature_dim)

    # forward method
    def forward(self, x):
        x = F.leaky_relu(self.fc1(x), 0.2)
        x = F.leaky_relu(self.fc2(x), 0.2)
        x = F.leaky_relu(self.fc3(x), 0.2)
        x = F.leaky_relu(self.fc4(x), 0.2)
        x = F.leaky_relu(self.fc5(x), 0.2)
        return torch.tanh(self.fc6(x))

class Discriminator(nn.Module):
    def __init__(self, d_input_image_size:int, d_input_feature_dim:int):
        super(Discriminator, self).__init__()
        self.fc1 = nn.Linear(d_input_image_size + d_input_feature_dim, 1024)
        self.fc2 = nn.Linear(self.fc1.out_features, self.fc1.out_features//2)
        self.fc3 = nn.Linear(self.fc2.out_features, self.fc2.out_features//2)
        self.fc4 = nn.Linear(self.fc3.out_features, 1)

    # forward method
    def forward(self, x):
        x = F.leaky_relu(self.fc1(x), 0.2)
        x = F.dropout(x, 0.3)
        x = F.leaky_relu(self.fc2(x), 0.2)
        x = F.dropout(x, 0.3)
        x = F.leaky_relu(self.fc3(x), 0.2)
        x = F.dropout(x, 0.3)
        return torch.sigmoid(self.fc4(x))


# build Generator and Discriminator
FEATURES = ["carat", "clarity", "color", "cut", "price", "shape"] # these are the features we also want to Generator to output
CSV_HEADERS = ["id"] + FEATURES
NUM_FEATURES = len(FEATURES)
image_shape = train_dataset[0]["image"].shape
print("image_shape",image_shape)
image_size = image_shape[0] * image_shape[1] * image_shape[2]
print("image_size", image_size)

G = Generator(
  g_input_dim = NOISE_DIM,
  g_output_image_size = image_size,
  g_output_feature_dim = NUM_FEATURES
).to(device)
D = Discriminator(
  d_input_image_size = image_size,
  d_input_feature_dim = NUM_FEATURES
).to(device)

# used saved models if you have them
saved_G = get_latest_model("g-",MODEL_BASE_PATH)
saved_D = get_latest_model("d-",MODEL_BASE_PATH)
starting_epoch = 1
if len(saved_G["filepath"]) > 0:
    G.load_state_dict(torch.load(saved_G["filepath"]))
    D.load_state_dict(torch.load(saved_D["filepath"]))
    starting_epoch = saved_G["latest_epoch"] + 1
print("EPOCHS", EPOCHS, "starting_epoch", starting_epoch)

# optimizer
G_optimizer = optim.Adam(G.parameters(), lr = LEARNING_RATE)
D_optimizer = optim.Adam(D.parameters(), lr = LEARNING_RATE)


def generate_images(base_path=""):
    with torch.no_grad():
        test_z = Variable(torch.randn(BATCH_SIZE, NOISE_DIM).to(device))
        generated = G(test_z) # generate images
        print(generated)
        print(generated.size())

        image_data = generated[:,0:image_size]
        feature_data = generated[:,image_size:]
        print(image_data.size())
        print(feature_data.size())
        print(feature_data)

        print(image_data.size(0), 3, image_shape[0], image_shape[1])

        save_image(image_data.view(image_data.size(0), 3, image_shape[0], image_shape[1]),base_path+'.png') # save the generated images
        pd.DataFrame(feature_data).to_csv(base_path+'.csv', header=CSV_HEADERS) # save the generated feature


def D_train(batch: dict):
    #=======================Train the discriminator=======================#

    D.zero_grad()

    # train discriminator on real
    x_real = torch.cat((
        batch["image"].view(-1, image_size),
        batch["carat"].view(-1,1),
        batch["clarity"].view(-1,1),
        batch["color"].view(-1,1),
        batch["cut"].view(-1,1),
        batch["price"].view(-1,1),
        batch["shape"].view(-1,1),
    ), 1).float()
    # print("x_real.shape", x_real.shape)
    # print("x_real", x_real[0])
    y_real = torch.ones(BATCH_SIZE, 1) # ones, ie all these are real examples
    x_real, y_real = Variable(x_real.to(device)), Variable(y_real.to(device))

    D_output = D(x_real)
    D_real_loss = loss_function(D_output, y_real)
    # D_real_score = D_output


    # train discriminator on fake
    z = Variable(torch.randn(BATCH_SIZE, NOISE_DIM).to(device))
    x_fake, y_fake = G(z), Variable(torch.zeros(BATCH_SIZE, 1).to(device)) # zeros, ie, all these are fake values

    D_output = D(x_fake)
    D_fake_loss = loss_function(D_output, y_fake)
    # D_fake_score = D_output

    # gradient backprop & optimize ONLY D's parameters
    D_loss = D_real_loss + D_fake_loss
    D_loss.backward()
    D_optimizer.step()

    return  D_loss.data.item()

def G_train():
    #=======================Train the generator=======================#
    G.zero_grad()

    z = Variable(torch.randn(BATCH_SIZE, NOISE_DIM).to(device)) # get noise input
    y = Variable(torch.ones(BATCH_SIZE, 1).to(device)) # ones, ie G wants D to think this is real

    G_output = G(z) # give G input noise
    D_output = D(G_output) # pass the output from G into D
    G_loss = loss_function(D_output, y) # get the loss between the desired D output and the actual D output

    # gradient backprop & optimize ONLY G's parameters
    G_loss.backward()
    G_optimizer.step()

    return G_loss.data.item()

# run epochs
for epoch in range(starting_epoch, EPOCHS+1):
    D_losses, G_losses = [], []

    # run each batch in the data
    for batch_idx, batch in enumerate(train_data_loader):
        batch_size = batch['image'].size()[0]
        print("epoch", epoch, "batch_idx", batch_idx, "batch_size", batch_size)

        # sometimes the input batch size isn't big enough
        # only train the D and G if the batch size is correct
        if batch_size==BATCH_SIZE:
            D_losses.append(D_train(batch))
            G_losses.append(G_train())
            break # debugging

    # after every 10th epoch, save the state of each model
    if epoch%SNAPSHOT == 0:
        filename_base = "-epoch-"+str(epoch)
        torch.save(G.state_dict(), MODEL_BASE_PATH+"/g"+filename_base)
        torch.save(D.state_dict(), MODEL_BASE_PATH+"/d"+filename_base)
    print('epoch', epoch)
    print('loss_d', torch.mean(torch.FloatTensor(D_losses)).item())
    print('loss_g', torch.mean(torch.FloatTensor(G_losses)).item())
    # run.log('loss_d', torch.mean(torch.FloatTensor(D_losses)).item())
    # run.log('loss_g', torch.mean(torch.FloatTensor(G_losses)).item())

    # save full batch of generated images
    generate_images(SNAPSHOT_BASE_PATH+'/sample_' + str(epoch))




# generate a final set of images
generate_images(SNAPSHOT_BASE_PATH+'/sample_final')
