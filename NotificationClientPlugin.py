# -*- coding: utf-8 -*-
from datetime import datetime
from naomi import app_utils
from naomi import plugin


# The Notification Client Plugin contains a method called
# "gather()" that runs every 30 seconds. If the plugin
# does not have a gather() method at the end of the __init__
# method, then it will not be added to the notifier and
# will not run again until Naomi is restarted.
# The base notification client has the following properties:
#   self._mic - the current microphone
#   self._brain - the current brain
#   self.gettext - the current translator
class MyNotificationClient(plugin.NotificationClientPlugin):
    # The gather function is fired every 30 seconds
    def gather(self, last_date):
        if(last_date is None):
            self._mic.say("First run")
        else:
            self._mic.say("Last run at {}".format(last_date))
        return datetime.now(tz=app_utils.get_timezone())
