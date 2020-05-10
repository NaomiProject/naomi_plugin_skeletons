# -*- coding: utf-8 -*-
from naomi import plugin


# The VADPlugin plugin type is used to alert Naomi when an audio clip contains
# a voice. More specifically, it is used by Naomi to determine when to start
# recording or stop recording.
# It has the following attributes:
#   self._input_device - a reference to the current input device. This is
#     mostly helpful for getting information about the input device itself.
class MyVADPlugin(plugin.VADPlugin):
    # The only method that needs to be overridden here is the _voice_detected
    # method. It receives a small clip of audio and returns True if it detects
    # a voice or False if it does not.
    def _voice_detected(self, *args, **kwargs):
        audio_clip = args[0]
        detected_voice = False
        return detected_voice
