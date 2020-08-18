# 🔍 Channels를 사용하여 채팅구현 하기

## 🔍 개발환경
* Django 3.1
* Docker
* redis

## 🔍 구성
* 참가할 대화방의 이름을 입력
* 대화방에 게시된 메시지 보기

## 🔍 Docker를 통한 Redis 설치 후 프로젝트와 연동
```
docker run -p 6379:6379 -d redis:5
```

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