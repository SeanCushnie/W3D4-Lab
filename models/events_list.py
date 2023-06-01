from models.event import *
import datetime


event1 = Event(datetime.datetime(2020, 1, 1), "Beyonce", 1000, "Ovo Hydro", "Concert")
event2 = Event(datetime.datetime(2021,1,1), "Nickelback", 5, "Ovo Hydro", "Bad Concert")

events = [event1, event2]