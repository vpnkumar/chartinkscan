from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()
from main import main

sched.add_job(main, 'interval', minutes=1)
sched.start()