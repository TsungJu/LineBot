# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
from linebot.models import TextSendMessage
import urllib.request

from app_core import line_bot_api

sched = BlockingScheduler()

@sched.scheduled_job('cron',day_of_week='tue-fri',minute='*/20')
def scheduled_job():
    url = "https://leonardlinebot.herokuapp.com/"
    conn = urllib.request.urlopen(url)

    for key, value in conn.getheaders():
        print(key,value)

@sched.scheduled_job('cron',day_of_week='wed,fri',hour=18)
def scheduled_get_off_work_notify():
    line_bot_api.push_message('Ueee79758d328394e6a1017520482dec6',TextSendMessage(text='Time to get off work !'))

sched.start()
