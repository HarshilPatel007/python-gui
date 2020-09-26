import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
from gi.repository import Gtk as gtk
from gi.repository import Gdk as gdk



class Main:

    def __init__(self):

        screen = gdk.Screen.get_default()
        provider = gtk.CssProvider()
        provider.load_from_path("styles/gtk-3.0/gtk-dark.css")
        gtk.StyleContext.add_provider_for_screen(screen, provider, gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        glade_file = "test.glade"
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

    def on_btnHelloWorld_clicked(self, widget=None, data=None):
        print("Hello World! from python GTK+")

    def on_btnOpenNewWindow_clicked(self, widget=None, data=None):
        glade_file = "helloworld.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(glade_file)
        self.builder.connect_signals(self)
        
        window_1 = self.builder.get_object("helloWorldWindow")
        window_1.connect("delete-event", self.child_quit)
        window_1.show()

    def on_btnOpenSecondWindow_clicked(self, widget=None, data=None):
        glade_file = "secondwindow.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(glade_file)
        self.builder.connect_signals(self)

        window_2 = self.builder.get_object("secondWindow")
        # gtk.Window.set_decorated(window_2, False) # Borderless window.
        window_2.connect("delete-event", self.child_quit)
        window_2.show()

if __name__ == "__main__":
    main = Main()
    gtk.main()
