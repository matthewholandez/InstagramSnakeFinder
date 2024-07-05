# InstagramSnakeFinder
## Requesting your Data
You must request a copy of your account data from Instagram to compare your followers and following this way.

* Request the data [through Instagram's account center](https://accountscenter.instagram.com/info_and_permissions/dyi/)
* Click only **'Some of your information'** and check **'Followers and following'** (under Connections). 
* Select 'Download to Device'
* For date range, select 'All time'
* For format, select 'JSON'

Instagram should prepare the data within the day. When you get the email, go back [to Instagram's account center](https://accountscenter.instagram.com/info_and_permissions/dyi/) and there should be a download link waiting.

## Installation
Prerequisites: latest version of Python
1. Clone this repository: `git clone https://github.com/matthewholandez/InstagramSnakeFinder.git` or via the web interface
2. Move the `followers_1.json` and `following.json` files from your Instagram data download into the same `InstagramSnakeFinder` folder. **Note:** if those files happened to be named differently in your download (which I hope never happens), change the file name in `main.py` accordingly.
3. Run `main.py`: `python main.py`
