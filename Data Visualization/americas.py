#coding=gbk
import pygal

wm = pygal.Worldmap()
wm.title = 'North,Central,and South America'

wm.add('North America',['ca','mx','us'])#add()����һ����ǩ��һ���б����߰�������Ҫͻ���Ĺ��ҵĹ�����
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])#ÿ�ε���add()����Ϊָ���Ĺ���ѡ��һ������ɫ
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
    'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')