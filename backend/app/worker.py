from celery import Celery
from app.core.config import REDIS_URL
celery_app = Celery('my_app', broker=REDIS_URL)
celery_app.autodiscover_tasks(['app'])