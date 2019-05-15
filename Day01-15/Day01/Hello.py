#import getpass
import turtle

username = input('用户名：')
#getpass模块在pycharm下不可用
#password = getpass.getpass('密码：')
password = input('密码：')
if username=='admin' and password == 'admin':
	print('正确，通过！')
else :
	print ('用户名或密码错误')

