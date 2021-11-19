#wenn einer der Monitore (Farbe oder S/W) gedrückt wird, dann gehe ins Label team_1_chapter_3
label chapter2_Freigabe:
    #Hauptszene für den Computer
    #überprüft, was momentan angezeigt werden soll
    label ComputerSzene:
    #verwende ein neues Hintergrundbild
        $ InventarCheck_state = True #Variable, um Inventar zu sperren
        $ HinweisCheck_state = True
        $ current_label = ""
        $ current_hinweis = ""
        #wurden Aufgaben aus CP2 bis 5 gelöst, dann zeige CP6 an
        if not (CP2_EditedSettings_state and CP3_Kursberechnung24_state and CP4_AbwurfPartII_state and CP5_FunkAppYes_state):
            #überprüfe auf OS
            if CP2_Computer_state:
                scene computer_off
                $ renpy.notify("Computer aus")
            else:
                #wurde Linux ausgewählt
                if isLinux:
                    scene computer_linux_on
                    $ renpy.notify("Linux OS")
                #wurde Windows ausgewählt
                elif isWindows:
                    scene computer_windows_on
                    $ renpy.notify("Windows OS")
                else:
                    scene computer_off
                    $ renpy.notify("Computer aus")
                #Apps dürfen angezeigt werden
                if CP2_OsWahl_state:
                    $ ShowScreen("App_Settings")
                    $ ShowScreen("App_Firefox")
                    $ ShowScreen("App_Edge")
                    $ ShowScreen("App_Chrome")
                    $ ShowScreen("App_Abwurf")
                    $ ShowScreen("App_Funk")
            $ HideScreen("monitorSW")
            $ HideScreen("monitorColor")
            #Keyboard wurde repariert
            if Keyboard_state:
                $ HideScreen("keyboardDummy")
                $ ShowScreen("keyboardNormal")
            else:
                $ ShowScreen("keyboardBroken")
            #Anzeige des Zurückbuttons
            $ HideScreen("BackButtonDummy")
            $ ShowScreen("BackButton")
            call HideObejects from _call_HideObejects
            call InitChapter3Vars from _call_InitChapter3Vars
        else:
            $ HideScreen("App_Settings")
            $ HideScreen("App_Firefox")
            $ HideScreen("App_Edge")
            $ HideScreen("App_Chrome")
            $ HideScreen("App_Abwurf")
            $ HideScreen("App_Funk")
            $ HideScreen("BackButtonDummy")
            $ ShowScreen("BackButton")
            $ HideScreen("keyboardDummy")
            $ ShowScreen("keyboardNormal")
            if CP2_Computer_state:
                scene computer_off
                $ renpy.notify("Computer aus")
            else:
                if isLinux:
                    scene computer_linux_on
                    $ renpy.notify("Linux OS")
                    $ ShowScreen("App_Duesenstart")
                elif isWindows:
                    scene computer_windows_on
                    $ renpy.notify("Windows OS")
                    $ ShowScreen("App_Duesenstart")
                else:
                    scene computer_off
                    $ renpy.notify("Computer aus")
            $ HideScreen("monitorSW")
            $ HideScreen("monitorColor")
            call HideObejects from _call_HideObejects1

        $ renpy.pause(hard=True)

    label InitChapter3Vars:
        $ enteredMonitorPW = ""
        $ encryptionKorrekt = False
        $ firewall = False
        $ antivir = False
        $ dasi = False
        $ mussWarten = False
        $ CP4_EarthImage20_state = False
        $ CP4_EarthImage60_state = False
        return

    #zerstörte Tastatur
    label keyboardBrokenClicked:
        $ InventarCheck_state = False
        $ HinweisCheck_state = False
        #Keyboard noch kaputt
        if not CP2_KeyboardBroken_state:
            $ HinweisCheck_state = True
            $ current_label = "keyboardBrokenClicked"
            $ current_hinweis = "CP2_keyboardBrokenClicked_Hinweis"
            $ HideScreen("BackButton")
            $ ShowScreen("BackButtonDummy")
            if mussWarten:
                $ renpy.notify("Bitte warten")
            else:
                menu:
                    "Wähle die Buchstaben in der richtigen Reihenfolge aus"
                    #wurde Taste D aufgehoben und auch ausgewählt
                    "D" if key_D_state and CP2_tmpD_state:
                        $ CP2_tmpD_state = False
                        #Eingabetext
                        $ CP2_tmpText += "D"
                        jump keyboardBrokenClicked
                    "E" if key_E_state and CP2_tmpE_state:
                        $ CP2_tmpE_state = False
                        $ CP2_tmpText += "E"
                        jump keyboardBrokenClicked
                    "I" if key_I_state and CP2_tmpI_state:
                        $ CP2_tmpI_state = False
                        $ CP2_tmpText += "I"
                        jump keyboardBrokenClicked
                    "L" if key_L_state and CP2_tmpL_state:
                        $ CP2_tmpL_state = False
                        $ CP2_tmpText += "L"
                        jump keyboardBrokenClicked
                    "N" if key_N_state and CP2_tmpN_state:
                        $ CP2_tmpN_state = False
                        $ CP2_tmpText += "N"
                        jump keyboardBrokenClicked
                    "O" if key_O_state and CP2_tmpO_state:
                        $ CP2_tmpO_state = False
                        $ CP2_tmpText += "O"
                        jump keyboardBrokenClicked
                    "P" if key_P_state and CP2_tmpP_state:
                        $ CP2_tmpP_state = False
                        $ CP2_tmpText += "P"
                        jump keyboardBrokenClicked
                    "R" if key_R_state and CP2_tmpR_state:
                        $ CP2_tmpR_state = False
                        $ CP2_tmpText += "R"
                        jump keyboardBrokenClicked
                    "S" if key_S_state and CP2_tmpS_state:
                        $ CP2_tmpS_state = False
                        $ CP2_tmpText += "S"
                        jump keyboardBrokenClicked
                    "U" if key_U_state and CP2_tmpU_state:
                        $ CP2_tmpU_state = False
                        $ CP2_tmpText += "U"
                        jump keyboardBrokenClicked
                    "W" if key_W1_state and CP2_tmpW1_state:
                        $ CP2_tmpW1_state = False
                        $ CP2_tmpText += "W"
                        jump keyboardBrokenClicked
                    "W" if key_W2_state and CP2_tmpW2_state:
                        $ CP2_tmpW2_state = False
                        $ CP2_tmpText += "W"
                        jump keyboardBrokenClicked
                    "X" if key_X_state and CP2_tmpX_state:
                        $ CP2_tmpX_state = False
                        $ CP2_tmpText += "X"
                        jump keyboardBrokenClicked
                    "{u}{b}Auswahl bestätigen{/b}{/u}":
                        pass
                    "{u}{b}Auswahl zurücksetzen{/b}{/u}":
                        $ CP2_tmpD_state = True #um zu merken, welche Taste man gedrückt hatte
                        $ CP2_tmpE_state = True
                        $ CP2_tmpI_state = True
                        $ CP2_tmpL_state = True
                        $ CP2_tmpN_state = True
                        $ CP2_tmpO_state = True
                        $ CP2_tmpP_state = True
                        $ CP2_tmpR_state = True
                        $ CP2_tmpS_state = True
                        $ CP2_tmpU_state = True
                        $ CP2_tmpW1_state = True
                        $ CP2_tmpW2_state = True
                        $ CP2_tmpX_state = True
                        $ CP2_tmpText = "" #zurücksetzen des Eingabewortes
                        jump keyboardBrokenClicked
                    "{u}{b}Zurück{/b}{/u}":
                        jump ComputerSzene
                menu:
                    "Eingabe \"[CP2_tmpText]\" bestätigen?"
                    "Ja":
                        pass
                    "Nein":
                        jump keyboardBrokenClicked
                #festes Passwort "LINUX"
                if CP2_tmpText.lower() == "linux":
                    $ HideScreen("keyboardBroken")
                    $ ShowScreen("keyboardDummy")
                    $ HinweisCheck_state = False
                    $ current_label = ""
                    $ current_hinweis = ""
                    "Knöpfe korrekt eingesetzt!"
                    #Keyboard wurde repariert
                    $ repairedKeyboard = True
                    $ renpy.notify("Knöpfe eingesetzt")
                    $ CP2_KeyboardBroken_state = True
                    $ Keyboard_state = True
                    commander "Haha, was für ein Zufall. Linux ist ein bekanntes, datensparsames Open Source Betriebssystem.
                    Schau es dir doch mal nach dem Escape-Spiel etwas genauer an."
                else:
                    $renpy.notify("Leider falsch")
                    $mussWarten = True
                    #Bestrafungstimer von 10s
                    $ set_time = 10
                    $ timer_range = 10
                    $ countdown_title ="Bitte warten..."
                    $ timer_jump = "KnopfTimerEnde"
                    #zeige 10s Countdown an
                    show screen countdown
                    $ renpy.pause(hard=True)
                menu:
                    "Menü beenden?"
                    "Ja":
                        $ HideScreen("keyboardDummy")
                        $ ShowScreen("keyboardNormal")
                        $ HideScreen("BackButtonDummy")
                        $ ShowScreen("BackButton")
                        $ HinweisCheck_state = True
                        $ InventarCheck_state = True
                        window hide
                        $ renpy.pause(hard=True)
                    "Nein":
                        jump keyboardClicked
        $ renpy.pause(hard=True)

    label KnopfTimerEnde:
        $mussWarten = False
        jump keyboardBrokenClicked
        return

    label CockpitOSTimerEnde:
        $mussWarten = False
        menu:
            "PC beenden?"
            "Ja":
                $ HideScreen("keyboardDummy")
                $ ShowScreen("keyboardNormal")
                $ InventarCheck_state = True
                window hide
                $ renpy.pause(hard=True)
            "Nein":
                pass
        jump OpenCockpitOS
        return

    #reparierte Tastatur
    label keyboardClicked:
        $ InventarCheck_state = False
        $ HinweisCheck_state = False
        #OS noch nicht ausgewählt
        if not CP2_OsWahl_state:
            scene computer_on
            $ HideScreen("keyboardNormal")
            $ ShowScreen("keyboardDummy")
            $ HideScreen("BackButton")
            $ ShowScreen("BackButtonDummy")
            call OpenCockpitOS from _call_OpenCockpitOS
            $ HideScreen("keyboardDummy")
            $ ShowScreen("keyboardNormal")
            $ HideScreen("BackButtonDummy")
            $ ShowScreen("BackButton")
            scene computer_off
            $ renpy.pause(hard=True)

            label OpenCockpitOS:
                #Strom noch nicht an
                if not CP2_OpenOs_state:
                    if mussWarten:
                        $renpy.notify("Bitte warten")
                        $ renpy.pause(hard=True)
                    else:
                        "Um den Computer starten zu können, benötigst du das Passwort aus dem Maschinenraum."
                        #dynamisches Passwort
                        while enteredMonitorPW != "1234":
                            python:
                                try:
                                    enteredMonitorPW = int(renpy.input("Passwort eingeben"))
                                except:
                                    fail = True
                            if fail:
                                $ fail = False
                                $ enteredMonitorPW = ""
                            else:
                                $ enteredMonitorPW = str(enteredMonitorPW*10/(year*month*day))
                            if enteredMonitorPW != "1234": #wenn falsch, dann warte 10s
                                $renpy.notify("Falsches Passwort")
                                $ set_time = 10
                                $ countdown_title ="Bitte warten..."
                                $ timer_jump = "CockpitOSTimerEnde"
                                show screen countdown
                                $ renpy.pause(hard=True)
                            if enteredMonitorPW == "1234": #wenn richtig, dann gehe weiter
                                commander "Sehr schön, der Maschinenraum konnte wieder den Strom anschalten."
                                $ CP2_OpenOs_state = True
                        menu:
                            "PC beenden?"
                            "Ja":
                                $ HideScreen("keyboardDummy")
                                $ ShowScreen("keyboardNormal")
                                $ HideScreen("BackButtonDummy")
                                $ ShowScreen("BackButton")
                                $ InventarCheck_state = True
                                $ HinweisCheck_state = True
                                scene computer_off
                                window hide
                                $ renpy.pause(hard=True)
                            "Nein":
                                pass

                #noch kein OS gewählt
                if not CP2_OS_state:
                    $ HideScreen("keyboardNormal")
                    $ ShowScreen("keyboardDummy")
                    $ HideScreen("BackButton")
                    $ ShowScreen("BackButtonDummy")
                    $renpy.notify("Herzlich Willkommen im CockpitOS")
                    #wechsel Szene
                    scene computer_on_select
                    #verändere Computertitel
                    $os_title = "Betriebssystem wählen"
                    menu:
                        "Windows 10":
                            $ HideScreen("BackButton")
                            $ ShowScreen("BackButtonDummy")
                            $ LooseEnergy(20) #reduziere Energie um 20 Einheiten
                            $ LooseData(20) #reduziere Datenvolumen um 20 Einheiten
                            $ os_title = ""
                            $ HideScreen("choose_OS")
                            commander "Nun gut, Windows ist nicht die optimale Wahl. Um möglichst viel Strom und Datenvolumen zu sparen,
                            stelle bitte Windows korrekt ein!"
                            #wechsel Szene
                            scene computer_boot_windows
                            pause 3.0
                            scene computer_windows_on
                            $ isWindows = True
                            jump prepareWindoof #erweiterte Einstellungen von Windows
                        "Linux":
                            $ HideScreen("BackButton")
                            $ ShowScreen("BackButtonDummy")
                            $ LooseEnergy(10)
                            $ LooseData(10)
                            $ os_title = ""
                            $ isLinux = True
                            $ HideScreen("choose_OS")
                            commander "Gute Wahl, dadurch sparen wir deutlich Strom und Datenvolumen!"
                            scene computer_boot_linux_01
                            pause 1.0
                            scene computer_boot_linux_02
                            pause 1.0
                            scene computer_boot_linux_03
                            pause 1.0
                            scene computer_boot_linux_04
                            pause 1.0
                            scene computer_linux_on
                            $ CP2_OS_state = True
                            $ CP2_OsWahl_state = True
                            $ HideScreen("BackButtonDummy")
                            $ ShowScreen("BackButton")
                            $ HideScreen("keyboardDummy")
                            $ ShowScreen("keyboardNormal")
                            jump PrepareDesktop
                        "Ausschalten":
                            $ os_title = ""
                            $ HideScreen("choose_OS")
                            jump ComputerSzene
                            window hide
                            $ renpy.pause(hard=True)
                    return
        else:
            if CP2_Computer_state:
                $ ShowScreen("os_title")
                $ os_title = "PC wird hochgefahren"
                pause 1.0
                $ os_title += "\n        ."
                pause 1.0
                $ os_title += " ."
                pause 1.0
                $ os_title += " ."
                pause 0.5
                $ os_title = ""
                $ HideScreen("os_title")
                $ CP2_Computer_state = False
            else:
                $ HideScreen("App_Settings")
                $ HideScreen("App_Firefox")
                $ HideScreen("App_Edge")
                $ HideScreen("App_Chrome")
                $ HideScreen("App_Abwurf")
                $ HideScreen("App_Funk")
                $ HideScreen("App_Duesenstart")
                $ ShowScreen("os_title")
                $ os_title = "PC wird heruntergefahren"
                pause 1.0
                $ os_title += "\n        ."
                pause 1.0
                $ os_title += " ."
                pause 1.0
                $ os_title += " ."
                pause 0.5
                $ os_title = ""
                $ HideScreen("os_title")
                $ CP2_Computer_state = True
            jump ComputerSzene
    label PrepareDesktop:
        $ ShowScreen("App_Settings")
        $ ShowScreen("App_Firefox")
        $ ShowScreen("App_Edge")
        $ ShowScreen("App_Chrome")
        $ ShowScreen("App_Abwurf")
        $ ShowScreen("App_Funk")
        jump ComputerSzene
        $ renpy.pause(hard=True)

    label EditSettings:
        $ InventarCheck_state = False
        $ HinweisCheck_state = False
        #noch keine Verbindung zum Maschinenraum
        if not CP2_Verbindung_state:
            $ renpy.notify("Einstellungen")
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
            "Du bist dabei, über einen Satelliten eine Verbindung zum Maschinenraum herzustellen."
            $os_title = "Wie soll die Verbindung verschlüsselt werden?"
            $ https = False
            menu:
                "HTTPS":
                    $ https = True
                    $os_title = ""
                    $ LooseEnergy(20)
                    $ LooseData(20)
                    #dient zur Überprüfung in CP6_DüsenstartCP.cpy, ob Aktion ausgeführt wird
                    $ encryptionChecker = False #Aktion wird ausgeführt
                    "Ein sicheres Verbindungsprotokoll wurde ausgewählt."
                    while encryptionKorrekt == False:
                        commander "Sehr gut, HTTPS ist ein sehr sicheres Protokoll."
                        $os_title = "Wähle einen sicheren Verbindungsschlüssel aus! Bitte notieren!"
                        menu:
                            "MAX!B3N":
                                "Passwörter, die Namen enthalten, sind leichter knackbar!"
                                "\"2T,eW.Ü!\" wäre ein sehr gutes Passwort gewesen! Bitte notiere dir dieses!" #evtl. in Nebenaufgabe enthalten!!!!
                                $ encryptionKorrekt = True
                            "1E05!97&":
                                "Passwörter, die (d)ein Geburtsdatum enthalten, sind leichter knackbar!"
                                "\"2T,eW.Ü!\" wäre ein sehr gutes Passwort gewesen! Bitte notiere dir dieses!" #evtl. in Nebenaufgabe enthalten!!!!
                                $ encryptionKorrekt = True
                            "2T,eW.Ü!":
                                #Richtiger Weg, da Passwort sehr komplex, aber dennoch leicht zu merken ist
                                "Sehr gutes Passwort. Es sieht zwar kompliziert aus, jedoch kann man sich eine einfache Eselbrücke bauen."
                                "2T,eW.Ü! -> {b}2{/b} {b}T{/b}eams{b},{/b} {b}e{/b}in {b}W{/b}ille{b}.{/b} {b}Ü!{/b}"
                                $ encryptionKorrekt = True
                                $ encryptionChecker = True
                            "pa$$word":
                                "Dieses und ähnliche \"Passwörter\" {b}NIE{/b} benutzen"
                                "\"2T,eW.Ü!\" wäre ein sehr gutes Passwort gewesen! Bitte notiere dir dieses!" #evtl. in Nebenaufgabe enthalten!!!!
                                $ encryptionKorrekt = True
                    $ HideScreen("choose_connectionKey")
                "HTTP":
                    $ LooseEnergy(10)
                    $ LooseData(10)
                    $os_title = ""
                    #dient zur Überprüfung in chapter_7.cpy, ob Aktion ausgeführt wird
                    $ encryptionChecker = False #Aktion wird ausgeführt
                    $ HideScreen("choose_connection")
                    "Ein unsicheres Verbindungsprotokoll wurde ausgewählt."
                    "\"2T,eW.Ü!\" wäre ein sehr gutes Passwort gewesen! Bitte notiere dir dieses!" #evtl. in Nebenaufgabe enthalten!!!!
                    commander "HTTP ist wie ein offener Brief mit Absender und Empfänger. Jeder kann ihn lesen!"
            $os_title = ""
            "Du möchtest wissen, ob deine Passwörter sicher sind?"
            #Verweis auf Internetseite "checkdeinpasswort"
            "Notiere dir oder besuche die Seite {a=https://checkdeinpasswort.de}checkdeinpasswort.de{/a}!"
            $ CP2_Verbindung_state = True
            menu:
                "Einstellungen beenden?"
                "Ja":
                    jump ComputerSzene
                    window hide
                    $ renpy.pause(hard=True)
                "Nein":
                    $ HideScreen("keyboardDummy")
                    $ ShowScreen("keyboardNormal")
                    $ HideScreen("BackButtonDummy")
                    $ ShowScreen("BackButton")

    label SystemCheck:
        $ InventarCheck_state = False
        $ HinweisCheck_state = False
        #
        if (not CP2_EditedSettings_state):
            $ renpy.notify("Einstellungen")
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
            "Du hast dich erfolgreich mit dem Maschinenraum verbunden!"
            commander "Der Maschinenraum hat mir gemeldet, dass sie für den Systemcheck unsere Freigabe benötigen."
            "Für die sichere Freigabe müssen vorher einige Einstellungen getroffen werden"
            $SysCounter = 0 #Counter, um Anzahl falscher Entscheidungen zu merken
            $tmp_text = ""
            $ ShowScreen("os_title")
            $os_title = "Firewall"
            menu:
                "Aktivieren":
                    $ firewall = True
                    $renpy.notify("Firewall aktiv")
                    commander "Gute Wahl, die Firewall schützt dich vor unerwünschten Netzwerkangriffen!"
                "Deaktivieren":
                    $ firewall = False
                    $renpy.notify("Firewall inaktiv")
                    $SysCounter += 1
                    commander "Nicht gut, ohne eine Firewall können User unerwünscht auf dein Netzwerk zugreifen!"

            $os_title = "Virenschutz"
            menu:
                "Aktivieren":
                    $ antivir = True
                    $renpy.notify("Virenschutz aktiv")
                    commander "Prima, ein guter Antivirenschutz kann dich vor den meisten Cyberbedrohungen schützen!"
                    commander "Verlasse dich aber nicht zu sehr auf diesen Schutz, sondern handel auch sicherheitsbewusst!"
                    commander "Öffne beispielweise bei einer dir unbekannten oder merkwürdig vorkommenden E-Mail nie den Anhang!"
                "Deaktivieren":
                    $ antivir = False
                    $renpy.notify("Virenschutz inaktiv")
                    $SysCounter += 1
                    commander "Schlechte Wahl, ein guter Antivirenschutz könnte dich vor den meisten Cyberbedrohungen schützen!"
                    commander "Verlasse dich aber nicht zu sehr auf solch einen Schutz, sondern handel auch sicherheitsbewusst!"
                    commander "Öffne beispielweise bei einer dir unbekannten oder merkwürdig vorkommenden E-Mail nie den Anhang!"

            $os_title = "Datensicherung"
            menu:
                "Aktivieren":
                    $ dasi = True
                    $renpy.notify("Datensicherung aktiv")
                    $SysCounter += 1
                    commander "Schlechte Entscheidung, zwar ist eine Datensicherung immer sehr zu empfehlen,
                    jedoch wird sie in diesem Fall nicht benötigt."
                    commander "Wir möchten sicher auf der Erde landen,
                    eine Datensciherung würde unnötig Ressourcen kosten!"
                    comander "Für dich privat ist es jedoch sehr sinnvoll,
                    deine Daten auf einem netzwerkfreien Medium zu speichern, um ungewollten Datenverlust zu vermeiden!"
                "Deaktivieren":
                    $ dasi = False
                    $renpy.notify("Datensicherung inaktiv")
                    "In diesem Fall ist es eine gute Wahl, dies spart Ressourcen! Für dich privat ist es jedoch sehr sinnvoll,
                    deine Daten auf einem netzwerkfreien Medium zu speichern, um ungewollten Datenverlust zu vermeiden!"
            $ os_title = ""
            "HTTPS:[https] \n Firewall: [firewall] \n Virenschutz: [antivir] \n Datensicherung: [dasi]"

            if SysCounter > 0: #höherer Verbrauch, je nach Anzahl falscher Angaben
                $ LooseEnergy(SysCounter*10+10)
                $ LooseData(SysCounter*10+10)
            else:
                $ LooseEnergy(10)
                $ LooseData(10)

            commander "Sehr schön, die Freigabe wurde erteilt. Ich übermittle nun das Passwort an den Maschinenraum."
            "Auf welche Weise möchtest du das Passwort an den Maschinenraum übermitteln?"
            $os_title = "Übertragungsart"
            menu:
                "per Textnachricht":
                    $ LooseEnergy(10)
                    $ LooseData(10)
                    commander "Eine Textnachricht sollte völlig ausreichend sein."
                "per Sprachnachricht":
                    $ LooseEnergy(20)
                    $ LooseData(20)
                    commander "Hmm so viel Daten und Strom für ein Passwort? Nun gut."
                "per Bildnachricht":
                    $ LooseEnergy(30)
                    $ LooseData(30)
                    commander "Hmm so viel Daten und Strom für ein Passwort? Nun gut."

            $os_title = "5iRDAPLF" #Passwort für Übermittlung und Entschlüsselung des Bauplanes
            call chapter_3_pw_uebermitteln from _call_chapter_3_pw_uebermitteln
            $ CP2_EditedSettings_state = True
            jump ComputerSzene
            window hide
            return
        else:
            $ renpy.notify("Einstellungen bereits gesetzt")
            pause 2.0
            jump ComputerSzene

    label chapter_3_pw_uebermitteln: #Überprüfung, ob Passwort notiert
        "Gebe das Passwort zur Systemfreigabe an den Maschinenraum weiter."
        menu:
            "Hast du das Passwort notiert/übermittelt?"
            "Ja":
                $ HideScreen("os_title")
            "Nein":
                call chapter_3_pw_uebermitteln from _call_chapter_3_pw_uebermitteln_1
        return

    label prepareWindoof:
        $ InventarCheck_state = False
        $ HinweisCheck_state = False
        "Bevor du mit Windows starten kannst, musst du noch einige Einstellungen treffen!"
        $ ShowScreen("os_title")
        $os_title = "Mikrofonzugriff erlauben?"
        #Counter, um Anzahl falscher Entscheidungen zu merken
        $WinCounter = 0
        #aufrufen eines Auswahlmenüs
        menu:
            "Erlauben":
                $ WinMic = True
                $WinCounter += 1
                $renpy.notify("Mikrofon aktiv")
                commander "Urgh, Windows muss nicht jederzeit Zugriff auf dein Mikrofon haben!"

            "Verbieten":
                $ WinMic = False
                $renpy.notify("Mikrofon inaktiv")
                commander "Gute Wahl, aktiviere es nur, wenn du sie wirklich benötigst!"

        $os_title = "Kamerazugriff erlauben?"
        menu:
            "Erlauben":
                $ WinCam = True
                $WinCounter += 1
                $renpy.notify("Kamera aktiv")
                commander "Urgh, Windows muss nicht jederzeit Zugriff auf deine Kamera haben!"
            "Verbieten":
                $ WinCam = False
                $renpy.notify("Kamera inaktiv")
                commander "Gute Wahl, aktiviere sie nur, wenn du es wirklich benötigst!"

        $os_title = "Erhebung von Telemetriedaten?"
        menu:
            "Erlauben":
                $ WinTele = True
                $WinCounter += 1
                $renpy.notify("Erhebung aktiv")
                commander "Schlechte Wahl, somit wirst du zu einem gläsernen Bürger!"
            "Verbieten":
                $ WinTele = False
                $renpy.notify("Erhebung inaktiv")
                commander "Sehr schön, du verstehst Privatsphäre!"

        $os_title = "Clouddienste erlauben?"
        menu:
            "Erlauben":
                $ WinClou = True
                $WinCounter += 1
                $renpy.notify("Clouddienste aktiv")
                commander "Clouddienste sind eine gute Möglichkeit Daten zu sichern, jedoch ist
                Microsoft im Thema Datenschutz sehr nachlässig."
                commander "Schaue doch einmal im Internet nach Cloudanbietern, welche in Deutschland gehostet werden und die
                deutsche DSGVO einhalten!"
            "Verbieten":
                $ WinClou = False
                $renpy.notify("Clouddienste inaktiv")
                commander "Eine gute Wahl in Bezug auf Microsofts Clouddienst. Dieser weißt erhebliche Mängel bezüglich des Datenschutzes auf. Es gibt jedoch auch sichere Cloudanbieter, welche
                in Deutschland gehostet werden und die DSGVO Ordnung einhalten müssen!"
                commander "Schaue einfach mal im Internet nach!"

        $os_title = "Spracherkennung erlauben?"
        menu:
            "Erlauben":
                $ WinDet = True
                $WinCounter += 1
                $renpy.notify("Spracherkennung aktiv")
                "Oh nein, bitte schalte eine Spracherkennung immer aus. #Belauschung"
            "Verbieten":
                $ WinDet = False
                $renpy.notify("Spracherkennung inaktiv")
                "Gute Entscheidung, niemand möchte abgehört werden!"

        $os_title = "" #löschen des OS-Titels
        $ HideScreen("BackButtonDummy")
        $ ShowScreen("BackButton")
        $ CP2_OS_state = True
        $ CP2_OsWahl_state = True
        if WinCounter > 3: #wenn größer 3, dann sehr hoher Verbrauch
            $ LooseEnergy(30)
            $ LooseData(50)
            menu:
                "PC verlassen?"
                "Ja":
                    jump ComputerSzene
                    window hide
                    $ renpy.pause(hard=True)
                "Nein":
                    $ HideScreen("keyboardDummy")
                    $ ShowScreen("keyboardNormal")
            jump PrepareDesktop
        else :
            if WinCounter > 0: #wenn zwischen 0 und 3, dann je nach Anzahl des Counters
                $ LooseEnergy(WinCounter*10)
                $ LooseData(WinCounter*10)
                menu:
                    "PC verlassen?"
                    "Ja":
                        jump ComputerSzene
                        window hide
                        $ renpy.pause(hard=True)
                    "Nein":
                        $ HideScreen("keyboardDummy")
                        $ ShowScreen("keyboardNormal")
                jump PrepareDesktop
            else:
                menu:
                    "PC verlassen?"
                    "Ja":
                        jump ComputerSzene
                        window hide
                        $ renpy.pause(hard=True)
                    "Nein":
                        $ HideScreen("keyboardDummy")
                        $ ShowScreen("keyboardNormal")
                jump PrepareDesktop #wenn 0, dann kein Abzug
