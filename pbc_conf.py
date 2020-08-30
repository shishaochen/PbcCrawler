#coding:utf-8
import logging

DOMAIN = 'www.pbc.gov.cn'
HOME_PAGE = 'http://' + DOMAIN
LIST_PAGE_URL_PATTERN = HOME_PAGE + '/zhengcehuobisi/125207/125213/125431/125475/17081/index{}.html'

logging.debug('=== PBC Spider Conf ===')
logging.debug('DOMAIN=%s', DOMAIN)
logging.debug('HOME_PAGE=%s', HOME_PAGE)
logging.debug('LIST_PAGE_URL_PATTERN=%s', LIST_PAGE_URL_PATTERN)
