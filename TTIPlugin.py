# -*- coding: utf-8 -*-
from naomi import plugin


# TTI plugins consume intents, then decide which intent to activate based
# on the incoming transcript.
class MyTTIPlugin(plugin.TTIPlugin):
    def add_intents(self, intents):
        # insert code to format the intents in such a way that the
        # intent engine can use them
        pass

    def get_plugin_phrases(self, passive_listen=False):
        phrases = []
        # insert code to retrieve a list of all the templates
        # for all of the intents consumed so far
        # ...
        return phrases

    def train(self):
        # This will be called after all the plugins have been loaded.
        # Use it for any finalization procedures before starting to
        # determine intents. Set self.trained to True so we know we
        # have completed the training step.
        self.trained = True

    def determine_intent(self, phrase):
        # insert a method of selecting an intent to service the phrase.
        # ...
        # return the result as an intentresult structure
        intentresult = {
            'action': selected_intent.action,
            'input': phrase,
            'intent': selected_intent.name,
            'matches': {
                'match1': ['value1'],
                'match2': ['value2']
            },
            'score': score
        }
        return intentresult
