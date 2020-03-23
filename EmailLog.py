import smtplib, email, email.mime.application, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from configparser import ConfigParser, RawConfigParser


empfaenger = ""


#Versendet eine Mail mit der Logdatei im Anhang und löscht die Datei nach dem versenden aus seinem Pfad.
def email_versenden():
    global empfaenger
    message = MIMEMultipart()
    message["Subject"] = "Achtung Kritischer Systemwert!!!"
    html = """
    <html>
      <body>
        <p>Hallo Admin,<br>
           </br>
           Einer der Folgenden Systemwerte hat den kritischen Wert überschritten:<br>
           -CPU<br>
           -Arbeitsspeicher<br>
           -Freier Speicherplatz<br>
           </br>
           Im Anhang befindet sich die Datei 'logfile.txt' mit einem Log mit allen soeben genannten Sytemwerten.<br>
           Bitte  überprüfen sie ihren PC!
           <br>
        </p>
      </body>
    </html>
    """
    part2 = MIMEText(html, "html")
    message.attach(part2)
    log_datei = ("logfile.txt")
    fo = open(log_datei, 'rb')
    attach = email.mime.application.MIMEApplication(fo.read(), _subtype='txt')
    fo.close()
    attach.add_header('content-disposition', 'attachment', filename=log_datei)
    message.attach(attach)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10) as server:
            config = ConfigParser()
            try:
                ini_öffnen = open("sender_config,ini")
                if ini_öffnen:
                    config.read("sender_config.ini")
            except:
                raw_parser = RawConfigParser()
                if ~config.has_section(""):
                    raw_parser.add_section("MAILDATEN")
                    raw_parser.set("MAILDATEN", "sender", "paustian.niklas@gmail.com")
                    raw_parser.set("MAILDATEN", "passwort", "yqejarzdwdfgycbj")
                    with open("sender_config.ini", "a") as maildaten:
                        raw_parser.write(maildaten)
                    config.read("sender_config.ini")
            sender = config['MAILDATEN']['sender']
            password = config['MAILDATEN']['passwort']
            server.login(sender, password)
            if empfaenger == "":
                empfaenger = input("Empfänger: ")
            server.sendmail(sender, empfaenger, message.as_string())
            print("Mail gesendet!")
            os.remove("logfile.txt")
    except Exception as e:
        if "timeout" in str(type(e)).lower():
            print("\nSMTP-Server Verbindung Timed out!\n")
        else:
            print(type(e))
