from sport_statistic import Gtk, GObject


class MainMenu(Gtk.MenuBar):
    __gsignals__ = {
        'open-file': (GObject.SIGNAL_RUN_FIRST, None, ()),
        'save-file': (GObject.SIGNAL_RUN_FIRST, None, ()),
        'insert-sportsman': (GObject.SIGNAL_RUN_FIRST, None, ()),
        'update-sportsman': (GObject.SIGNAL_RUN_FIRST, None, ()),
        'delete-sportsman': (GObject.SIGNAL_RUN_FIRST, None, ())
    }

    # UI elements
    def __init__(self, area):
        super().__init__()

        # File menu
        file_menu = Gtk.Menu()
        menu_item_file = Gtk.MenuItem("Файл")
        menu_item_file.set_submenu(file_menu)

        # Menu items
        menu_item_open = Gtk.MenuItem("Открыть")
        menu_item_open.connect("activate", self.on_open)
        file_menu.append(menu_item_open)

        menu_item_save = Gtk.MenuItem("Сохранить")
        menu_item_save.connect("activate", self.on_save)
        file_menu.append(menu_item_save)

        menu_item_exit = Gtk.MenuItem("Выход")
        menu_item_exit.connect("activate", Gtk.main_quit)
        file_menu.append(menu_item_exit)

        # Add file menu to menu bar
        self.append(menu_item_file)

        # Sportsmen menu
        sportsmen_menu = Gtk.Menu()
        menu_item_sportsmen = Gtk.MenuItem("Спортсмены")
        menu_item_sportsmen.set_submenu(sportsmen_menu)

        menu_item_add_sportsman = Gtk.MenuItem('Добавить спортсмена')
        menu_item_add_sportsman.connect("activate", self.on_insert)
        sportsmen_menu.append(menu_item_add_sportsman)

        menu_item_open_sportsman = Gtk.MenuItem("Изменить данные спортсмена")
        menu_item_open_sportsman.connect("activate", self.on_update)
        sportsmen_menu.append(menu_item_open_sportsman)

        menu_item_delete_sportsman = Gtk.MenuItem("Удалить данные спортсмена")
        menu_item_delete_sportsman.connect("activate", self.on_delete)
        sportsmen_menu.append(menu_item_delete_sportsman)

        self.append(menu_item_sportsmen)

        area.pack_start(self, False, False, 0)

    def on_insert(self, widget):
        self.emit('insert-sportsman')

    def on_update(self, widget):
        self.emit('update-sportsman')

    def on_delete(self, widget):
        self.emit('delete-sportsman')

    def on_open(self, widget):
        self.emit('open-file')

    def on_save(self, widget):
        self.emit('save-file')