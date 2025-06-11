from app.tasks import launch_script_task
from app.schemas import TaskParams

def test_launch_task_direct():
    params = TaskParams(param1="foo", param2=1)
    result = launch_script_task.run(params)
    assert result["result"] == "success"