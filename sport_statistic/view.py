from sport_statistic import Gtk, GObject
from sport_statistic.main_menu import MainMenu


class TreeViewWindow(Gtk.Window):
    def __init__(self, list_store):
        super().__init__(title="Список спорстменов")
        layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(layout)

        main_menu_area = Gtk.Box()
        self.main_menu = MainMenu(main_menu_area)

        self.tree_view = Gtk.TreeView(list_store)

        for i, col_title in enumerate(["Фамилия", "Код команды", "Колличество баллов", "Место в рейтинге"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # Make column sortable and selectable
            column.set_sort_column_id(i)

            self.tree_view.append_column(column)
        layout.pack_start(main_menu_area, False, False, 0)
        layout.pack_start(self.tree_view, False, False, 0)


class EntryWindow(Gtk.Window):
    __gsignals__ = {
        'save-inserted': (GObject.SIGNAL_RUN_FIRST, None, ()),
        'save-updated': (GObject.SIGNAL_RUN_FIRST, None, ()),
    }

    def __init__(self):
        super().__init__()
        layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(layout)

        surname_box = Gtk.Box()
        surname_label = Gtk.Label("Фамилия:")
        self.surname = Gtk.Entry()

        team_code_box = Gtk.Box()
        team_code_label = Gtk.Label("Код команды:")
        self.team_code = Gtk.Entry()

        score_box = Gtk.Box()
        score_label = Gtk.Label("Количество баллов:")
        self.score = Gtk.Entry()

        button_box = Gtk.HButtonBox()
        self.save = Gtk.Button(stock=Gtk.STOCK_OK)
        self.cancel = Gtk.Button(stock=Gtk.STOCK_CANCEL)

        self.cancel.connect("clicked", self.on_cancel)

        surname_box.pack_start(surname_label, False, False, 0)
        surname_box.pack_end(self.surname, False, False, 0)

        team_code_box.pack_start(team_code_label, False, False, 0)
        team_code_box.pack_end(self.team_code, False, False, 0)

        score_box.pack_start(score_label, False, False, 0)
        score_box.pack_end(self.score, False, False, 0)

        button_box.pack_start(self.save, False, False, 0)
        button_box.pack_start(self.cancel, False, False, 0)

        layout.pack_start(surname_box, False, False, 0)
        layout.pack_start(team_code_box, False, False, 0)
        layout.pack_start(score_box, False, False, 0)
        layout.pack_start(button_box, False, False, 0)

    def on_cancel(self, widget):
        self.close()

    def show_for_insert(self):
        self.set_title('Добавление спортсмена')
        self.save.connect("clicked", self.on_insert_clicked)
        self.show_all()

    def show_for_update(self, row):
        self.set_title('Редактирование спортсмена')
        self.surname.set_text(row[0])
        self.team_code.set_text(row[1])
        self.score.set_text(str(row[2]))
        self.save.connect("clicked", self.on_update_clicked)
        self.show_all()

    def get_saving_fields(self):
        return [self.surname.get_text(), self.team_code.get_text(), self.score.get_text()]

    def on_insert_clicked(self, widget):
        if self.is_ready_for_save():
            self.emit('save-inserted')
            self.close()

    def on_update_clicked(self, widget):
        if self.is_ready_for_save():
            self.emit('save-updated')
            self.close()

    def is_ready_for_save(self):
        return self.surname.get_text() != '' and self.team_code.get_text() != '' and self.score.get_text() != ''