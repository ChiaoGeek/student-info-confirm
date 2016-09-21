#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Image
import ImageDraw
import MySQLdb
import datetime
import time
import ImageFont
import os, sys 
def convetpic(impath,text):	#input: the path needed to be convert. Output: the object of  converted  image
	im = Image.open(impath)
	new = Image.new('RGB', (95,176), 'white')
	out = im.resize((95,136))
	new.paste(out, (0,0))
	draw = ImageDraw.Draw(new)
	ttfont = ImageFont.truetype ('/usr/share/fonts/truetype/windows/msyh.ttf', 14)
	text = text.decode('UTF-8')
	xy = ttfont.getsize(text)
	xy = ((95 - xy[0])/2,140) 
	draw.text(xy,text, font = ttfont,fill="black")
	return new

#convetpic('/home/chiaochiong/paste/a.jpg','函数调用').save('/home/chiaochiong/python/x.jpg')
# convetpic('/home/chiaochiong/paste/a.jpg')




db = MySQLdb.connect("localhost", "root", "", "sw", charset="utf8")
cursor = db.cursor()
i = 0
sql = "select * from `sw_stu`"
try:
   cursor.execute(sql)
   rows = cursor.fetchall()
   if rows:
   	for row in rows:
   		pic = '/home/chiaochiong/zp/'+row[5]+'.jpg'
   		if os.path.exists(pic):
   			i = i + 1  		
   			convetpic(pic, row[6]).save('/home/chiaochiong/sw/convert/'+row[5]+'.jpg')

   		else:
   			print row[0]
   	print i

except:
   db.rollback()


db.close()
