#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk
import os, sys



class GUI:
    def __init__(self):
        window = Gtk.Window()
        window.connect('destroy', Gtk.main_quit)
        textview = Gtk.TextView()
        enforce_target = Gtk.TargetEntry.new('text/plain', Gtk.TargetFlags(4), 129)
        # textview.drag_dest_set(Gtk.DestDefaults.ALL, [enforce_target], Gdk.DragAction.COPY)
        textview.connect("drag-data-received", self.on_drag_data_received)
        textview.drag_dest_set_target_list([enforce_target])
        window.add(textview)
        window.show_all()

    def on_drag_data_received(self, widget, drag_context, x,y, data,info, time):

        print(data.get_text())

def main():
    app = GUI()
    Gtk.main()

if __name__ == "__main__":
    sys.exit(main())