from sport_statistic import Gtk
from sport_statistic.view import TreeViewWindow, EntryWindow
from sport_statistic import file_utility


class Controller:
    def __init__(self, model):
        self.model = model
        self.tree_view_window = TreeViewWindow(model.list_store)
        self.entry_window = None

        self.tree_view_window.main_menu.connect('open-file', self.open_file)
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
        model, self.selected_row = self.tree_view_window.tree_view.get_selection().get_selected()
        if self.selected_row is not None:
            self.entry_window = EntryWindow()
            self.entry_window.connect('save-updated', self.update_in_list_store)
            self.entry_window.show_for_update(model[self.selected_row])

    def delete_selected_row(self, widget):
        model, selected_row = self.tree_view_window.tree_view.get_selection().get_selected()
        self.model.list_store.remove(selected_row)

    def insert_in_list_store(self, widget):
        data = self.entry_window.get_saving_fields()
        self.model.append(data)

    def update_in_list_store(self, widget):
        row = self.entry_window.get_saving_fields()
        self.model.list_store[self.selected_row][0] = row[0]
        self.model.list_store[self.selected_row][1] = row[1]
        self.model.list_store[self.selected_row][2] = float(row[2])

    def open_file(self, widget):
        file_open_dialog = Gtk.FileChooserDialog("Открыть файл:", self.tree_view_window, Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_OPEN, Gtk.ResponseType.OK,
                                        Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
        response = file_open_dialog.run()
        if response == Gtk.ResponseType.OK:
            list_from_file = file_utility.read(file_open_dialog.get_file())
            self.model.populate_list_store(list_from_file)

        file_open_dialog.destroy()
