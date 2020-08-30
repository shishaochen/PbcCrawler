#coding:utf-8
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)-15s [%(filename)s:%(lineno)d] %(levelname)s %(message)s'
)

import argparse
import bs4
import collections
import os
import time

from pbc_conf import HOME_PAGE, LIST_PAGE_URL_PATTERN
from pbc_http import get_url_content


NewsLink = collections.namedtuple('NewsLink', ['title', 'url'])


def extract_news_url(text):
    ''' 从目录页抽取公告链接 '''
    soup = bs4.BeautifulSoup(text, 'html.parser')
    url_list = []
    for item in soup.select('font[class="newslist_style"] a'):
        news_url = HOME_PAGE + item.get_attribute_list('href')[0]
        url_list.append(NewsLink(title=item.text, url=news_url))
    return url_list


def main(FLAGS):
    news_link_list = []

    # 抽取所有的公告链接
    for page_no in range(1, FLAGS.num_pages + 1):
        list_page_url = LIST_PAGE_URL_PATTERN.format(page_no)
        logging.info('Parsing list page@[%d] ...', page_no)
        text = get_url_content(list_page_url)
        extracted = extract_news_url(text)
        news_link_list.extend(extracted)
        time.sleep(FLAGS.time_interval)

    # 打印抓取结果
    for idx, item in enumerate(news_link_list):
        logging.info('[%03d] <%s>@[%s]', idx, item.title, item.url)

    # 抽取所有的公告链接
    for item in news_link_list:
        local_path = os.path.join(FLAGS.output_dir, item.title + '.html')
        news_content = get_url_content(item.url)
        with open(local_path, 'w', encoding='utf-8') as fout:
            logging.info('Writing content of [%s] ...', item.title)
            fout.write(news_content)
        time.sleep(FLAGS.time_interval)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='从中国人民银行网站抓取货币政策司的公开市场交易公告')
    parser.add_argument('--num_pages', type=int, default=5, help='抓取多少页的公告')
    parser.add_argument('--output_dir', type=str, default='.', help='存储抓取结果的目录')
    parser.add_argument('--time_interval', type=float, default=0.5, help='两次抓取间隔的秒数')
    FLAGS = parser.parse_args()
    main(FLAGS)
