#!/usr/bin/python
from urllib2 import urlopen

def main():
  print"Hello world"
  getData()

def getData():
    url = "https://dog.ceo/api/breeds/list/all"
    print(urlopen(url).read())

if __name__=='__main__':
  main()
