from urllib.request import urlopen
from multiprocessing.dummy import Pool as ThreadPool
import time

urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
    'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/',
    'http://docs.python.org/devguide/',
    'http://www.python.org/community/awards/'
    # etc..
    ]


"""
# Make the Pool of workers
pool = ThreadPool(4)
# Open the urls in their own threads
# and return the results
results = pool.map(urllib2.urlopen, urls)
#close the pool and wait for the work to finish
pool.close()
pool.join()
"""


time_begin = time.clock()
results = []
for url in urls:
    result = urlopen(url)
    results.append(result)

time_end = time.clock()
print("1")
print(time_end - time_begin)

# ------- VERSUS ------- #


# ------- 4 Pool ------- #
time_begin = time.clock()

pool = ThreadPool(4)
results = pool.map(urlopen, urls)

time_end = time.clock()
print("4")
print(time_end - time_begin)

# ------- 8 Pool ------- #
time_begin = time.clock()

pool = ThreadPool(8)
results = pool.map(urlopen, urls)

time_end = time.clock()
print("8")
print(time_end - time_begin)

# ------- 13 Pool ------- #
time_begin = time.clock()

pool = ThreadPool(13)
results = pool.map(urlopen, urls)

time_end = time.clock()
print("13")
print(time_end - time_begin)




#end
