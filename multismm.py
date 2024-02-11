import requests as r
import re, time, random, os, json
from requests.exceptions import ConnectionError

M = '\033[1;31m'; H = '\033[1;32m'; K = '\033[1;33m'; B = '\033[1;34m'; P = '\033[1;37m'; N = '\033[0m'
cvurl = lambda url, host='https://www.like4like.org/': host + url if host not in url else url

class Setup:
    account_list = [('tukimins','akun123'), ('jamalud','akun123'), ('azzamxyz','akun123'), ('ipanxs','akun123'), ('animexyz','akun123'), ('tukimans','akun123')] #- paste akun (uname, pw)
    session_list = []

    def __init__(self):
        os.system('clear')
        for uname, passw in self.account_list:
            self.login(uname, passw)

        os.system('clear')
        print()
        print(f'{B}╔╦╗{N}┌─┐   {B}╔═╗{N}┌─┐┌┐┌┌─┐┬   ')
        print(f'{B}║║║{N}┌─┘───{B}╠═╝{N}├─┤│││├┤ │   {H}⟦{M}⟐{H}⟧{N} KLOWOR TEAM')
        print(f'{B}╩ ╩{N}└─┤   {B}╩  {N}┴ ┴┘└┘└─┘┴─┤ {H}⟦{M}⟐{H}⟧{N} Meizug ────{H}┈┈{N}╮')
        print(f'{N}     ╰────────────────────────────────────╯')
        print(f'{B}❲{H}➣{B}❳{N} Number of accounts:{M} {len(self.session_list)}')
        print(f'{B}❲{H}➣{B}❳{N} Total credits:{K} Ntar 99999999')
        print()
        print(f'{H}❲{M}1{H}❳{N} Mining bulk coins')
        print(f'{H}❲{M}2{H}❳{N} Make an order')
        print()

        chs = int(input(f'{M} -{N} Chose:{K} '))
        if chs in [0o1]: self.mining()


    def login(self, uname, passw):
        with r.session() as ses:
            ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
            ses.headers.update({'Accept': 'application/json, text/javascript, */*; q=0.01', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'Referer': 'https://www.like4like.org/earn-credits.php?feature=youtube', 'sec-ch-ua': '"Google Chrome";v="118", "Chromium";v="118", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'User-Agent': ua, 'X-Requested-With': 'XMLHttpRequest'})
            
            source = ses.get(cvurl('login')).text
            data = {'time': re.search(r'"time=(.*?)\&', source).group(1),'token': re.search(r'\&token=(.*?)";', source).group(1),'username':uname,'password':passw,'recaptcha':''}
            post = ses.post(cvurl('api/login.php'), data=data).json()
            if post['success']:
                self.session_list.append((ses, uname))
                print(f'{N}Info:{B} ({H}{uname}{B}|{H}{passw}{B}){N} Berhasil masuk.')
            else:
                print(f'{N}Info:{B} ({M}{uname}{B}|{M}{passe}{B}){N} Gagal masuk.')

    def mining(self):
        print(f'{N}\nGunakan{B} ({M} CTRL{N} +{M} C {B}){N} untuk berhenti.')
        print(f'{N}Support by {B}"{P}TEAM KLOWOR ID{B}"', end='\n\n')
        while True:
            try:
                for ses, uname in self.session_list:
                    feature = random.choice(['askfml', 'facebookcom', 'facebook', 'facebooksub', 'facebookusersub','facebooksha', 'facebookvid', 'flickr', 'instagramcom', 'instagramfol','instagramlik', 'myspacecon', 'odrujoi', 'pinterestfol', 'pinterestrep','reverbnationfan', 'soundcloudfol', 'soundcloudlik', 'soundcloudlis','soundcloudrep', 'tiktokfol', 'tiktoklike', 'twitch', 'twitter', 'twitterfav','twitterret', 'vkontaktefol', 'vkontaktejoi', 'vimeolik', 'sites', 'youtubec','youtube', 'youtubes', 'youtubev'])
                    data, rewards = self.take_assignments(ses, feature)
                    if data is None and rewards is None: continue
            
                    api = ses.post(cvurl('api/validate-task.php'), data=data).json()
                    if api['success']:
                        credit = api["data"]["credits"]
                        if credit == 0: continue
                        
                        print(f'{N}Session:{H} {ses.cookies["PHPSESSID"]}{M}({H}{uname}{M})')
                        print(f'{N}Koin: {H}+{K}{rewards} {B}>>{H} {credit}{N} koin', end='\n\n')
                        time.sleep(5)
                    else:
                        pass
            except ConnectionError:
                print(f'{N}Koneksi error:{M} {time.time()}')
                time.sleep(30)
            except KeyboardInterrupt:
                break


    def take_assignments(self, ses, feature):
        ses.get(cvurl(f'earn-credits.php?feature={feature}'))
        api = ses.get(cvurl(f'api/get-tasks.php?feature={feature}')).json()
        if api['success']:
            try: core = api['data']['tasks'][0]
            except: return (None, None)

            patch = {'idzat': core['idlink'],'vrsta': core['featureType'],'idcod': core['taskId'],'feature': feature,'_': int(time.time() *1000)}
            api = ses.get(cvurl('api/start-task.php?' + '&'.join('%s=%s'%(key, value) for key, value in patch.items()))).json()
            if api['success']:
                data = {'url': core['url'],'idzad': patch['idcod'],'idlinka': patch['idzat'],'idclana': api['data']['codedTask'] +'=true','vrsta': patch['vrsta'],'feature': feature,'addon': 'false','version': ''}
                return (data, core['value'])

        return (None, None)
        

Setup()


