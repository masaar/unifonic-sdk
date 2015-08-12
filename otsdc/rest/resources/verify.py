import requests
from otsdc.url.url_creator import VerifyUrl
from otsdc.rest.resources import resources_properties
from otsdc.rest.model.response_model import ResponseStatus,GetCodeResponse

class VerifyResource:
    __appSid = ''
    __verifyUrl = None
    payload = None
    
    def __init__(self, appSid = None, verifyUrl = None):
        self.__appSid = appSid
        self.__verifyUrl = verifyUrl
        
    def getCode(self, recipient = None, body = None,securityType = None, expiry = None, senderId = None):
        if recipient is None :
            raise TypeError('Recipient is mandatory')
        if body is None :
            raise TypeError('Body is mandatory')
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        self.setPayload(payload, resources_properties.RECIPIENT,recipient)
        self.setPayload(payload, resources_properties.BODY,body)
        self.setPayload(payload, resources_properties.SECURITY_TYPE,securityType)
        self.setPayload(payload, resources_properties.EXPIRY,expiry)
        self.setPayload(payload, resources_properties.SENDERID,senderId)
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__verifyUrl.urlGetCode(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            messageResp = GetCodeResponse(**(jsonResp['data']))
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,messageResp
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)
            
    def verifyNumber(self, recipient = None, passCode = None):
        if recipient is None :
            raise TypeError('Recipient is mandatory')
        if passCode is None :
            raise TypeError('passCode is mandatory')
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        self.setPayload(payload, resources_properties.RECIPIENT,recipient)
        self.setPayload(payload, resources_properties.PASSCODE,passCode)
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__verifyUrl.urlVerifyNumber(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,None
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)
            
    def setPayload(self,payload = {}, key = None, val = None):
        if val is not None :
            payload[key] = val