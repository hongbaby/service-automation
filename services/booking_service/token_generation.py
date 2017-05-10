import time
import random
import hashlib
import hmac
import base64


# consumeKey, maxAge
def dict_to_string(dict_data={}):
    a = []
    if not dict_data:
        for key in sorted(dict_data.iterkeys()):
            a.append((key + "=" + dict_data[key]))
        return ''.join(a)
    else:
        return ''


def convert_bytes_to_string(str):
    result = ''
    first = True
    for c in str:
        if first and c == '0':
            pass
        else:
            result = result + c
        first = not first
    return result


def generate_token(consume_key='abcd12341234'):
    secret_key = "oboe_secret_1234567890-=!@#$%^&*()_+"
    timestamp = str(time.time()).split('.')[0]
    nonce = str(random.randint(100000, 999999))

    dict_data = {'ConsumerKey': consume_key, 'Timestamp': timestamp, 'Nonce': nonce}
    security_data = dict_to_string(dict_data)

    return convert_bytes_to_string(hmac.new(secret_key, security_data, hashlib.sha1).hexdigest())
