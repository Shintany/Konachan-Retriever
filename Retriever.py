from bs4 import BeautifulSoup
from tools import *
import threading
import time
import shutil
import requests
#import urllib
from urllib.request import *

class Retriever(threading.Thread):
    def __init__(self, _tagList, _nb, pbl, labellist):        
        self.tagList = _tagList
        self.nb = _nb
        self.pbl = pbl
        self.labellist = labellist
        threading.Thread.__init__(self)

    def run(self):
        # print('Running multithreading (', len(self.tagList), '...')
        for i in range(0, len(self.tagList)):
            # print ('Thread created')
            ThreadedTask(self.tagList[i], self.nb, self.pbl[i], self.labellist[i]).start()

class ThreadedTask(threading.Thread):
    def __init__(self, _tag, _nb, _pb, _label):
        self.downloaded = 0
        self.tag = _tag
        self.nb = _nb
        self.pb = _pb
        self.label = _label
        threading.Thread.__init__(self)

    def run(self):
        # print('This Thread will take in charge : ' + self.tag)
        i = 1
        path = 'data/' + self.tag + '/'
        nb_file = create_directory(path)
        while(self.downloaded != self.nb):
            if i == 1:
                url = "https://konachan.com/post?tags=" + self.tag
            else:
                url = "https://konachan.com/post?page=" + str(i) + "&tags=" + self.tag
            # print ('Connecting to ' + url)

            response = requests.get(url, stream=True)

            if(response.status_code == 200):
                #print ('Connected!')

                # INITIALIZING VARS
                database_path = path + 'database.csv'
                data = response.text
                soup = BeautifulSoup(data, 'lxml')

                # FINDING <ul id=post-line-posts/>
                content = soup.find('ul', {'id': 'post-list-posts'})
                if type(content) == 'NoneType':
                    exit()
                database = open(database_path, 'a')
                for link in content.find_all('a', 'directlink'):
                    # CHECK IF THE IMAGE WAS ALREADY DOWNLOADED
                    if not already_dl(link['href'], database_path):
                        f = open('data/' + self.tag + '/' + str(self.downloaded+nb_file) + '.jpg', 'wb')
                        f.write(urlopen(link['href']).read())
                        f.close()
                        database.write(link['href'])
                        database.write('\n')
                        self.downloaded = self.downloaded + 1
                        prct = (float(self.downloaded) /
                        float(self.nb)) * 100
                        # print 'Progress :',prct, "% -> Tag : " + self.tag
                        self.pb['value'] = prct
                    if(self.downloaded == self.nb):
                        break
                    # END IF
                # END FOR
                database.close()
            # END IF
            else:
                print ('This tag ' + self.tag + ' do not seem to exist...')
                break
            # END ELSE
            del response
            i = i + 1
        # END WHILE
        self.pb['value'] = 0
        self.label.pack_forget()
        self.pb.pack_forget()
        # print ('Done!')
