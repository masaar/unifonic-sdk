class VoiceUrl:
    __pathVoice = 'Voice/'
    __urlCall = ''
    __urlGetCallIDStatus = ''
    __urlGetCallsDetails = ''
    __urlTTSCall = ''

    def __init__(self, urlBase):
        urlVoice = urlBase + self.__pathVoice
        self.__urlCall = urlVoice + 'Call'
        self.__urlGetCallIDStatus = urlVoice + 'GetCallIDStatus'
        self.__urlGetCallsDetails = urlVoice + 'GetCallsDetails'
        self.__urlTTSCall = urlVoice + 'TTSCall'

    def urlCall(self):
        return self.__urlCall

    def urlGetCallIDStatus(self):
        return self.__urlGetCallIDStatus

    def urlGetCallsDetails(self):
        return self.__urlGetCallsDetails

    def urlTTSCall(self):
        return self.__urlTTSCall

class VerifyUrl:
    __pathVerify = 'Verify/'
    __urlGetCode = ''
    __urlVerifyNumber = ''
    
    def __init__(self, urlBase):
        urlVerify = urlBase + self.__pathVerify
        self.__urlGetCode = urlVerify + 'Send'
        self.__urlVerifyNumber = urlVerify + 'GetEmailsReport'
        
    def urlGetCode(self):
        return self.__urlGetCode
    
    def urlVerifyNumber(self):
        return self.__urlVerifyNumber


class EmailUrl:
    __pathEmail = 'Email/'
    __urlSend = ''
    __urlGetEmailReport = ''
    
    def __init__(self, urlBase):
        urlEmail = urlBase + self.__pathEmail
        self.__urlSend = urlEmail + 'Send'
        self.__urlGetEmailReport = urlEmail + 'GetEmailsReport'
        
    def urlSend(self):
        return self.__urlSend
    
    def urlGetEmailReport(self):
        return self.__urlGetEmailReport

class AccountUrl:
    __pathAccount = 'Account/'
    __urlGetBalance = ''
    __urlAddSenderID = ''
    __urlGetSenderIDStatus = ''
    __urlGetSenderIDs = ''
    __urlDeleteSenderID = ''
    __urlGetDefaultSenderID = ''
    __urlChangeDefaultSenderID = ''
    
    def __init__(self, urlBase):
        urlAccount = urlBase + self.__pathAccount
        self.__urlGetBalance = urlAccount + 'GetBalance';
        self.__urlAddSenderID = urlAccount + 'addSenderID';
        self.__urlGetSenderIDStatus = urlAccount + 'getSenderIDStatus';
        self.__urlGetSenderIDs = urlAccount + 'getSenderIDs';
        self.__urlDeleteSenderID = urlAccount + 'DeleteSenderID';
        self.__urlGetDefaultSenderID = urlAccount + 'GetAppDefaultSenderID';
        self.__urlChangeDefaultSenderID = urlAccount + 'changeAppDefaultSenderID';
        
    def urlGetBalance(self):
        return self.__urlGetBalance
    
    def urlAddSenderID(self):
        return self.__urlAddSenderID
    
    def urlGetSenderIDStatus(self):
        return self.__urlGetSenderIDStatus
    
    def urlGetSenderIDs(self):
        return self.__urlGetSenderIDs
    
    def urlDeleteSenderID(self):
        return self.__urlDeleteSenderID
    
    def urlGetDefaultSenderID(self):
        return self.__urlGetDefaultSenderID
    
    def urlChangeDefaultSenderID(self):
        return self.__urlChangeDefaultSenderID
        

class MessageUrl:
    __pathMessage = 'Messages/'    
    __urlSend = ''
    __urlSendBulk = ''
    __urlGetMessageIDStatus = ''
    __urlGetMessageReport = ''
    __urlGetMessageDetails = ''
    
    def __init__(self,urlBase):
        urlMessage = urlBase + self.__pathMessage
        self.__urlSend = urlMessage + 'Send'
        self.__urlSendBulk = urlMessage + 'SendBulk'
        self.__urlGetMessageIDStatus = urlMessage + 'GetMessageIDStatus'
        self.__urlGetMessageReport = urlMessage + 'GetMessagesReport'
        self.__urlGetMessageDetails = urlMessage + 'GetMessagesDetails'
        
    def urlSend(self):
        return self.__urlSend
    
    def urlSendBulk(self):
        return self.__urlSendBulk
    
    def urlGetMessageIDStatus(self):
        return self.__urlGetMessageIDStatus
    
    def urlGetMessageReport(self):
        return self.__urlGetMessageReport
        
    def urlGetMessageDetails(self):
        return self.__urlGetMessageDetails