import psutil
from datetime import datetime
from EmailLog import email_versenden
from configparser import ConfigParser, RawConfigParser


schwellenwerte_config = ConfigParser()
program_run = True
currentTime = datetime.now()
wasCritical = False
cpu_stats = psutil.cpu_stats()
raw_parser = RawConfigParser()


#Prüft ob die .ini mit den Schwellenwerten vorhanden ist. Wenn sie es nicht ist wird sie erstellt.
def schwellenwerte_vorhanden():
    try:
        ini_öffnen = open("schwellenwerte_config.ini")
        if ini_öffnen:
            schwellenwerte_config.read("schwellenwerte_config.ini")
    except:
        if ~schwellenwerte_config.has_section(""):
            raw_parser.add_section("SCHWELLENWERTE")
            raw_parser.set("SCHWELLENWERTE", "cpu_critical", "5")
            raw_parser.set("SCHWELLENWERTE", "cpu_warning", "70")
            raw_parser.set("SCHWELLENWERTE", "ram_critical", "90")
            raw_parser.set("SCHWELLENWERTE", "ram_warning", "70")
            raw_parser.set("SCHWELLENWERTE", "ssd_critical", "5")
            raw_parser.set("SCHWELLENWERTE", "ssd_warning", "30")
            with open("schwellenwerte_config.ini", "a") as schwellenwerte:
                raw_parser.write(schwellenwerte)
            schwellenwerte_config.read("schwellenwerte_config.ini")


#Prüft ob die CPU-Auslastung einen bestimmten Wert überschreitet und gibt diesen Wert dann aus, selbst wenn der Wert nicht überschritten ist.
#Zudem wird dieser Wert auch in eine Logdatei geschrieben.
def cpu():
    global wasCritical
    cpu_prozent = psutil.cpu_percent(interval=1)
    schwellenwerte_vorhanden()
    cpu_critical = int(schwellenwerte_config['SCHWELLENWERTE']['cpu_critical'])
    cpu_warning = int(schwellenwerte_config['SCHWELLENWERTE']['cpu_warning'])
    if cpu_prozent >= cpu_critical:
        wasCritical = True
        print('\t' + '\t' + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + '\t' + 'CPU-Kritisch: ' + str(cpu_prozent) + '%')
        write_log("CPU-Kritisch: " + str(cpu_prozent) + '%')
    elif cpu_prozent >= cpu_warning:
        print(datetime.now().strftime('%d-%m-%Y %H:%M:%S') + '\t' + 'CPU-Warnung: ' + str(cpu_prozent) + '%')
        write_log("CPU-Warnung: " + str(cpu_prozent) + '%')
    else:
        print(datetime.now().strftime('%d-%m-%Y %H:%M:%S') + '\t' + 'CPU-Auslastung: ' + str(cpu_prozent) + '%')
        write_log("CPU-Auslastung: " + str(cpu_prozent) + '%')


#Macht das gleiche wie die Methode CPU nur mit der Ram-Auslastung.
def ram():
    global wasCritical
    ram_prozent = psutil.virtual_memory().percent
    schwellenwerte_vorhanden()
    ram_critical = int(schwellenwerte_config['SCHWELLENWERTE']['ram_critical'])
    ram_warning = int(schwellenwerte_config['SCHWELLENWERTE']['ram_warning'])
    if ram_prozent >= ram_critical:
        wasCritical = True
        print('\t' + '\t' + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + '\t' + 'RAM-Kritisch: ' + str(ram_prozent) + '%')
        write_log("RAM-Kritisch: " + str(ram_prozent) + '%')
    elif ram_prozent >= ram_warning:
        print(datetime.now().strftime('%d-%m-%Y %H:%M:%S') + '\t' + 'RAM-Warnung: ' + str(ram_prozent) + '%')
        write_log("RAM-Warnung: " + str(ram_prozent) + '%')
    else:
        print(datetime.now().strftime('%d-%m-%Y %H:%M:%S') + '\t' + 'RAM-Auslastung: ' + str(ram_prozent) + '%')
        write_log("RAM-Auslastung: " + str(ram_prozent) + '%')


#Macht das gleiche wie die Methode CPU nur mit dem freien Speicher.
def ssd():
    global wasCritical
    ssd_frei_prozent = float(psutil.disk_usage("/").free) / float(psutil.disk_usage("/").total)*100
    schwellenwerte_vorhanden()
    ssd_critical = int(schwellenwerte_config['SCHWELLENWERTE']['ssd_critical'])
    ssd_warning = int(schwellenwerte_config['SCHWELLENWERTE']['ssd_warning'])
    if ssd_frei_prozent <= ssd_critical:
        ssd_frei_prozent = str(ssd_frei_prozent)[0:5]
        wasCritical = True
        print('\t' + '\t' + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + '\t' + 'SSD-Frei Kritisch: ' + str(ssd_frei_prozent)[0:4] + '%')
        write_log("SSD-Frei Kritisch: " + str(ssd_frei_prozent)[0:4] + '%')
    elif ssd_frei_prozent <= ssd_warning:
        print(datetime.now().strftime('%d-%m-%Y %H:%M:%S') + '\t' + 'SSD-Frei Warnung: ' + str(ssd_frei_prozent)[0:4] + '%')
        write_log("SSD-Frei Warnung: " + str(ssd_frei_prozent)[0:4] + '%')
    else:
        print(datetime.now().strftime('%d-%m-%Y %H:%M:%S') + '\t' + 'SSD-Frei: ' + str(ssd_frei_prozent)[0:4] + '%')
        write_log("SSD-Frei: " + str(ssd_frei_prozent)[0:4] + '%')


#Öffnet die Datei 'logfile.txt' und schreibt in den Methoden cpu, ram, ssd dementsprechendes in die Datei. Wenn die Datei nicht vorhanden ist wird diese angelegt.
#Wenn eine Kritische Melung innerhalb der letzten 60 Sekunden aufgetaucht ist, wird eine Mail mit dem Log versendet.
def write_log(msg):
    global wasCritical
    file = open("logfile.txt", "a")
    file.write(str(datetime.now().strftime('%d-%m-%Y %H:%M:%S')) + " " + msg + "\n")
    if (datetime.now() - currentTime).seconds > 5 and wasCritical == True:
        wasCritical = False
        #sende_mail()


#Ruft die Globale Variable currentTime auf und setzt damit die Zeit neu auf den jetztigen Zeitpunkt und führt die Methode 'email_versenden' aus 'EmailLog.py' aus.
def sende_mail():
    global currentTime
    currentTime = datetime.now()
    email_versenden()
