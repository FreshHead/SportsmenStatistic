from sport_statistic import Gtk
from sport_statistic.view import TreeViewWindow, EntryWindow


class Controller:
    def __init__(self, model):
        self.model = model
        self.tree_view_window = TreeViewWindow(model.list_store)
        self.entry_window = None
        self.selected_row_until_update = None

        self.tree_view_window.main_menu.connect('insert-sportsman', self.open_insert_form)
        self.tree_view_window.main_menu.connect('update-sportsman', self.open_update_form)
        self.tree_view_window.main_menu.connect('delete-sportsman', self.delete_selected_row)

        self.tree_view_window.connect('delete-event', Gtk.main_quit)

        self.tree_view_window.show_all()

    def open_insert_form(self, widget):
        self.entry_window = EntryWindow()
        self.entry_window.connect('save-inserted', self.insert_in_list_store)
        self.entry_window.show_for_insert()

    def open_update_form(self, widget):
        model, selected_row = self.tree_view_window.tree_view.get_selection().get_selected()
        if selected_row is not None:
            self.entry_window = EntryWindow()
            self.entry_window.connect('save-updated', self.update_in_list_store)
            self.entry_window.show_for_update(self.selected_row_until_update)

    def delete_selected_row(self, widget):
        model, selected_row = self.tree_view_window.tree_view.get_selection().get_selected()
        self.model.list_store.remove(selected_row)

    def insert_in_list_store(self, widget):
        data = self.entry_window.get_saving_fields()
        self.model.append(data)

    def update_in_list_store(self, widget):
        pass

