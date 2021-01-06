import argparse
import os

import yaml
from watchdog.events import FileSystemEventHandler

from monitor.services import UpdateQueue


class ConfigHandler:
    folders = []
    queue_url = ""
    config_file = None

    def __init__(self, args: argparse.Namespace):
        if args.folder and args.queue_url:
            self.folders = args.folder.split(",")
            self.queue_url = args.queue_url
        elif args.config_file:
            self.config_file = os.path.abspath(
                args.config_file if str(args.config_file).startswith("/") else os.getcwd() + "/" + args.config_file)
            if not os.path.exists(self.config_file):
                raise Exception("Config File {file} does not exist!".format(file=self.config_file))
            with open(self.config_file, "r") as yml_file:
                config = yaml.load(yml_file.read(), Loader=yaml.FullLoader)
                self.folders = config['folders']
                self.queue_url = config['queue_url']
        self.__verify_folder_paths()
        print("Queue_URL: " + self.queue_url)

    def __verify_folder_paths(self):
        valid_paths = []
        for folder in self.folders:
            if str(folder).startswith("/"):
                valid_paths.append(folder)
                folder_path = folder
            else:
                prefix = "/".join(self.config_file.split("/")[:-1]) if self.config_file else os.getcwd()
                folder_path = os.path.abspath(prefix + "/" + folder)
            if not os.path.exists(folder_path):
                raise Exception("Path {folder} to monitor doesn't exist".format(folder=folder_path))


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
