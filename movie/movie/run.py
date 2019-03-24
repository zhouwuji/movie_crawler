# from scrapy.cmdline import execute
# from os import system
import subprocess
from merge import Merge

name = '22tu'

if __name__ == '__main__':
    # cmd = f'scrapy crawl {name}'
    # execute(cmd.split(' '))
    for episode in range(30, 31):
        SOAP_ID = '28230'
        EPISODE = episode
        SOAP_NAME = 'doutinghao'
        print(f"正在下载的片名是：{SOAP_NAME}\n剧集是：{EPISODE}")
        child_crawl = subprocess.call(f"scrapy crawl {name} \
        -a SOAP_ID={SOAP_ID} -a EPISODE={EPISODE} -a SOAP_NAME={SOAP_NAME}")
        # child_crawl.wait()
        print(f'正在合成ts文件')
        merge = Merge(SOAP_NAME=SOAP_NAME, EPISODE=EPISODE)
        merge.main()
        print(f"{SOAP_NAME}_{EPISODE}下载完毕")