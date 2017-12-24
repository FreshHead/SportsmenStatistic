from sport_statistic import Gtk
from sport_statistic.controller import Controller
from sport_statistic.model import Model
from sport_statistic.view import TreeViewWindow, EntryWindow

Controller(Model())
Gtk.main()
