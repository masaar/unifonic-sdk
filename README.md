# SMS-Voice-PythonSDK

## Installation
Download the source code and then run:
```
python setup.py install
```
## Example

Here is the example to Use Message API
```python

from otsdc.rest.resources.message import MessageResource
from otsdc.url.http_url import HttpOTSUrl

urlHttp = HttpOTSUrl()
x = MessageResource(appSid='yourAppsID', messageUrl=urlHttp.getMessageURL())
(stat,resp) = x.send('962xxxxxxxxx', 'body')
print(stat)
print(resp)
print(resp.Balance)

```