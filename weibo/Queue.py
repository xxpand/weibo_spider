class Queue:
    url_likes = []
    url_comments = []
    url_tweets = []
    url_host = []
    html_likes = []
    html_comments = []
    html_hosts = []
    html_tweets = []
    def add_url_likes(self, dic):  # 赞页面的url
        number = len(self.url_likes)
        if number > 10000:
            print("当前队列已满")
            return 0
        else:
            self.url_likes.append(dic)
            print("点赞url队列数量：", number + 1)
            return 1

    def add_url_comments(self, dic):  # 评论页面url
        number = len(self.url_comments)
        if number > 10000:
            print("当前队列已满")
            return 0
        else:
            self.url_comments.append(dic)
            print("评论url队列数量：", number + 1)
            return 1

    def add_url_host(self, dic):  # 微博主页url
        number = len(self.url_host)
        if number > 10000:
            print("当前队列已满")
            return 0
        else:
            self.url_host.append(dic)
            print("主页url队列数量：", number + 1)
            return 1

    def add_url_tweets(self, dic):  # 每一页微博url
        number = len(self.url_tweets)
        if number > 10000:
            print("当前队列已满")
            return 0
        else:
            self.url_tweets.append(dic)
            print("微博url队列数量：", number + 1)
            return 1

    def add_host_html(self, html):  # 微博主页html
        number = len(self.html_hosts)
        if number > 10000:
            print("当前队列已满")
            return 0
        else:
            self.html_hosts.append(html)
            print("主页html队列数量：", number + 1)
            return 1

    def add_comment_html(self, html):  # 评论页面html
        number = len(self.html_comments)
        if number > 10000:
            print("当前队列已满")
            return 0
        else:
            self.html_comments.append(html)
            print("评论html队列数量：", number + 1)
            return 1

    def add_like_html(self, html):  # 点赞页面html
        number = len(self.html_likes)
        if number > 10000:
            print("当前队列已满")
            return 0
        else:
            self.html_likes.append(html)
            print("点赞html队列数量：", number + 1)
            return 1

    def add_tweet_html(self, html):  # 每一页微博html
        number = len(self.html_tweets)
        if number > 10000:
            print("队列已满")
            return 0
        else:
            self.html_tweets.append(html)
            print("微博页面html队列数量：", number + 1)
            return 1

    def del_likes_url(self):
        del self.url_likes[0]

    def del_comments_url(self):
        del self.url_comments[0]

    def del_host_url(self):
        del self.url_host[0]

    def del_tweet_url(self):
        del self.url_tweets[0]

    def del_tweet_html(self):
        del self.html_tweets[0]

    def del_host_html(self):
        del self.html_hosts[0]

    def del_comment_html(self):
        del self.html_comments[0]

    def del_like_html(self):
        del self.html_likes[0]
