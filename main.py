import os
from gtts import gTTS
import speech_recognition as sr
import webbrowser
from time import ctime
import random
import ccxt
kraken = ccxt.kraken() # Für Kyptobörse

r = sr.Recognizer() #initializiere dem Recognizer als r

gerufen = False

class Person:
    name = 'Dein_Name'

# aufnahme von audio und setzte als text um.
def audio_aufnahme(eingabe=False):
    with sr.Microphone() as mic:
        if eingabe:
            sprechen(eingabe)
        audio = r.listen(mic)
        sprach_daten = ''
        try:
            sprach_daten = r.recognize_google(audio, language='DE-de')
        except sr.UnknownValueError:
            print("Nicht recognized")
        except sr.RequestError:
            print("System nicht erreichbar")
        print(f">> {sprach_daten.lower()}")
        return sprach_daten.lower()


def sprechen(audio_string):
    tts = gTTS(text=audio_string, lang='de')
    audio_datei = 'audio.mp3'
    tts.save(audio_datei)
    os.system('play ' + audio_datei + ' tempo 1.5') #spielt die datei mit sox
    os.remove(audio_datei) #hiermit wird die datei wieder gelöscht



def kripto_mana():
    for trade in kraken.fetch_trades('MANA/EUR'): # MANA mit ETH für Etherium usw verstellbar
        mana = float(f'{trade["price"]}')
        return mana

def kripto_btc():
    for trade in kraken.fetch_trades('BTC/EUR'):
        btc = float(f'{trade["price"]}')
        return btc

def there_exists(terms):
    for term in terms:
        if term in sprach_daten:
            return True

def antwort(sprach_daten):
    import time
    global gerufen
    def check_uhr():
        time = ctime().split(" ")[3].split(":")[0:2]
        minuten = time[1]
        return minuten

    if there_exists(['wer bist du', 'wie heißt du', 'wie soll ich dich nennen']):
        ich_bin = ["Ich bin Katja", "Vielleicht willst du mal par antworten hinzufügen",
                   "Ich bin die verrückte spaß assistent Katja", "Katja"]
        ich = ich_bin[random.randint(0, len(ich_bin) - 1)]
        sprechen(ich)
        gerufen = False

    if there_exists(['katja liebst du mich', 'hast du mich lieb', 'katja magst du mich']):
        liebe = [f"Warum fragst du so etwas {Person.name}", "Natürlich, du bist ja mein schöpfer",
                   "Schreib doch par neue lines dann können wir uns mehr unterhalten"]
        ant = liebe[random.randint(0, len(liebe) - 1)]
        sprechen(ant)

    #Uhr
    elif there_exists(["wie spät ist es","sag mir die zeit","wie viel uhr ist es"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            stunden = '12'
        else:
            stunden = time[0]
        minuten = time[1]
        uhr = f'Es ist {stunden} Uhr {minuten}'
        sprechen(uhr)


    elif there_exists(["erstelle alarm", "erstelle ein alarm"]):
        alarm = sprach_daten.split("alarm")[-1]
        os.system("sleep {}h && play alarm.mp3".format(alarm))


    # Youtube
    elif there_exists(['suche auf youtube']):
        suche = sprach_daten.split('suche auf youtube')[-1]
        url = f"https://www.youtube.com/results?search_query={suche}"
        sprechen('Mal schauen was ich in youtube finde')
        webbrowser.get().open(url)

    # Duckduckgo
    elif there_exists(['suche im internet']):
        suche_net = sprach_daten.split('suche im internet')[-1]
        url_net = f"https://duckduckgo.com/?q={suche_net}&t=ffab&atb=v256-1&ia=web"
        sprechen('Mal schauen was ich finden kann')
        webbrowser.get().open(url_net)

    # Mein Github
    elif there_exists(['öffne mein github']):
        url_github = f"https://github.com/Saizzou-dev"
        sprechen('Neue Projekte auf lager? Na dann')
        webbrowser.get().open(url_github)

    # Netflix
    elif there_exists(['öffne netflix']):
        url_netflix = f"https://www.netflix.com"
        sprechen('Lust auf eine neue serie')
        webbrowser.get().open(url_netflix)

    # Amazon
    elif there_exists(['öffne amazon serien']):
        url_amazon = f"https://www.amazon.de/Amazon-Video/b/<URL>" # Dies ist benutzer relevant
        sprechen('Lust auf eine neue serie')
        webbrowser.get().open(url_amazon)


    #Screenshot
    elif there_exists(['mach ein screenshot']):
        sprechen("Wähle dem bereich aus")
        os.system('gnome-screenshot -a') # Der Mouse Zeiger ändert sich damit eine auswahl vorhanden ist und nicht ganzer screen gespeichert wird


    # Programme
    elif there_exists(['öffne virtuellen pc']):
        sprechen("VM Player wird geöffnet")
        os.system('vmplayer') # Als Beispiel

    elif there_exists(['öffne python']):
        sprechen("PyCharm wird geöffnet")
        os.system('charm') # Als Beispiel

    elif there_exists(['öffne java']):
        sprechen("Java wird geöffnet")
        os.system('eclipse') # Wenn nicht in PATH dann erstellen

    elif there_exists(['öffne eine skitze']):
        sprechen("draw io wird geöffnet")
        os.system('drawio') # Als Beispiel

    elif there_exists(['öffne handschrifft']):
        sprechen("journal für pen tablet wird geöffnet")
        os.system('xournalpp') # Als Beispiel

    elif there_exists(['öffne notizen']):
        sprechen("deine notizen werden geöffnet")
        os.system('cherrytree') # Als Beispiel


    # System befehle
    elif there_exists(['katja mach ein neustart']):
        sicher = audio_aufnahme('Soll ich wirklich ein neustart machen?')
        sicher = audio_aufnahme()
        time.sleep(2)
        if 'ja' in sicher:
            os.system('reboot')

    elif there_exists(['katja fahr dem pc runter']):
        sicher = audio_aufnahme('Soll ich wirklich ein neustart machen?')
        sicher = audio_aufnahme()
        time.sleep(2)
        if 'ja' in sicher:
            os.system('shutdown')

    elif there_exists(['mach einen update','führe ein update durch']): # ACHTUNG WIRD NICHT EMPFOHLEN 
        sprechen("Ein update wird durchgeführt")
        os.system('echo <password> | sudo -S apt update') # Password hier einsetzen
        sprechen("Der update wurde erledigt jetzt wird der upgrade gemacht")
        os.system('echo <password> | sudo -S apt upgrade >> bericht.txt') # Password hier einsetzen
        sprechen("Der upgrade wurde erledigt. Der bericht steht in dem Projekt ordner")

    # Kripto Börse
    elif there_exists(['wie ist die kryptobörse','was macht die kryptobörse']):
        sprechen("Ich überprüfe es sofort")
        btc = kripto_btc()
        sprechen(f'{Person.name} Bitcoin steht grade bei {btc} Euro')
        mana = kripto_mana()
        sprechen(f'Und Mana coin steht bei {mana}')

    # Jede Stunde überprüft ob KryptoCoin Großen Wert Verlusst hat
    elif (check_uhr() == "01"):
        gerufen = False
        mana_txt = open("mana_stats.txt","r")
        stat_mana = mana_txt.read()
        mana_now = kripto_mana()
        if ((int(stat_mana)/int(mana_now)).strip(3) < 0.95):
            sprechen('Sir, Mana coin ist gesunken')
            mana_txt.close()
            mana_txt = open("mana_stats.txt", "w")
            mana_txt.write(mana_now)


while True:
    if not gerufen:
        sprach_daten = audio_aufnahme()
        if (str(sprach_daten) == 'katja'): #Katja wird nicht reagieren , erst nach dem sie gerufen wird!
            sprechen(f"Ja bitte {Person.name}")
            gerufen = True

    if gerufen:
        sprach_daten = audio_aufnahme()
        antwort(sprach_daten)
