import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class SportsmanWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Current Sportsman")
        layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(layout)

        surname_box = Gtk.Box()
        layout.pack_start(surname_box, False, False, 0)

        surname_label = Gtk.Label("Фамилия:")
        surname_box.pack_start(surname_label, False, False, 0)

        surname = Gtk.Entry()
        surname_box.pack_end(surname, False, False, 0)

        team_code_box = Gtk.Box()
        layout.pack_start(team_code_box, False, False, 0)

        team_code_label = Gtk.Label("Код команды:")
        team_code_box.pack_start(team_code_label, False, False, 0)

        team_code = Gtk.Entry()
        team_code_box.pack_end(team_code, False, False, 0)

        score_box = Gtk.Box()
        layout.pack_start(score_box, False, False, 0)

        score_label = Gtk.Label("Количество баллов:")
        score_box.pack_start(score_label, False, False, 0)

        score = Gtk.Entry()
        score_box.pack_end(score, False, False, 0)

        place_box = Gtk.Box()
        layout.pack_start(place_box, False, False, 0)

        place_label = Gtk.Label("Место в итоге:")
        place_box.pack_start(place_label, False, False, 0)

        place = Gtk.Entry()
        place_box.pack_end(place, False, False, 0)

