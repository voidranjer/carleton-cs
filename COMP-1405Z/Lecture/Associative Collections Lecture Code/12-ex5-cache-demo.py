#Write a program that has two functions – read(url) and cachedread(url, cache).

import time
import webdev

#read the url and return the contents
def read(url):
    contents = webdev.readurl(url)
    return contents


cache = {}

#read the url if it is not in the cache, update the cache, and return the contents
#if the url is in the cache, return the contents immediately
def cachedread(url):
    if url in cache:
        return cache[url]
    contents = read(url)
    cache[url] = contents
    return contents

import random
repeats = 50
start = time.time()
for i in range(repeats):
    url = "https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-" + str(random.randint(0,9)) + ".html"
    read(url)
end = time.time()
print("Uncached reads took : " + str(end-start) + " seconds")

start = time.time()
for i in range(repeats):
    url = "https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-" + str(random.randint(0,9)) + ".html"
    cachedread(url)
end = time.time()
print("Cached reads took : " + str(end-start) + " seconds")


for i in range(repeats):
    url = "https://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-" + str(random.randint(0,9)) + ".html"
    if read(url) != cachedread(url):
        print("There is something wrong here.")
