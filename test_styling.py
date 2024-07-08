import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GLib

width = 800
height = 480

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="My title")

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10) # space between widget is 10 pix
        self.box.set_border_width(20)
        self.box.set_homogeneous(False)
        self.add(self.box)

        # normal text
        self.text = Gtk.Label(label="Hello world!")
        self.box.pack_start(self.text, True, True, 0)

        # justify
        self.text1 = Gtk.Label()
        self.text1.set_text("Hello world!\nHow are you")
        self.text1.set_justify(Gtk.Justification.LEFT)
        self.box.pack_start(self.text1, True, True, 0)

        self.text2 = Gtk.Label()
        self.text2.set_text("Hello world!\nHow are you")
        self.text2.set_justify(Gtk.Justification.RIGHT)
        self.box.pack_start(self.text2, True, True, 0)

        # line wrap

        self.text3 = Gtk.Label()
        self.text3.set_text("The sun sets low, a golden hue, The sky a canvas, painted new. Whispers of wind, a gentle breeze, Dancing through the autumn trees.")
        self.text3.set_line_wrap(True)
        self.text3.set_justify(Gtk.Justification.FILL)
        self.box.pack_start(self.text3, True, True, 0)

        # xml in pygtk

        self.text4 = Gtk.Label()
        self.text4.set_markup("<b>The sun sets low, a golden hue, The sky a canvas, painted new. Whispers of wind, a gentle breeze, Dancing through the autumn trees.</b>")
        self.box.pack_start(self.text4, True, True, 0)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def button_clicked(self, widget):
        print("idk")

window = MainWindow()
Gtk.main()