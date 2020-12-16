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
        payload = { 'email': self.getRandomEmail(), 'username': 'aa', 'first_name': self.getRandomName(10), 'password': self.getRandomPassword() } 
        for username in self.usernames:
            if (self.isTimeToRefresh()):
                refresh_count = 0
                self.refreshSession()
            payload['username'] = username
            payload['email'] = self.getRandomEmail()
            payload['first_name'] = self.getRandomName(10)
            payload['password'] = self.getRandomPassword()
            r = self.session.post(REG_URL, data=payload)
            r_decoded = json.loads(r.text);
            time.sleep(.5)
            try:
                if ('errors' in r_decoded and 'username' in r_decoded['errors']):
                    print('username ' + username + ' is unavailable.')
                else:
                    print(r.text)
                    print('USERNAME ' + username + ' IS AVAILABLE.')
            except:
                print(r.text)


    def getRandomEmail(self):
        a = ['flee', 'nar', '22jk', 'afjkaf', 'sfjk','sfjskf', 'afsasfj','asfkjfka','sjfkjfsi','af','sisi','boo','plah','gimar']
        b = ['gmail.com', 'yahoo.com', 'hotmail.com', 'live.com']
        email_address = ''
        for i in range(0, random.randint(2, 4)):
            email_address += a[random.randint(0, len(a) - 1)]
        email_host = b[random.randint(0, len(b) - 1)]
        email_address += '@' + email_host
        return email_address

    def getRandomName(self, num):
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        name = ''
        for i in range(0, random.randint(6, num)):
            name += alphabet[random.randint(0, len(alphabet) - 1)]
        return name

    def getRandomPassword(self):
        lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        nums = ['1', '2','3','4','5','6','7','8','9']
        symbols = ['!', '?', '$']
        password = ''
        for i in range(0, random.randint(7, 15)):
            chartype = random.randint(0, 3)
            if chartype == 0:
                password += lower[random.randint(0, len(lower) - 1)]
            elif chartype == 1:
                password += upper[random.randint(0, len(upper) - 1)]
            elif chartype == 1:
                password += nums[random.randint(0, len(nums) - 1)]
            elif chartype == 3:
                password += symbols[random.randint(0, len(symbols) - 1)]
        return password



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


