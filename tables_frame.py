import tkinter as tk
from tkinter import ttk
import random

from constants import LABEL_FONT

GAME_TYPES = (
    "Blackjacjk", 
    "Roulette", 
    "Carribean Style Poker", 
    "Texas Holdem",
    "Mini Pundo Pago"
)

class Table:

    def __init__(self, table_name="t1", game=None):
        self.table_name = table_name
        if game is None:
            game = random.choice(GAME_TYPES)
        self.game = game
        self.pit = 3
        self.minimum_bet = 20
        self.maximum_bet = 40
        self.n_seats = 7
        self.flot = 50000


class TableInfoFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)
        self.columnconfigure(tuple(range(2)), weight=1)

        self.title_label = tk.Label(self, text="Πληροφορίες Τραπεζιού", font=LABEL_FONT)
        self.title_label.grid(row=0, column=0, columnspan=2, sticky=tk.NW, padx=10, pady=10)
        
        self.t_name_label = tk.Label(self, text="Όνομα τραπεζιού:")
        self.t_name_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        
        self.t_game_label = tk.Label(self, text="PIT:")
        self.t_game_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

        self.t_pit_label = tk.Label(self, text="Παιχνίδι:")
        self.t_pit_label.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

        self.t_name_show = tk.Label(self, text="")
        self.t_name_show.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        self.t_pit_show = tk.Label(self, text="")
        self.t_pit_show.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        self.t_game_show = tk.Label(self, text="")
        self.t_game_show.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)


    def show_table(self, table):
        self.t_name_show.config(text=table.table_name)
        self.t_pit_show.config(text=table.pit)
        self.t_game_show.config(text=table.game)


class TableCreateFrame(tk.Frame):

    def __init__(self, root, table_add_func, **options):
        super().__init__(root, **options)

        self.table_add_func = table_add_func

        self.table_name_strvar = tk.StringVar(self)
        self.table_game_strvar = tk.StringVar(self)
        self.table_flot_intvar = tk.IntVar(self)


        self.title_label = tk.Label(self, text="Δημιουργία τραπεζιού", font=LABEL_FONT)
        self.title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky=tk.NW)

        self.tb_label = tk.Label(self, text="Όνομα τραπεζιού:")
        self.tb_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        self.table_name_entry = tk.Entry(self, textvariable=self.table_name_strvar)
        self.table_name_entry.grid(row=1, column=1, padx=5, pady=10, sticky=tk.W)

        self.tt_label = tk.Label(self, text="Τύπος παιχνιδιού:")
        self.tt_label.grid(row=2, column=0, padx=5, pady=10, sticky=tk.EW)

        self.game_type_box = ttk.Combobox(self, values=GAME_TYPES, state="readonly", textvariable=self.table_game_strvar)
        self.game_type_box.current(0)
        self.game_type_box.grid(row=2, column=1, padx=5, pady=10, sticky=tk.EW)

        self.flot_label = tk.Label(self, text="Λεφτά τραπεζιού:")
        self.flot_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

        self.integer_vcmd = (self.register(self.integer_validator))
        self.flot_entry = tk.Entry(self, textvariable=self.table_flot_intvar, validate='all', validatecommand=(self.integer_vcmd, '%P'), justify=tk.RIGHT)
        
        self.flot_entry.grid(row=3, column=1, padx=5, pady=10, sticky=tk.W)

        self.submit_button = tk.Button(self, text="Δημιουργία", command=self.register_table)
        self.submit_button.grid(row=4, column=2, padx=5, pady=10, sticky=tk.NSEW)

    def integer_validator(self, P):
        return str.isdigit(P) or P == ""

    def register_table(self):
        new_table = Table(self.table_name_strvar.get(), self.table_game_strvar.get())

        self.table_add_func(new_table)

class TablesFrame(tk.Frame):

    def __init__(self, root, **options):
        super().__init__(root, **options)

        self.tables = [Table(table_name=f"Table {i}") for i in range(5)]
        self.COLUMN_NAMES = ("Table", "Game")

        self.N_ROWS = 3
        self.N_COLS = 2

        self.rowconfigure(tuple(range(1, self.N_ROWS)), weight=1)
        #self.columnconfigure(tuple(range(self.N_COLS)), weight=1, minsize=200)
        self.columnconfigure(0, weight=3, minsize=300)
        self.columnconfigure(1, weight=1)
        

        self.title_label = tk.Label(self, text="Τραπέζια", font=LABEL_FONT)
        self.title_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NW)

        self.tables_treeview = ttk.Treeview(self, columns=self.COLUMN_NAMES)

        for column in self.COLUMN_NAMES:
            self.tables_treeview.heading(column, text=column)
            self.tables_treeview.column(column, width=1, anchor=tk.W, stretch=True)

        self.tables_treeview.column("#0", width=1, stretch=False)
        self.tables_treeview.grid(row=1, column=0, rowspan=2, sticky=tk.NSEW, padx=10, pady=10)


        for idx, table in enumerate(self.tables):
            self.tables_treeview.insert('', 'end', values=(table.table_name, table.game), iid=idx)


        self.table_info_frame = TableInfoFrame(self)
        self.table_info_frame.grid(row=1, column=1, sticky=tk.NSEW)

        # self.table_info_frame.show_table(self.tables[0])
        self.tables_treeview.bind_class('all', '<Button-1>', self.on_mouse_click)

        self.create_table_frame = TableCreateFrame(self, table_add_func=self.add_table)
        self.create_table_frame.grid(row=2, column=1, sticky=tk.NSEW)

    def on_mouse_click(self, event):
        selected = self.tables_treeview.selection()

        if len(selected) != 1:
            return

        self.table_info_frame.show_table(self.tables[int(selected[0])])

    def add_table(self, table):
        idx = len(self.tables)
        self.tables.append(table)
        self.tables_treeview.insert('', 'end', values=(table.table_name, table.game), iid=idx)


if __name__ == "__main__":
    from single_frame_runner import single_frame_runner

    single_frame_runner(TablesFrame)
  