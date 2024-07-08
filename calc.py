import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GLib

width = 800
height = 600

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Calc")

        self.set_border_width(10)

        self.listbox = Gtk.ListBox() # space between widget is 10 pix
        self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(self.listbox)

        # entry
        entry_row = Gtk.ListBoxRow()
        entry_box = Gtk.Box(spacing=10)
        entry_box.set_border_width(10)
        entry_row.add(entry_box)

        self.entry = Gtk.Entry()
        entry_box.pack_start(self.entry, True, True, 0)

        # special

        special_row = Gtk.ListBoxRow()
        special_box = Gtk.Box(spacing=10)
        special_box.set_border_width(10)
        special_row.add(special_box)

        for i in ["(", ")", " ", "AC"]:
            button = Gtk.Button(label=i)
            button.connect("clicked", self.button_clicked)

            special_box.pack_start(button, True, True, 0)

        # first row 1, 2, 3
        first_row = Gtk.ListBoxRow()
        box_1 = Gtk.Box(spacing=10)
        box_1.set_border_width(10)
        first_row.add(box_1)

        for i in [1, 2, 3, "/"]:
            self.button = Gtk.Button(label=str(i))
            self.button.connect("clicked", self.button_clicked)

            box_1.pack_start(self.button, True, True, 0)

        # second 4, 5, 6
        second_row = Gtk.ListBoxRow()
        box_2 = Gtk.Box(spacing=10)
        box_2.set_border_width(10)
        second_row.add(box_2)

        for i in [4, 5, 6, "*"]:
            button = Gtk.Button(label=str(i))
            button.connect("clicked", self.button_clicked)

            box_2.pack_start(button, True, True, 0)

        # latest 6, 7, 9
        third_row = Gtk.ListBoxRow()
        box_3 = Gtk.Box(spacing=10)
        box_3.set_border_width(10)
        third_row.add(box_3)

        for i in [7, 8, 9, "-"]:
            button = Gtk.Button(label=str(i))
            button.connect("clicked", self.button_clicked)

            box_3.pack_start(button, True, True, 0)

        # 0 . and = +

        latest_row = Gtk.ListBoxRow()
        box_4 = Gtk.Box(spacing=10)
        box_4.set_border_width(10)
        latest_row.add(box_4)

        for i in [0, ".", "=", "+"]:
            button = Gtk.Button(label=str(i))
            button.connect("clicked", self.button_clicked)

            box_4.pack_start(button, True, True, 0)

        # add

        self.listbox.add(entry_row)
        self.listbox.add(special_row)  # Add the special_row instead of special_box
        self.listbox.add(first_row)
        self.listbox.add(second_row)
        self.listbox.add(third_row)
        self.listbox.add(latest_row)

        self.listbox.show_all()

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def calculator(self, expression):
        try:
            result = eval(expression)
            if result is not None:
                return result
            else:
                return ""
        except Exception as e:
            return f"Error: {e}"

    def button_clicked(self, widget):
        data = self.entry.get_text()
        label = widget.get_label()

        if label == "AC":
            self.entry.set_text("")
        elif label == "=":
            data = data.replace(' ', '')

            if data == "":
                self.entry.set_text("")
                return

            result = str(self.calculator(data))
            self.entry.set_text(result)
        else :
            self.entry.set_text(data + label)

window = MainWindow()
Gtk.main()
