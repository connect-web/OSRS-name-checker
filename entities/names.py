import os

def get_names(filename: str) -> list[str]:
    with open(os.path.join('data', 'input', filename), 'r') as x:
        usernames = [username for username in x.read().splitlines() if username]
    return usernames

def save_outputs(filename: str, valid: list[str], banned: list[str]):
    if valid:
        with open(os.path.join('data', 'output', f'{filename}_valid.txt'), 'w') as x:
            for username in valid:
                x.write(f'{username}\n')

    if banned:
        with open(os.path.join('data', 'output', f'{filename}_banned.txt'), 'w') as x:
            for username in banned:
                x.write(f'{username}\n')