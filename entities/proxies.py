import random
import time

random.seed(time.time())

default_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0'}


def load_proxy(line: str) -> dict:
    """
    Proxies are expected to be
    ip:port:username:password
    while user:pass authentcation is enabled.
    """
    ip, port, username, password = line.split(':')
    proxy_line = f'{username}:{password}@{ip}:{port}'

    session_proxy = {'http': f'http://{proxy_line}',
                     'https': f'https://{proxy_line}',
                     }
    return session_proxy


with open('proxies.txt', 'r') as x:
    proxies = [
        load_proxy(line)
        for line in x.read().splitlines()
    ]


def get_proxy() -> dict:
    return random.choice(proxies)
