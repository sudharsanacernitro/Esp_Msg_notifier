#!/home/sudharsan/myenv/bin/python3
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
import middleware
# Initialize the D-Bus main loop
DBusGMainLoop(set_as_default=True)

# Callback function for new notifications
def notification_handler(bus, message):
    if message.get_member() == "Notify":
        # Extract relevant information from the message
        args = message.get_args_list()
        app_name = args[0]
        notification_id = args[1]
        app_icon = args[2]
        summary = args[3]
        body = args[4]
        actions = args[5]
        hints = args[6]
        expire_timeout = args[7]

        # Print or process the notification data as needed
        print(f"Received Notification: {summary} - {body}")
        middleware.send(str(summary)+" : "+str(body))

# Connect to the session bus and add a match rule for notifications
bus = dbus.SessionBus()
bus.add_match_string_non_blocking("eavesdrop='true',type='method_call',interface='org.freedesktop.Notifications',member='Notify'")
bus.add_message_filter(notification_handler)

# Start the main loop to capture notifications
GLib.MainLoop().run()
