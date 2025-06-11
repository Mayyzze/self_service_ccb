import time
import logging
from app.schemas import TaskParams

logger = logging.getLogger("script_runner")
handler = logging.FileHandler("logs/script.log")
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def ccb(params : TaskParams) -> dict:
    params = params.dict()
    logger.info(f"Début de la tâche avec params: {params}")
    time.sleep(15)  # Simulation d'un traitement long
    logger.info("Tâche terminée")
    return {"result": "success", "params": params}