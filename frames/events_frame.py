import tkinter as tk
from tkinter.messagebox import askyesno
import sys
from db import Event

from .edit_pop import EditPopFrame
import logging

logger = logging.getLogger(__name__)


class EventsFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)

        self.config(highlightbackground="black", highlightthickness=1)

        self.events_frame = tk.Listbox(self)
        self.events_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.events_frame_scrollbar = tk.Scrollbar(root)
        self.events_frame_scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.events_frame.config(yscrollcommand=self.events_frame_scrollbar.set)
        self.events_frame_scrollbar.config(command=self.events_frame.yview)

        self.events_frame.bind('<Delete>', self.on_delete)
        self.events_frame.bind('e', self.on_edit)
        self.idx = 0
        self.last_pk = -1
        self.refresh()
        logger.debug('events frame initialised')

    def refresh(self):
        """
        Can be called programatically
        We check the self.last_pk to see what the lowest ID is so we only query for records higher than that
        TODO: Fix
        """

        self.events_frame.delete(0,tk.END)
        # for elem in self.events_frame.children:
        #     elem.destroy()
        
        if self.last_pk:
            events = self.get_new_records(0)
            for i, ev in enumerate(events):
                self.update_last_pk(ev.pk)
                evstr = self.format_event_string(ev)
                self.events_frame.insert(0, evstr)

            
        # fn=sys._getframe(1).f_code.co_name
        # logger.warning(f'focus called')
        # self.events_frame
        # if self.last_pk:
        #     events = self.get_new_records(self.last_pk)
        #     for i, ev in enumerate(events):
        #         self.update_last_pk(ev.pk)
        #         evstr = self.format_event_string(ev)
        #         self.events_frame.insert(0, evstr)
        # else:
        #     self.events = self.get_last_n_events()
        #     self.last_pk = 0
        #     for i, ev in enumerate(self.events):
        #         self.update_last_pk(ev.pk)
        #         self.idx = i
        #         evstr = self.format_event_string(ev)
        #         self.events_frame.insert(tk.END, evstr)

    def on_delete(self, event=None):
        selected = self.events_frame.curselection()
        if len(selected) != 1:
            return
        
        sel_text = self.events_frame.get(selected[0])
        sel_pk = int(sel_text[1:sel_text.find(']')])

        answer = askyesno(title='Επιβεβαίωση', message='Είσαι σίγουρος ότι θέλεις να το αφεραίσεις?')

        if answer:
            Event.query.delete_one(sel_pk)
            self.events_frame.delete(selected[0])
            self.refresh()

    def on_edit(self, event=None):
        selected = self.events_frame.curselection()
        if len(selected) != 1:
            return
        
        sel_text = self.events_frame.get(selected[0])
        sel_pk = int(sel_text[1:sel_text.find(']')])

        event_object = Event.query.select("*").in_pk(sel_pk).one()

        popup = tk.Toplevel()
        popup.geometry("300x300")
        popup.title("Edit")

        edit_frame = EditPopFrame(popup, event_object)
        edit_frame.pack(fill=tk.BOTH, expand=True)
        
        popup.bind("<Destroy>", lambda evt: self.refresh())
        

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
