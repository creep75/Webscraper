from bs4 import BeautifulSoup
import urllib.request
from Connection import Connection
from multiprocessing.dummy import Pool as ThreadPool

"""Site Class zum grundsätzlichen Aufbau des Site Objects

Folgende Methoden werden zu Verfügung gestellt...

"""


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
        """Methode zum Laden der Konf

        :param Sitename: Name der Site
        :return: Config
        """
        if self.__Kontostand - betrag < -self.__Kontokorrent:
            # Deckung nicht genuegend
            return False
        else:
            self.__Kontostand -= betrag
            ziel.__Kontostand += betrag
            return True

    def scraping(self):

        """

        :rtype: object
        :param ebenen:
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
            print(link)


