from .worker import celery_app
from app.services.ccb import ccb
from app.schemas import TaskParams

@celery_app.task
def launch_script_task(params : dict) -> dict:
    task_params = TaskParams(**params)
    return ccb(task_params)