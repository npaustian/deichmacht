import psutil, sys, platform, socket
from os import getcwd

#Die Methode Zeigt diverse Systemwerte an. Jedoch wird zuerst geprüft ob das Betriebssystem MacOS(darwin), Windows(win32) oder Linux(linux) ist.
#Es gibt dem Nutzer eine Übersicht wie viel Leistung der PC zur verfügung hat und unter welchen Namen er erreichbar ist.
def systemwerte():
    # Prüfung ob das Betriebssystem MacOS ist.
    if sys.platform.startswith('darwin'):
        print("\nSysteminformationen:",
              "\nRechner: ", platform.node(),
              "\nHostname: ", socket.getfqdn(),
              "\nIP-Adresse: ", socket.gethostbyname(socket.gethostname()),
              "\nPython-Version: ", platform.python_version(),
              "\nAktuelles Verzeichnis:", getcwd(),
              "\nBetriebssystem: ", platform.uname().system,
              "\nFestplattenpeicher: ", str(psutil.disk_usage("/").total)[0:3], "GB",
              "\nArbeitsspeicher: ", str(psutil.virtual_memory().total)[0], "GB",
              "\nProzessor: ", platform.processor(),
              "\n\tLogische Kerne: ", psutil.cpu_count(logical=True),
              "\n\tPhysische Kerne: ", psutil.cpu_count(logical=False), "\n"
              )
    # Prüfung ob das Betriebssystem Windows ist.
    elif sys.platform.startswith('win32'):
        print("\nSysteminformationen:",
              "\nRechner: ", platform.node(),
              "\nHostname: ", socket.getfqdn(),
              "\nIP-Adresse: ", socket.gethostbyname(socket.gethostname()),
              "\nPython-Version: ", platform.python_version(),
              "\nAktuelles Verzeichnis:", getcwd(),
              "\nBetriebssystem: ", platform.uname().system,
              "\nProzessor: ", platform.processor(),
              "\n\tLogische Kerne: ", psutil.cpu_count(logical=True),
              "\n\tPhysische Kerne: ", psutil.cpu_count(logical=False), "\n"
              )
    #Prüfung ob das Betriebssystem Linux ist.
    elif sys.platform.startswith('linux'):
        print("\nSysteminformationen:",
              "\nRechner: ", platform.node(),
              "\nHostname: ", socket.getfqdn(),
              "\nIP-Adresse: ", socket.gethostbyname(socket.gethostname()),
              "\nPython-Version: ", platform.python_version(),
              "\nAktuelles Verzeichnis:", getcwd(),
              "\nBetriebssystem: ", platform.uname().system,
              "\nProzessor: ", platform.processor(),
              "\n\tLogische Kerne: ", psutil.cpu_count(logical=True),
              "\n\tPhysische Kerne: ", psutil.cpu_count(logical=False), "\n"
              )
