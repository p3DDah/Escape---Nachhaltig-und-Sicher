label computerWandClicked_Reparieren:
    $ HinweisCheck_state = False
    $ InventarCheck_state = False
    $ ImageButtonActivate_state = False
    #Düsenantrieb noch nicht repariert
    if not CP5_Reparatur_state:
        commander "Laut dem Systemcheck muss noch einiges repariert werden. Repariere aber nur wirklich notwendiges!"

        $Akk2_init = True
        $Akk5_init = True
        $Akk10_init = True
        $Cock_init = True
        $Haupt_init = True
        $Seit1_init = True
        $Seit2_init = True
        $RepTimer = 0 #gibt die Wartezeit an, wie lange man warten muss, bis alles repariert wurde

        label reparatur:
            menu:
                "Was möchtest du repariert haben?"
                "Akkuzelle 2" if Akk2_init:
                    $Akk2_init = False
                    $RepTimer += 18
                    $ LooseEnergy(20)
                    jump reparatur
                "Akkuzelle 5" if Akk5_init:
                    $Akk5_init = False
                    $RepTimer += 18
                    $ LooseEnergy(20)
                    jump reparatur
                "Akkuzelle 10" if Akk10_init:
                    $Akk10_init = False
                    $RepTimer += 19
                    $ LooseEnergy(20)
                    jump reparatur
                "Cockpit-Zentrale" if Cock_init:
                    $Cock_init = False
                    $RepTimer += 35
                    $ LooseEnergy(20)
                    jump reparatur
                "Hauptantriebsdüse" if Haupt_init:
                    $Haupt_init = False
                    $RepTimer += 10
                    $ LooseEnergy(5)
                    jump reparatur
                "Seitenantriebsdüse 1" if Seit1_init:
                    $Seit1_init = False
                    $RepTimer += 6
                    $ LooseEnergy(5)
                    jump reparatur
                "Seitenantriebsdüse 2" if Seit2_init:
                    $Seit2_init = False
                    $RepTimer += 7
                    $ LooseEnergy(5)
                    jump reparatur
                "{u}{b}Auswahl bestätigen{/b}{/u}":
                    pass
                "{u}{b}Auswahl zurücksetzen{/b}{/u}":
                    $Akk2_init = True
                    $Akk5_init = True
                    $Akk10_init = True
                    $Cock_init = True
                    $Haupt_init = True
                    $Seit1_init = True
                    $Seit2_init = True
                    $RepTimer = 0
                    jump reparatur
                "{u}{b}Zurück{/b}{/u}":
                    jump reparatur
            if (RepTimer == 0 or RepTimer < 18):
                commander "Laut Systemcheck müssen noch einige Teile repariert werden"
                jump reparatur
            $ CP5_Reparatur_state = True
            menu:
                "Komponentenreparatur beenden?"
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

    "Um die Komponenten zu reparieren, benötigst du die Teile aus dem Puzzle."
    "Wenn du alle Teile gefunden hast, dann wird zum Starten der Komponenten ein Sicherheitspasswort
    benötigt."
    commander "Schrankverwalter Professor Eich hatte dieses Passwort erstellt. Er war bekannt dafür, seine Kennwörter anhand der Maschinenteile zu erstellen."
    commander "Schau dir am Besten einen einzelnen Buchstaben je Wort an und füge ihn mit je einem anderen Buchstaben eines anderer Wortes zusammen."

    label reparierenWort_label:
        $ HinweisCheck_state = True
        $ current_label = "reparierenWort_label"
        $ current_hinweis = "CP5_reparierenWort_label_Hinweis"
        $ reparierenWort = renpy.input("Lösungswort? (8-stellig)")
        if reparierenWort.lower() == "whatsapp":
            $ current_label = ""
            $ current_hinweis = ""
            $ InventarCheck_state = True
            "Passwort korrekt"
            commander "Nun können wir mit der Reparatur beginnen"
            $ set_time = RepTimer #je mehr ausgewählt desto länger
            $ countdown_title ="Reparatur läuft..."
            $ timer_jump = 'ReparaturFertig'
            show screen countdown
        else:
            "Das war leider nicht richtig, versuche es erneut"
            jump reparierenWort_label

label ReparaturFertig:
    $ finishReparieren = True
    $ ImageButtonActivate_state = True
    $ HideScreen("choose_zeitpunkt")
    $ renpy.notify("Reparatur erfolgreich")
    commander "Das war aber ein \"tolles\" Passwort. Für Whatsapp gibt es gute Alternativen, Threema oder Signal zum Beispiel!"

    $ CP6_UnlockDoor_state += 1

    if CP6_UnlockDoor_state >= 4:
        jump lastScene

    window hide
    $ renpy.pause(hard=True)
    #$ renpy.pause(hard=True)
