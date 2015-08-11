from otsdc.url.url_creator import *

class DefaultOTSUrl:
    __urlBase = ''
    __accountURL = None
    __messageURL = None
    __voiceURL = None
    __emailURL = None
    __verifyURL = None
    
    def __init__(self, urlBase):
        self.__urlBase = urlBase
        self.__accountURL = AccountUrl(urlBase)
        self.__messageURL = MessageUrl(urlBase)
        self.__voiceURL = VoiceUrl(urlBase)
        self.__emailURL = EmailUrl(urlBase)
        self.__verifyURL = VerifyUrl(urlBase)
    
    def getAccountURL(self):
        return self.__accountURL
    
    def getMessageURL(self):
        return self.__messageURL
    
    def getVoiceURL(self):
        return self.__voiceURL
    
    def getEmailURL(self):
        return self.__emailURL
    
    def getVerifyURL(self):
        return self.__verifyURL

class HttpOTSUrl(DefaultOTSUrl):
    __defaultUrlBase = 'http://api.otsdc.com/rest/'
    
    def __init__(self, urlBase = __defaultUrlBase):
        DefaultOTSUrl.__init__(self, urlBase)
        
class HttpsOTSUrl(DefaultOTSUrl):
    __defaultUrlBase = 'https://api.otsdc.com/rest/'
    
    def __init__(self, urlBase = __defaultUrlBase):
        DefaultOTSUrl.__init__(self, urlBase)
        
