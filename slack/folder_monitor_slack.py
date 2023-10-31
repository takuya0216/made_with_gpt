import time
import os
from dotenv import load_dotenv

from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler, FileMovedEvent

from slackbot import SlackBot

class MyFolderHandlerSlack(FileSystemEventHandler):
    def __init__(self, slackbot=None):
        self.slackbot = slackbot

    def on_created(self, event):
        if event.is_directory:
            msg = f"フォルダ作成: {event.src_path}"
            print(msg)
            self.slackbot.send_message(msg)
        else:
            msg = f"ファイル作成: {event.src_path}"
            print(msg)
            self.slackbot.send_message(msg)

    def on_deleted(self, event):
        if event.is_directory:
            msg = f"フォルダ削除: {event.src_path}"
            print(msg)
            self.slackbot.send_message(msg)

        else:
            msg = f"ファイル削除: {event.src_path}"
            print(msg)
            self.slackbot.send_message(msg)

    def on_moved(self, event: FileMovedEvent):
        if event.is_directory:
            msg = f"フォルダ移動: {event.src_path} -> {event.dest_path}"
            print(msg)
            self.slackbot.send_message(msg)
        else:
            msg = f"ファイル移動: {event.src_path} -> {event.dest_path}"
            print(msg)
            self.slackbot.send_message(msg)

class Checker(MyFolderHandlerSlack):
    
    def __init__(self, path=None, slackbot=None):
        self.path = path
        self.slackbot = slackbot

    def watch(self):
        event_handler = MyFolderHandlerSlack(self.slackbot)
        observer = PollingObserver()
        
        if type(self.path) is list:
            for path in self.path:
                observer.schedule(event_handler, path, recursive=True)
        else:
            observer.schedule(event_handler, self.path, recursive=True)

        observer.start()
        print(f"Monitoring {self.path} for changes...")

        try:
            while True:
                time.sleep(5) 
        except KeyboardInterrupt:
            observer.stop()
        
        observer.join()

if __name__ == "__main__":
    #Slack OAuth Tokens
    token=''
    #Slack Channel ID for Message
    channel_id=''
    slackbot = SlackBot(token, channel_id)

    load_dotenv('./.env')
    path = os.environ['PATHES'].split(',') 
    
    chcker = Checker(path, slackbot) 
    chcker.watch()