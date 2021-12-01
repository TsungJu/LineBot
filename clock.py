# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
import urllib

sched = BlockingScheduler()

@sched.scheduled_job('cron',day_of_week='mon-fri',minute='*/20')
def scheduled_job():
    url = "https://leonardlinebot.herokuapp.com/"
    conn = urllib.request.urlopen(url)

    for key, value in conn.getheaders():
        print(key,value)

sched.start()
