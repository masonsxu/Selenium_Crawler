# Selenium_Crawler

一个使用 selenium 模块爬取（Twitter、New York Times）网站的可配置爬虫代码

## 代码更新

*2020/10/29 修改了每次爬取时覆盖上次爬取的文件的bug*

*2020/10/29 修改了项目文件目录结构*

## 使用方式

![image-20201029113954488](https://gitee.com/masonsxu/cloudimg/raw/master//img/image-20201029113954488.png)

### 文件夹中的文件分别对应内容

==New_York_Times_Crawler==：存 New York Tiems 的爬虫代码

 ==New_York_Times_Data==：存放成功爬取的数据，格式分别为 csv 和 excel

 ==news_crawler.py==： New York Tiems 的爬虫代码

 ==news_url.txt==：存放想要爬取的 New York Tiems 的 url 地址（可以放置多条地址）

==Twitter_Crawler==：存放 Twitter 的爬虫代码

 ==TwitterData==：存放成功爬取的数据，格式分别为 csv 和 excel

 ==twitter_crawler.py==：Twitter 的爬虫代码

 ==twitter_url.txt==：存放想要爬取的 Twitter 的 url 地址（可以放置多条地址）

## 爬虫所对应的网站的网页结构

### New York Tiems

[地址样例](https://www.nytimes.com/search?dropmab=true&endDate=20201015&query=racism&sections=U.S.%7Cnyt%3A%2F%2Fsection%2Fa34d3d6c-c77f-5931-b951-241b4e28681c&sort=best&startDate=20191015)

![image-20201029125538757](https://gitee.com/masonsxu/cloudimg/raw/master//img/image-20201029125538757.png)

### Twitter

[地址样例](<https://twitter.com/search?q=The%20US%20(xenophobia%20OR%20racism%20OR%20racist%20OR%20exclusion)%20until%3A2020-10-01%20since%3A2019-10-01&src=typed_query>)

![image-20201029130119525](https://gitee.com/masonsxu/cloudimg/raw/master//img/image-20201029130119525.png)

## 准备运行代码

### Selenium 模块

本代码使用的是 Python 中的 Selenium 模块，如果没有 Selenium 模块的使用经验的话请浏览https://www.cnblogs.com/linhaifeng/articles/7783599.html中的有界浏览器使用方式。

### 可能会遇到的问题

Twitter 和 New York Times 访问速度过慢

爬虫代码中断

### 解决方法

访问速度过慢的话，这个没有办法帮你，==网络环境的问题请自行查找解决办法==

爬虫代码中断，一般情况下，网络环境没问题，设置的 URL 完整的话不会出现爬虫代码中断的错误，==遇到的话请多跑几遍代码在询问，并附上错误信息==
