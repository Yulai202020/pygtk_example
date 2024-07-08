import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GLib

width = 800
height = 480

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="My title")

        self.grid = Gtk.Grid(spacing=10) # space between widget is 10 pix
        self.add(self.grid)

        self.button = Gtk.Button(label="Idk")
        self.button.connect("clicked", self.button_clicked)
        self.box.pack_start(self.button, True, True, 0)

        self.test = Gtk.Entry()
        self.box.pack_start(self.test, True, True, 0)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def button_clicked(self, widget):
        print("idk")

window = MainWindow()
Gtk.main()