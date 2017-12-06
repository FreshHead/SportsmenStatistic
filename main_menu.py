from gi.repository import Gtk

# UI elements
menu_bar = Gtk.MenuBar()


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

    menu_item_open_sportsmen = Gtk.MenuItem("Открыть данные спортсмена")
    sportsmen_menu.append(menu_item_open_sportsmen)

    menu_bar.append(menu_item_sportsmen)

    area.pack_start(menu_bar, False, False, 0)
