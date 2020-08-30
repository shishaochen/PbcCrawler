# 抓取中国人民银行官网货币政策司的公开市场业务交易公告

## 0. 程序说明

作者：史少晨

参考文档：https://www.cnblogs.com/sumuyi/p/12334154.html

## 1. 环境配置

安装标准版 Python 3，并添加 2 个第三方包。
```bash
python3 -m pip install beautifulsoup4  # 解析网页
python3 -m pip install PyExecJS        # 解析 JavaScript
```

## 2. 参数说明

在 Windows CMD 或 Linux Bash 中执行命令：
```bash
python3 -u crawl.py --help
```

屏幕会输出一段命命令行参数说明，形如：
```text
usage: crawl.py [-h] [--num_pages NUM_PAGES] [--output_dir OUTPUT_DIR]
                [--time_interval TIME_INTERVAL]

从中国人民银行网站抓取货币政策司的公开市场交易公告

optional arguments:
  -h, --help            show this help message and exit
  --num_pages NUM_PAGES
                        抓取多少页的公告
  --output_dir OUTPUT_DIR
                        存储抓取结果的目录
  --time_interval TIME_INTERVAL
                        两次抓取间隔的秒数
```

最关键的参数是 `--num_pages=N`，决定了将爬取最新的公告数量（单页是 20 份公告）。

## 3. 执行样例

在 Windows CMD 或 Linux Bash 中执行命令：
```bash
python3 -u crawl.py --num_pages=1
```

屏幕会输出一段日志，形如：
```text
2020-08-30 19:12:47,444 [crawl.py:37] INFO Parsing list page@[1] ...
2020-08-30 19:12:47,445 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/17081/index1.html
2020-08-30 19:12:47,780 [pbc_http.py:57] INFO Get new URL: http://www.pbc.gov.cn/WZWSREL3poZW5nY2VodW9iaXNpLzEyNTIwNy8xMjUyMTMvMTI1NDMxLzEyNTQ3NS8xNzA4MS9pbmRleDEuaHRtbA==?wzwschallenge=V1pXU19DT05GSVJNX1BSRUZJWF9MQUJFTDczMzI4NA==
2020-08-30 19:12:47,781 [pbc_http.py:53] INFO [1] HTTP GET: http://www.pbc.gov.cn/WZWSREL3poZW5nY2VodW9iaXNpLzEyNTIwNy8xMjUyMTMvMTI1NDMxLzEyNTQ3NS8xNzA4MS9pbmRleDEuaHRtbA==?wzwschallenge=V1pXU19DT05GSVJNX1BSRUZJWF9MQUJFTDczMzI4NA==
2020-08-30 19:12:51,249 [crawl.py:45] INFO [000] <公开市场业务交易公告 [2020]第169号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4078485/index.html]
2020-08-30 19:12:51,249 [crawl.py:45] INFO [001] <公开市场业务交易公告 [2020]第168号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4078160/index.html]
2020-08-30 19:12:51,251 [crawl.py:45] INFO [002] <公开市场业务交易公告 [2020]第167号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4077802/index.html]
2020-08-30 19:12:51,251 [crawl.py:45] INFO [003] <公开市场业务交易公告 [2020]第166号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4077023/index.html]
2020-08-30 19:12:51,251 [crawl.py:45] INFO [004] <公开市场业务交易公告 [2020]第165号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4075945/index.html]
2020-08-30 19:12:51,252 [crawl.py:45] INFO [005] <公开市场业务交易公告 [2020]第164号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4075144/index.html]
2020-08-30 19:12:51,252 [crawl.py:45] INFO [006] <公开市场业务交易公告 [2020]第163号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4074801/index.html]
2020-08-30 19:12:51,253 [crawl.py:45] INFO [007] <公开市场业务交易公告 [2020]第162号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4074599/index.html]
2020-08-30 19:12:51,253 [crawl.py:45] INFO [008] <公开市场业务交易公告 [2020]第161号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4073769/index.html]
2020-08-30 19:12:51,254 [crawl.py:45] INFO [009] <公开市场业务交易公告 [2020]第160号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4072750/index.html]
2020-08-30 19:12:51,254 [crawl.py:45] INFO [010] <公开市场业务交易公告 [2020]第159号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4071683/index.html]
2020-08-30 19:12:51,255 [crawl.py:45] INFO [011] <公开市场业务交易公告 [2020]第158号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4071329/index.html]
2020-08-30 19:12:51,255 [crawl.py:45] INFO [012] <公开市场业务交易公告 [2020]第157号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4071015/index.html]
2020-08-30 19:12:51,255 [crawl.py:45] INFO [013] <公开市场业务交易公告 [2020]第156号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4070805/index.html]
2020-08-30 19:12:51,257 [crawl.py:45] INFO [014] <公开市场业务交易公告 [2020]第155号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4070026/index.html]
2020-08-30 19:12:51,257 [crawl.py:45] INFO [015] <公开市场业务交易公告 [2020]第154号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4069160/index.html]
2020-08-30 19:12:51,257 [crawl.py:45] INFO [016] <公开市场业务交易公告 [2020]第153号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4068174/index.html]
2020-08-30 19:12:51,258 [crawl.py:45] INFO [017] <公开市场业务交易公告 [2020]第152号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4067922/index.html]
2020-08-30 19:12:51,258 [crawl.py:45] INFO [018] <公开市场业务交易公告 [2020]第151号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4067627/index.html]
2020-08-30 19:12:51,259 [crawl.py:45] INFO [019] <公开市场业务交易公告 [2020]第150号>@[http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4067075/index.html]
2020-08-30 19:12:51,319 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4078485/index.html
2020-08-30 19:12:51,388 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第169号] ...
2020-08-30 19:12:51,890 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4078160/index.html
2020-08-30 19:12:51,985 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第168号] ...
2020-08-30 19:12:52,487 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4077802/index.html
2020-08-30 19:12:52,559 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第167号] ...
2020-08-30 19:12:53,060 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4077023/index.html
2020-08-30 19:12:53,129 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第166号] ...
2020-08-30 19:12:53,630 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4075945/index.html
2020-08-30 19:12:53,767 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第165号] ...
2020-08-30 19:12:54,268 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4075144/index.html
2020-08-30 19:12:54,333 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第164号] ...
2020-08-30 19:12:54,836 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4074801/index.html
2020-08-30 19:12:54,929 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第163号] ...
2020-08-30 19:12:55,430 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4074599/index.html
2020-08-30 19:12:55,471 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第162号] ...
2020-08-30 19:12:55,972 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4073769/index.html
2020-08-30 19:12:57,042 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第161号] ...
2020-08-30 19:12:57,544 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4072750/index.html
2020-08-30 19:13:00,264 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第160号] ...
2020-08-30 19:13:00,764 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4071683/index.html
2020-08-30 19:13:00,858 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第159号] ...
2020-08-30 19:13:01,360 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4071329/index.html
2020-08-30 19:13:01,474 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第158号] ...
2020-08-30 19:13:01,974 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4071015/index.html
2020-08-30 19:13:02,372 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第157号] ...
2020-08-30 19:13:02,874 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4070805/index.html
2020-08-30 19:13:02,934 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第156号] ...
2020-08-30 19:13:03,435 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4070026/index.html
2020-08-30 19:13:03,474 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第155号] ...
2020-08-30 19:13:03,975 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4069160/index.html
2020-08-30 19:13:04,048 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第154号] ...
2020-08-30 19:13:04,548 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4068174/index.html
2020-08-30 19:13:04,589 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第153号] ...
2020-08-30 19:13:05,091 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4067922/index.html
2020-08-30 19:13:05,127 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第152号] ...
2020-08-30 19:13:05,628 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4067627/index.html
2020-08-30 19:13:05,697 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第151号] ...
2020-08-30 19:13:06,198 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4067075/index.html
2020-08-30 19:13:06,238 [crawl.py:52] INFO Writing content of [公开市场业务交易公告 [2020]第150号] ...
2020-08-30 19:13:06,740 [pbc_http.py:53] INFO [0] HTTP GET: http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125431/125475/4066334/index.html
```

如果参数 `--output_dir=X` 未被指定，那么所有抓取的文章都会写到工作目录。
