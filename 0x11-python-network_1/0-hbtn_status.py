#!/usr/bin/python3
"""Fetches the URL: https://intranet.hbtn.io/status
"""

from urllib.request import Request, urlopen

def fetch_url(url):
    """Fetches content from the given URL and returns it."""
    req = Request(url)
    with urlopen(req) as res:
        return res.read()

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    content = fetch_url(url)
    utf8_content = content.decode('utf-8')
    
    print('Body response:')
    print('\t- type: {_type}'.format(_type=type(content)))
    print('\t- content: {_content}'.format(_content=content))
    print('\t- utf8 content: {_utf8_c}'.format(_utf8_c=utf8_content))
