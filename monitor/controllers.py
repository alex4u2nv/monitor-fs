from watchdog.events import FileSystemEventHandler

from monitor.services import UpdateQueue


class EventsHandler(FileSystemEventHandler):
    """Monitor folder  and push events to SQS """
    updatequeue = None

    def __init__(self, updatequeue: UpdateQueue):
        self.updatequeue = updatequeue

    def on_moved(self, event):
        super(EventsHandler, self).on_moved(event)
        self.updatequeue.put_event(event)

    def on_created(self, event):
        super(EventsHandler, self).on_created(event)
        self.updatequeue.put_event(event)

    def on_deleted(self, event):
        super(EventsHandler, self).on_deleted(event)
        self.updatequeue.put_event(event)

    def on_modified(self, event):
        super(EventsHandler, self).on_modified(event)
        self.updatequeue.put_event(event)
