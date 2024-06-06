import requests
from time import sleep

from entities.proxies import get_proxy, default_headers

valid_requests = 0
proxy_errors = 0

def check_name(username: str) -> int:
    try:
        url = f'https://secure.runescape.com/m=hiscore_oldschool/index_lite.json?player={username}'
        r = requests.get(url, proxies=get_proxy(), headers=default_headers)

        if r.status_code == 429:
            # Rate limited, we need to try again
            sleep(5)
            return check_name(username)


        global valid_requests
        valid_requests += 1
        if valid_requests % 10 == 0:
            print(f'{valid_requests} valid requests')



        return r.status_code
    except Exception as e:
        global proxy_errors
        proxy_errors += 1
        if proxy_errors % 10 == 0:
            print(f'{proxy_errors} proxy errors [{e}]')
        return check_name(username)