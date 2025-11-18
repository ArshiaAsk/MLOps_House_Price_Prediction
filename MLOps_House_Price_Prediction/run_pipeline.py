import click
from pipelines.training_pipelines import ml_pipeline
from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri

@click.command()
def main():
    
    run = ml_pipeline()
    print("Now run\n"
          f"    mlflow ui --backend-store-uri '{get_tracking_uri() } '\n")
    

if __name__ == "__main__":
    main()