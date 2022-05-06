from util import getEnviroment
import redis
import Sender
from rq import Queue

env = getEnviroment.getEnvData()


class Worker:
    def __init__(self):
        pass

    def getConnection(self):
        return redis.client.Redis(
            host=env.get("redis_host"),
            port=env.get("redis_port"),
            db=env.get("redis_db"),
            password=env.get("redis_password")
        )

    def start(self):
        print("Wpp Worker Started....")
        from rq import Connection
        from rq import Worker as WorkerModule
        import sys

        with Connection():
            redis = self.getConnection()
            queue = Queue(connection=redis)
            w = WorkerModule(queues=[queue], connection=redis)
            w.work(with_scheduler=True)


if __name__ == "__main__":
    worker = Worker()
    worker.start()
