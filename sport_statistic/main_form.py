import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from sport_statistic_lib.sportsmen_mocker import *
from main_menu import MainMenu


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Sportsmen Statistic")
        layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(layout)

        main_menu_area = Gtk.Box()

        people_list_store = Gtk.ListStore(str, str, float, int)

        sm = SportsmenMocker()
        sm.execute()
        self.sportsmen = sm.sportsmen

        for item in self.sportsmen:
            people_list_store.append(item.get_tuple())

        sportsmen_tree_view = Gtk.TreeView(people_list_store)

        for i, col_title in enumerate(["Фамилия", "Код команды", "Колличество баллов", "Место в рейтинге"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # Make column sortable and selectable
            column.set_sort_column_id(i)

            sportsmen_tree_view.append_column(column)

        selected_row = sportsmen_tree_view.get_selection()
        selected_row.connect("changed", self.item_selected)

        layout.pack_start(main_menu_area, False, False, 0)
        layout.pack_start(sportsmen_tree_view, True, True, 0)
        MainMenu(main_menu_area, selected_row)

    @staticmethod
    def item_selected(selection):
        model, row = selection.get_selected()
        if row is not None:
            print("Фамилия: ", model[row][0])
            print("Команда: ", model[row][1])
            print("Баллы: ", model[row][2])
            print("")


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
