import imp
import os
import pluginloader

def loadPlugins():
    for i in pluginloader.getPlugins():
        print("Loading plugin " + i["name"])
        plugin = pluginloader.loadPlugin(i)
        plugin.run()

