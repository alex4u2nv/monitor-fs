import json
import time

import boto3
import uuid


class UpdateQueue:
    sqs = None
    queue_url = None

    def __init__(self, queue_url):
        self.queue_url = queue_url
        self.sqs = boto3.client('sqs')

    def test_queue(self):
        response = self.sqs.send_message(
            QueueUrl=self.queue_url,
            MessageBody="Testing " + time.ctime()
        )


    def put_event(self, event):
        message = json.dumps({
            "event_type": event.event_type,
            "is_directory": event.is_directory,
            "src_path": event.src_path
        })
        response = self.sqs.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message
        )
