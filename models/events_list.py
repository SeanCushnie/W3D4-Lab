from models.event import *
import datetime


event1 = Event(datetime.datetime(2020, 1, 1), "Beyonce", 1000, "Ovo Hydro", "Concert", True)
event2 = Event(datetime.datetime(2021,1,1), "Nickelback", 5, "Ovo Hydro", "Bad Concert", True)

events = [event1, event2]

def add_new_event(event):
    events.append(event)