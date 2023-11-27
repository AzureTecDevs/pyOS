import os
import requests
print('Updating...')
url = 'https://raw.githubusercontent.com/AzureTecDevs/pyOS/main/init.py'
r = requests.get(url, allow_redirects=True)
open(f'init.py', 'wb').write(r.content)
