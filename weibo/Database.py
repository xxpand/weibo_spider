from pymongo import MongoClient
import pymongo


class DB:
    comments_set = pymongo.collection.Collection
    likes_set = pymongo.collection.Collection
    follow_set = pymongo.collection.Collection

    def __init__(self):
        conn = MongoClient("127.0.0.1", 27017)
        db = conn.weibo
        self.comments_set = db.comments
        self.likes_set = db.likes
        self.follow_set = db.follow_set

    def insert(self, hostname, comments):
        self.comments_set.insert({"host": hostname, "comments": comments})

    def insert_likes(self, host_name, likes):
        self.likes_set.insert({"host": host_name, "likes": likes})

    def insert_follows(self, host_name, follows):
        self.follow_set.insert({"host": host_name, "follows": follows})

    def find_comments(self):
        for i in self.comments_set.findall():
            print(i)

    def find_likes(self):
        for i in self.likes_set.findall():
            print(i)

    def find_fellows(self):
        for i in self.follow_set.findall():
            print(i)
