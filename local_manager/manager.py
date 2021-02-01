import os
import time 
import datetime 
from datetime import datetime

def search():
    pass

def alert(message):
    audio_file="audio-srcs/music_marimba_chord.wav"
    os.system(f"paplay {audio_file} & notify-send '{message}'")

def schedule_alert(event=None, thresh="1"):
    ''' 
    threshold is the value in seconds, before the start of the event
    the type of frequencies are ['day', 'week', 'month', 'annual', 'fleet']
    1) day: alert issued daily 
    2) week: alert issued every week 
    3) fleet: alert issued only once
    4) month: alert issued once every month
    5) annual: alert issued once every year
    '''
    audio_file="audio-srcs/music_marimba_chord.wav" 
    e=event.to_dict()
    # if e['frequency'] in ['week', 'month']:
    #     alert(f"\"{e['name']} occurs every\"{e['frequency']}")
    # elif e['frequency'] in []:
    #     pass

    message = "HELLO WORLD"
    os.system(f'''echo "paplay {audio_file} & notify-send '{message}'" | at 13:34''')
    # os.system(f"notify-send 'alert scheduled for {} event {e['name'] at {e['start']}}'")

    # if type(time) == datetime:

def check_conflict(schedule, event):
    pass

def parse_dt_info(dt_info, freq="week"):
    
    if freq == "day":
        pass  
    elif freq == "week":
        pass 
    elif freq == "month":
        pass 
    elif freq == "annual":
        pass 
    # else 

def validate(dt_string):
    '''
    Made to format the start datetime. Validates the date string. Returns a datetime object if valid, otherwise returns a None object. 
    '''
    return None