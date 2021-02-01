import json
import time
import datetime 
import prettytable as PT
from datetime import datetime as dt
from local_manager.exceptions import EventExistsError, EventDoesntExistError
# from local_manager.

class Event:
    '''
    Store event info. Frquency of event can be ['']
    '''
    def __init__(self, name, datetime_info, frequency="daily"):
        self.name=name
        self.start=start
        self.frequency=frequency
        self.datetime_info=datetime_info 

    def from_dict(self):
        pass 

    def to_dict(self):
        pass

    def __str__(self):
        return f"{self.type.title()} Event: "

    def __repr__(self):
        return f""

class Schedule:
    def __init__(self, path=None):
        if path:
            self.events=json.load(open(path, "r"))
        else:
            self.events={}
    
    def add(self, name, start, duration):
        e=Event(name, start, duration)
        if name not in self.events:
            self.events[name]=e
        else:
            raise(EventExistsError(e))        

    def edit(self, name, start="", duration=""):
        if name not in self.events:
            raise(EventDoesntExistError)
        if start != "":
            self.events[name].start=start        
        if duration != "":
            self.events[name].duration=duration

    def delete(self, ):
        pass


class DailySchedule(Schedule):
    def __init__(self, name=None):
        Schedule.__init__(self, name)

    def add(self, name, start, duration):
        e=Event(name, start, duration)
        if name not in self.events:
            self.events[name]=e
        else:
            raise(EventExistsError(e))

    def edit(self, name, start, duration):
        e=Event(name, start, duration)
        
    def show(self):
        pass

    def dump(self, path):
        pass
    
    def read(self, path):
        pass

class DeadlineSchedule:
    def __init__(self, name, end):
        self.name=name
        self.end=end
    
    def show(self):
        pass

    def dump(self, path):
        pass 
    
    def read(self, path):
        pass

class WeeklySchedule:
    pass

class MonthlySchedule:
    pass

class HolidaySchedule:
    def __init__(self):
        pass

class Reminders:
    def __init__(self):
        pass 
