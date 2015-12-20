from Site import Site
from Connection import Connection
import requests
import random
from proxylist import ProxyList
from time import sleep

class style:
   BOLD = '\033[1m'
   END = '\033[0m'
#Seite = Site('Mindmachine', 'http://www.derstandard.at', 'utf-8', 'Mindmachinetest','','','')
#Seite.scraping()
#print(Seite.Project)
#print(Seite.content)
#for link in Seite.content.find_all('a',href=True, text=True):
   # print(link.string, link.get("href"))
   #print(link.get('href'))

pl = ProxyList()
pl.load_file('C:/Users/creep/PycharmProjects/Testprojekt/Proxyliste.txt')
pl.random()


user_agents = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
]

Conn = Connection()

def random_proxies():
    """
    Methode zur Auswahl der Proxies per Zufallsgenerator
    :return: Proxy
    """
    return pl.random().address()


def random_user_agents():
    """
    Methode zur Auswahl der User Agents per Zufallsgenerator
    :return: User Agent
    """
    return random.choice(user_agents)


def check_proxy(session):
    """
    Methode zur Überprüfung des Proxies
    :param session:
    """
    session.proxies = random_proxies()
    session.headers = random_user_agents()
    randtime = random.randint(0, 1000)/1000
    sleep(randtime)
    response = session.get('http://canihazip.com/s')
    returned_ip = response.text
    #print(returned_ip)
    print('Sleep: ' + style.BOLD + str(randtime) + style.END)
    print('Der verwendete Proxy ist:' + style.BOLD +  session.proxies + style.END)
    print(session.headers)
    #if returned_ip != proxy_host:
    #    raise BaseException('Proxy check failed: {} not used while requesting')
    #else:
     #   print('yeah')


#session = requests.Session()
s = requests.Session()
#s.proxies = proxies
#session.headers = random_user_agent()  # will imported with "from user_agents import random_user_agent"
#session.proxies = {'http': "http://{username}:{password}@{host}:{port}/".format(**proxy)}
for i in range (0, 20):
    print('Durchlauf: ' + str(i))
    check_proxy(s)

