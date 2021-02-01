import os
import json
import time
import argparse
import datetime
from colors import color
from local_manager.exceptions import InvalidScheduleType, InvalidOperationType
from local_manager.models import DailySchedule, WeeklySchedule, MonthlySchedule, HolidaySchedule, DeadlineSchedule, Reminders

# Argument parser (to run it properly as a terminal tool)
parser = argparse.ArgumentParser(description='This is a schedule management and sharing software')
parser.add_argument('--schedule_type', type=str, default='weekly', help="Type of schedule to be updated. Pick from ['daily', 'weekly', 'monthly', 'holidays', 'reminders']")
parser.add_argument('--opcode', type=str, default='show', help="Type of operation to be carried out. Pick from ['add', 'delete', 'show', 'edit']")
parser.add_argument('--datetime_info', type=str, default=None, help="Start time of event (date or time).\nStart time/dates are to be formatted as below.\n() indicates optional arguments. Format for time: "+color("HRS:MINS:(am/pm)", bg='blue')+".\nFormat for date: "+color("DAY:MNTH:YR", bg='blue')+". Format for datetime: "+color("\"DAY:MNTH:YR HRS:MINS:(am/pm)\"", bg='blue'))
parser.add_argument('--name', type=str, default=None, help="Duration of event in hours")
args = parser.parse_args()

# file environment variables
valid_scheds = ['daily', 'weekly', 'monthly', 'holidays', 'reminders']
valid_ops = ['add', 'delete', 'show', 'edit']
db_files = [f"database/{sched}.json" for sched in valid_scheds]

# init json database
try:
    os.mkdir('database')
except FileExistsError:
    pass

for fname in db_files:
    if not os.path.exists(fname):
        with open(fname, "w") as f:
            json.dump({}, f, indent=4)
print(args.schedule_type)
print(args.datetime_info)
print(args.opcode)
print(args.name)

if args.schedule_type not in valid_scheds: 
    raise(InvalidScheduleType(args.schedule_type))
if args.opcode not in valid_ops:
    raise(InvalidOperationType(args.opcode))
