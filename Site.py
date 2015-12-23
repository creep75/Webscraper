"""Site Class zum grundsätzlichen Aufbau des Site Objects

Aufbau siehe __init__ Methode

"""
from bs4 import BeautifulSoup
import urllib.request
from Connection import Connection
from multiprocessing.dummy import Pool as ThreadPool
from time import sleep
import random
from style import style





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
        der Random Methode von Proxies (+ Überprüfung derselben) und User Agents)

        :param Sitename: Name der Site
        :return: Config
        """
        return True

    def scraping(self):

        """
        Diese Methode wird zum rudimentären Scraping verwendet und dient nur als Demo für die Proxy
        Random Methode und die User Agents Random Methode.

        Am Anfang wird ein neues Connection Object erzeugt.
        Danach wird mittels der Methode check_proxy() ein Proxy per Zufall ausgewählt und gleich überprüft (Kriterien siehe
        Methode check_proxy()). Wenn der Proxy nicht den Kriterien entspricht wird automatisch ein neuer ausgewählt bis
        ein funktionsfähiger zu Verfügung steht. (Somit ist es möglich jeden Aufruf von einem anderen Proxy
        durchführen zu lassen). Zusätzlich wird pro Aufruf der Useragent per Zufall manipuliert.
        Um das Verhalten noch etwas "menschlicher" zu machen wird zwischen den Aufrufen ein random sleep verwendet,
        somit erscheinen die Aufrufe in den Logfiles der abgeschöpften Server nicht allzu verdächtig.
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
            randtime = random.randint(0, 1000)/1000
            sleep(randtime)
            print('Sleep: ' + style.BOLD + str(randtime) + style.END)
            response = session_new.get(completeLink)
            print(response.text)





