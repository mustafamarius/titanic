from prefect.deployments import Deployment
from main import train_pipeline # assure-toi que c'est bien le nom exact de ta flow
from prefect.infrastructure import Process



if __name__ == "__main__":
    
    train_pipeline.deploy(
        name="weekly-titanic-train",
        cron="0 6 * * 1",  # chaque lundi à 6h
        work_pool_name="default-agent-pool",
    )