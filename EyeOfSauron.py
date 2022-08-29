from xml.dom.minidom import Element


x,y = input().split('(')
a = x.count('|')
b = y.count('|')
if(a==b):
    print('correct')
else:
    print('fix')

