# Generative Adversarial Network

## Set Up

1. Create a virutal conda environment
```
conda create --name diamond python=3.8
conda activate diamond
```

2. Install Packages
```
python -m pip install azureml-sdk pandas scikit-image torch torchvision
```

## Running locally
Run ```python gan.py```


## Running on Microsft Azure
I followed this tutorial series to run the script on the Microsoft Azure: https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-1st-experiment-sdk-setup-local. You can follow that tutorial to set up a workplace or 

1. Fill out ```src/create_workspace_template.py``` with your account credentials and run it
2. Run ```src/create_compute.py```
3. Run ```src/upload_data.py```
4. Run ```src/run_gan.py```