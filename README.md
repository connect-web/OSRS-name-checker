# Simple Python OSRS Hiscores checker

You can easily check usernames from the hiscores on old school runescape to see if a user exists on the hiscores.

- This is a simple method of checking if a user is banned.
- This is not 100% deterministic standalone because a user may have changed their username but combined with a username-change checker this will verify bans.



# Usage


### Proxies setup
- Requries a file named ```proxies.txt``` in project root.
- Proxies.txt will contain a proxy per line in the format: ```ip:port:username:password```.

### Input file setup

- Place files with usernames on each line in the directory ```data/input``` multiple files are supported.

### Run

- ```python3 main.py``` Run the main file and the usernames will be checked.

### Output

- The results are stored in ```data/output/``` with two separate files per input, one file for ```valid``` accounts and another file for ```banned``` accounts.