import praw
import requests
import os
import glob
import random
import sys
import shutil

maxMemes=21
subredditlist = ['memes','dankmemes'];
subredditpoststoignorelist = [1,2];



def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if (47 < ord(c) < 58 or 64 < ord(c) < 91 or 96 < ord(c) < 123 or ord(c)==32))
    return ''.join(stripped)



reddit = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')







fileDir = os.path.dirname(os.path.realpath('__file__'))







subdirectories = os.listdir(fileDir)

if 'memes' in subdirectories:
	shutil.rmtree('memes')



fileDir=fileDir+'\memes'

os.makedirs(fileDir)



for i in range(0,len(subredditlist)):
	c=subredditlist[i]
	postsToIgnore=subredditpoststoignorelist[i]
	subreddit = reddit.subreddit(c)

	if not os.path.exists(''+fileDir+'/'+c+'Hot'):
		os.makedirs(''+fileDir+'/'+c+'Hot')



	i=0



	for submission in subreddit.hot(limit=maxMemes+postsToIgnore):
		if(i<postsToIgnore):
			i=i+1
			continue
		if('.png' in submission.url):
			filename = os.path.join(fileDir, ''+c+'Hot/'+''+str(random.randint(0,200))+' - '+strip_non_ascii(submission.title)+'.png')
		else:
			filename = os.path.join(fileDir, ''+c+'Hot/'+''+str(random.randint(0,200))+' - '+strip_non_ascii(submission.title)+'.jpg')
		f = open(filename,'wb')
		f.write(requests.get(''+submission.url).content)
		f.close()
		i=i+1


	if not os.path.exists(''+fileDir+'/'+c+'New'):
		os.makedirs(''+fileDir+'/'+c+'New')




	i=0



	for submission in subreddit.new(limit=maxMemes+postsToIgnore):
		if(i<postsToIgnore):
			i=i+1
			continue
		if('.png' in submission.url):
			filename = os.path.join(fileDir, ''+c+'New/'+''+str(random.randint(0,200))+' - '+strip_non_ascii(submission.title)+'.png')
		else:
			filename = os.path.join(fileDir, ''+c+'New/'+''+str(random.randint(0,200))+' - '+strip_non_ascii(submission.title)+'.jpg')
		f = open(filename,'wb')
		f.write(requests.get(''+submission.url).content)
		f.close()
		i=i+1


