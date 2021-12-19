# run this model to upload existing models to azure
from azureml.core import Workspace
ws = Workspace.from_config()
datastore = ws.get_default_datastore()
datastore.upload(src_dir='./outputs', target_path='outputs', overwrite=True)
