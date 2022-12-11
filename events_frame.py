import tkinter as tk
from tkinter import Listbox, LEFT, BOTH, RIGHT, END, Scrollbar
import sys
from db import Event
import logging
logger = logging.getLogger(__name__)


class EventsFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)

        self.config(highlightbackground="black", highlightthickness=1)

        self.events_frame = Listbox(self)
        self.events_frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.events_frame_scrollbar = Scrollbar(root)
        self.events_frame_scrollbar.pack(side=RIGHT, fill=BOTH)
        self.events_frame.config(yscrollcommand=self.events_frame_scrollbar.set)
        self.events_frame_scrollbar.config(command=self.events_frame.yview)
        self.idx = 0
        self.last_pk = None
        self.refresh()
        logger.debug('events frame initialised')

    def refresh(self):
        """
        Can be called programatically
        We check the self.last_pk to see what the lowest ID is so we only query for records higher than that
        TODO: Fix
        """
        fn=sys._getframe(1).f_code.co_name
        logger.warning(f'focus called')
        self.events_frame
        if self.last_pk:
            events = self.get_new_records(self.last_pk)
            for i, ev in enumerate(events):
                self.update_last_pk(ev.pk)
                evstr = self.format_event_string(ev)
                self.events_frame.insert(0, evstr)
        else:
            self.events = self.get_last_n_events()
            self.last_pk = 0
            for i, ev in enumerate(self.events):
                self.update_last_pk(ev.pk)
                self.idx = i
                evstr = self.format_event_string(ev)
                self.events_frame.insert(END, evstr)

    def update_last_pk(self, pk):
        if self.last_pk < pk:
            self.last_pk = pk

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
        new_events = Event.query.select('*').gt_field('pk', highest_pk)
        return new_events

    def get_last_n_events(self, num_rows=100):
        """
        Return the last n-events in the Events table
        """
        last_events = Event.query.select('*').desc_field('pk').limit(num_rows)
        return last_events
