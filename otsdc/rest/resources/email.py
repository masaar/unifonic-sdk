import requests
from otsdc.url.url_creator import EmailUrl
from otsdc.rest.resources import resources_properties
from otsdc.rest.model.response_model import ResponseStatus, EmailResponse, EmailReportResponse

class EmailResource:
    __appSid = ''
    __emailUrl = None
    payload = None
    
    def __init__(self, appSid = None, emailUrl = None):
        self.__appSid = appSid
        self.__emailUrl = emailUrl
        
    def send(self,sender = None, recipient = None, body = None, subject = None):
        if sender is None:
            raise TypeError('sender is mandatory')
        
        if recipient is None:
            raise TypeError('recipient is mandatory')
        
        if body is None:
            raise TypeError('body is mandatory')
        
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        self.setPayload(payload, resources_properties.FROM,sender)
        self.setPayload(payload, resources_properties.RECIPIENT,recipient)   
        self.setPayload(payload, resources_properties.BODY,body)
        self.setPayload(payload, resources_properties.SUBJECT,subject)          
        httpResponse = requests.post(self.__emailUrl.urlSend(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            messageResp = EmailResponse(**(jsonResp['data']))
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,messageResp
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)
    
    def getEmailsReport(self,emailStatus = None, subject = None, dateCreated = None, sender = None, dateFrom = None, dateTo = None):
        payload = {}
        payload[resources_properties.APPSID] = self.__appSid
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        self.setPayload(payload, resources_properties.EMAIL_STATUS,emailStatus)
        self.setPayload(payload, resources_properties.SUBJECT,subject)   
        self.setPayload(payload, resources_properties.DATE_CREATED,dateCreated)
        self.setPayload(payload, resources_properties.FROM,sender)      
        self.setPayload(payload, resources_properties.DATE_FROM,dateFrom)      
        self.setPayload(payload, resources_properties.DATE_TO,dateTo)          
        httpResponse = requests.post(self.__emailUrl.urlGetEmailReport(),data=payload, headers = headers)
        if httpResponse.status_code < 400 :
            jsonResp = httpResponse.json()
            messageResp = EmailReportResponse(**(jsonResp['data']))
            del jsonResp['data']
            respStat = ResponseStatus(**jsonResp)
            return respStat,messageResp
        else :
            print(httpResponse)
            raise Exception(str(httpResponse.status_code) + httpResponse.text)
    
    def setPayload(self,payload = {}, key = None, val = None):
        if val is not None :
            payload[key] = val

