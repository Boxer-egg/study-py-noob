import os
import time
import sys
import urllib.request
import schedule
print(sys.getsizeof(False))  # 28
print(sys.getsizeof(True))  # 28
print(sys.getsizeof(time))  # 72
print(sys.getsizeof('你好'))  # 78

print(time.time())
print(time.localtime())

# print(urllib.request.urlopen('https://www.github.com').read())

print(dir(schedule))
