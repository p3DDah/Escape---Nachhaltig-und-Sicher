label chapter4_Abwurfeinstellung:
    $ InventarCheck_state = False
    $ HinweisCheck_state = False
    label InitChapter5Vars:
        $mic = False
        $cam = False
        $wlan = False
        $gps = False
        $abwurfPW = ""
        $SatPoss = False
        return

    label OpenAbwurfSettings:
        $ InventarCheck_state = False
        $ HinweisCheck_state = False
        #Einstellungen der Abwurfapp noch nicht eingestellt
        if not CP4_AbwurfPartI_state:
            $ ShowScreen("App_Abwurf_Settings_Title")
            $ HideScreen("App_Settings")
            $ HideScreen("App_Firefox")
            $ HideScreen("App_Edge")
            $ HideScreen("App_Chrome")
            $ HideScreen("App_Abwurf")
            $ HideScreen("App_Funk")
            $ HideScreen("keyboardNormal")
            $ ShowScreen("keyboardDummy")
            $ HideScreen("BackButton")
            $ ShowScreen("BackButtonDummy")
            call InitChapter5Vars from _call_InitChapter5Vars
            commander "Es wird Zeit den automatischen Abwurf der Raumsonden einzustellen! Nur so können wir sicher landen!"
            commander "Die App zum Bestimmen der Abwurfszeit muss sich mit dem Stromausfall zurückgesetzt haben."
            commander "Konfiguriere sie bitte wieder richtig. Beachte dabei, ob du über einen Satelliten oder lokal auf dem Rechner den Abwurf berechnen möchtest!"
            $ ShowScreen("choose_mic")
            menu:
                "Aktivieren":
                    #Mikrofon wurde ausgewählt
                    $ mic = True
                    $renpy.notify("Mikrofon aktiv")
                    $LooseEnergy(10)
                    commander "Warum muss das Mikrofon für eine Einstellung der Abwurfszeit aktiviert sein?
                    Nun gut du wirst dir schon etwas dabei gedacht haben."
                "Deaktivieren":
                    $ mic = False
                    $renpy.notify("Mikrofon inaktiv")
                    commander "Korrekt, das benötigen wir zur Berechnung nicht!"
            $ HideScreen("choose_mic")
            $ ShowScreen("choose_cam")
            menu:
                "Aktivieren":
                    #Kamera wurde ausgewählt
                    $ cam = True
                    $renpy.notify("Kamera aktiv")
                    $LooseEnergy(10)
                    commander "Du hat die kamera aktiviert? Möchtest du etwa mit den Aliens kommunizieren?
                    Ich denke für die Berechnung hätten wir diese nicht benötigt."
                "Deaktivieren":
                    $ cam = False
                    $renpy.notify("Kamera inaktiv")
                    commander "Supi, ein unnötiger Stromverbraucher weniger!"
            $ HideScreen("choose_cam")
            $ ShowScreen("choose_wlan")
            menu:
                "Aktivieren":
                    #Wlan wurde ausgewählt
                    $ wlan = True
                    $renpy.notify("WLAN aktiv")
                    $LooseData(10)
                    $SatPoss = True
                    commander "Sehr gut, kostet zwar etwas Strom, dafür können wir über den Satelliten
                    die Berechnungen ausführen und so wiederum Strom sparen."
                    commander "Denk aber daran, dass aufgrund der Berechnung über den Satelliten auch das Datenvolumen und
                    die benötigte Zeit steigt!"
                "Deaktivieren":
                    $ wlan = False
                    $renpy.notify("WLAN inaktiv")
                    commander "Hmm die Möglichkeit zur Berechnungen über den Satelliten, um so Strom zu sparen,
                    ist nun leider entfallen. Hoffen wir, dass der Strom für die Berechnung noch ausreicht!"
            $ HideScreen("choose_wlan")
            $ ShowScreen("choose_gps")
            menu:
                "Aktivieren":
                    #GPS wurde ausgewählt
                    $ gps = True
                    $renpy.notify("GPS aktiv")
                    $LooseData(10)
                    commander "Gute Wahl, nur so können wir unseren Standort bestimmen!"
                "Deaktivieren":
                    $ gps = True
                    $renpy.notify("GPS inaktiv")
                    commander "Urgh, ich muss da mal eingreifen.
                    Ohne GPS-Modul könne wir doch gar nciht unseren Standort lokalisieren."
                    commander "Ich habe es wieder aktiviert! Danke mir später hihi."
                    $renpy.notify("GPS aktiv")
                    $LooseData(10)
            $ HideScreen("choose_gps")
            #Anzeige, welche Teile ausgewählt wurden
            "Mikrofon: [mic] \n Kamera: [cam] \n WLAN: [wlan] \n GPS: [gps]"
            $LooseEnergy(10)
            $LooseData(10)
            $ ShowScreen("choose_zeitpunkt")
            menu:
                "Wie soll der Abwurfszeitpunkt berechnet werden?"
                "Über lokalen Boardcomputer":
                    $ mussWarten = True
                    $ LooseEnergy(30)
                    $ LooseData(10)
                    # überprüft ob das Earth Image angezeigt werden soll im 20 Sekunden Countdown
                    $ CP4_EarthImage20_state = True
                    commander "Ich hoffe das war die richtige Entscheidung!"
                    commander "Zwar sparen wir dadurch Daten (Übertragung zum Satellit entfällt) und Zeit (schnellere Berechnung),
                    jedoch verbrauchen wir eine Menge an Strom."
                    $ set_time = 20
                    $ countdown_title ="Berechnung läuft..."
                    $ timer_jump = "ZeitpunktBerechnet"

                "Über Satellit, welcher durch eine kabellose Netzwerkverbindung mit dem Raumschiff gekoppelt ist" if SatPoss == True:
                    $ mussWarten = True
                    $ LooseEnergy(10)
                    $ LooseData(30)
                    $ CP4_EarthImage60_state = True
                    commander "Ich hoffe das war die richtige Entscheidung!"
                    commander "Zwar sparen wir dadurch Strom (lokale Berechnung und somit erhöhte Rechenpower entfällt) ,
                    jedoch verbrauchen wir eine Menge an Daten."
                    $ set_time = 60
                    $ countdown_title ="Berechnung läuft..."
                    $ timer_jump = "ZeitpunktBerechnet"
            show screen countdown
            label Wartemenue:
                $ InventarCheck_state = False
                $ HinweisCheck_state = False
                if mussWarten:
                    $ renpy.notify("Bitte warten")
                else:
                    $ CP4_AbwurfPartI_state = True
                    # überprüft ob das Earth Image angezeigt werden soll im 60 Sekunden Countdown
                    $ CP4_EarthImage60_state = False
                    $ tmp = 1
                    menu:
                        "Abwurfapp verlassen?"
                        "Ja":
                            #blende die einzelnen Earth Images aus
                            while tmp != 21:
                                $ HideScreen("Earth"+str(tmp))
                                $ tmp += 1
                            jump ComputerSzene
                            window hide
                            $ renpy.pause(hard=True)
                        "Nein":
                            while tmp != 21:
                                $ HideScreen("Earth"+str(tmp))
                                $ tmp += 1
                            jump OpenAbwurfApp
        else:
            jump OpenAbwurfApp
        $ renpy.pause(hard=True)

    label ZeitpunktBerechnet:
        $ HideScreen("choose_zeitpunkt")
        $ HideScreen("App_Abwurf_Settings_Title")
        $ renpy.notify("Abwurfzeitpunkt berechnet")
        $ mussWarten = False
        jump Wartemenue
        $ renpy.pause(hard=True)

    label OpenAbwurfApp:
        $ InventarCheck_state = False
        $ HinweisCheck_state = False
        #Aktivierung des Abwurfs noch nicht abgeschlossen
        if not CP4_AbwurfPartII_state:
            #analoges Spiegelrätsel noch nicht abgeschlossen
            if not CP4_Spiegel_state:
                $ HinweisCheck_state = True
                $ current_label = "OpenAbwurfApp"
                $ current_hinweis = "CP4_OpenAbwurfApp_Hinweis"
                $ HideScreen("App_Settings")
                $ HideScreen("App_Firefox")
                $ HideScreen("App_Edge")
                $ HideScreen("App_Chrome")
                $ HideScreen("App_Abwurf")
                $ HideScreen("App_Funk")
                $ HideScreen("keyboardNormal")
                $ ShowScreen("keyboardDummy")
                $ HideScreen("BackButton")
                $ ShowScreen("BackButtonDummy")
                $ ShowScreen("App_Abwurf_Title")
                $ abwurfPW = ""
                commander "Zum Aktivieren benötigen wir noch ein Passwort! Tja und das weiß nur unser Schrankverwalter Professor Eich, der natürlich nicht hier ist."
                commander "So ein Schlingel aber auch, er gibt NIE seine Passwörter preis!"
                commander "Aber hey, ich habe hier ein paar Unterlagen von ihm mit wirren Wörtern gefunden, vielleicht hilft uns das weiter."
                #festes Passwort "XCHAT" aus spiegelverkehrt (analog)
                while abwurfPW.lower() != "xchat":
                    $abwurfPW = renpy.input("Wie lautet das Passwort? (5-stellig)")
                    if abwurfPW.lower() != "xchat":
                        $renpy.notify("Falsches Passwort")
                        menu:
                            "Abwurfapp verlassen?"
                            "Ja":
                                $ HideScreen("App_Abwurf_Title")
                                jump ComputerSzene
                                window hide
                                $ renpy.pause(hard=True)
                            "Nein":
                                pass
                    else:
                        $ renpy.notify("Korrekt")
                        $ HideScreen("App_Abwurf_Title")
                        $ HinweisCheck_state = False
                        $ current_label = ""
                        $ current_hinweis = ""
                        menu:
                            "Abwurfapp verlassen?"
                            "Ja":
                                $ CP4_Spiegel_state = True
                                jump ComputerSzene
                                window hide
                                $ renpy.pause(hard=True)
                            "Nein":
                                pass
                $ HideScreen("App_Abwurf_Title")
                $ CP4_Spiegel_state = True
                commander "Du bist spitze! Und übrigens, XChat ist ein cooler Messenger für Windows und Linux. Probier ihn doch mal aus, wenn wir wieder auf der Erde sind."
            $ ShowScreen("os_title")
            $ HideScreen("App_Settings")
            $ HideScreen("App_Firefox")
            $ HideScreen("App_Edge")
            $ HideScreen("App_Chrome")
            $ HideScreen("App_Abwurf")
            $ HideScreen("App_Funk")
            $ HideScreen("keyboardNormal")
            $ ShowScreen("keyboardDummy")
            $ HideScreen("BackButton")
            $ ShowScreen("BackButtonDummy")
            $ ShowScreen("App_Abwurf_Title")
            commander "Nun müssen wir nur das eine Passwort an den Maschinenraum übermitteln. Nur wie? Entscheide weise!"
            $os_title = "Übertragungsart"
            menu:
                "per Textnachricht":
                    $ LooseEnergy(10)
                    $ LooseData(10)
                    commander "Eine Textnachricht sollte völlig ausreichend sein, um ein einzelnes Passwort zu senden!"
                "per Sprachnachricht":
                    $ LooseEnergy(20)
                    $ LooseData(20)
                    commander "Hmm so viel Daten und Strom für ein einzelnes Passwort? Nun gut, deine Entscheidung."
                "per Bildnachricht":
                    $ LooseEnergy(30)
                    $ LooseData(30)
                    commander "Hmm so viel Daten und Strom für ein einzelnes Passwort? Nun gut, deine Entscheidung."
            $ password = 2134*year*month*day/10
            $os_title = "[password]" #Passwort zum Übermitteln
            call chapter_5_pw_uebermitteln from _call_chapter_5_pw_uebermitteln
            $ HideScreen("os_title")
            $ CP4_AbwurfPartII_state = True
            $ HideScreen("App_Abwurf_Title")
            jump ComputerSzene
        else:
            $ renpy.notify("Abwurfsapp nicht verfügbar")
            pause 2.0
            jump ComputerSzene
        $ renpy.pause(hard=True)

    label chapter_5_pw_uebermitteln:
        "Übermittle das Passwort für den Fragebogen an den Maschinenraum."
        menu:
            "Hast du das Passwort übermittelt/notiert?"
            "Ja":
                $ HideScreen("os_title")
            "Nein":
                call chapter_5_pw_uebermitteln from _call_chapter_5_pw_uebermitteln_1
        return
