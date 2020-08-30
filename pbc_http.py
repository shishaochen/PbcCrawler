#coding:utf-8
import bs4
import execjs
import logging
import re
import requests

from pbc_conf import DOMAIN, HOME_PAGE


_CURRENT_SESSION = requests.session()
_SHARED_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Host': DOMAIN,
    'Referer': HOME_PAGE,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
}


class _NeedRedirection(Exception):
    def __init__(self, html):
        super(_NeedRedirection, self).__init__()
        self.html = html


def _http_get(page_url):
    ''' 发起 HTTP GET 请求 '''
    rsp = _CURRENT_SESSION.get(page_url, headers=_SHARED_HEADERS, timeout=10)
    rsp.encoding = 'utf-8'
    if '请开启JavaScript并刷新该页' in rsp.text:
        raise _NeedRedirection(rsp.text)
    return rsp.text


def _generate_new_url(html):
    ''' 获取重定向地址 '''
    soup = bs4.BeautifulSoup(html, 'html.parser')
    js_code = soup.select('script')[0].string
    js_code = re.sub(r'atob\(', 'window["atob"](', js_code)
    js_fn = 'function getURL(){ var window = {};' + js_code + 'return window["location"];}'
    ctx = execjs.compile(js_fn)
    tail = ctx.call('getURL')
    return HOME_PAGE + tail


def get_url_content(page_url, retries=10):
    ''' 获取 PBC 网页内容 '''
    for idx in range(retries):
        try:
            logging.info('[%d] HTTP GET: %s', idx, page_url)
            return _http_get(page_url)
        except _NeedRedirection as e0:
            page_url = _generate_new_url(e0.html)
            logging.info('Get new URL: %s', page_url)
        except Exception as e1:
            logging.warning('Eat failure: %s', e1)
    raise RuntimeError('Failed to get content of [%s] after [%d] retries!', page_url, retries)
