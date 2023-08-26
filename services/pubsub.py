import redis

class PubSubService():
  def __init__(self) -> None:
    self.r = redis.Redis(host='ecommerce-redis', port=6379, decode_responses=True)

  def subscribe(self, channel: str):
    pubsub = self.r.pubsub()
    pubsub.subscribe(channel)

    return pubsub

  def publish(self, channel: str, msg: str) -> None:
    self.r.publish(channel, msg)

pubsub = PubSubService()