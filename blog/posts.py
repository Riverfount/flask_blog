from datetime import datetime
from typing import Any

import pymongo

from blog.database import mongo
from slugify import slugify


def get_all_posts(published: bool = True) -> list[dict[str, Any]]:
    posts = mongo.db.post.find({"published": published})
    return posts.sort('date', pymongo.DESCENDING)


def get_post_by_slug(slug: str) -> dict:
    post = mongo.db.post.find_one({"slug": slug})
    return post


def update_post_by_slug(slug: str, data: dict[str, Any]) -> dict[str, Any]:
    # Todo: Se o título mudar, atulizar o slug (falhar se já existir)
    updated = mongo.db.post.find_one_and_update({"slug": slug}, {"$set": data})
    return updated


def new_post(title: str, content: str, published: bool = True) -> str:
    slug = slugify(title)
    msg = 'There is a post with the same title.'
    if not get_post_by_slug(slug):
        mongo.db.post.insert_one(
            {
                'title': title,
                'content': content,
                'published': published,
                'slug': slug,
                'date': datetime.now(),
            }
        )
        msg = slug
    return msg
