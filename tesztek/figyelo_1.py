import os
import sys
import time
from test import *

class Watcher(object):
    running = True
    refresh_delay_secs = 1


    def __init__(self, watch_file, call_func_on_change=None, *args, **kwargs):
        self._cached_stamp = 0
        self.filename = watch_file
        self.call_func_on_change = call_func_on_change
        self.args = args
        self.kwargs = kwargs


    def look(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp

            print('File changed')
            if self.call_func_on_change is not None:
                self.call_func_on_change(*self.args, **self.kwargs)


    def watch(self):
        while self.running:
            try:

                time.sleep(self.refresh_delay_secs)
                self.look()
            except KeyboardInterrupt:
                print('\nDone')
                break
            except FileNotFoundError:

                pass
            except:
                print('Unhandled error: %s' % sys.exc_info()[0])

def custom_action(text):
    return str(ertek())

watch_file = 'hom.py'

watcher = Watcher(watch_file, custom_action, text='változott')
watcher.watch()
