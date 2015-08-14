# SMS-Voice-PythonSDK

## Installation
Download the source code and then run:
```
python setup.py install
```
## Example

Here is the example to Use Message API
```python

from otsdc.rest.client import OTSRestClient
from otsdc.url.http_url import HttpOTSUrl

client = OTSRestClient(appSid='yourAppSid')

acct = client.accountResource
(stat,resp) = acct.getBalance()
print(stat)
print(resp)

msg = client.messageResource
(stat,resp) = msg.send('9627xxxxxxx', 'Content Msg')
print(stat)
print(resp)

```