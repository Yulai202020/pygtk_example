import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GLib

width = 800
height = 480

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="My title")

        self.set_default_size(width, height)

        self.button = Gtk.Button(label="Idk")
        self.button.connect("clicked", self.button_clicked)
        self.add(self.button)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def button_clicked(self, widget):
        print("idk")

window = MainWindow()
Gtk.main()