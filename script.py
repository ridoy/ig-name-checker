import requests
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
        payload = { 'email': 'simbop131738@gmail.com', 'username': 'aa', 'first_name': 'beep', 'password': 'bauiop90!' }
        for username in usernames:
            if (self.isTimeToRefresh()):
                refresh_count = 0
                self.refreshSession()
            print(username)
            payload['username'] = username
            r = self.session.post(REG_URL, data=payload)
            r_decoded = json.loads(r.text);
            time.sleep(.5)
            print r_decoded
            if (r_decoded['dryrun_passed'] == True):
                print('USERNAME ' + username + ' IS AVAILABLE.')

    def generateUsernames(self):
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        print('Generating usernames...')
        for i in range(0, 26):
            for j in range(0, 26):
                for k in range(0, 26):
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

