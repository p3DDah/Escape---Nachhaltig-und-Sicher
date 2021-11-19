label chapter3_Kursberechnung:
    $ InventarCheck_state = False
    $ HinweisCheck_state = False
    #noch keinen Browser ausgewählt
    if not CP3_BrowserWahl_state:
        label InitChapter4Vars:
            $browserPW = ""
            $cipher = ""
            return

        #Firefox als Browser auswählen
        label OpenFirefox: #wenn Button berührt
            $ InventarCheck_state = False
            $ HinweisCheck_state = False
            #Abfrage, ob Aufgabe schon beendet
            if CP3_Kursberechnung24_state:
                jump OpenBrowser
            else:
                #gibt an, welcher Browser ausgewählt wurde
                if CP3_Browser == "":
                    pass
                elif CP3_Browser == "Firefox":
                    jump OpenBrowser
                else:
                    "Bitte wähle [CP3_Browser] aus."
                    jump ComputerSzene
            $ HideScreen("BackButton")
            $ ShowScreen("BackButtonDummy")
            $ HideScreen("keyboardNormal")
            $ ShowScreen("keyboardDummy")
            menu:
                "Möchtest du diesen Browser verwenden?"
                "Ja":
                    $ CP3_Browser = "Firefox"
                "Nein":
                    jump ComputerSzene
                    window hide
                    $ renpy.pause(hard=True)
            $LooseEnergy(10)
            $LooseData(10)
            commander "Gute Wahl, Firefox ist ein datensparsamer, moderner und sicherer OpenSource Browser!"
            $ CP3_BrowserWahl_state = True
            menu:
                "Browser beenden?"
                "Ja":
                    jump ComputerSzene
                    window hide
                    $ renpy.pause(hard=True)
                "Nein":
                    pass
            jump OpenBrowser
            $ renpy.pause(hard=True)

        #Edge als Browser auswählen
        label OpenEdge: #wenn Button berührt
            $ InventarCheck_state = False
            $ HinweisCheck_state = False
            if CP3_Kursberechnung24_state:
                jump OpenBrowser
            else:
                if CP3_Browser == "":
                    pass
                elif CP3_Browser == "Edge":
                    jump OpenBrowser
                else:
                    "Bitte wähle [CP3_Browser] aus."
                    jump ComputerSzene
            $ HideScreen("BackButton")
            $ ShowScreen("BackButtonDummy")
            $ HideScreen("keyboardNormal")
            $ ShowScreen("keyboardDummy")
            menu:
                "Möchtest du diesen Browser verwenden?"
                "Ja":
                    $ CP3_Browser = "Edge"
                "Nein":
                    jump ComputerSzene
                    window hide
                    $ renpy.pause(hard=True)
            $LooseEnergy(30)
            $LooseData(40)
            commander "Schlechte Wahl, da Edge viel Datenvolumen benötigt! Microsoft ist dafür bekannt, Nutzerdaten zu sammeln. "
            $ CP3_BrowserWahl_state = True
            menu:
                "Browser beenden?"
                "Ja":
                    jump ComputerSzene
                    window hide
                    $ renpy.pause(hard=True)
                "Nein":
                    pass
            jump OpenBrowser
            $ renpy.pause(hard=True)

        #Chrome als Browser auswählen
        label OpenChrome: #wenn Button berührt
            $ InventarCheck_state = False
            $ HinweisCheck_state = False
            if CP3_Kursberechnung24_state:
                jump OpenBrowser
            else:
                if CP3_Browser == "":
                    pass
                elif CP3_Browser == "Chrome":
                    jump OpenBrowser
                else:
                    "Bitte wähle [CP3_Browser] aus."
                    jump ComputerSzene
            $ HideScreen("BackButton")
            $ ShowScreen("BackButtonDummy")
            $ HideScreen("keyboardNormal")
            $ ShowScreen("keyboardDummy")
            menu:
                "Möchtest du diesen Browser verwenden?"
                "Ja":
                    $ CP3_Browser = "Chrome"
                "Nein":
                    jump ComputerSzene
                    window hide
                    $ renpy.pause(hard=True)
            $LooseEnergy(30)
            $LooseData(40)
            commander "Schlechte Wahl, da Chrome sehr viel Datenvolumen benötigt! Google ist für seine umfangreiche Datensamlung bekannt."
            $ CP3_BrowserWahl_state = True
            menu:
                "Browser beenden?"
                "Ja":
                    jump ComputerSzene
                    window hide
                    $ renpy.pause(hard=True)
                "Nein":
                    pass
            jump OpenBrowser
            $ renpy.pause(hard=True)
        #springe zu OpenBrowser, egal welcher Browser

    #Kursberechnung mit dem jeweiligen Browsers
    label OpenBrowser:
        $ InventarCheck_state = False
        $ HinweisCheck_state = False
        #Kursberechnung noch nicht abgeschlossen
        if not CP3_Kursberechnung24_state:
            #wechsel Szene
            scene browser_open
            $ HideScreen("App_Settings")
            $ HideScreen("App_Firefox")
            $ HideScreen("App_Edge")
            $ HideScreen("App_Chrome")
            $ HideScreen("App_Abwurf")
            $ HideScreen("App_Funk")
            $ HideScreen("BackButton")
            $ ShowScreen("BackButtonDummy")
            $ HideScreen("keyboardNormal")
            $ ShowScreen("keyboardDummy")
            "Herzlich Willkommen bei Kursberechnung24.de"
            #Kreuzworträtsel noch nicht abgeschlossen
            if not CP3_Kreuz_state:
                $ HinweisCheck_state = True
                $ current_label = "OpenBrowser"
                $ current_hinweis = "CP3_OpenBrowserKreuz_Hinweis"
                #wechsel Szene
                scene browser_open_kreuzwort
                call InitChapter4Vars from _call_InitChapter4Vars
                #festes Passwort "eutdchfvuedi", ergibt sich aus dem Kreuzworträtsel
                while browserPW.lower() != "eutdchfvuedi":
                    $browserPW = renpy.input("Wie lautet das Lösungswort?")
                    if browserPW.lower() != "eutdchfvuedi":
                        $ renpy.notify("Falsches Lösungswort")
                        menu:
                            "Kursberechnung beenden?"
                            "Ja":
                                jump ComputerSzene
                                window hide
                                $ renpy.pause(hard=True)
                            "Nein":
                                pass
                    else:
                        $ renpy.notify("Korrekt")
                        $ CP3_Kreuz_state = True
                        $ HinweisCheck_state = False
                        $ current_label = ""
                        $ current_hinweis = ""
                        menu:
                            "Kursberechnung beenden?"
                            "Ja":
                                jump ComputerSzene
                                window hide
                                $ renpy.pause(hard=True)
                            "Nein":
                                pass

            #Cipher-Rätsel noch nicht beendet
            if not CP3_Cipher_state:
                $ HinweisCheck_state = True
                $ current_label = "OpenBrowser"
                $ current_hinweis = "CP3_OpenBrowserCipher_Hinweis"
                scene browser_open_coords
                "Löse das Cipher-Rästel"
                "Das Lösungswort aus dem Kreuzworträtsel hilft."
                #festes Passwort "325365", ergibt sich aus Cipher Rätsel
                while cipher != "325365":
                    $cipher = renpy.input("Wie lauten die Koordinaten (6-stellige Zahl)?")
                    if cipher != "325365":
                        $renpy.notify("Leider Falsch")
                        menu:
                            "Kursberechnung beenden?"
                            "Ja":
                                jump ComputerSzene
                                window hide
                                $ renpy.pause(hard=True)
                            "Nein":
                                pass
                    else:
                        $renpy.notify("Korrekt")
                        $ HinweisCheck_state = False
                        $ current_label = ""
                        $ current_hinweis = ""
                        $ CP3_Cipher_state = True
                        menu:
                            "Kursberechnung beenden?"
                            "Ja":
                                jump ComputerSzene
                                window hide
                                $ renpy.pause(hard=True)
                            "Nein":
                                pass
            #wechsel Szene
            scene browser_open
            commander "Super, wir haben nun die Koordinaten für den neuen Kurs. Sehr gut gemacht!"
            commander "Nun müssen wir diese nur noch an den Maschinenraum übermitteln, sodass unsere Kollegen die Kurskorrektur durchführen können."
            commander "Hmm ich sehe gerade, es muss einiges übermittelt werden."
            commander "Per Text wäre es ressourcensparender, dafür aber auch informationsärmer. Per Bild gegenteilig und per Sprache wäre sowohl als auch."
            commander "Hmm schwierige Entscheidung... Wähle lieber du hihi."
            menu:
                "Wie möchtest du die Daten an den Maschinenraum übergeben?"
                "per Text":
                    $LooseEnergy(10)
                    $LooseData(10)
                    commander "Hmm wenn ich so darüber nachdenke, dann war das vielleicht nicht die beste Wahl."
                    commander "Wir haben zwar somit Daten und Strom gespart, jedoch werden wir es dem Maschinenraum
                    durch die wenig gesendeten Daten schwierig machen diese auszuwerten."
                    $ password = 3412 * year * month * day /10
                    #spezifisches, dynamisches Passwort für Text, verursacht im Maschienraum bestimmte Auswirkung
                    $os_title = "[password]"
                "per Sprache":
                    $LooseEnergy(20)
                    $LooseData(20)
                    commander "Hmm eine recht gute Wahl, wir konnten dem Maschienraum ausreichend Daten senden
                    und haben nicht zu viele Ressourcen verbraucht. Ich denke die beste Option wäre aber per Bild gewesen,
                    da der Maschineraum so einen großen Zeitvorteil gewonnen hätte."
                    $ password = 4123 * year * month * day /10
                    #spezifisches, dynamisches Passwort für Sprache
                    $os_title = "[password]"
                "per Bild":
                    $LooseEnergy(30)
                    $LooseData(30)
                    commander "Eine sehr gute Wahl, sie verbraucht zwar am meisten Ressourcen, jedoch verschaffen wir
                    dem Maschinenraum aufgrund der hohen Datenmenge einen entscheidenen Zeitvorteil!"
                    $ password = 1243 * year * month * day /10
                    #spezifisches, dynamisches Passwort für Sprache
                    $os_title = "[password]"
            $ ShowScreen("os_title_black")
            call chapter_4_pw_uebermitteln from _call_chapter_4_pw_uebermitteln
            $ HideScreen("os_title_black")
            $ CP3_Kursberechnung24_state = True
            jump ComputerSzene
            $ renpy.pause(hard=True)
        else:
            $ renpy.notify("Kursberechnung bereits abgeschlossen")
            pause 2.0
            jump ComputerSzene

    label chapter_4_pw_uebermitteln:
        "Übermittle das Passwort zur Koordinatenübertragung an den Maschinenraum."
        menu:
            "Hast du das Passwort übermittelt/notiert?"
            "Ja":
                pass
            "Nein":
                call chapter_4_pw_uebermitteln from _call_chapter_4_pw_uebermitteln_1
        return
