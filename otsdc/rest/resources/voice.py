import requests
from otsdc.url.url_creator import VoiceUrl
from otsdc.rest.resources import resources_properties
from otsdc.rest.model.response_model import ResponseStatus,CallResponse,CallStatusResponse,CallsDetailsResponse

class VoiceResource:
    __appSid = ''
    __voiceUrl = None
    payload = None
    
    def __init__(self, appSid = None, voiceUrl = None):
        self.__appSid = appSid
        self.__voiceUrl = voiceUrl
        
    def call(self, recipient = None, content = None, callType = None, callerId = None, timeScheduled = None, delay = None, repeat = None):
        if recipient is None :
            raise TypeError('Recipient is mandatory')
        if content is None :
            raise TypeError('content is mandatory')
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        self.setPayload(payload, resources_properties.RECIPIENT,recipient)
        self.setPayload(payload, resources_properties.CONTENT,content)
        self.setPayload(payload, resources_properties.CALL_TYPE,callType)
        self.setPayload(payload, resources_properties.CALLERID,callerId)
        self.setPayload(payload, resources_properties.TIME_SCHEDULED,timeScheduled)
        self.setPayload(payload, resources_properties.DELAY,delay)
        self.setPayload(payload, resources_properties.REPEAT,repeat)
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__voiceUrl.urlCall(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            messageResp = CallResponse(**(jsonResp['data']))
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,messageResp
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)
            
    def getCallIDStatus(self, callId = None):
        if callId is None :
            raise TypeError('callId is mandatory')
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        self.setPayload(payload, resources_properties.CALLID,callId)
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__voiceUrl.urlGetCallIDStatus(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            messageResp = CallStatusResponse(**(jsonResp['data']))
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,messageResp
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)
            
    def getCallsDetails(self, dateTo = None, dateFrom = None, callId = None, status = None, country = None):
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        self.setPayload(payload, resources_properties.DATE_TO,dateTo)
        self.setPayload(payload, resources_properties.DATE_FROM,dateFrom)
        self.setPayload(payload, resources_properties.CALLID,callId)
        self.setPayload(payload, resources_properties.STATUS,status)
        self.setPayload(payload, resources_properties.COUNTRY,country)
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__voiceUrl.urlGetCallsDetails(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            messageResp = CallsDetailsResponse(**(jsonResp['data']))
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,messageResp
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)
            
    def ttsCall(self, recipient = None, content = None, language = 'english'):
        if recipient is None :
            raise TypeError('recipient is mandatory')
        if content is None :
            raise TypeError('content is mandatory')
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        self.setPayload(payload, resources_properties.RECIPIENT,recipient)
        self.setPayload(payload, resources_properties.CONTENT,content)
        self.setPayload(payload, resources_properties.LANGUAGE,language)
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__voiceUrl.urlTTSCall(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            messageResp = TTSCallResponse(**(jsonResp['data']))
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,messageResp
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)
            