import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
from gi.repository import Gtk as gtk
from gi.repository import Gdk as gdk



class Main:

    def __init__(self):

        screen = gdk.Screen.get_default()
        provider = gtk.CssProvider()
        provider.load_from_path("styles/Matcha-dark-aliz/gtk-dark.css")
        gtk.StyleContext.add_provider_for_screen(screen, provider, gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        glade_file = "ui/main.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(glade_file)
        self.builder.connect_signals(self)



        # btn = self.builder.get_object("btnHelloWorld")
        # btn.connect("clicked", self.HelloWorld)

        window = self.builder.get_object("mainWindow")
        window.connect("delete-event", gtk.main_quit)
        window.show_all()

    def child_quit(self, widget, event):
        window = widget.get_child()
        window.destroy()
        widget.hide()
        return True

    def on_btn_helloworld_clicked(self, widget=None, data=None):
        print("Hello World! from python GTK+")

    def on_btn_open_helloworld_window_clicked(self, widget=None, data=None):
        glade_file = "ui/helloworld.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(glade_file)
        self.builder.connect_signals(self)
        
        helloworld_window = self.builder.get_object("helloWorldWindow")
        helloworld_window.connect("delete-event", self.child_quit)
        helloworld_window.show()

    def on_btn_open_calender_window_clicked(self, widget=None, data=None):
        glade_file = "ui/calender.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(glade_file)
        self.builder.connect_signals(self)

        calender_window = self.builder.get_object("calenderWindow")
        # gtk.Window.set_decorated(window_2, False) # Borderless window.
        calender_window.connect("delete-event", self.child_quit)
        calender_window.show()

    def on_about_activate(self, widget=None, data=None):
        glade_file = "ui/about.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(glade_file)
        self.builder.connect_signals(self)

        about_window = self.builder.get_object("aboutWindow")
        about_window.connect("delete-event", self.child_quit)
        about_window.show()

if __name__ == "__main__":
    main = Main()
    gtk.main()
