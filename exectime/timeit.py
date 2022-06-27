# coding: utf-8

__author__ = 'Mário Antunes'
__version__ = '0.1'
__email__ = 'mariolpantunes@gmail.com'
__status__ = 'Development'


import math
import time
import numpy as np


def RSE(y, y_hat):
    RSS = np.sum(np.square(y - y_hat))
    rse = math.sqrt(RSS / (len(y) - 2))
    return rse


def exectime(n):
    def decorate(fn):
        def wrapper(*args, **kwargs):
            # execute first time
            begin = time.perf_counter()
            rv = fn(*args, **kwargs)
            end = time.perf_counter()

            # durations list 
            durations = [end-begin]

            for i in range(1, n):
                begin = time.perf_counter()
                for _ in range(i+1):
                    fn(*args, **kwargs)
                end = time.perf_counter()

                durations.append(end-begin)
            
            # convert to milliseconds:
            durations = [1000*seconds for seconds in durations]

            x = np.arange(1, n+1)
            m, b = np.polyfit(x, durations, 1)

            y_hat = x*m+b

            return m, RSE(durations, y_hat), rv
        return wrapper
    return decorate