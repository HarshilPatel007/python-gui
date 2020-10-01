# https://en.it1352.com/article/2f6d75817da34d8d842bc8788691b4b9.html

from gi.repository import Gtk, Gdk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="TreeView Drag and Drop")
        self.connect("delete-event", Gtk.main_quit)
        self.set_border_width(10)
        self.set_default_size(400, 300)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.store = Gtk.TreeStore(bool, str)
        self.view = Gtk.TreeView(model=self.store)
        vbox.add(self.view)

        renderer_toggle = Gtk.CellRendererToggle()
        column_toggle = Gtk.TreeViewColumn("", renderer_toggle, active=0)
        renderer_toggle.connect("toggled", self.on_toggled)
        self.view.append_column(column_toggle)

        renderer_name = Gtk.CellRendererText()
        column_name = Gtk.TreeViewColumn("Name", renderer_name, text=1)
        self.view.append_column(column_name)

        self.view.connect("drag-begin", self.drag_begin)
        self.view.connect("drag-data-get", self.drag_data_get)
        self.view.connect("drag-drop", self.drag_drop)
        self.view.connect("drag-data-delete", self.drag_data_delete)
        self.view.connect("drag-data-received", self.drag_data_received)
        self.view.connect("drag-end", self.drag_end)

        targets = [("text/uri-list", 0, 0)]
        self.view.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK,
            targets, Gdk.DragAction.DEFAULT|Gdk.DragAction.MOVE)
        self.view.enable_model_drag_dest(targets, Gdk.DragAction.DEFAULT)

        self.add_test_data()

    def add_test_data(self):
        parent = self.store.append(None, [True, "Item 1"])
        self.store.append(parent, [True, "Item 2"])
        self.store.append(None, [True, "Item 3"])
        self.store.append(None, [True, "Item 4"])

    def on_toggled(self, cellrenderer, path):
        self.store[path][0] = not self.store[path][0]

    def drag_begin(self, treeview, context):
        print("===================")
        print("Drag started")

    def drag_data_get(self, treeview, context, selection, info, time):
        print("===================")
        print("Drag data requested by destination")
        treeselection = treeview.get_selection()
        model, iter = treeselection.get_selected()
        data = bytes(model.get_value(iter, 1), "utf-8")
        selection.set(selection.get_target(), 8, data)

    def drag_drop(self, treeview, context, selection, info, time):
        print("===================")
        print("Drag data droped")

    def drag_data_received(self, treeview, context, x, y, selection, info, time):
        print("===================")
        print("Drag data received")
        drop_info = self.view.get_dest_row_at_pos(x, y)
        data = selection.get_data().decode("utf-8")
        if drop_info is not None:
            drop_path, drop_position = drop_info[0], drop_info[1]
            print(drop_position)
            drop_iter = self.store.get_iter(drop_path)
            #0=Before, 1=After, 2=INTO_OR_BEFORE, 3=INTO_OR_AFTER
            if drop_position == Gtk.TreeViewDropPosition.BEFORE:
                print("Droped before {}".format(drop_path))
                self.store.insert_before(None, drop_iter, [True, data])
            elif drop_position == Gtk.TreeViewDropPosition.AFTER:
                print("Droped after {}".format(drop_path))
                self.store.insert_after(None, drop_iter, [True, data])
            else:
                self.store.insert_after(drop_iter, None, [True, data])

    def drag_end(self, treeview, context):
        print("===================")
        print("Drag data end")

    def drag_data_delete(self, treeview, context):
        print("===================")
        print("Drag data delete")

win = MainWindow()
win.show_all()
Gtk.main()