# -*- coding: utf-8 -*-
from naomi import plugin


# The stt_trainer plugin provides a plugin that is used with the
# NaomiSTTTrainer.py program to train a stt engine based on the
# contents of your audiolog database.
#
# The audiolog database is a database of recordings of you speaking
# to your Naomi. Actual recordings of you speaking to your Naomi
# are the best source of training material since the resulting STT
# model will be adapted to your voice, background noise, microphone,
# etc.
#
# To start saving recordings, run Naomi with the --save-audio flag.
# This will save any audio picked up any time the Voice Activity
# Detector indicates that Naomi should start listening. This will
# include passive phrases ("Naomi"), active phrases ("what time is
# it"), people speaking near Naomi but not to Naomi, and, depending
# on your VAD plugin, even loud noises.
#
# After collecting about 50 recordings or so, you probably want to
# switch to only collecting active phrases, which means that audio
# will only be collected once Naomi thinks it has heard its wake word.
#
# This can be accomplished by adding the following to your profile.yml:
#   audiolog:
#     save_active_audio: True
#
# The NaomiSTTTrainer.py program allows you to review recordings,
# verify or correct transcriptions, associate recordings with
# specific speakers, and verify or correct intents associated with
# the recordings.
#
# Once you have a database of recordings built up, you can then use
# that information to train a specific STT engine. That is where this
# plugin comes in.
class MySTT_TrainerPlugin(plugin.STTTrainerPlugin):
    # The only required method for this this plugin type is HandleCommand.
    # This method receives a command and description and returns an HTML
    # response, the next command and a description. The reason for this
    # is because it can take a very long time to actually train a STT
    # engine, and that training can typically be split into distinct
    # stages or loops, with feedback being provided to the user.
    #
    # command allows the output to split into stages, and description allows
    # a description to be passed in with the incoming command.
    # If the nextcommand is the empty string, then the program concludes.
    def HandleCommand(self, command, description):
        response = []
        nextcommand = ""
        if command == "":
            response.append("""<p>Started: {} <span class="success">Success</span></p>""".format(" ".join(description)))
            nextcommand = "testfailure"
            description.append("Test Failure")
        if command == "testfailure":
            response.append("""<p>This is what failure looks like: {} <span class="failure">Failure</span></p>""".format(" ".join(description)))
        return response, nextcommand, description
