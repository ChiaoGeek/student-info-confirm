#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Image
import ImageDraw
import MySQLdb
import datetime
import time
import ImageFont
import os, sys 
########################################################################################################
def pasteimg(impath,department,stuclass,cord):   #input: the path needed to be convert. Output: the object of  converted  image
   im = Image.open(impath)
   page = str(cord[0])
   x = cord[1]
   y = cord[2]
   left = 20*y+(y-1)*95
   up = 80+(x-1)*176
   if not os.path.exists('/home/chiaochiong/sw/result/'+department+'/'+stuclass+'_'+page+'.jpg'):
      new = Image.new('RGB',(595,842),'white')
      draw = ImageDraw.Draw(new)
      ttfont = ImageFont.truetype('/usr/share/fonts/truetype/windows/msyh.ttf', 23)
      ttfont2 = ImageFont.truetype('/usr/share/fonts/truetype/windows/msyh.ttf', 18)
      text = stuclass+"班新生信息确认表"
      text = text.decode('UTF-8')
      text2 = u'班主任签字：'
      xy = ttfont.getsize(text)
      print xy[1]
      xy = ((595 - xy[0])/2,25)
      draw.text(xy,text, font = ttfont,fill="black")
      draw.text((400,790),text2, font = ttfont2,fill="black")
      new.save('/home/chiaochiong/sw/result/'+department+'/'+stuclass+'_'+page+'.jpg', 'jpeg')
      bg = Image.open('/home/chiaochiong/sw/result/'+department+'/'+stuclass+'_'+page+'.jpg')
      print up
      print left
      bg.paste(im,(left,up))
      bg.save('/home/chiaochiong/sw/result/'+department+'/'+stuclass+'_'+page+'.jpg', 'jpeg')

   bg = Image.open('/home/chiaochiong/sw/result/'+department+'/'+stuclass+'_'+page+'.jpg')
   print up
   print left
   bg.paste(im,(left,up))
   bg.save('/home/chiaochiong/sw/result/'+department+'/'+stuclass+'_'+page+'.jpg', 'jpeg')

######################################################################################################
def getcord(i):
   if i <=20:
      l = 1
      if i<=5:
         m = 1
      else:
         m = i / 5
         x = i%5
         if m!=0 and x!=0:
            m=m+1
      n = i % 5 
      if n == 0:
         n =5
   elif i >20 and i<= 40:
      l = 2
      if (i-20)<=5:
         m = 1
      else:
         m = (i-20) / 5
         x = (i-20)%5
         if m!=0 and x!=0:
            m=m+1
      n = (i-20) % 5 
      if n == 0:
         n =5
   elif i >40 and i<= 60:
      l = 3
      if (i-40)<=5:
         m = 1
      else:
         m = (i-40) / 5
         x = (i-40)%5
         if m!=0 and x!=0:
            m=m+1
      n = (i-40) % 5 
      if n == 0:
         n =5
   return (l,m,n)
########################################################################################

db = MySQLdb.connect("localhost", "root", "", "sw", charset="utf8")
cursor = db.cursor()
sql = 'select * from `sw_class`'
try:
   cursor.execute(sql)
   rows = cursor.fetchall()
   if rows:
      for row in rows: 
         arr = row[2].split('-')
         num = row[3] 
         for x in range(0,num):
            i = 0
            sql_two = "select * from `sw_stu` where banji ='"+arr[x]+"'"
            cursor.execute(sql_two)
            rets = cursor.fetchall()
            if rets:
               for ret in rets:
                  if os.path.exists('/home/chiaochiong/sw/convert/'+ret[5]+'.jpg'):
                     i = i + 1
                     if not os.path.exists('/home/chiaochiong/sw/result/'+ret[1]):
                        os.chdir('/home/chiaochiong/sw/result')
                        os.mkdir(ret[1])
                     cord = getcord(i)
                     pasteimg('/home/chiaochiong/sw/convert/'+ret[5]+'.jpg', ret[1], ret[3], cord)

                     
                        
                       
except:
   db.rollback()


db.close()
