from pygame import *
import sys,os,shutil
from time import sleep

def choosing_pictures():
	pictures=[]
	for dirname,dirnames,filenames in os.walk('.'):
		for index,dirs in enumerate(dirnames):
			print'%s %10s' % (dirs,index)
		break

	choice=raw_input("choose >>> ")	

	directory='./%s' %dirnames[int(choice)]
	print directory

	for dirname,dirnames2,filenames in os.walk(directory):
		for filename in filenames:
			files=directory+'/'+filename
			pictures+=[files]
	return pictures,filenames,choice,dirnames

def get_dir():
	global dirnaems,choice
	final_dir=''
	for char in dirnames[int(choice)]:
		if char==' ':
			final_dir+='\\'
		final_dir+=char
	return final_dir

#def moving_file():
#	global dirnames,filenames,choice,pictures,i
#	final_dir=get_dir()
#	direc='mv ~/Pictures/htp/%s/%s ~/Pictures/gnc' % (final_dir,filenames[i])
#	print direc
#	os.system(direc)
	

def checkevents():
	global check,filenames,i,pictures,filenames
	final_dir=''
	for events in event.get():
		if events.type==QUIT:
			quit()
			sys.exit()
		if events.type==KEYDOWN:
			if events.key==K_UP:
				check=0
			if events.key==K_RIGHT:
				check=350
	#		if events.key==K_LEFT:
#				check=-4
#				moving_file()
#				pictures.pop(i)
#				filenames.pop(i)
#				i-=1
			if events.key==K_DOWN:
				check=350
				i-=2
				break
#			if events.key==K_q:
#				final_dir=get_dir()
#				del_pics=0
#				while del_pics<i:
#					current_pic=filenames[del_pics]
#					query='rm ~/Pictures/cele/%s/%s'%(final_dir,current_pic)
#					print query
#					os.system(query)
#					del_pics+=1
#				quit()
#				sys.exit()
	clock.tick(100)
	if check<=300:
		check+=1
		checkevents()

def resize_pic():
	global images,image_w,image_h
	if image_h>image_w:
		ratio=float(image_w)/float(image_h)
		nw=round(ratio*h)
		images=transform.scale(images,(nw,h))
	elif image_w>image_h:
		ratio=float(image_w)/float(image_h)
		nh=round(w/ratio)
		images=transform.scale(images,(w,nh))

	return images

pictures,filenames,choice,dirnames=choosing_pictures()

w=1370
h=690
check=0
picture=display.set_mode((w,h))
WHITE=(255,255,255)
clock=time.Clock()
length=len(pictures)
i=0

while i<length:
	images=image.load(pictures[i])
	image_w=images.get_width()
	image_h=images.get_height()
	if image_w>w or image_h>h:
		images=resize_pic()

	picture.fill(WHITE)
	picture.blit(images,(0,0))
	clock.tick(1)
	display.update()

	checkevents()
	i+=1
	check=0

