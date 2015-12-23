"""Site Class zum grundsätzlichen Aufbau des Site Objects

Aufbau siehe __init__ Methode

"""
from bs4 import BeautifulSoup
import urllib.request
from Connection import Connection
from multiprocessing.dummy import Pool as ThreadPool




class Site(object):
    def __init__(self, Name, Url, Encoding,
                 Project,
                 Table, td, href):
        """
        Ist der Konstruktur

        :param Name: Name der Site
        :param Url: Url der Site
        :param Encoding: Encoding der Site
        :param Project: um welches Projekt geht es
        :param Table: String des Tables
        :param td: String für td
        :param href: Wie wird ein Link erkannt
        """
        self.Url = Url
        self.Encoding = Encoding
        self.Project = Project
        self.Table = Table
        self.td = td
        self.href = href
        self.content = ''

    def loadconfig(self, Sitename):
        """Methode zum Laden der Konfiguration.
        In späterer Folge kann diese Klasse zum Laden der Konfiguration verwendet werden.
        Derzeit ist sie nur als TODO vorhanden. (vorliegender Scraping Prototyp dient nur zur Verifizierung
        der Round Robin Methode von Proxies und User Agents)

        :param Sitename: Name der Site
        :return: Config
        """
        return True

    def scraping(self):

        """
        Diese Methode wird zum rudimentären Scraping verwendet und dient nur als Demo für die Proxy
        Roundrobin Methode und die User Agents Round Robin Methode
        :rtype: object

        """
        new_conn = Connection()
        session_new = new_conn.check_proxy()
        while not session_new:
              session_new = new_conn.check_proxy()

        response = session_new.get(self.Url)
        print('Url = ' + self.Url)
        soup = BeautifulSoup(response.text, "html.parser")
        self.content=soup
        for link in soup.find_all('a', href=True, text=True):
            assert isinstance(link, object)
            #print(link)
            completeLink = self.Url + link['href']
            print(completeLink)
            session_new = new_conn.check_proxy()
            response = session_new.get(completeLink)
            print(response.text)





