from otsdc.rest.resources import resources_properties
from collections import namedtuple

ResponseStatus = namedtuple('ResponseStatus', 'success,message,errorCode')
MessageResponse = namedtuple('MessageResponse','MessageID,Status,Recipient,NumberOfUnits,Cost,Balance,TimeCreated,CurrencyCode')
BulkResponse = namedtuple('BulkResponse','Messages,NumberOfUnits,Cost,Balance,TimeCreated,CurrencyCode')
MessageIDStatus = namedtuple('MessageIDStatus','Status,DLR')
MessagesReportResponse = namedtuple('MessagesReportResponse','Cost,TotalTextMessages,NumberOfUnits,CurrencyCode')
MessagesDetailsResponse = namedtuple('MessagesDetailsResponse','messages,CurrencyCode,TotalTextMessages,Page')

Balance = namedtuple('Balance','Balance,CurrencyCode,SharedBalance')
SenderID = namedtuple('SenderID','SenderID,IsDefault,Status,DateCreated')
SenderList = namedtuple('SenderList','senderNames')

EmailResponse = namedtuple('EmailResponse','EmailID,EmailStatus,Cost,Balance,Recipient,TimeCreated')
EmailReportResponse = namedtuple('EmailReportResponse','Cost,TotalEmails,CurrencyCode')

GetCodeResponse = namedtuple('GetCodeResponse','MessageID,Status,Recipient,NumberOfUnits,Cost,CurrencyCode,Balance,TimeCreated')

CallResponse = namedtuple('CallResponse','CallStatus,CallDuration,Cost,Balance,DateCreated,DateStarted,DateEnded,Recipient,CallID')
CallStatusResponse = namedtuple('CallStatusResponse','callStatus,CallDuration,Price,DateCreated,DateStarted,DateEnded')
CallsDetailsResponse = namedtuple('CallsDetailsResponse','calls,CurrencyCode,TotalVoiceMessages,Page')
TTSCallResponse = namedtuple('TTSCallResponse','CallID,CallStatus,CallDuration,Price,Balance,Recipient,DateCreated')