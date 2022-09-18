from datetime import datetime
from typing import Any

from blog.database import mongo
from slugify import slugify


def get_all_posts(published: bool = True) -> list[dict[str, Any]]:
    posts = mongo.db.post.find({"published": published})
    return posts.sort('date')


def get_post_by_slug(slug: str) -> dict:
    post = mongo.db.post.find_one({"slug": slug})
    return post


def update_post_by_slug(slug: str, data: dict[str, Any]) -> dict[str, Any]:
    # Todo: Se o título mudar, atulizar o slug (falhar se já existir)
    return mongo.db.posts.find_one_and_update({"slug": slug}, {"$set": data})


def new_post(title: str, content: str, published: bool = True) -> str:
    slug = slugify(title)
    # Todo: verificar se post com esse slug já existe
    mongo.db.post.insert_one(
        {
            'title': title,
            'content': content,
            'published': published,
            'slug': slug,
            'date': datetime.now(),
        }
    )
    return slug
