import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileMovedEvent

class MyFolderHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            print(f"Directory created: {event.src_path}")
        else:
            print(f"File created: {event.src_path}")

    def on_deleted(self, event):
        if event.is_directory:
            print(f"Directory deleted: {event.src_path}")
        else:
            print(f"File deleted: {event.src_path}")

    def on_moved(self, event: FileMovedEvent):
        if event.is_directory:
            print(f"Directory moved: {event.src_path} -> {event.dest_path}")
        else:
            print(f"File moved: {event.src_path} -> {event.dest_path}")

class Checker(MyFolderHandler):

    def __init__(self, path=None):
        self.path = path

    def watch(self):
        event_handler = MyFolderHandler()
        observer = Observer()
        
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
    path = "/Volumes/aichidijital/"
    chcker = Checker(path) 
    chcker.watch()
