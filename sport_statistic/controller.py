from sport_statistic import Gtk
from sport_statistic_lib.common.app_settings import AppSettings
from sport_statistic_lib.utility import file_utilities_factory, log_utility
from sport_statistic.view import TreeViewWindow, EntryWindow


class Controller:
    def __init__(self, model):
        self.settings = AppSettings()
        self.logger = log_utility.create_logger(level=self.settings.log_level, filename=self.settings.log_filename)
        self.logger.info("App is started")
        self.file_utility = file_utilities_factory.create(self.settings.file_type)
        self.model = model
        self.tree_view_window = TreeViewWindow(model.list_store)
        self.entry_window = None
        self.selected_row = None

        self.tree_view_window.main_menu.connect('open-file', self.open_file)
        self.tree_view_window.main_menu.connect('save-file', self.save_file)
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
            path_to_file = file_open_dialog.get_file().get_path()
            list_from_file = self.file_utility.read(path_to_file)
            try:
                self.model.populate_list_store(list_from_file)
            except Exception:
                self.logger.error("Файл %s имеет неправильный формат", path_to_file)
                dialog = Gtk.MessageDialog(type=Gtk.MessageType.ERROR,
                                           buttons=Gtk.ButtonsType.CANCEL,
                                           text="Ошибка при открытии файла",
                                           secondary_text="Неправильный формат файла данных: "
                                                          + file_open_dialog.get_file().get_basename())
                dialog.run()
                dialog.destroy()
        file_open_dialog.destroy()

    def save_file(self, widget):
        file_save_dialog = Gtk.FileChooserDialog("Открыть файл:", self.tree_view_window, Gtk.FileChooserAction.SAVE,
                                                 (Gtk.STOCK_SAVE_AS, Gtk.ResponseType.OK,
                                                  Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))
        response = file_save_dialog.run()
        if response == Gtk.ResponseType.OK:
            list_store_iter = self.model.list_store.get_iter_first()
            rows_for_save = []
            for i in range(0, len(self.model.list_store)):
                rows_for_save += [self.model.list_store.get(list_store_iter, 0, 1, 2)]
                list_store_iter = self.model.list_store.iter_next(list_store_iter)
            self.file_utility.write(file_save_dialog.get_file().get_path(), rows_for_save)

        file_save_dialog.destroy()
