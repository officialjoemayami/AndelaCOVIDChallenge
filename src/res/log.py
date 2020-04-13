import logging
import time

class LOG():
    def __init__(self, path):
        # configure logging
        self.path = path

    # using infomation log
    def info(self):
        logging.getLogger('estimator').setLevel(logging.INFO)
        logging.basicConfig(filename='covid.log', level=logging.INFO, format='%(message)s \t\t done in %(asctime)s seconds', datefmt='%M:%S')
        return logging.info(f' {time.time()} \t\t {self.path}') # console log to covid.log
    
    # using warning log
    def warning(module):
        logging.getLogger(module).setLevel(logging.WARNING)