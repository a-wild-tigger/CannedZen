import glob, imp
from os.path import join, basename, splitext, abspath, dirname

from Engines import EngineRegistrar
#from Interacts import InteractRgistrar
#from Deployments import genDeployment

def getEngineFactory(name):
    try: return EngineRegistrar.classFactories[name]
    except KeyError: return None

def getPackage(name):
    return EngineRegistrar.getPackage(name)

def getPackages():
    return EngineRegistrar.packages

def getPackageNames():
    return EngineRegistrar.packages.keys()

#Not working for some reason
#def getInteract(pack1name, pack2name):
#    return InteractRegistrar.getInteraction(pack1name, pack2name)

#def getInteracts():
#    return InteractRegistrar.custom_pairs

#def getInteractNames():
#    return InteractRegistrar.custom_pairs.keys()

#def generateDeployment(packages):
#    return genDeployment(packages)