import datetime
import jwt
from django.conf import settings


def create_token(payload, timeout=5):
    salt = settings.SECRET_KEY
    headers = {'typ': 'jwt', 'alg': 'HS256'}
    salt = '2g5iu3489yfhdsiunbf802njdc897dffja03h2i5r1289juewhuiofhqio'
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout),  # 设置Token过期时间
    token = jwt.encode(payload=payload, key=salt, algorithm='HS256')
    return token
