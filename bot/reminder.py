import os
from datetime import datetime

import pytz
from dotenv import load_dotenv
from flask_apscheduler import APScheduler
from linebot.models import TextSendMessage

from .db import db
from .models import Cancellation, Group
from .handlers import line_bot_api

def start_scheduler(app):
    load_dotenv()
    scheduler = APScheduler()
    timezone = pytz.timezone('Asia/Tokyo')
    scheduler.init_app(app)
    scheduler.scheduler.configure(timezone=timezone)
    scheduler.start()

    @scheduler.task(
        "cron",
        id="reminder",
        day_of_week="sun,tue,thu,sat",
        year="3000",
    )
    def task1():
        with app.app_context():
            todays_day = datetime.now(timezone).weekday()
            option = Cancellation.query.filter_by(day_of_the_week=todays_day)

            if option.count() == 0:
                remindtext = "体温を入力してね" + "\n" + os.environ["SPREADSHEET_URL"]
                pushText = TextSendMessage(text=remindtext)
                for group in Group.query.all():
                    line_bot_api.push_message(to=group.group_id, messages=pushText)
            else:
                db.session.delete(option.first())
                db.session.commit()
                print("deleted")
            print("running task 1!")
