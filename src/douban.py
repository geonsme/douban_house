# -*- coding:utf-8 -*-

import requests
import setting
import io
import sys

def main():
    req = None
    url = 'https://www.douban.com/group/539160/discussion?start=100'
    try:
        #req = requests.get(url)
        #print (req.content)
        print ("%s" % u'这是我')
    except Exception, e:
        print str(e)
        return

if __name__ == "__main__":
    print 'zz打发打发'
    main()