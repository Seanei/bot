import datetime
import telegram;

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, BaseFilter
from cal_setup import get_calendar_service
import pickle
def update(now, end):
    service = get_calendar_service()
    # Call the Calendar API
    now = now.isoformat() + 'Z'  # 'Z' indicates UTC time
    end = end.isoformat() + 'Z'
    events_result = service.events().list(
        calendarId='primary', timeMin=now,
        timeMax=end, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])
    ls = {}
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('time'))

        desc = event['description'].split()
        dayOfWeek = event['description'].split()[4][:-1]
        place = desc[desc.index('Lageplan:') + 1: desc.index('Modul:')][0]
        room = ' '.join(desc[desc.index('Raum:') + 1: desc.index('|')])
        if dayOfWeek in ls.keys():
            sched = ls[dayOfWeek] + (start[11:-9] + ', ' + event['summary']) + ', ' + place + ', ' + room + '\n'
            ls[dayOfWeek] = sched
        elif dayOfWeek not in ls.keys():
            ls[dayOfWeek] = (start[11:-9] + ', ' + event['summary']) + ', ' + place + ', ' + room + '\n'
    return ls
def today():
    now = datetime.datetime.utcnow() - datetime.timedelta(hours=int(datetime.datetime.utcnow().hour))
    end = now + datetime.timedelta(days=1)
    ls = update(now, end)

    result = ''
    if len(ls) == 0:
        return 'chill'
    else:
        for i in ls.keys():
            result = i + '\n' + ls[i]
    return result

def tomorrow():
    now = datetime.datetime.utcnow() - datetime.timedelta(hours=int(datetime.datetime.utcnow().hour)) + datetime.timedelta(days=1)
    end = now + datetime.timedelta(days=1)
    ls = update(now, end)

    result = ''
    if len(ls) == 0:
        return 'chill'
    else:
        for i in ls.keys():
            result = i + '\n' + ls[i]
    return result

def nextweek():
    now = datetime.datetime.utcnow() - datetime.timedelta(hours=int(datetime.datetime.utcnow().hour), days=(int(datetime.datetime.utcnow().weekday())+1)) + datetime.timedelta(weeks=1)
    end = now + datetime.timedelta(weeks=1)
    ls = update(now,end)
    result = ''
    for i in ls.keys():
        result =result + i +'\n'+ls[i] + '\n'

    return result


def week():
    now = datetime.datetime.utcnow() - datetime.timedelta(hours=int(datetime.datetime.utcnow().hour),days=(int(datetime.datetime.utcnow().weekday())+1))
    end = now + datetime.timedelta(weeks=1)
    ls=update(now,end)

    result = ''
    for i in ls.keys():
        result = result + i +'\n'+ls[i] + '\n'
    return result
