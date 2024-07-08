import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GLib

width = 800
height = 480

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="My title")

        self.set_border_width(10)

        self.listbox = Gtk.ListBox() # space between widget is 10 pix
        self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(self.listbox)

        # first row

        first_row = Gtk.ListBoxRow()
        box_1 = Gtk.Box()
        box_1.set_border_width(10)
        first_row.add(box_1)

        self.button = Gtk.Button(label="Idk")
        self.button.connect("clicked", self.button_clicked)
        box_1.pack_start(self.button, True, True, 0)

        second_row = Gtk.ListBoxRow()
        box_2 = Gtk.Box()
        box_2.set_border_width(10)
        second_row.add(box_2)

        self.test = Gtk.Entry()
        box_2.pack_start(self.test, True, True, 0)

        self.listbox.add(first_row)
        self.listbox.add(second_row)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def button_clicked(self, widget):
        print("idk")

window = MainWindow()
Gtk.main()