import asyncio
import aioredis
from flask import Flask
from prettyconf import config


DEBUG = config('DEBUG', cast=config.boolean, default=False)
CHANNEL = config('CHANNEL', default='test')
REDIS_HOST = config('REDIS_HOST', default='redis://redis')


async def go(msg):
    redis = await aioredis.create_redis_pool(
        REDIS_HOST)
    await redis.publish(CHANNEL, msg)
    redis.close()
    await redis.wait_closed()


loop = asyncio.get_event_loop()
app = Flask(__name__)


@app.route("/")
def notify():
    loop.run_until_complete(go('test message'))
    return "OK"
