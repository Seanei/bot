import datetime
import telegram;

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, BaseFilter
from cal_setup import get_calendar_service
import pickle
def update():
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.datetime.utcnow() - datetime.timedelta(hours=int(datetime.datetime.utcnow().hour),days=(int(datetime.datetime.utcnow().weekday())+1))
    end = now + datetime.timedelta(weeks=2)
    now = now.isoformat() + 'Z'  # 'Z' indicates UTC time
    end = end.isoformat() + 'Z'
    events_result = service.events().list(
        calendarId='primary', timeMin=now,
        timeMax=end, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])
    ls = {}
    events1=events[:int(len(events)/2)]
    week = str((int(datetime.datetime.today().strftime("%V"))) % 2)
    for event in events1:
        start = event['start'].get('dateTime', event['start'].get('date'))
        desc = event['description'].split()
        dayOfWeek = event['description'].split()[4][:-1]
        place = desc[desc.index('Lageplan:') + 1: desc.index('Modul:')][0]
        room = ' '.join(desc[desc.index('Raum:') + 1: desc.index('|')])
        if dayOfWeek in ls.keys():
            sched = ls[dayOfWeek] + (start[11:-9] + ', ' + event['summary']) + ', ' + place + ', ' + room + '\n'
            ls[dayOfWeek] = sched
        elif dayOfWeek not in ls.keys():
            ls[dayOfWeek] = (start[11:-9] + ', ' + event['summary']) + ', ' + place + ', ' + room + '\n'
    pickle.dump(ls, open('week'+ str(week)+'.bin', "wb"), 1)
    print(ls)
    events2 = events[int(len(events) / 2):]
    ls = {}
    for event in events2:
        start = event['start'].get('dateTime', event['start'].get('date'))
        desc = event['description'].split()
        dayOfWeek = event['description'].split()[4][:-1]
        place = desc[desc.index('Lageplan:') + 1: desc.index('Modul:')][0]
        room = ' '.join(desc[desc.index('Raum:') + 1: desc.index('|')])

        if dayOfWeek in ls.keys():

            sched = ls[dayOfWeek] + (start[11:-9] + ', ' + event['summary']) + ', ' + place + ', ' + room + '\n'
            ls[dayOfWeek] = sched
        elif dayOfWeek not in ls.keys():
            ls[dayOfWeek] = (start[11:-9] + ', ' + event['summary']) + ', ' + place + ', ' + room + '\n'

    print(ls)
    pickle.dump(ls, open('week'+ str(week)+'.bin', "wb"), 1)

def today():
    week = str((int(datetime.datetime.today().strftime("%V"))+1) % 2)
    ls = pickle.load(open('week'+str(week)+'.bin', "rb"))
    res=datetime.datetime.utcnow().weekday()
    if res > 4:
        res = 'chill'
    else:
        days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        day=days[res]
        res=ls[day]

    return res

def tomorrow():
    week = str((int((datetime.datetime.today()+datetime.timedelta(days=1)).strftime("%V"))) % 2)
    ls = pickle.load(open('week'+str(week)+'.bin', "rb"))
    res=int((datetime.datetime.utcnow()+datetime.timedelta(days=1)).weekday())
    if res > 4:
        res = 'chill'
    else:
        days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        day=days[res]
        res=ls[day]
    return res

def nextweek():
    week = str((int((datetime.datetime.today()+datetime.timedelta(weeks=1)).strftime("%V"))) % 2)

    ls = pickle.load(open('week'+str(week)+'.bin', "rb"))
    res=''
    for i in ls.keys():
        res= res + i + '\n' + ls[i] + '\n'
    return res


def week():
    week = str(int(datetime.datetime.today().strftime("%V")) % 2)

    ls = pickle.load(open('week'+str(week)+'.bin', "rb"))
    res=''
    res=''
    for i in ls.keys():
        res= res + i + '\n' + ls[i] + '\n'

    return res
