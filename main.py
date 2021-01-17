import time
from downloader import download
from parser import parse
from database import savedb

if __name__ == '__main__':
    movie_id = '1292722'
    offset=0
    num=0
    sleep = 5
    while 1:
        url = f'https://movie.douban.com/subject/{movie_id}/comments?start={offset}&limit=20&status=P&sort=new_score'
        print(url)
        page = download(url)
        data = parse(page, movie_id, num)
        savedb(movie_id, data)
        num += 1
        offset += 20

        print(f"休息{sleep}s，继续抓取...")
        time.sleep(sleep)
