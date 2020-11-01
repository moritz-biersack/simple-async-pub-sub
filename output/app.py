import asyncio
import aioredis
from prettyconf import config


CHANNEL = config('CHANNEL', default='test')
REDIS_HOST = config('REDIS_HOST', default='redis://redis')


async def main():
    redis = await aioredis.create_redis_pool(REDIS_HOST)

    ch1, = await redis.subscribe(CHANNEL)
    assert isinstance(ch1, aioredis.Channel)

    async def reader(channel):
        async for message in channel.iter():
            print("Got message:", message)
    asyncio.get_running_loop().create_task(reader(ch1))
    # await redis.wait_closed()


def run_server():
    loop = asyncio.get_event_loop()

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()


if __name__ == "__main__":
    print('Start listening...')
    run_server()
