from gi.repository import Gtk

from model import sportsmen
from main_menu import *


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Sportsmen Statistic")
        layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(layout)

        main_menu_area = Gtk.Box()

        people_list_store = Gtk.ListStore(str, str, float, int)

        for item in sportsmen:
            people_list_store.append(list(item))

        people_tree_view = Gtk.TreeView(people_list_store)

        for i, col_title in enumerate(["Фамилия", "Код команды", "Колличество баллов", "Место в рейтинге"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # Make column sortable and selectable
            column.set_sort_column_id(i)

            people_tree_view.append_column(column)

        layout.pack_start(main_menu_area, False, False, 0)
        layout.pack_start(people_tree_view, True, True, 0)
        create_main_menu(main_menu_area)


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
