
"""Connection Klasse zum grundsätzlichen Aufbau des Connection Objects

Aufbau siehe __init__ Methode

"""
import requests
import random
from proxylist import ProxyList
from time import sleep
from style import style




class Connection(object):
    def __init__(self):

        """
        Dies ist der Konstruktor der Connection Klasse
        Bei der Erstellung des Objektes werden folgende Tätikeiten
        ausgeführt:\n

        Laden des UserAgentsfile\n
        Laden des Proxy Files
        """
        self.SOURCE_FILE_USERAGENTS='config/Useragents.txt'
        self.SOURCE_FILE_PROXIES='config/Proxyliste3.txt'
        self.SOURCE_FILE_VALID_PROXIES='config/Proxylistevalid.txt'

        f = open(self.SOURCE_FILE_USERAGENTS)
        self.agents = f.readlines()

        p = open(self.SOURCE_FILE_PROXIES)
        self.proxyliste = p.readlines()


        self.pl = ProxyList()
        self.pl.load_file(self.SOURCE_FILE_VALID_PROXIES)
        self.pl.random()

    def check_all_proxies_in_file(self):
        """Check aller Proxies, welcher in einem File (siehe Variable SOURCE_FILE_PROXIES im Konstruktur) hinterlegt
        sind.
        Es werden folgende Punkte überprüft:

        * Ist der Proxy aktiv ?\n
        * Wird von der Seite 'http://canihazip.com/s' die IP Adresse des Proxies oder die eigene zurückgeliefert ?

        Wenn er aktiv ist und von der oben genannten Seite die IP des Proxies geliefert wird, gilt er als verwendbar
        und wird in die Datei 'proxylistevalid.txt' geschrieben.
        Diese dient als Ausgangsbasis für die Auswahl per Zufallsverfahren beim tatsächlichen Scrapen

        :rtype: object
        """
        for all_proxies in self.proxyliste:
            returned_ip = ''
            session = requests.Session()
            proxies = {
                       'http': all_proxies.strip('\n'),
                         }
            session.proxies = proxies
            print('Übergebener proxy: ' + str(session.proxies))
            try:
               response = session.get('http://api.ipify.org/', proxies = session.proxies, timeout=1)
               returned_ip = response.text
               print('Zurückgegebene IP Adresse: ' + returned_ip)
            except:
                pass
            finally:
               if returned_ip != '':
                     print('Rausgeschnittener Proxy: ' + str(session.proxies["http"][0:session.proxies["http"].find(":")]))
                     if returned_ip == session.proxies["http"][0:session.proxies["http"].find(":")]:
                        validproxies = open(self.SOURCE_FILE_VALID_PROXIES, 'a')
                        validproxies.write(all_proxies)


    def random_proxies(self):
        """
        Methode zur Auswahl der Proxies per Zufallsgenerator.
        Übernimmt das self.pl Object der Klasse
        :return: Proxy als dict
        """
        proxies = {
                  'http': self.pl.random().address(),
                  }
        print('Proxyneu =' + str(proxies))
        return proxies


    def random_user_agents(self):
        """
        Methode zur Auswahl der User Agents per Zufallsgenerator
        Übernimmt das self.agents Object der Klasse
       :return: User Agent
        """
        return random.choice(self.agents).strip()


    def check_proxy(self):
        """
        Methode zur Überprüfung des Proxies (+ Übernahme des Proxies per Zufall + Übernahme des Useragents per Zufall)

        Wird im Zuge des Scrapens angesprochen.
        Es wird mittels der Methode random_proxies(self) ein Proxy per Zufall ausgewählt und nach folgenden
        Gesichtspunkten geprüft:

        * Ist der Proxy aktiv ?\n
        * Wird von der Seite 'http://canihazip.com/s' die IP Adresse des Proxies oder die eigene zurückgeliefert ?

       Wenn er aktiv ist und von der oben genannten Seite die IP des Proxies geliefert wird, gilt er als verwendbar
       und die Session wird der aufrufenden Stelle retouniert und gilt als verwendbar.

       Zusätzlich wird der Header der Session manipuliert und mittels der Methode random_user_agents(self) ein
       User Agent per Zufall ausgewählt

        :rtype: session
        """

        session = requests.Session()
        session.proxies = self.random_proxies()
        session.headers = self.random_user_agents()

        try:
            response = session.get('http://api.ipify.org/', proxies = session.proxies)
            while not response:
                      session.proxies = self.random_proxies()
                      response = session.get('http://api.ipify.org/', proxies = session.proxies, timeout=0.001)
            returned_ip = response.text
        finally:


               print('Der verwendete Proxy ist:' + style.BOLD +  str(session.proxies) + style.END)
               print('Suche: '  + str(session.proxies["http"].find(":")))

               try:
                   print('Returned IP: ' + str(returned_ip))
                   print('Proxy Substring' + str(session.proxies["http"][0:session.proxies["http"].find(":")]))
                   if returned_ip == session.proxies["http"][0:session.proxies["http"].find(":")]:
                    return session
               except:
                    return False
