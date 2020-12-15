import requests
import random
import time
import json

CHROME_WIN_UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
BASE_URL = 'https://www.instagram.com/'
REG_URL = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
STORIES_UA = 'Instagram 123.0.0.21.114 (iPhone; CPU iPhone OS 11_4 like Mac OS X; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/605.1.15'

class IGUsernameChecker:
    def __init__(self):
        self.session = None
        self.refresh_count = 0
        self.refresh_at = 40
        self.usernames = []
        print('Checking username availabilities...')

        self.refreshSession()
        self.generateUsernames()
        payload = { 'email': self.getRandomEmail(), 'username': 'aa', 'first_name': self.getRandomString(10), 'password': self.getRandomString(15) } 
        print(payload)
        for username in self.usernames:
            if (self.isTimeToRefresh()):
                refresh_count = 0
                self.refreshSession()
            print(username)
            payload['username'] = username
            print(payload)
            r = self.session.post(REG_URL, data=payload)
            print(r.text)
            r_decoded = json.loads(r.text);
            time.sleep(.5)
            print(r_decoded)
            if (r_decoded['dryrun_passed'] == True):
                print('USERNAME ' + username + ' IS AVAILABLE.')

    def getRandomEmail(self):
        a = ['flee', 'nar', '22jk', 'afjkaf', 'sfjk','sfjskf', 'afsasfj','asfkjfka','sjfkjfsi','af','sisi','boo','plah','gimar']
        b = ['gmail.com', 'yahoo.com', 'hotmail.com', 'live.com']
        email_address = ''
        for i in range(0, random.randint(2, 4)):
            email_address += a[i]
        email_host = b[random.randint(0, len(b) - 1)]
        email_address += '@' + email_host
        return email_address

    def getRandomString(self, num):
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        name = ''
        for i in range(0, random.randint(6, num)):
            name += alphabet[i]
        return name

    def generateUsernames(self):
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        print('Generating usernames...')
        for i in range(25, 0, -1):
            for j in range(25, 0, -1):
                for k in range(25, 0, -1):
                    username = alphabet[i] + alphabet[j] + alphabet[k]
                    self.usernames.append(username)
        print('Finished generating ' + str(len(self.usernames)) + ' usernames');


    def refreshSession(self):
        print('Refreshing session.')
        self.session = requests.Session()
        self.session.headers.update({'user-agent': STORIES_UA})
        r = self.session.get(REG_URL)
        csrftoken = r.cookies.get('csrftoken')
        self.session.headers.update({'x-csrftoken': csrftoken})

    def isTimeToRefresh(self):
        return self.refresh_count >= self.refresh_at

IGUC = IGUsernameChecker()


