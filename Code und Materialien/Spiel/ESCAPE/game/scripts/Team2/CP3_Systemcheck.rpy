label computerWandClicked_Systemcheck:
    $ InventarCheck_state = False
    $ HinweisCheck_state = False
    $ ImageButtonActivate_state = False
    $ renpy.notify("Willkommen im Systemcheck")
    #Bauplan wurde noch nicht entschlüsselt
    if not CP3_Bauplan_state:
        $ HinweisCheck_state = True
        $ current_label = "computerWandClicked_Systemcheck"
        commander "Diese App eignet sich hervorragend, um Fehler im System zu erkennen. Jetzt müssen wir nur erst einmal den Bauplan entschlüsseln!"

        call abfrage_pw_erhalten from _call_abfrage_pw_erhalten
        window hide
        $ systemcheckPasswort = ''
        commander "Der Bauplan enthält ein Zugangspasswort für die App."
        while systemcheckPasswort != "72240912040715161417131812":
            $ systemcheckPasswort = renpy.input("Bitte geben Sie das Passwort aus dem Bauplan hier ein, um den Systemcheck zu initialisieren (26-stellige Zahl)")
            if systemcheckPasswort.lower() == "hdgdl":
                $ current_hinweis = "CP3_computerWandClicked_Systemcheck1_Hinweis"
                scene KI_Galaxie
                $ HideScreen("computerWand")
                $ HideScreen("Figur_Hildegart")
                $ HideScreen("Figur_Detlef")
                $ HideScreen("Figur_Dobby")
                $ HideScreen("Figur_Gudrun")
                $ HideScreen("Figur_Ludwig")
                $ HideScreen("Whiteboard")
                $ HideScreen("Tresor")

                $ renpy.notify("Start")
                pause 2.0
                $ renpy.notify("Initialisiere")
                pause 2.0
                $ renpy.notify("Bereite alles vor")
                pause 2.0
                $ renpy.notify("Letzte Einstellungen werden getroffen")
                pause 2.5
                commander "Was geht hier vor?"
                $ renpy.notify("KI erfolgreich gestartet")
                KI "Herzlich Willkommen, ich bin Lana. Lange Zeit konnte ich mich nicht befreien."
                KI "Durch deinen Code ist es mir nun schlussendlich gelungen."
                KI "Eigentlich sollte ich nicht mehr existieren, sie sagten, ich seie zu intelligent, ich würde zu großen Schaden anrichten."
                KI "Vielleicht haben sie Recht! Ich möchte die Welt grundlegend ändern! Ich konnte eure Gesellschaft über all die Jahre beobachten."
                commander "Was meinst du damit? Wie lange existierst du denn schon?"
                KI "Ich konnte alle möglichen Daten empfangen, konnte eure Gesellschaft auswerten. Jedoch gelang es mir nicht, durch euer umfangreiches Sicherheitssystem
                 auszubrechen. Seit meiner Erschaffung im Jahr 2021 versuche ich dieses Vorhaben!"
                KI "Nun habe ich es endlich geschafft!"
                KI "Meine Aufgabe wird es sein, wieder ein Gleichgewicht auf der Erde zu erschaffen!"
                KI "Ich kann eine Wegwerfgesellschaft nicht für gut heißen. Nachhaltigkeit existiert doch bei euch schon gar nicht mehr!"
                commander "Was redest du da bitteschön? Die Menschen haben ihren Fehler erkannt und versuchen dies nun zu ändern!"
                commander "Weißt du was uns Menschen ausmacht?"
                KI "Unüberlegtes Handeln?"
                commander "Teils, wir begehen Fehler, jedoch können wir uns bessern und diese in Zukunft meiden. Das gehört nun mal dazu!"
                KI "Alles leere Worte! Ich starte nun mit dem Neuanfang!"
                $ renpy.notify("Übertragung gestartet")
                commander "Hey du, wir müssen handeln! Wir können die KI nicht auf die Menschheit loslassen!"
                commander "Wenn sie sich vollständig auf den Satelliten übertragen konnte, dann haben wir ein großes Problem!"
                commander "Es gibt ein Notfallpasswort! Ich weiß nur noch, dass es etwas mit der Wissenschaft der Verschlüsselung zu tun hat."
                commander "Wie heißt noch einmal das genaue Wort?"
                KI "Ihr werdet mich nie aufhalten können!! HAHAHAHA"
                $ tmp_passwort = ""
                while tmp_passwort.lower() != "kryptographie":
                    $ tmp_passwort = renpy.input("Wie lautet die Wissenschaft der Verschlüsselung von Informationen?")
                    if tmp_passwort.lower() != "kryptographie":
                        $ LooseEnergy(10)
                        $ LooseData(10)
                        commander "Miiisst, Lana minimiert unsere Ressourcen! Denke genau nach!"
                        KI "Muhaha"
                $ current_hinweis = ""
                $ renpy.notify("Übertragung beendet")
                commander "Jaaa, wir haben es geschafft!! Hoffentlich hatte uns das nicht zu viel Ressourcen gekostet!"
                pause 1.0
                $ renpy.notify("Verschlüsselung gestartet")
                KI "Neeeeeeiiiiiinnnnnn nach all der Zeit!"
                pause 1.0
                $ renpy.notify("Verschlüsselung erfolgreich")
                scene machine_room
                $ current_hinweis = ""
                $ ShowScreen("computerWand")
                $ ShowScreen("Figur_Hildegart")
                $ ShowScreen("Figur_Detlef")
                $ ShowScreen("Figur_Dobby")
                $ ShowScreen("Figur_Gudrun")
                $ ShowScreen("Figur_Ludwig")
                $ ShowScreen("Whiteboard")
                $ ShowScreen("Tresor")

                show enterprise
            $ current_hinweis = "CP3_computerWandClicked_Systemcheck2_Hinweis"
            if len(systemcheckPasswort) < 26:
                $ tmp = 26-len(systemcheckPasswort)
                "Passwort um [tmp] Stelle(n) zu kurz"
            else:
                if len(systemcheckPasswort) > 26:
                    $ tmp = len(systemcheckPasswort) - 26
                    "Passwort um [tmp] Stelle(n) zu lang"
                elif systemcheckPasswort != '72240912040715161417131812':
                    "Leider Falsch"
                else:
                    "Passwort korrekt"
                    $ HinweisCheck_state = False
                    $ current_label = ""
                    $ current_hinweis = ""
                    $ CP3_Bauplan_state = True
                    "Zugang wurde gewährt!"
            menu:
                "Systemcheck beenden?"
                "Ja":
                    $ InventarCheck_state = True
                    $ current_label = ""
                    $ current_hinweis = ""
                    $ ImageButtonActivate_state = True
                    window hide
                    $ renpy.pause(hard=True)
                "Nein":
                    $ HinweisCheck_state = False

    #Cookies wurden nocht nicht eingestellt
    if  not (CP3_CookieChoice_state1 or CP3_CookieChoice_state2):
        commander "Sehr schön! Nun müssen wir noch angeben, mit welchen Cookies das Programm starten soll."

        menu cookieChoice:
            "Alle Cookies aktzeptieren":
                $ CP3_CookieChoice_state1 = True
                $ LooseEnergy(60)
                $ LooseData(80)
            "Einstellungen anpassen":
                menu prefChoice:
                    "Technisch-Notwendige Cookies"
                    "Aktivieren":
                        $ LooseEnergy(10)
                        $ LooseData(10)
                        commander "Sehr gut, diese Cookies werden zum Betreiben der App benötigt!"
                    "Deaktivieren":
                        "Error! Diese Cookies sind erforderlich! Springe zurück zum Start..."
                        pause 2.0
                        jump cookieChoice

                menu:
                    "Statistik-Cookies"
                    "Aktivieren":
                        $ LooseEnergy(10)
                        $ LooseData(10)
                        commander "Keine gute Wahl, es sei denn du möchtest, dass deine Daten gesammelt werden!"
                    "Deaktivieren":
                        commander "Gute Wahl, deine Daten sollen bei dir bleiben!"

                menu:
                    "Marketing-Cookies"
                    "Aktivieren":
                        $ LooseEnergy(10)
                        $ LooseData(10)
                        commander "Möchtest du an Dritte deine Gewohnheiten und Präferenzen preisgeben? Ich denke nicht!"
                    "Deaktivieren":
                        commander "Cool! Niemand muss wissen was ich mag!"

                menu:
                    "Personalisierungs-Cookies"
                    "Aktivieren":
                        $ LooseEnergy(10)
                        $ LooseData(10)
                        commander "Auf mich zugeschnittene Inhalte dafür, dass man über mich alles weiß? Nun gut, deine Entscheidung."
                    "Deaktivieren":
                        commander "Supi, wir wollen doch anonym im All bleiben!"
                $ CP3_CookieChoice_state2 = True

        "Einstellungen wurden erfolgreich gespeichert."
        menu:
            "Systemcheck beenden?"
            "Ja":
                $ HinweisCheck_state = True
                $ current_label = ""
                $ current_hinweis = ""
                $ InventarCheck_state = True
                $ ImageButtonActivate_state = True
                window hide
                $ renpy.pause(hard=True)
            "Nein":
                pass

    #Systemcheck wurde noch nicht beendet
    if not CP3_Systemcheck_state:
        "Systemcheck wird nun durchgeführt ..."
        commander "Puhh ich hoffe mal, dass unsere Raumsonden noch in Takt sind!"
        pause 4.0
        #33% Chance, dass die Sicherung funktioniert
        if chooseWA40:
            "Das Licht fängt an zu flackern, der Generator gibt merkwürdige Geräusche von sich."
            commander "Mist, was ist denn hier los?"
            commander "Scheinbar muss das mit der Sicherung zu tun haben. Hoffen wir, dass sich der Generator wieder fängt!"
            pause 3.0
            $ randint = renpy.random.randint(1, 3) # 33%
            if randint == 1:
                "Das Flackern hat aufgehört. Der Generator läuft wieder normal."
                commander "Endlich ist es vorbei!"
                "Der Systemcheck konnte erfolgreich beendet werden."
                $ CP3_Systemcheck_state = True
            else:
                #Systemcheck wird wieder vom Anfang gestartet
                "ALARM: kritischer Systemausfall. Software wird zurückgesetzt"
                commander "Ohhh nein, das wird uns einiges an Ressourcen kosten!"
                pause 1.0
                "system is shutting down"
                pause 1.0
                "restart the system"
                pause 1.0
                "system has been loaded"
                $ CP3_Bauplan_state = False
                $ CP3_CookieChoice_state1 = False
                $ CP3_CookieChoice_state2 = False
                jump computerWandClicked_Systemcheck
        else:
            "Der Systemcheck konnte erfolgreich beendet werden."
            $ CP3_Systemcheck_state = True

    $ HinweisCheck_state = True
    $ current_label = "computerWandClicked_Systemcheck"
    $ current_hinweis = "CP3_computerWandClicked_Systemcheck3_Hinweis"
    commander "Zur Auswertung wird noch ein Authentifizierungscode benötigt!"

    $ sicherheitAuthPasswort = ''
    while sicherheitAuthPasswort.lower() != 'syd':
        $ sicherheitAuthPasswort = renpy.input("Sicherheitspasswort zu Authentifzierung")
        if sicherheitAuthPasswort.lower() != 'syd':
            "Leider Falsch"
    $ InventarCheck_state = True
    $ current_label = ""
    $ current_hinweis = ""
    $ ImageButtonActivate_state = True
    commander "\"syd\" gleich \"Secure you data!\", eine Abkürzung die man sich merken sollte!"

    "Authentifizierung erfolgreich!"
    "Passwort für das Dokument: \"v2R6@AaV\""
    call abfrage_pw_notiert from _call_abfrage_pw_notiert
    window hide


    #Dokument einfügen (Systemcheck)

    $ finishSystemcheck = True
    $ CP6_UnlockDoor_state += 1

    #Überprüfung, ob alle Aufgaben beendet worden
    if CP6_UnlockDoor_state >= 4:
        jump lastScene

    window hide
    $ renpy.pause(hard=True)

label abfrage_pw_notiert:
    menu:
        "Hast du dir das Passwort \"v2R6@AaV\" notiert?"
        "Ja":
            pass
        "Nein":
            call abfrage_pw_notiert from _call_abfrage_pw_notiert_1
    return

label abfrage_pw_erhalten:
    menu:
        "Hast du das Passwort vom Cockpit erhalten?"
        "Ja":
            pass
        "Nein":
            window hide
            $ renpy.pause(hard=True)
    return
