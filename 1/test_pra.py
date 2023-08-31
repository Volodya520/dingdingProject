import requests
import time
import hmac
import hashlib
import base64
import urllib.parse
timestamp = str(round(time.time() * 1000))

secret = 'SEC7a6b03b91f2891c258bc59254160c9cbef453261d0b752932c47c39db2cfb653'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
print(sign)
print(timestamp)

