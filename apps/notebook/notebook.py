import gi, json
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GLib

width = 800
height = 480

filename = "example.json"

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="My title")
        self.text = []
        with open(filename) as f:
            json_data = json.loads(f.read())
            self.text = json_data

        self.set_border_width(10)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.adding_page = Gtk.Box()
        self.adding_page.set_border_width(10)
        self.text_of_note = Gtk.Entry()

        self.submit = Gtk.Button(label="Submit")
        self.submit.connect("clicked", self.addiction)
        
        self.adding_page.add(self.text_of_note)
        self.adding_page.add(self.submit)
        
        self.add_pages()

        self.notebook.show_all()

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
    
    def clear_all_pages(self):
        while self.notebook.get_n_pages() > 0:
            self.notebook.remove_page(-1)

    def add_pages(self):
        for i in range(1, len(self.text) + 1):
            page = Gtk.Box()
            page.set_border_width(10)
            page.add(Gtk.Label(label=self.text[i-1]))
            self.notebook.append_page(page, Gtk.Label(label=f"{i} - Page"))


        self.text_of_note.set_text("")
        self.notebook.append_page(self.adding_page, Gtk.Label(label="Add note"))
    
    def addiction(self, widget):
        text_to_add = self.text_of_note.get_text()
        self.text_of_note.set_text("")
        self.text.append(text_to_add)

        new_page = Gtk.Box()
        new_page.set_border_width(10)
        new_page.add(Gtk.Label(label=text_to_add))

        position = len(self.notebook.get_children())-1

        # Insert the new page at the calculated positio
        self.notebook.insert_page(new_page, tab_label=Gtk.Label(label=f"{len(self.text)} - Page"), position=position)
        self.notebook.show_all()

        with open(filename, "w") as f:
            json_str = json.dumps(self.text, indent=4)
            f.write(json_str)


window = MainWindow()
Gtk.main()