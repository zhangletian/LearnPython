#coding=gbk

import string
import re
from urllib.request import urlopen

class DouBanSpider(object) :
    """��ļ�Ҫ˵��

    ������Ҫ����ץȡ����ǰ250�ĵ�Ӱ����

    Attributes:
        page: ���ڱ�ʾ��ǰ������ץȡҳ��
        cur_url: ���ڱ�ʾ��ǰ��ȡץȡҳ���url
        datas: �洢����õ�ץȡ���ĵ�Ӱ����
        _top_num: ���ڼ�¼��ǰ��top����
    """

    def __init__(self) :
        self.page = 1
        self.cur_url = "http://movie.douban.com/top250?start={page}&filter=&type="
        self.datas = []
        self._top_num = 1
        print("�����Ӱ����׼������, ׼����ȡ����...")

    def get_page(self, cur_page) :
        """
        ���ݵ�ǰҳ����ȡ��ҳHTML

        Args: 
            cur_page: ��ʾ��ǰ��ץȡ����վҳ��

        Returns:
            ����ץȡ������ҳ���HTML(unicode����)

        Raises:
            URLError:url�������쳣
        """
        url = self.cur_url
        my_page = urlopen(url.format(page = (cur_page - 1) * 25)).read().decode("utf-8")

        return my_page

    def find_title(self, my_page) :
        """
        ͨ�����ص�������ҳHTML, ����ƥ��ǰ250�ĵ�Ӱ����

        Args:
            my_page: ����ҳ���HTML�ı���������ƥ��
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
        �������, ����������ץȡҳ��ķ�Χ
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
    print("����������ȡ����...")

if __name__ == '__main__':
    main()