import sys
sys.path.insert(0, './libs')
import helper

def render():
	print(helper.greeting('Peter', 'Parker'))


render()


###########################################
from helper import greeting
def render():
	print(greeting('Peter', 'Parker'))


render()

###########################################
import helper as hp
def render():
	print(hp.greeting('Peter', 'Parker'))


render()