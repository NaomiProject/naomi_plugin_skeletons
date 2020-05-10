# -*- coding: utf-8 -*-
from naomi import plugin


class MyVisualizationsPlugin(plugin.VisualizationsPlugin):
    # The visualizations type plugin does not actually have to override any
    # methods. When a visualizations type plugin is loaded into Naomi, it
    # registers the methods that it contains. Then when you want to run a
    # visualization, you import the naomi.visualizations library and run
    # "visualizations.run_visualization("visualization_name",parameters)
    # since more than one user may have defined a visualization method
    # of the same name, it is important to use *args and **kwargs to accept
    # arguments, and gracefully return if any of your expected arguments are
    # missing.
    # Visualizations are designed so a single call can be used for multiple
    # purposes and media. For example, the mic_volume() method is used by the
    # snr_vad plugin to display a volume bar at the bottom of the screen
    # through the terminal visualizations plugin, but also uses the intensity
    # of a single LED to show volume in the Google_AIY_Voice_Kit_v1
    # visualization plugin, and uses a series of multicolor LEDs on the
    # SeeedStudio repeaker mic hat for the same purpose in the
    # Respeaker 4Mic Volume visualization plugin. Multiple plugins can be used
    # to service the same request to run_visualizations().
    def my_visualization(self, *args, **kwargs):
        print("my_visualization activated")
