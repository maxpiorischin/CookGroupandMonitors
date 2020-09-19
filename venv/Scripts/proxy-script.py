#!C:\Users\maxpi\PycharmProjects\ShopifyMonitor\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'proxy.py==2.2.0','console_scripts','proxy'
__requires__ = 'proxy.py==2.2.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('proxy.py==2.2.0', 'console_scripts', 'proxy')()
    )
