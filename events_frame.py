import tkinter as tk
from tkinter import Listbox, LEFT, BOTH, RIGHT, END, Scrollbar
import os
from db import Event
import logging
logger = logging.getLogger(__name__)


class EventsFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)

        self.config(highlightbackground="black", highlightthickness=1)

        # ισόρρoπησε το grid
        #self.rowconfigure(tuple(range(4)), weight=1)
        #self.columnconfigure(tuple(range(3)), weight=1)
        #self.rowconfigure(1, weight=2)
        #self.rowconfigure(0, weight=2)
        self.events_frame = Listbox(self)
        self.events_frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.events_frame_scrollbar = Scrollbar(root)
        self.events_frame_scrollbar.pack(side=RIGHT, fill=BOTH)
        self.events_frame.config(yscrollcommand=self.events_frame_scrollbar.set)
        self.events_frame_scrollbar.config(command=self.events_frame.yview)
        self.idx = 0
        self.last_pk = None

    def refresh(self):
        """
        Can be called programatically
        We check the self.last_pk to see what the lowest ID is so we only query for records higher than that
        """
        logger.warning(f'refresh called')
        self.events_frame
        if self.last_pk:
            events = self.get_new_records(self.last_pk)
            for i, ev in enumerate(events):
                evstr = self.format_event_string(ev)
                self.events_frame.insert(0, evstr)
        else:
            self.events = self.get_last_n_events()
            self.last_pk = 0
            for i, ev in enumerate(self.events):
                if self.last_pk < ev.pk:
                    self.last_pk = ev.pk
                self.idx = i
                evstr = self.format_event_string(ev)
                self.events_frame.insert(END, evstr)

    def format_event_string(self, ev:Event) -> str:
        """
        Pretty-format the event row into human-comprehensible data
        """
        #ev_id = ev.id
        evstr = f'[{ev.pk:09}] {ev.event_timestamp.strftime("%Y-%m-%d - %H:%M:%S")} : {ev.employee_name} : {ev.event_description} : {ev.event_result}'
        return evstr

    def get_new_records(self, highest_pk):
        """
        return all records newer than "highest_pk" primary key
        """
        new_events = Event.query.select('*').gt_field('pk', highest_pk).desc()
        return new_events


    def get_last_n_events(self, num_rows=100):
        """
        Return the last n-events in the Events table
        """
        last_events = Event.query.select('*').desc().limit(num_rows)
        return last_events
