label computerWandClicked_Browser:
    $ HinweisCheck_state = False
    $ InventarCheck_state = False
    $ ImageButtonActivate_state = False
    $ renpy.notify("Willkommen im Browser")
    $ goodBrowserChoice = False

    #Suchmaschine wurde noch nicht ausgewählt
    if not CP2_browserChoice_state:
        commander "Wir benötigen Informationen über das Raumschiff. Ich denke mit dieser Software können wir Erfolg haben!"
        menu browserChoice:
            "Suche dir bitte eine datensparsame Suchmaschine aus"
            "Lite.qwant.com":
                $ goodBrowserChoice = True
                $ CP2_browserChoice_state = True
                commander "Sehr gute Wahl! Qwant ist ein ressourcensparender Browser."
            "Google.com":
                $ CP2_browserChoice_state = True
                commander "Urgh, schlechte Wahl! Google sammelt erhebliche Mengen sensible Daten von dir."
                # Bad
            "Yahoo.com":
                $ CP2_browserChoice_state = True
                commander "Urgh, schlechte Wahl! Yahoo sammelt erhebliche Mengen sensible Daten von dir."
                # Bad
            "Web.de":
                $ CP2_browserChoice_state = True
                commander "Urgh, schlechte Wahl! Web sammelt erhebliche Mengen sensible Daten von dir."
                # Bad
            "DuckDuckGo.com":
                $ CP2_browserChoice_state = True
                $ goodBrowserChoice = True
                commander "Sehr gute Wahl! DuckDuckGo ist ein ressourcensparender Browser."
            "Bing.com":
                $ CP2_browserChoice_state = True
                commander "Urgh, schlechte Wahl! Bing sammelt erhebliche Mengen sensible Daten von dir."
                # Bad
            "T-Online.de":
                $ CP2_browserChoice_state = True
                commander "Urgh, schlechte Wahl! T-Online sammelt erhebliche Mengen sensible Daten von dir."
                # Bad
            "MetaGer.de":
                $ CP2_browserChoice_state = True
                $ goodBrowserChoice = True
                commander "Sehr gute Wahl! MetaGer ist ein ressourcensparender Browser mit Sitz in Deutschland."
            "Beenden":
                $ HinweisCheck_state = True
                $ current_label = ""
                $ current_hinweis = ""
                $ InventarCheck_state = True
                $ ImageButtonActivate_state = True
                window hide
                $ renpy.pause(hard=True)

        if goodBrowserChoice:
            $ LooseEnergy(10)
            $ LooseData(10)
        else:
            $ LooseEnergy(40)
            $ LooseData(50)

    #Suchmaschine wurde noch nicht konfiguriert
    if not CP2_browserConfig_state:
        commander "Konfiguriere anschließend noch deine Suchmaschine."

        $ enableForceHttps = False
        $ enableEmptyStartpage = False
        $ enableCoockieManagement = False
        $ enableTrackerBlocking = False
        $ blockMicro = False
        $ blockAccessToPersonalData = False
        $ blockProfiling = False

        #Browser Konfiguration
        menu:
            "Erzwingung von HTTPS"
            "Aktivieren":
                $ enableForceHttps = True
                $renpy.notify("HTTPS aktiv")
                commander "Somit sollten unsere Verbindungen abgesichert sein. Sehr gut!"
            "Deaktivieren":
                $ enableForceHttps = False
                $renpy.notify("HTTPS inaktiv")
                $ LooseEnergy(5)
                $ LooseData(5)
                commander "Ohne Verschlüsselung ist es sehr leicht unsere Daten auszuspähen. Nicht die beste Entscheidung!"

        menu:
            "Startseite deines Browsers"
            "Online Startseite":
                $ enableEmptyStartpage = False
                $renpy.notify("Startseite: Online Startseite")
                $ LooseEnergy(5)
                $ LooseData(5)
                commander "Durch deine Wahl verbrauchen wir nun unnötig mehr Ressourcen. Achte bitte bei deiner nächsten Entscheidung
                auf etwas mehr Nachhaltigkeit!"
            "leere Seite":
                $ enableEmptyStartpage = True
                $renpy.notify("Startseite: leere Seite")
                commander "Sehr schön, somit verschwenden wir keine unnötigen Ressourcen!"

        menu:
            "Cookie-Management (z.B. automatisches Löschen von Cookies)"
            "Aktivieren":
                $ enableCoockieManagement = True
                $renpy.notify("Cookie-Management aktiv")
                commander "Super! Je weniger Cookies aktiviert sind, desto geringer der Strom- und Datenverbrauch.
                Ebenso können wir so unsere Daten besser schützen."
            "Deaktivieren":
                $ enableCoockieManagement = False
                $renpy.notify("Cookie-Management inaktiv")
                $ LooseEnergy(10)
                $ LooseData(10)
                commander "Je mehr Cookies aktiviert sind, desto höher der Strom- und Datenverbrauch. Achte bitte auf
                 die übrigen Ressourcen!"

        menu:
            "Blockieren von Trackern (z.B. uBlock Origin)"
            "Aktivieren":
                $ enableTrackerBlocking = True
                $renpy.notify("Blockieren von Trackern aktiv")
                commander "Gute Wahl, so können uns die Aliens nicht finden hihi."
            "Deaktivieren":
                $ enableTrackerBlocking = False
                $renpy.notify("Blockieren von Trackern inaktiv")
                $ LooseEnergy(10)
                $ LooseData(10)
                commander "Mist, nun könnten uns Aliens aufspüren und einen erhöhten Ressourcenverbrauch
                haben wir dazu auch noch!"

        menu:
            "Mikrofonzugriff erlauben"
            "Erlauben":
                $ blockMicro = False
                $renpy.notify("Mikrofon aktiv")
                $ LooseEnergy(10)
                $ LooseData(10)
                commander "Brauchen wir das wirklich? Wir möchten auf der Erde sicher landen und keinen Kontakt mit Außerirdischen aufnehmen!"
            "Verbieten":
                $ blockMicro = True
                $renpy.notify("Mikrofon inaktiv")
                commander "Klasse! Sowas muss man wirklich nur aktivieren, wenn man auch wirklich mit jemandem sprechen möchte!"

        menu:
            "Zugriffserlaubnis personenbezogener Daten"
            "Erlauben":
                $ blockAccessToPersonalData = False
                $renpy.notify("Zugriff auf personenbezogene Daten erteilt")
                $ LooseEnergy(5)
                $ LooseData(5)
                commander "Urgh, so schnell kann man zu einem gläsernen Bürger werden."
            "Verbieten":
                $ blockAccessToPersonalData = True
                $renpy.notify("Zugriff auf personenbezogene Daten verweigert")
                commander "Richtig und wichtig! Unsere Daten gehören nur uns!"

        menu:
            "Erlaubnis zur Profilbildung"
            "Erlauben":
                $ blockProfiling = False
                $renpy.notify("Erlaubnis zur Profilbildung erteilt")
                $ LooseEnergy(5)
                $ LooseData(5)
                commander "Oha nicht gut! Ich möchte nicht in eine Schublade gesteckt werden."
            "Verbieten":
                $ blockProfiling = True
                $renpy.notify("Erlaubnis zur Profilbildung verweigert")
                "Gute Wahl! Dadurch bleiben wir unabhängig und werden nicht irgendwelchen Kategorien zugeordnet."
        menu:
            "Browser beenden?"
            "Ja":
                $ CP2_browserConfig_state = True
                $ HinweisCheck_state = True
                $ current_label = ""
                $ current_hinweis = ""
                $ InventarCheck_state = True
                $ ImageButtonActivate_state = True
                window hide
                $ renpy.pause(hard=True)
            "Nein":
                $ CP2_browserConfig_state = True

    #alle 4 Fragen wurden noch nicht beendet
    if not (CP2_browserFrage1_state and CP2_browserFrage2_state and CP2_browserFrage3_state and CP2_browserFrage4_state):
        $ HinweisCheck_state = True
        $ current_label = "computerWandClicked_Browser"
        commander "Sehr gut, du hast alle Einstellungen getroffen. Nun müssen wir nach den Informationen suchen!"

        "Verwende nun einen Browser deiner Wahl (bevorzugt sind jene, welche in der Spieleanleitung stehen)."
        "Falls du die Zeit übrig haben solltest, so konfiguriere gleich deinen Browser richtig! Hilfestellungen dazu findeste du
        im Security-by-Design Kompass."

        commander "Soo und los gehts mit der Informationsbeschaffung!"

        $ schiffFrage1 = ''
        $ schiffFrage2 = ''
        $ schiffFrage3 = ''
        $ schiffFrage4 = ''

        if not CP2_browserFrage1_state:
            $ current_hinweis = "CP2_computerWandClicked_Browser1_Hinweis"
            while schiffFrage1.lower() != 'ncc-1701-d':
                $ schiffFrage1 = renpy.input("Wie lautet der Name des Schiffes ***-****-*?")
                if schiffFrage1.lower() != 'ncc-1701-d':
                    "Leider Falsch"
                elif schiffFrage1.lower() == 'ncc-1701-d':
                    "Korrekt!"
                    $ CP2_browserFrage1_state = True
                menu:
                    "Browser beenden?"
                    "Ja":
                        $ InventarCheck_state = True
                        $ current_label = ""
                        $ current_hinweis = ""
                        $ ImageButtonActivate_state = True
                        window hide
                        $ renpy.pause(hard=True)
                    "Nein":
                        pass

        if not CP2_browserFrage2_state:
            $ current_hinweis = "CP2_computerWandClicked_Browser2_Hinweis"
            while schiffFrage2 != '42':
                $ schiffFrage2 = renpy.input("Wie viele Decks hat das Schiff?")
                if schiffFrage2 != '42':
                    "Leider Falsch"
                elif schiffFrage2 == '42':
                    "Korrekt!"
                    $ CP2_browserFrage2_state = True
                menu:
                    "Browser beenden?"
                    "Ja":
                        $ InventarCheck_state = True
                        $ current_label = ""
                        $ current_hinweis = ""
                        $ ImageButtonActivate_state = True
                        window hide
                        $ renpy.pause(hard=True)
                    "Nein":
                        pass

        if not CP2_browserFrage3_state:
            $ current_hinweis = "CP2_computerWandClicked_Browser3_Hinweis"
            while (schiffFrage3.lower() != 'antimaterie' and schiffFrage3.lower() != 'materie'):
                $ schiffFrage3 = renpy.input("Welche Art von Reaktor wird benutzt: ***********-Reaktor oder *******-Reaktor")
                if (schiffFrage3.lower() != 'antimaterie' and schiffFrage3.lower() != 'materie'):
                    "Leider Falsch"
                elif (schiffFrage3.lower() == 'antimaterie' or schiffFrage3.lower() == 'materie'):
                    "Korrekt!"
                    $ CP2_browserFrage3_state = True
                menu:
                    "Browser beenden?"
                    "Ja":
                        $ InventarCheck_state = True
                        $ current_label = ""
                        $ current_hinweis = ""
                        $ ImageButtonActivate_state = True
                        window hide
                        $ renpy.pause(hard=True)
                    "Nein":
                        pass

        if not CP2_browserFrage4_state:
            $ current_hinweis = "CP2_computerWandClicked_Browser4_Hinweis"
            while schiffFrage4 != '2371':
                $ schiffFrage4 = renpy.input("Wann wurde das Schiff durch einen Warpkernbruch zerstört? (Jahreszahl)")
                if schiffFrage4 != '2371':
                    "Leider Falsch"
                    menu:
                        "Browser beenden?"
                        "Ja":
                            $ InventarCheck_state = True
                            $ current_label = ""
                            $ current_hinweis = ""
                            $ ImageButtonActivate_state = True
                            window hide
                            $ renpy.pause(hard=True)
                        "Nein":
                            pass
            $ CP2_browserFrage4_state = True
            "Korrekt!"

        $ finishWebBrowser = True
        $ HinweisCheck_state = True
        $ InventarCheck_state = True
        $ current_label = ""
        $ current_hinweis = ""
        $ ImageButtonActivate_state = True
        commander "Sehr gut, wir haben einen Bauplan erhalten! Leider ist dieser noch verschlüsselt."
        $ CP6_UnlockDoor_state += 1

        #Überprüfung, ob alle Aufgaben beendet worden
        if CP6_UnlockDoor_state >= 4:
            jump lastScene

        #Bauplan-Dokument einfügen!!!

        window hide
        $ renpy.pause(hard=True)
