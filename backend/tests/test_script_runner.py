from app.services.ccb import ccb
from app.schemas import TaskParams

def test_run_ccb():
    params = TaskParams(param1="foo", param2=1)
    result = ccb(params)
    assert result["result"] == "success"