from sport_statistic import Gtk
from sport_statistic.view import EntryWindow


class Controller:
    def __init__(self, model, tree_view_window):
        self.model = model
        self.tree_view_window = tree_view_window
        self.entry_window = None
        self.tree_view_window.main_menu.connect('insert-sportsman', self.insert_sportsman)
        self.tree_view_window.main_menu.connect('update-sportsman', self.update_sportsman)
        self.tree_view_window.main_menu.connect('delete-sportsman', self.delete_sportsman)

        self.tree_view_window.connect('delete-event', Gtk.main_quit)

        for item in self.model.sportsmen_list:
            self.tree_view_window.list_store.append(item.get_tuple())

        self.tree_view_window.show_all()

    def insert_sportsman(self, widget):
        self.entry_window = EntryWindow()
        self.entry_window.show_for_insert()

    def update_sportsman(self, widget):
        model, selected_row = self.tree_view_window.tree_view.get_selection().get_selected()
        if selected_row is not None:
            self.entry_window = EntryWindow()
            self.entry_window.show_for_update(model[selected_row][0], model[selected_row][1], model[selected_row][2])

    def delete_sportsman(self, widget):
        pass
