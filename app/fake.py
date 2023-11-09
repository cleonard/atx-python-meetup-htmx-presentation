"""Using the faker pkg to generate blog content"""

import random
import re
from pprint import pprint

from faker import Faker

RE_SPACE = re.compile(r"\s+")

fake = Faker()


def content():
    return fake.text(max_nb_chars=280)


def author():
    return fake.name()


def generate_post():
    post_data = {
        "author": author(),
        "content": content(),
    }
    return post_data
