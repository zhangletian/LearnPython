#coding=gbk
import pygal

wm = pygal.Worldmap()
wm.title = 'North,Central,and South America'

wm.add('North America',['ca','mx','us'])#add()接受一个标签和一个列表，后者包括我们要突出的国家的国别码
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])#每次调用add()都将为指定的国家选择一种新颜色
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
    'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')