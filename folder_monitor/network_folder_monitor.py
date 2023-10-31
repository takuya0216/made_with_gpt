import time
from watchdog.observers.polling import PollingObserver
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
    folders = ['/Volumes/aichidijital/sanjudo',
    '/Volumes/aichidijital/sineiadag',
    '/Volumes/aichidijital/meiwapr',
    '/Volumes/aichidijital/freebox66',
    '/Volumes/aichidijital/adcommuni',
    '/Volumes/aichidijital/nittoad',
    '/Volumes/aichidijital/salcom',
    '/Volumes/aichidijital/comhouse',
    '/Volumes/aichidijital/shinkoagency',
    '/Volumes/aichidijital/kotayakuba',
    '/Volumes/aichidijital/adcremoo',
    '/Volumes/aichidijital/naganaepri',
    '/Volumes/aichidijital/eisyoudo',
    '/Volumes/aichidijital/toyoprint',
    '/Volumes/aichidijital/adtown',
    '/Volumes/aichidijital/igarashipr',
    '/Volumes/aichidijital/fukuhakudcs',
    '/Volumes/aichidijital/totaladco',
    '/Volumes/aichidijital/spotlight',
    '/Volumes/aichidijital/piagoapita'
    ]
    path = "/Volumes/aichidijital"
    
    checker = Checker(folders)
    checker.watch()
    
