import GetCookie
import requests
from Queue import Queue
from Parser import Parser
import time
from Agents import agents
import random

class GetData:

    def __init__(self):
        self.cookie = GetCookie.login()
        self.q = Queue()


    def get_host_main(self, url):
        html = requests.get(url, cookies=self.cookie).content.decode("utf-8")
        self.q.html_hosts.append(html)

    def get_tweet_html(self, url_dic):
        for i in range(1, int(url_dic['page_amount']) + 1):
            html = requests.get(url_dic['url'] + str(i), cookies=self.cookie,
                                headers={"user-agent": random.choice(agents)}).content.decode("utf-8")
            self.q.add_tweet_html(html)
            if i > 1:
                return
            time.sleep(1)

    def get_likes_html(self, url_dic):
        for i in range(1, int(url_dic['page_amount']) + 1):
            html = requests.get(url_dic["url"] + str(i), cookies=self.cookie,
                                headers={"user-agent": random.choice(agents)}).content.decode("utf-8")
            self.q.add_like_html(html)
            time.sleep(1)

    def get_comments_html(self, url_dic):
        for i in range(1, int(url_dic['page_amount']) + 1):
            print(url_dic['url'] + str(i))
            html = requests.get(url_dic["url"] + str(i), cookies=self.cookie,
                                headers={"user-agent": random.choice(agents)}).content.decode("utf-8")
            self.q.add_comment_html(html)


if __name__ == "__main__":
    getdata = GetData()
    q = Queue()
    p = Parser()
    q.add_url_host("https://weibo.cn/u/5599359526")
    while 1:
        getdata.get_host_main(q.url_host[0])  # 获取主页面
        q.del_host_url()  # 从队列中删除爬过的主页面url
        p.parse_numberOfTweet(q.html_hosts[0])  # 解析微博数量，算出共有多少页
        q.del_host_html()  # 删除解析过的页面
        getdata.get_tweet_html(q.url_tweets[0])  # 获取每一页微博的html
        q.del_tweet_url()
        p.parse_fpage(q.html_tweets[0])  # 从微博页面中解析出评论页面的url
        q.del_tweet_html()
        getdata.get_comments_html(q.url_comments[0])  # 获取评论页面的html
        q.del_comments_url()
        p.parse_comments(q.html_comments[0])  # 解析出评论内容
        q.del_comment_html()

        getdata.get_likes_html(q.url_likes[0])  # 获取点赞页面html
        q.del_likes_url()

        p.parse_likes(q.html_likes[0])  # 解析点赞内容
        q.del_like_html()
