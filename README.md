# 🔍 Django Channels tutorial

## 🔍 개발환경
* Django 3.1
* Docker
* redis

## 🔍 구성
* 참가할 대화방의 이름을 입력
* 대화방에 게시된 메시지 보기

## 🔍 개념정리
* `Websocket`이란 실시간으로 양방향 통신이 가능하게 해주는 기술이다. Web 환경은 HTTP 기반인 `요청 및 응답` 으로 데이터를 주고받기 때문에 네트워크 연결을 실시간으로 유지하지 않는다. 그렇기 때문에 실시간으로 데이터를 주고 받기위한 새로운 개념인 `WebSocket` 이 필요하게 됐다.

* `Channels` 는 간단하게 말하면 HTTP 프로토콜뿐 아니라, 장기간 연결을 필요로 하는 프로토콜인 WebSockets, chat protocols, IoT protocols 등을 핸들링할 수 있도록 해준다.

* `ASGI`는 Asyncrhonous Server Gateway Interface의 약자로 쉽게 설명하면 WSGI의 비동기식 버전이다.

## 🔍 Docker를 통한 Redis 설치 후 프로젝트와 연동
* 튜토리얼에서는 backing store로서 Redis를 채널 레이어로 사용했다. port 6379에서 Redis server를 run하고, chennel_redis를 설치해야 한다.
```
docker run -p 6379:6379 -d redis:5
```
``` 
python3 -m pip install channels_redis
```

* settings.py 에 채널 레이어를 설정한다.
```python
# settings.py

ASGI_APPLICATION = 'chatsite.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
```

* 도커는 [Docker install](https://www.docker.com/get-started) 에서 다운받으면 된다.


## 🔍참고문서 및 블로그
* [https://channels.readthedocs.io/en/latest/tutorial/part_1.html#](https://channels.readthedocs.io/en/latest/tutorial/part_1.html#)
* [채널 Channel & 웹소켓 Websocket (feat.django tutorial)](https://velog.io/@matisse/Django-advanced-channel-socket)
* [[Django] Channels, 비동기적 채팅 구현하기 - WebSocket](https://ssungkang.tistory.com/entry/Django-Channels-%EB%B9%84%EB%8F%99%EA%B8%B0%EC%A0%81-%EC%B1%84%ED%8C%85-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-WebSocket-1)