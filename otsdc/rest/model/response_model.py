from otsdc.rest.resources import resources_properties
from collections import namedtuple

ResponseStatus = namedtuple('ResponseStatus', 'success,message,errorCode')
MessageResponse = namedtuple('MessageResponse','MessageID,Status,Recipient,NumberOfUnits,Cost,Balance,TimeCreated,CurrencyCode')
BulkResponse = namedtuple('BulkResponse','Messages,NumberOfUnits,Cost,Balance,TimeCreated,CurrencyCode')
MessageIDStatus = namedtuple('MessageIDStatus','Status,DLR')
MessagesReportResponse = namedtuple('MessagesReportResponse','Cost,TotalTextMessages,NumberOfUnits,CurrencyCode')
MessagesDetailsResponse = namedtuple('MessagesDetailsResponse','messages,CurrencyCode,TotalTextMessages,Page')