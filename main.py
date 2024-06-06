import concurrent.futures
import os
from typing import Tuple, List, Any

from entities import (
    check_name, get_names,save_outputs, Status
)

THREAD_CONCURRENCY = 25

def main():
    # get all files in data/input
    filenames = [
        file
        for file in os.listdir(os.path.join('data', 'input'))
        if not os.path.isdir(file) # ignore folders.
    ]

    for filename in filenames:
        # read file and load usernames
        usernames = get_names(filename)

        print(f'checking {len(usernames)} users.')

        # check hiscores API to see if usernames exist
        valid, banned = check_names(usernames)

        # save responses to valid, banned files respectively.
        save_outputs(filename, valid, banned)



def check_names(usernames) -> tuple[list[str], list[str]]:
    valid_accounts = []
    banned_accounts = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=THREAD_CONCURRENCY) as executor:
        # Submit tasks to the executor
        future_to_username = {executor.submit(check_name, username): username for username in usernames}

        for future in concurrent.futures.as_completed(future_to_username):
            username = future_to_username[future]
            try:
                result = future.result()
                status_type = Status.from_code(result)
                if status_type == Status.VALID:
                    valid_accounts.append(username)
                elif status_type == Status.BANNED:
                    banned_accounts.append(username)
                else:
                    print(f'{result} is an unhandled status code.')

            except Exception as exc:
                print(f"Error occurred while downloading {username}: {exc}")

    return valid_accounts, banned_accounts


if __name__ == '__main__':
    main()
