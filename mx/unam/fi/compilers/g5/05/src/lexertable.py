import re

token = [
    (r'\bprint\b', 'keyword'),
    (r'\bint\b', 'keyword'),
    (r'\bfloat\b', 'keyword'),
    (r'\bdouble\b', 'keyword'),
    (r'\blong\b', 'keyword'),
    (r'=','operator'),
    (r'\+','operator'),
    (r'\-','operator'),
    (r'\*','operator'),
    (r'\/','operator'),
    (r';', 'keyword'),
    (r'\s+', None),
]