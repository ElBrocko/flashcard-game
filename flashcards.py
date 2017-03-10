#flashcards for breakfast hour

import sys
import random

questions = {'initialize repo':'git init', 'change directories':'cd', 'find out where we are':'pwd', 'kill a program in terminal': 'control+c','clear your terminal screen': 'control+k', 'create new file': 'touch', 'view all files in finder': 'open .', 'remove something': 'rm', 'remove everything forever and potentially cry': 'rm -rf', 'navigate two directories up': '../..', 'display everything in a file': 'cat', 'display everything in a file page by page': 'less', 'add everything in a folder to staging area': 'git add .', 'commit changes in git': 'git commit -m', 'push changes to repo': 'git push', 'add and commit tracked files in git at the same time': 'git -a -m', 'download a git repo':'git clone', 'look at the history of a repo': 'git log', 'get a list of files not tracked by git': 'git status', 'look at changes in the repo before staging and committing': 'git diff', 'make a new directory': 'mkdir', 'list everything within a directory': 'ls', 'copy a file or directory': 'cp', 'move a file or directory':'mv', 'change permission modifiers': 'chmod'}
# responses = ['git init', 'cd', 'pwd']


def flashcards(questions):
	shuffle_dict = questions.items()
	random.shuffle(shuffle_dict)
	for key, value in shuffle_dict:
		print key
		try:
		 	answer = str(input("Enter your response as a string \n"))
		 	if answer == value:
				print "Yay!"
			else:
				print "Hmm. What I had was: " + value
		except:
			print "I said 'as a string'!"
			sys.exit()

flashcards(questions)
