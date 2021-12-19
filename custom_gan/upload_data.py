# run this file to upload all the training data to azure
from azureml.core import Workspace
ws = Workspace.from_config()
datastore = ws.get_default_datastore()
datastore.upload(src_dir='../scraping/data/square', target_path='square', overwrite=True)
datastore.upload_files(['../scraping/data/diamonds_catalog.csv'], target_path='catalog', overwrite=True)
