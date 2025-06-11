from fastapi import APIRouter
from app.tasks import launch_script_task
from app.schemas import TaskParams

router = APIRouter()

@router.post("/launch-task")
def launch_task(params: TaskParams):
    task = launch_script_task.delay(params.dict())
    return {"task_id": task.id, "status": "Task submitted"}