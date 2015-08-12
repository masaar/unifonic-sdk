import requests
from otsdc.url.url_creator import AccountUrl
from otsdc.rest.resources import resources_properties
from otsdc.rest.model.response_model import ResponseStatus, Balance, SenderID, SenderList


class AccountResource:
    __appSid = ''
    __accountUrl = None
    payload = None
    
    def __init__(self, appSid = None, accountUrl = None):
        self.__appSid = appSid
        self.__accountUrl = accountUrl
        
    def getBalance(self):
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__accountUrl.urlGetBalance(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            messageResp = Balance(**(jsonResp['data']))
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,messageResp
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)
    
    def addSenderId(self, senderId = None):
        if senderId is None :
            raise TypeError('senderId is mandatory')    
        
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        self.setPayload(payload, resources_properties.SENDERID,senderId)        
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__accountUrl.urlAddSenderID(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            messageResp = SenderID(**(jsonResp['data']))
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,messageResp
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)
          
    def getSenderIDStatus(self, senderId = None):
        if senderId is None :
            raise TypeError('senderId is mandatory')    
        
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        self.setPayload(payload, resources_properties.SENDERID,senderId)        
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__accountUrl.urlGetSenderIDStatus(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            messageResp = SenderID(**(jsonResp['data']))
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,messageResp
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)
          
    def getSenderIDS(self):
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid      
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__accountUrl.urlGetSenderIDs(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            messageResp = SenderList(**(jsonResp['data']))
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,messageResp
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)

    def deleteSenderID(self, senderId = None):
        if senderId is None :
            raise TypeError('senderId is mandatory')    

        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        self.setPayload(payload, resources_properties.SENDERID,senderId)        
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__accountUrl.urlDeleteSenderID(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            del jsonResp['data']            
            respStat = ResponseStatus(**jsonResp)
            return respStat,None
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)

    def getAppDefaultSenderID(self):
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid      
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__accountUrl.urlGetDefaultSenderID(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            messageResp = SenderID(**(jsonResp['data']))
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,messageResp
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)

    def changeAppDefaultSenderID(self, senderId = None):
        if senderId is None :
            raise TypeError('senderId is mandatory')    

        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        self.setPayload(payload, resources_properties.SENDERID,senderId)        
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__accountUrl.urlChangeDefaultSenderID(),data=payload, headers = headers)
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