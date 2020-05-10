# -*- coding: utf-8 -*-
from naomi import plugin

class MyTTSPlugin(plugin.TTSPlugin):
    # The only methods you have to define here are "get_voices" and "say"

    # The get_voices method takes no parameters and returns a list of voices.
    def get_voices(self):
        voices = [
            "English - american male",
            "English - american female",
            "English - british male",
            "English - british female",
            "English - canadian male",
            "English - canadian female"
        ]
        return voices

    # The "say" method has two parameters:
    #   phrase (required) - a phrase to be spoken
    #   voice (optional) - a voice to be used. If None, then use the default.
    def say(self, phrase, voice=None):
        pass
