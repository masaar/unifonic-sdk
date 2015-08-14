import requests
from otsdc.url.url_creator import MessageUrl
from otsdc.rest.resources import resources_properties
from otsdc.rest.model.response_model import ResponseStatus,MessageResponse,BulkResponse,MessageIDStatus,MessagesReportResponse,MessagesDetailsResponse

class MessageResource:
    __appSid = ''
    __messageUrl = None
    payload = None
    
    def __init__(self, appSid = None, messageUrl = None):
        self.__appSid = appSid
        self.__messageUrl = messageUrl
        
    def send(self, recipient = None, body = None, senderId = None, priority = None):
        if recipient is None :
            raise TypeError('Recipient is mandatory')
        if body is None :
            raise TypeError('Body is mandatory')
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        self.setPayload(payload, resources_properties.RECIPIENT,recipient)
        self.setPayload(payload, resources_properties.BODY,body)
        self.setPayload(payload, resources_properties.SENDERID,senderId)
        self.setPayload(payload, resources_properties.PRIORITY,priority)
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__messageUrl.urlSend(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            messageResp = MessageResponse(**(jsonResp['data']))
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,messageResp
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)
            
    def sendBulk(self, recipients = [], body = None, senderId = None, priority = None):
        if recipient is None :
            raise TypeError('Recipient is mandatory')
        if body is None :
            raise TypeError('Body is mandatory')
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        recipient = ''
        for recip in recipients:
            recipient = recipient + recip + ','
        
        if recipient != '' :
            recipient = recipient[0:(len(recipient)-1)]
            
        self.setPayload(payload, resources_properties.RECIPIENT,recipient)
        self.setPayload(payload, resources_properties.BODY,body)
        self.setPayload(payload, resources_properties.SENDERID,senderId)
        self.setPayload(payload, resources_properties.PRIORITY,priority)
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__messageUrl.urlSendBulk(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            bulkResp = BulkResponse(**(jsonResp['data']))
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,bulkResp
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)
        
    def getMessageIDStatus(self, messageId = None):
        if messageId is None :
            raise TypeError('messageId is mandatory')
        
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        self.setPayload(payload, resources_properties.MESSAGEID,messageId)
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__messageUrl.urlGetMessageIDStatus(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            messageResp = MessageIDStatus(**(jsonResp['data']))
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,messageResp
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)
    
    def getMessagesReport(self, dateFrom = None,dateTo = None,senderId = None,status = None, dlr = None, country = None):
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        self.setPayload(payload, resources_properties.DATE_FROM,dateFrom)
        self.setPayload(payload, resources_properties.DATE_TO,dateTo)
        self.setPayload(payload, resources_properties.SENDERID,senderId)
        self.setPayload(payload, resources_properties.STATUS,status)
        self.setPayload(payload, resources_properties.DLR,dlr)
        self.setPayload(payload, resources_properties.COUNTRY,country)
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__messageUrl.urlGetMessageReport(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            messageResp = MessagesReportResponse(**(jsonResp['data']))
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,messageResp
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)
        
    def getMessagesDetails(self, messageId = None, dateFrom = None,dateTo = None,senderId = None,status = None, dlr = None, country = None, limit = None, page = None):
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        self.setPayload(payload, resources_properties.MESSAGEID,messageId)
        self.setPayload(payload, resources_properties.DATE_FROM,dateFrom)
        self.setPayload(payload, resources_properties.DATE_TO,dateTo)
        self.setPayload(payload, resources_properties.SENDERID,senderId)
        self.setPayload(payload, resources_properties.STATUS,status)
        self.setPayload(payload, resources_properties.DLR,dlr)
        self.setPayload(payload, resources_properties.COUNTRY,country)
        self.setPayload(payload, resources_properties.LIMIT,limit)
        self.setPayload(payload, resources_properties.PAGE,page)
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        httpResponse = requests.post(self.__messageUrl.urlGetMessageDetails(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            messageResp = MessagesDetailsResponse(**(jsonResp['data']))
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,messageResp
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)
        
    
    def setPayload(self,payload = {}, key = None, val = None):
        if val is not None :
            payload[key] = val