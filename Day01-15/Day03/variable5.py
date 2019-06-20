"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:百分制成绩转等级制成绩
			90分以上    --> A
			80分~89分    --> B
			70分~79分	   --> C
			60分~69分    --> D
			60分以下    --> E


Date    : 2019-05-24 14:39:24
Author  : Younth Yang (8593009@qq.com)
"""

value=int(input('请输入成绩:'))
score= 'A'
if value>=90:
	score='A'
elif value>=80 and value <=89 :
	score='B'
elif value>=70 and value <=79 :
	score='C'
elif value>=60 and value <=69 :
	score='D'
else :
	score='E'

print('score =',score)