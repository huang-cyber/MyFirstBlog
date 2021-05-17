# coding: utf-8
"""
The structure of the website
"""
import sys

from handlers.index import IndexHandler

url = [
    (r'/', IndexHandler),
    (r'/user', UserHandler)
]