

import datetime
from flask import request
import jwt

from config import JWT_SECRET_KEY

# 토큰 유효성 검증 함수


def getUserEmail():
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, JWT_SECRET_KEY,
                         algorithms=['HS256'])
    email = payload['email']
    return email


def isTokenVaild():

    token_receive = request.cookies.get('mytoken')
    print(token_receive)
    try:
        # decode
        payload = jwt.decode(token_receive, JWT_SECRET_KEY,
                             algorithms=['HS256'])
        print(payload)
        
        # 만약 이렇게 다 구현할거면
        # decode된 결과가 조작이되지않았는지 검사하는 기능도 필요하다.1

        # 라이브러리 더 찾아보고 해야겠다..
        expire_time = datetime.datetime.strptime(
            payload['expire'], '%Y-%m-%d %H:%M:%S')
        print(expire_time)
        if expire_time < datetime.datetime.now():
            # 만료 시간이 현재 시각보다 이전인 경우 로그인 페이지로 리디렉션
            print("Token has expired")
            return False
        else:
            # 로그인 성공
            print("로그인성공")
            return True
    except:
        return False
