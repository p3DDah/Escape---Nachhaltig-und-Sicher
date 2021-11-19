label chapter5_FunkReparatur:
    $ InventarCheck_state = False
    $ HinweisCheck_state = False
    label FunkApp:
        $ InventarCheck_state = False
        $ HinweisCheck_state = False
        #Test des Funkgerätes noch nicht abgeschlossen
        if not CP5_FunkAppNo_state:
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
            $ ShowScreen("App_Funk_Title")
            $ renpy.notify("Kommunikationsapp")
            commander "Diese App ist hervorragend, um nach unserer Ankunft auf der Erde mit der Mission Control Kontakt aufzunehmen."
            commander "Lass uns mit einen kurzen Test des Funkgerätes starten!"
            menu:
                "Möchtest du mit dem Test starten?"
                "Ja":
                    $ mussWarten = True
                    #zufällige Zeit zwischen 16 und 50s
                    $ set_time = renpy.random.randint(16, 50)
                    $ countdown_title ="Empfang wird getestet ..."
                    $ timer_jump = "FunkTest"
                "Nein":
                    $ HideScreen("App_Funk_Title")
                    jump ComputerSzene
                    window hide
                    $ renpy.pause(hard=True)
            show screen countdown

            #Testdurchlauf mit funktionierendem Funkgerät
            label TestDurchlauf:
                $ InventarCheck_state = False
                $ HinweisCheck_state = False
                #einfache Warteanimation
                if mussWarten:
                    $ renpy.notify("Bitte warten")
                    $ ShowScreen("os_title")
                    $ tmp = 0
                    $ os_title = "\n \n \n \n"
                    while mussWarten:
                        pause 0.99
                        #wenn tmp == 3 , dann setze os_title zurück
                        if tmp == 3:
                            $ os_title = "\n \n \n \n"
                            $ tmp = 0
                        else:
                            $ os_title += ". "
                            $ tmp += 1
                else:
                    $ os_title = "\n \n \n \n Das Kommunikationsgerät weißt keine Fehler auf."
                    commander "Sehr schön, das Funkgerät funktioniert noch!"
                    $ HideScreen("App_Funk_Title")
                    play sound "alarm.mp3"
                    #Variable dient zum Springen zum Turbulenzen Label
                    $ CP5_continue_state = True
                    $ CP5_FunkAppNo_state = True
                    #Verstecke alle Objekte die zum PC gehören
                    call HideObjectsPC from _call_HideObjectsPC
        else:
            #Funkgerät wurde repariert
            if CP5_FunkAppYes_state:
                $ renpy.notify("Kommunikations- und Standortaufbau erfolgreich")
                pause 2.0
                jump ComputerSzene
            else:
                #mindestens ein Reparaturteil wurde ausgewählt
                if CP5_VarSelect_state:
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
                    $ ShowScreen("App_Funk_Title")
                    $ renpy.notify("Kommunikationsapp")
                    label TeileAuswahl:
                        $ InventarCheck_state = False
                        $ HinweisCheck_state = False
                        #Kommunikationstest und Standorttest noch nicht erfolgreich
                        if not (CP5_KommTest_state and CP5_StandortTest_state):
                            if mussWarten:
                                $ renpy.notify("Bitte warten")
                                $ ShowScreen("os_title")
                                $ tmp = 0
                                $ os_title = "\n \n \n \n"
                                while mussWarten:
                                    pause 0.99
                                    if tmp == 3:
                                        $ os_title = "\n \n \n \n"
                                        $ tmp = 0
                                    else:
                                        $ os_title += ". "
                                        $ tmp += 1
                            else:
                                menu:
                                    "Wähle die Teile für die Reparatur aus."
                                    #Mikrofon wurde im Inventar ausgewählt
                                    "Mikrofon" if usedMic:
                                        $ usedMic = False
                                        #Mikrofon wurde ausgewählt
                                        $ CP5_UsedMic = True
                                        jump TeileAuswahl
                                    "Kamera" if usedCam:
                                        $ usedCam = False
                                        $ CP5_UsedCam = True
                                        jump TeileAuswahl
                                    "GPS" if usedGPS:
                                        $ usedGPS = False
                                        $ CP5_UsedGPS = True
                                        jump TeileAuswahl
                                    "Lautsprecher" if usedSpeaker:
                                        $ usedSpeaker = False
                                        $ CP5_UsedSpeaker = True
                                        jump TeileAuswahl
                                    "WLAN-Modul" if usedWLAN:
                                        $ usedWLAN = False
                                        $ CP5_UsedWLAN = True
                                        jump TeileAuswahl
                                    "{u}{b}Auswahl bestätigen{/b}{/u}":
                                        pass
                                    "{u}{b}Auswahl zurücksetzen{/b}{/u}":
                                        if CP5_UsedWLAN:
                                            $ usedWLAN = True
                                        $ CP5_UsedWLAN = False
                                        if CP5_UsedSpeaker:
                                            $ usedSpeaker = True
                                        $ CP5_UsedSpeaker = False
                                        if CP5_UsedGPS:
                                            $ usedGPS = True
                                        $ CP5_UsedGPS = False
                                        if CP5_UsedCam:
                                            $ usedCam = True
                                        $ CP5_UsedCam = False
                                        if CP5_UsedMic:
                                            $ usedMic = True
                                        $ CP5_UsedMic = False
                                        $ CP5_KommTest_state = False
                                        jump TeileAuswahl
                                    "{u}{b}Zurück{/b}{/u}":
                                        $ HideScreen("App_Funk_Title")
                                        jump ComputerSzene
                                menu:
                                    "Möchtest du folgende Teile verwenden?\n
                                    Mikrofon: {b}[CP5_UsedMic]{/b}
                                    Kamera: {b}[CP5_UsedCam]{/b}\n
                                    GPS: {b}[CP5_UsedGPS]{/b}\n
                                    Lautsprecher: {b}[CP5_UsedSpeaker]{/b}\n
                                    WLAN-Modul: {b}[CP5_UsedWLAN]{/b}"
                                    "Ja":
                                        pass
                                    "Nein":
                                        jump TeileAuswahl
                            commander "Nun, das Funkgerät sollte jetzt wieder funktionieren. \nLass uns aber sicherheitshalber nochmal einen Check durchführen."
                            commander "Der Test wird die Kommunikationfähigkeit und die Standortermittlung prüfen."
                    #teste, ob die benötigten Teile für die Kommunikation angebracht worden sind
                    label ZweiterTestdurchlaufPartI:
                        $ InventarCheck_state = False
                        $ HinweisCheck_state = False
                        #Kommunikationstest noch nicht abgeschlossen
                        if not CP5_KommTest_state:
                            menu:
                                "Möchtest du mit dem Kommunikationstest starten?"
                                "Ja":
                                    $ mussWarten = True
                                    $ set_time = renpy.random.randint(16, 30)
                                    $ countdown_title ="Kommunikationsfähigkeit wird getestet ..."
                                    $ timer_jump = "KommTest"
                                "Nein":
                                    $ HideScreen("App_Funk_Title")
                                    jump ComputerSzene
                                    window hide
                                    $ renpy.pause(hard=True)
                            show screen countdown

                    #teste, ob die benötigten Teile für die Standortermittlung angebracht worden sind
                    label ZweiterTestdurchlaufPartII:
                        $ InventarCheck_state = False
                        $ HinweisCheck_state = False
                        # Standorttest noch nicht erfolgreich
                        if not CP5_StandortTest_state:
                            if mussWarten:
                                $ renpy.notify("Bitte warten")
                                $ ShowScreen("os_title")
                                $ tmp = 0
                                $ os_title = "\n \n \n \n"
                                while mussWarten:
                                    pause 0.99
                                    if tmp == 3:
                                        $ os_title = "\n \n \n \n"
                                        $ tmp = 0
                                    else:
                                        $ os_title += ". "
                                        $ tmp += 1
                            else:
                                menu:
                                    "Möchtest du mit dem Standortermittlungstest starten?"
                                    "Ja":
                                        $ mussWarten = True
                                        $ set_time = renpy.random.randint(16, 30)
                                        $ countdown_title ="Standortermittlung wird getestet ..."
                                        $ timer_jump = "StandortTest"
                                    "Nein":
                                        $ HideScreen("App_Funk_Title")
                                        jump ComputerSzene
                                        window hide
                                        $ renpy.pause(hard=True)
                                show screen countdown

                    #Verschlüsselung der Funkverbindung
                    label EnterEncryptionKey:
                        $ InventarCheck_state = False
                        $ HinweisCheck_state = False
                        if mussWarten:
                            $ renpy.notify("Bitte warten")
                            $ ShowScreen("os_title")
                            $ tmp = 0
                            $ os_title = "\n \n \n \n"
                            while mussWarten:
                                pause 0.99
                                if tmp == 3:
                                    $ os_title = "\n \n \n \n"
                                    $ tmp = 0
                                else:
                                    $ os_title += ". "
                                    $ tmp += 1
                        else:
                            menu:
                                "Kommunikationsapp beenden?"
                                "Ja":
                                    $ HideScreen("App_Funk_Title")
                                    $ HideScreen("Check_Encryption_Title")
                                    jump ComputerSzene
                                    window hide
                                    $ renpy.pause(hard=True)
                                "Nein":
                                    pass

                            $ HideScreen("App_Funk_Title")
                            $ ShowScreen("Check_Encryption_Title")
                            commander "Wir müssen unbedingt unsere Funkverbindung verschlüsseln!"
                            commander "Ohne Verschlüsselung sind wir leichtes Opfer für feindliche Länder,
                            mit falschem Chiffrierschlüssel können unsere Kollegen unsere Nachricht nicht entschlüsseln!"
                            commander "Finde den korrekten Schlüssel!"
                            $encryptionKey = renpy.input("Schlüssel eingeben (8-stellig)")
                            if encryptionKey == "2T,eW.Ü!":
                                $renpy.notify("Verschlüsselung aktiviert")
                                commander "Sehr schön! Bald sind wir mit den Vorbereitungen fertig."
                                $ CP5_FunkAppYes_state = True
                                $ HideScreen("Check_Encryption_Title")
                                jump ComputerSzene
                            else:
                                jump ErrorCountdown
                        $ renpy.pause(hard=True)
                else:
                    $ HideScreen("BackButton")
                    $ ShowScreen("BackButtonDummy")
                    $ HideScreen("keyboardNormal")
                    $ ShowScreen("keyboardDummy")
                    "Wähle im Inventar aus, welche Gegenstände du zur Reparatur des Fungerätes verwenden möchtest."
                    $ renpy.notify("keine Kommunikation möglich")
                    pause 2.0
                    jump ComputerSzene

    $ renpy.pause(hard=True)


    label FunkTest:
        $ renpy.notify("Test erfolgreich")
        $ mussWarten = False
        jump TestDurchlauf
        $ renpy.pause(hard=True)

    label KommTest:
        $ InventarCheck_state = False
        $ HinweisCheck_state = False
        #nur erfolgreich, wenn Mikrofon und Lautsprecher verwendet wurden
        if CP5_UsedMic and CP5_UsedSpeaker:
            $ renpy.notify("Kommunikationstest erfolgreich")
            $ os_title = "Test bestanden"
            $ CP5_KommTest_state = True
            pause 2.0
            $ os_title = ""
            $ mussWarten = False
            jump ZweiterTestdurchlaufPartII
        else:
            $ renpy.notify("Kommunikationstest fehlgeschlagen")
            $ os_title = "Test fehlgeschlagen"
            pause 2.0
            $ os_title = ""
            commander "Hm komisch, irgendwas scheint nicht zu funktionieren. Vielleicht fehlt ein Teil."
            $ mussWarten = False
            jump TeileAuswahl
        $ renpy.pause(hard=True)

    label StandortTest:
        $ InventarCheck_state = False
        $ HinweisCheck_state = False
        #nur erfolgreich, wenn GPS verwendet wurde
        if CP5_UsedGPS:
            $ renpy.notify("Standortermittlung erfolgreich")
            $ os_title = "Test bestanden"
            $ CP5_StandortTest_state = True
            pause 2.0
            $ os_title = ""
            $ mussWarten = False
            jump EnterEncryptionKey
        else:
            $ renpy.notify("Standortermittlung fehlgeschlagen")
            $ os_title = "Test fehlgeschlagen"
            pause 2.0
            $ os_title = ""
            commander "Hm komisch, irgendwas scheint nicht zu funktionieren. Vielleicht fehlt ein Teil."
            $ mussWarten = False
            jump TeileAuswahl
        $ renpy.pause(hard=True)

    #zeige Teile nacheinander an
    label ShowChapter6Objects:
        pause 0.5
        $ ShowScreen("Mikrofon")
        pause 0.1
        $ ShowScreen("GPS")
        pause 0.2
        $ ShowScreen("Speaker")
        pause 0.1
        $ ShowScreen("Kamera")
        pause 0.1
        $ ShowScreen("WLAN")
        return

    label InitChapter6Vars:
        $usedMic = False
        $usedCam = False
        $usedGPS = False
        $usedSpeaker = False
        $usedWLAN = False
        $encryptionKey = ""

        $micro_state = True
        $gps_state = True
        $speaker_state = True
        $camera_state = True
        $wifi_state = True
        return

    #dient zur Anzeige der benötigten Teile
    label Turbulenzen:
        $ InventarCheck_state = False
        $ HinweisCheck_state = False
        commander "Was ist das?"
        commander "Mist mist mist, ein erneuter Asteroidensturm!"
        commander "Gut festhalten, gleich prallen sie auf!!!!!"
        $ CP5_continue_state = False
        call ShowChapter6Objects from _call_ShowChapter6Objects
        call InitChapter6Vars from _call_InitChapter6Vars
        commander "Urrgh das waren starke Turbulenzen. Unser Funkgerät wurde dabei zerstört!"
        commander "Könntest du es bitte wieder zusammenbauen? Lass die Teile, die evtl. nicht benötigt werden einfach weg."
        commander "Denke daran, wir möchten mit dem Gerät Kontakt aufnehmen und unseren Standort senden können!"
        $ renpy.pause(hard=True)

    label UseMic:
        #temporärer Sound
        play sound "audio/code_accept.mp3"
        $usedMic = True
        call CheckFunk from _call_CheckFunk
        $ LooseEnergy(10)
        $ renpy.pause(hard=True)

    label UseCam:
        #temporärer Sound
        play sound "audio/code_accept.mp3"
        $usedCam = True
        call CheckFunk from _call_CheckFunk_1
        $ LooseEnergy(20)
        $ renpy.pause(hard=True)

    label UseGPS:
        #temporärer Sound
        play sound "audio/code_accept.mp3"
        $usedGPS = True
        call CheckFunk from _call_CheckFunk_2
        $ LooseEnergy(10)
        $ renpy.pause(hard=True)

    label UseSpeaker:
        #temporärer Sound
        play sound "audio/code_accept.mp3"
        $usedSpeaker = True
        call CheckFunk from _call_CheckFunk_3
        $ LooseEnergy(10)
        $ renpy.pause(hard=True)

    label UseWLAN:
        #temporärer Sound
        play sound "audio/code_accept.mp3"
        $usedWLAN = True
        call CheckFunk from _call_CheckFunk_4
        $ LooseEnergy(10)
        $ LooseData(10)
        $ renpy.pause(hard=True)

    #Überprüfung, ob ein Gegenstand ausgewählt wurde, sodass die Kommunikationsapp wieder funktioniert
    label CheckFunk:
        if usedMic or usedGPS or usedSpeaker or usedWLAN or usedCam:
            $ CP5_VarSelect_state = True
            $ renpy.notify("Reparatur möglich!")
        return

    label OpenFunk:
        $ HideScreen("monitorFunk")
        $ HideScreen("MikrofonPlaced")
        $ HideScreen("KameraPlaced")
        $ HideScreen("WLANPlaced")
        $ HideScreen("GPSPlaced")
        $ HideScreen("SpeakerPlaced")
        $ HideScreen("Mikrofon")
        $ HideScreen("GPS")
        $ HideScreen("Speaker")
        $ HideScreen("Kamera")
        $ HideScreen("WLAN")
        $ ShowScreen("keyboardFunk")
        $ renpy.pause(hard=True)

    label ErrorCountdown:
        $renpy.notify("Falscher Schlüssel")
        $ HideScreen("Check_Encryption_Title")
        $ set_time = 10
        $ countdown_title ="Bitte warten..."
        $ timer_jump = "EnterEncryptionKey"
        show screen countdown
        $ renpy.pause(hard=True)
