from apscheduler.schedulers.background import BackgroundScheduler
from .utils import scrap


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrap, 'interval', seconds=86400)
    scheduler.start()