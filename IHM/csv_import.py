import csv
import json


from flaskapp.db import init_db
from flaskapp.models import LinkedIn, Document



init_db("mongodb://mongo:27017", "CEA")

with open("LinkedInPosts_20220521_2.csv", "r") as f:
    for row in csv.reader(f, delimiter=","):
        if row[0] != "" and row[0] != "author":
            doc = Document(author=row[0], content=row[1])
            doc.save()

with open("/shared/influenceurs-posts-p0.json", "r") as f:
    posts = json.load(f)
    docs = [Document(**doc) for doc in posts["posts"]]
    print(docs)
    Document.insert_many(docs)

# with open("/shared/keyword_posts-p0.json", "r") as f:
#     posts = json.load(f)
#     docs = [Document(**doc) for doc in posts["posts"]]
#     Document.insert_many(docs)

