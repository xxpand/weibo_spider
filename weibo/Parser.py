from bs4 import BeautifulSoup
import re
from Queue import Queue
from Database import DB


class Parser:
    def __init__(self):
        self.list = list()
        self.comments = []  # 评论结果
        self.comments_userurl = []  # 从评论里面爬取到的用户url
        self.likes = []  # 赞爬取结果
        self.queue = Queue()  # 爬取队列对象
        self.db = DB()

    def parse_numberOfTweet(self, html):  # 获取每一页微博的url
        dic = {}
        soup = BeautifulSoup(html, 'lxml')
        base_url = soup.find('td').contents[0]['href']
        url = re.search('/[\d*]{1,}', base_url).group() + "?page="
        base_page = soup.find('span', attrs={"class": "tc"}).text
        page_amount = int(re.search('[\d]{1,}', base_page, re.M | re.I).group()) / 10 + 1
        dic["url"] = "https://weibo.cn/u" + url
        dic["page_amount"] = page_amount
        self.queue.add_url_tweets(dic)

    # TODO:解析整个页面
    def parse_fpage(self, html):  # 获取评论页面url
        soup = BeautifulSoup(html, 'lxml')

        for i in soup.find_all('a', attrs={"class": "cc"}):
            if "原文评论" in i.text:
                pass
            else:
                dic = {}
                dic["url"] = re.search('https://[a-z]{1,}.cn/comment/.*[?]', i["href"], re.M | re.I).group() + "page="
                num = int(re.search('[\d]+', i.text).group())
                if num == 0:
                    pass
                else:
                    dic["page_amount"] = num / 10 + 1
                    print(dic)
                    self.queue.add_url_comments(dic)

    # TODO:解析评论页面
    def parse_comments(self, html):  # 获取评论页面的内容

        soup = BeautifulSoup(html, "lxml")
        self.comments = []  # 将评论list清空
        self.comments_userurl = []  # 把用户urllist清空
        like_dic = {}
        comments_html = soup.find_all('div',id=re.compile("C_"))
        host_name = soup.find("a", attrs={"class": ""}).text[2:-3]
        like_soup = soup.find('a', attrs={'href': re.compile('/atti')})
        like_dic['url'] = "https://weibo.cn" + str(
            re.search("/attitu[\w]{1,}/[\w]{1,}\?", like_soup['href']).group()) + "page="
        like_dic['page_amount'] = int(re.search('[\d]+', like_soup.text).group()) / 10 + 1

        print(like_dic)
        self.queue.add_url_likes(like_dic)

        for content in comments_html:
            comment_dict = dict()
            comment_dict["comment_content"] = content.find(attrs={"class": "ctt"}).text  # 获取评论内容
            comment_dict["comment_username"] = content.find("a").text  # 获取评论者的昵称
            comment_user_url = content.find("a").attrs["href"]  # 获取评论者的链接
            self.queue.add_url_host("https://weibo.cn"+comment_user_url)  # 取评论用户url做为爬取队列
            print(comment_dict, comment_user_url)

            self.comments.append(comment_dict)

        self.db.insert(host_name, self.comments)  # 插入数据库

    # TODO:解析点赞页面
    def parse_likes(self, html):  # 获取点赞页面的内容
        self.likes = []
        likes = []
        soup = BeautifulSoup(html, "lxml")
        host_name = soup.find("div", attrs={"class": ""}).text.split(":")[0]
        n = 0
        for i in soup.find_all(attrs={"class": "ct"}):
            n += 1
            if n == 1:
                continue
            else:
                likes.append(i.previous_sibling.previous_sibling.text)
        self.db.insert_likes(host_name, likes)
