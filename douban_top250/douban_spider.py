#coding=gbk

import string
import re
from urllib.request import urlopen

class DouBanSpider(object) :
    """类的简要说明

    本类主要用于抓取豆瓣前250的电影名称

    Attributes:
        page: 用于表示当前所处的抓取页面
        cur_url: 用于表示当前争取抓取页面的url
        datas: 存储处理好的抓取到的电影名称
        _top_num: 用于记录当前的top号码
    """

    def __init__(self) :
        self.page = 1
        self.cur_url = "http://movie.douban.com/top250?start={page}&filter=&type="
        self.datas = []
        self._top_num = 1
        print("豆瓣电影爬虫准备就绪, 准备爬取数据...")

    def get_page(self, cur_page) :
        """
        根据当前页码爬取网页HTML

        Args: 
            cur_page: 表示当前所抓取的网站页码

        Returns:
            返回抓取到整个页面的HTML(unicode编码)

        Raises:
            URLError:url引发的异常
        """
        url = self.cur_url
        my_page = urlopen(url.format(page = (cur_page - 1) * 25)).read().decode("utf-8")

        return my_page

    def find_title(self, my_page) :
        """
        通过返回的整个网页HTML, 正则匹配前250的电影名称

        Args:
            my_page: 传入页面的HTML文本用于正则匹配
        """
        temp_data = []
        movie_items = re.findall(r'<span.*?class="title">(.*?)</span>', my_page, re.S)
        for index, item in enumerate(movie_items) :
            if item.find("&nbsp") == -1 :
                temp_data.append("Top" + str(self._top_num) + " " + item)
                self._top_num += 1
        self.datas.extend(temp_data)

    def start_spider(self) :
        """
        爬虫入口, 并控制爬虫抓取页面的范围
        """
        while self.page <= 10 :
            my_page = self.get_page(self.page)
            self.find_title(my_page)
            self.page += 1

def main():
    my_spider = DouBanSpider()
    my_spider.start_spider()
    filename = 'DoubanMovies250.txt'
    with open (filename,'w') as file_object:
        for item in my_spider.datas :
            file_object.write(item + '\n')
    print("豆瓣爬虫爬取结束...")

if __name__ == '__main__':
    main()