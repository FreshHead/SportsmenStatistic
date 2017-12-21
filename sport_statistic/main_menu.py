from gi.repository import Gtk
from sport_statistic.sportsman_form import SportsmanWindow

# UI elements
menu_bar = Gtk.MenuBar()


def on_add_sportsman_clicked(widget):
    pass


def on_open_sportsman_clicked(widget):
    sportsman_window = SportsmanWindow()
    sportsman_window.show_all()


def on_delete_sportsman_clicked(widget):
    pass


def create_main_menu(area):
    # File menu
    file_menu = Gtk.Menu()
    menu_item_file = Gtk.MenuItem("Файл")
    menu_item_file.set_submenu(file_menu)

    # Menu items
    menu_item_open = Gtk.MenuItem("Открыть")
    file_menu.append(menu_item_open)

    menu_item_exit = Gtk.MenuItem("Выход")
    menu_item_exit.connect("activate", Gtk.main_quit)
    file_menu.append(menu_item_exit)

    # Add file menu to menu bar
    menu_bar.append(menu_item_file)

    # Sportsmen menu
    sportsmen_menu = Gtk.Menu()
    menu_item_sportsmen = Gtk.MenuItem("Спортсмены")
    menu_item_sportsmen.set_submenu(sportsmen_menu)

    menu_item_add_sportsman = Gtk.MenuItem('Добавить спортсмена')
    menu_item_add_sportsman.connect("activate", on_add_sportsman_clicked)
    sportsmen_menu.append(menu_item_add_sportsman)

    menu_item_open_sportsman = Gtk.MenuItem("Открыть данные спортсмена")
    menu_item_open_sportsman.connect("activate", on_open_sportsman_clicked)
    sportsmen_menu.append(menu_item_open_sportsman)

    menu_item_delete_sportsman = Gtk.MenuItem("Удалить данные спортсмена")
    menu_item_delete_sportsman.connect("activate", on_delete_sportsman_clicked)
    sportsmen_menu.append(menu_item_delete_sportsman)

    menu_bar.append(menu_item_sportsmen)

    area.pack_start(menu_bar, False, False, 0)
