import urllib.request
import sys

#returns the string contents of the page at url, or "" if there is an error
def readurl(url):
	try:
		fp = urllib.request.urlopen(url)
		mybytes = fp.read()

		mystr = mybytes.decode(sys.stdout.encoding)
		fp.close()
		return mystr
	except Exception as e:
		print(e)
		print("Failed to read: " + url)
		return ""
