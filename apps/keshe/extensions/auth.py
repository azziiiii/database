from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
import jwt
from jwt import exceptions


class JwtQueryAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        salt = settings.SECRET_KEY
        try:
            payload = jwt.decode(token, salt, True)
        except exceptions.ExpiredSignatureError:
            raise AuthenticationFailed({'code': '401', 'error': '登录超时,请重新登录'})
        except jwt.InvalidTokenError:
            raise AuthenticationFailed({'code': '401', 'error': '用户不存在或未登录'})
        return (payload, token)
