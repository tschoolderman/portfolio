import random

from app.extensions import db
from app.models.post import Post

db.create_all()


for i in range(0, 10):
    random_num = random.randrange(1, 1000)
    post = Post(title=f"Post #{random_num}", content=f"Content #{random_num}")
    db.session.add(post)
    print(post)
    print(post.content)
    print("--")
    db.session.commit()
