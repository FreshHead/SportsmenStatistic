from sport_statistic import Gtk
from sport_statistic_lib.sportsmen_mocker import SportsmenMocker


class Model:
    def __init__(self):
        sm = SportsmenMocker()
        sm.execute()
        self.list_store = Gtk.ListStore(str, str, float, int)
        self.populate_list_store(sm.sportsmen_list)

    def populate_list_store(self, list_with_data):
        self.list_store.clear()
        for item in list_with_data:
            self.list_store.append([item[0], item[1], float(item[2]), 0])
        self.calculate_place()

    def append(self, row):
        self.list_store.append([row[0], row[1], float(row[2]), 0])
        self.calculate_place()

    def calculate_place(self):
        self.list_store.set_sort_column_id(2, Gtk.SortType.DESCENDING)
        i = 1
        for row in self.list_store:
            row[3] = i
            i += 1