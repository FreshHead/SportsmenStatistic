from sport_statistic import Gtk
from sport_statistic.main_menu import MainMenu


class TreeViewWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Список спорстменов")
        layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(layout)

        main_menu_area = Gtk.Box()
        self.main_menu = MainMenu(main_menu_area)

        self.list_store = Gtk.ListStore(str, str, float, int)
        self.tree_view = Gtk.TreeView(self.list_store)

        for i, col_title in enumerate(["Фамилия", "Код команды", "Колличество баллов", "Место в рейтинге"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # Make column sortable and selectable
            column.set_sort_column_id(i)

            self.tree_view.append_column(column)
        layout.pack_start(main_menu_area, False, False, 0)
        layout.pack_start(self.tree_view, False, False, 0)


class EntryWindow(Gtk.Window):
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

        self.save = Gtk.Button()

        surname_box.pack_start(surname_label, False, False, 0)
        surname_box.pack_end(self.surname, False, False, 0)

        team_code_box.pack_start(team_code_label, False, False, 0)
        team_code_box.pack_end(self.team_code, False, False, 0)

        score_box.pack_start(score_label, False, False, 0)
        score_box.pack_end(self.score, False, False, 0)

        layout.pack_start(surname_box, False, False, 0)
        layout.pack_start(team_code_box, False, False, 0)
        layout.pack_start(score_box, False, False, 0)
        layout.pack_start(self.save, False, False, 0)

    def show_for_insert(self):
        self.set_title('Добавление спортсмена')
        self.save.set_label('Добавить')
        self.show_all()

    def show_for_update(self, surname, team_code, score):
        self.set_title('Редактирование спортсмена')
        self.surname.set_text(surname)
        self.team_code.set_text(team_code)
        self.score.set_text(str(score))
        self.save.set_label('Сохранить изменения')
        self.show_all()
