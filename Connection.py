import requests
import random
from proxylist import ProxyList
from time import sleep
from style import style

"""Site Connection zum grundsätzlichen Aufbau des Site Objects

Folgende Methoden werden zu Verfügung gestellt...

"""


class Connection(object):
    def __init__(self):

        """
        Konstruktor
        """
        #self.Url = Url
        SOURCE_FILE='Useragents.txt'

        f = open(SOURCE_FILE)
        self.agents = f.readlines()

        self.pl = ProxyList()
        self.pl.load_file('C:/Users/creep/PycharmProjects/Testprojekt/Proxyliste3.txt')
        self.pl.random()


    def random_proxies(self):
        """
        Methode zur Auswahl der Proxies per Zufallsgenerator
        :return: Proxy
        """
        proxies = {
                  'http': self.pl.random().address(),
                  }
        print('Proxyneu =' + str(proxies))
        return proxies


    def random_user_agents(self):
        """
        Methode zur Auswahl der User Agents per Zufallsgenerator
       :return: User Agent
        """
        return random.choice(self.agents).strip()


    def check_proxy(self):
        """
        Methode zur Überprüfung des Proxies
        :param session:
        """

        session = requests.Session()
        session.proxies = self.random_proxies()
        session.headers = self.random_user_agents()
        #print(session.headers)
        randtime = random.randint(0, 1000)/1000
        sleep(randtime)
        try:
            response = session.get('http://canihazip.com/s', proxies = session.proxies)
            while not response:
                      session.proxies = self.random_proxies()
                      response = session.get('http://canihazip.com/s', proxies = session.proxies, timeout=0.001)
            returned_ip = response.text
        finally:

               print('Sleep: ' + style.BOLD + str(randtime) + style.END)
               print('Der verwendete Proxy ist:' + style.BOLD +  str(session.proxies) + style.END)
               print('Suche: '  + str(session.proxies["http"].find(":")))

               try:
                   print('Returned IP: ' + str(returned_ip))
                   print('Proxy Substring' + str(session.proxies["http"][0:session.proxies["http"].find(":")]))
                   if returned_ip == session.proxies["http"][0:session.proxies["http"].find(":")]:
                    return session
               except:
                    return False
