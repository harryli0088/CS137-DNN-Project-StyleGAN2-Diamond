# run this file to run the gan in azure

from azureml.core import Workspace
from azureml.core import Experiment
from azureml.core import Environment
from azureml.core import ScriptRunConfig
from azureml.core import Dataset

if __name__ == "__main__":
    ws = Workspace.from_config()

    datastore = ws.get_default_datastore()
    catalog_path = Dataset.File.from_files(path=(datastore, 'catalog/diamonds_catalog.csv'))
    data_path = Dataset.File.from_files(path=(datastore, 'square'))

    experiment = Experiment(workspace=ws, name='day1-experiment-data')

    config = ScriptRunConfig(
        source_directory='./',
        script='gan.py',
        compute_target='cpu-cluster',
        arguments=[
            '--catalog_path', catalog_path.as_named_input('catalog_path').as_mount(),
            '--data_path', data_path.as_named_input('data_path').as_mount(),
            ]
        )

    # set up pytorch environment
    env = Environment.from_conda_specification(name='pytorch-env',file_path='.azureml/pytorch-env.yml')
    config.run_config.environment = env

    run = experiment.submit(config)
    aml_url = run.get_portal_url()
    print("Submitted to an Azure Machine Learning compute cluster. Click on the link below")
    print("")
    print(aml_url)
