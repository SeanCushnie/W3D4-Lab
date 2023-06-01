from flask import render_template, request
import datetime
from app import app
from models.events_list import events, add_new_event, remove_event
from models.event import Event

@app.route("/")
def index():
    for item in events:
        names = []
        names.append(item.name_of_event)
    return render_template("index.html", events = events, names = names)

@app.route("/", methods=["Post"])
def add_event():
    event_date = request.form["date"]
    event_name=request.form["name_of_event"]
    event_number_of_guests=request.form["number_of_guests"]
    event_room_location=request.form["room_location"]
    event_description=request.form["description"]
    event_passed = False
    event = Event(event_date, event_name, event_number_of_guests, event_room_location, event_description, event_passed)
    add_new_event(event)
    names = []
    for item in events:
        names.append(item.name_of_event)
    return render_template("index.html", events = events, names = names)

@app.route("/delete/<num>")
def delete_event(num):
    num = int(num)
    event = events[num]
    remove_event(event)
    names = []
    for item in events:
        names.append(item.name_of_event)
    return render_template("index.html", events = events, names = names)