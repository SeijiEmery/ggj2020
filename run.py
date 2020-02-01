#!/usr/bin/env python3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from subprocess import Popen
from multiprocessing import Process
import time

currently_running_process = None

def rebuild(cmd="dub run", launch_new_process=True):
    global currently_running_process

    if currently_running_process is not None:
        retcode = currently_running_process.poll()
        if retcode is None:
            print("Killing currently running process...")
            currently_running_process.terminate()
            currently_running_process.wait()
            print("terminated with returncode %s" % currently_running_process.returncode)
            currently_running_process = None
        else:
            print("process already terminated with returncode %s" % currently_running_process.returncode)

    if launch_new_process:
        print("launching new process")
        currently_running_process = Popen(cmd.split(), shell=False)

def matches_event_filter(path, event_type):
    if path.endswith('.d') or path.endswith('.py'):
        if event_type in ('modified', 'added', 'deleted'):
            return True
        print('observed unknown change on file "%s": %s' % (path, event_type))
        return True
    return False

class FileWatcher (FileSystemEventHandler):
    def on_any_event(self, event):
        if matches_event_filter(event.src_path, event.event_type):
            print("change on observed d file! '%s': '%s'" % (event.src_path, event.__class__.__dict__))
            rebuild()

def start_file_watchers():
    observer = Observer()
    observer.schedule(FileWatcher(), '.', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    # rebuild()
    start_file_watchers()
