# 豆瓣电影短评展示

> 程序通过python main.py运行，通过修改main.py指定movie_id和自增offset实现爬取相应电影的所有短评。


### 程序已知问题

1. 通过while循环爬取网页，直到下一个网页中没有相应的元素来判断是否抓取完。
2. 不需要登录豆瓣进行爬取，可能数据比真实数据少几个页面
3. 程序可以重复执行，爬取同一个影评会追加到数据库中，造成数据重复。暂时没想到好办法
