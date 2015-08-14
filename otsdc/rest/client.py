from otsdc.rest.resources.account import AccountResource
from otsdc.rest.resources.email import EmailResource
from otsdc.rest.resources.message import MessageResource
from otsdc.rest.resources.verify import VerifyResource
from otsdc.rest.resources.voice import VoiceResource
from otsdc.url.http_url import *

class OTSRestClient:
    appSid = ''
    url = None
    accountResource = None
    emailResource = None
    messageResource = None
    verifyResource = None
    voiceResource = None
    
    def __init__(self, appSid = None, url = HttpOTSUrl()):
        self.url = url
        self.appSid = appSid
        self.accountResource = AccountResource(self.appSid, self.url.getAccountURL())
        self.emailResource = EmailResource(self.appSid, self.url.getEmailURL())
        self.messageResource = MessageResource(self.appSid, self.url.getMessageURL())
        self.verifyResource = VerifyResource(self.appSid, self.url.getVerifyURL())
        self.voiceResource = VoiceResource(self.appSid, self.url.getVoiceURL())
        