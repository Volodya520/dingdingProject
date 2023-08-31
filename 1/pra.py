import requests
import time
import hmac
import hashlib
import base64
import urllib.parse

def secret_msg():
    timestamp = str(round(time.time() * 1000))
    secret = 'SEC7a6b03b91f2891c258bc59254160c9cbef453261d0b752932c47c39db2cfb653'
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return sign,timestamp

def report_message():
    webhook="https://oapi.dingtalk.com/robot/send?access_token=219d8a9961c4a6a50d9d55554551f368770ea9e3df63955f6b6d053994a3e1f3"
    sign,timestamp=secret_msg()
    url='%s&sign=%s&timestamp=%s'%(webhook,sign,timestamp)
    data = {
     "msgtype": "markdown",
     "markdown": {
         "title":"日报填写",
         "text": "#### 日报填写   \n "
                 "> [点击进入飞书填写日报](https://ai7co363eo.feishu.cn/base/IJHcbX38SaKDtYsu7OycKiqmn2d?table=tbl0owhxs3eACaOm&view=vewGcZ1swG)"
     },
      "at": {
          "atMobiles": [
              "13091799490"
          ],
          "atUserIds": [
              "user123"
          ],
          "isAtAll":True
      }
    }
    res = requests.post(url, json=data)
    return res

if __name__ == '__main__':
    report_message()


