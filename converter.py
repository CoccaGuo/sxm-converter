# converter.py by CoccaGuo at 2020/12/04 13:49
# converter.py by CoccaGuo at 2020/12/05 14:07 + @_convert_it decorator
# converter.py by CoccaGuo at 2020/12/05 15:14 + multithread support. note that matplotlib GUI(Qt) won't work outside of main thread.
import random, os
import threading
from functools import wraps
from typing import IO
import matplotlib.pyplot as plt
import sxm2png

#config format
class Config:
    def __init__(self) -> None:
        self.output_dir = None
        self.target_dir = None
        self.format = ".png"
        self.fig_channel = "Current"
        self.threads = 1
        self.convert_percent = 0.05 

    @staticmethod
    def default():
        return Config()
    

class Converter:
    def __init__(self, cfg: Config):
        self.cfg = cfg

    def __convert_it(func):
        @wraps(func)
        def convert(this):
            plt.gca() # activate a Qt app in main thread
            list_iter = iter(func(this))
            iter_lock = threading.Lock()
            thread_list = [_Convert_thread(this.cfg, list_iter, iter_lock) for i in range(this.cfg.threads)]
            try:
                for thread in thread_list: thread.start()
            except StopIteration as e:
                for thread in thread_list: thread.join()
                print("finished.")
        return convert

    @__convert_it
    def convert_all(self):
        return os.listdir(self.cfg.target_dir)
    
    @__convert_it
    def convert_randomly(self):
        dir_list = os.listdir(self.cfg.target_dir)
        return random.sample(dir_list, int(len(dir_list)*self.cfg.convert_percent))


class _Convert_thread(threading.Thread):
    def __init__(self, cfg, list_iter, iter_lock: threading.Lock):
        super(_Convert_thread, self).__init__()
        self.cfg = cfg
        self.list_iter = list_iter
        self.iter_lock = iter_lock

    def run(self):
        while True:
            file = ""
            self.iter_lock.acquire()
            file = next(self.list_iter)
            self.iter_lock.release()
            sxm2png.save(os.path.join(self.cfg.target_dir, file), os.path.join(self.cfg.output_dir, file + self.cfg.format), channel=self.cfg.fig_channel)
            print("working with: "+os.path.join(self.cfg.target_dir, file))




