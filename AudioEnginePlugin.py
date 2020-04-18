#-*- coding: utf-8 -*-
from naomi import plugin

# The AudioEnginePlugin requires two classes, the AudioEnginePlugin
# which is used to retrieve information about device objects and the
# objects themselves.
# This is a class that is used to access information about audio devices
# most methods pass a device object back to the calling program.
class MyAudioEngine(plugin.AudioEnginePlugin):
    def get_devices(self, device_type=plugin.audioengine.DEVICE_TYPE_ALL):
        devices = []
        # Insert code to populate devices with a list of MyAudioDevice objects
        return devices

    # the get_default_device() method returns an output device (default)
    # or an input device(if the output parameter is set to False)
    def get_default_device(output=True):
        # insert code to retrieve the default MyAudioDevice device
        return device_object

    # the get_device_by_slug() method returns a device by a string (slug)
    # which identifies it.
    def get_device_by_slug(self, slug):
        #insert code to retrieve the device by name (slug)
        return device


class MyAudioDevice(plugin.audioengine.AudioDevice):
    # types tells the user whether this is an input device,
    # an output device, or both.
    def types(self):
        types = []
        # insert code to populate types with the types of functions
        # this device provides. This can be
        #   plugin.audioengine.DEVICE_TYPE_INPUT
        # and/or
        #   plugin.audioengine.DEVICE_TYPE_OUTPUT
        return tuple(types)

    def supports_format(self, bits, channels, rate, output=True):
        supported = False
        # Populate "supported" with either True or False depending on
        # whether the device is compatible with the bits, channels and
        # rate and is either an output device (output=True) or an input
        # device (output=False)
        return supported

    # open_stream() opens a new streaming device and returns a
    # handle to use to either pass data to the device (output=True) or 
    # retrieve data from the device (output=False)
    @contextlib.contextmanager
    def open_stream(self, bits, channels, rate,  chunksize=1024, output=True):
        # insert code to open a stream
        try:
            yield stream
        finally:
            stream.close()

    # record yields frames as they are received
    def record(self, chunksize, *args):
        with self.open_stream(*args, chunksize=chunksize,
                              output=False) as stream:
            while True:
                yield stream.read()[1]

