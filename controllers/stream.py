from flask import Blueprint, Response
from services.pubsub import pubsub

stream = Blueprint('stream', __name__, url_prefix='/stream')

@stream.get('/')
def stream_listen():
  def stream_events():
    events = pubsub.subscribe('orders')

    for event in events.listen():
      yield f'data: {event}\n\n'
  
  return Response(stream_events(), mimetype='text/event-stream')