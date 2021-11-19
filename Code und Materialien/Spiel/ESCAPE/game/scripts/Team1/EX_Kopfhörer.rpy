#Zusatzaufgabe Kopfhörer finden

label FindeKopfhoerer:
    if not EX_Box_state:
        $ HinweisCheck_state = True
        $ current_label = "FindeKopfhoerer"
        $ current_hinweis = "EX_FindeKopfhoerer_Hinweis"
        $ InventarCheck_state = False
        $ Box_Code = ""
        $ renpy.notify("Verschlossen!")
        commander "Hmm die Kiste ist verschlossen. Wir benötigen einen 3-stelligen Zahlencode!"
        while Box_Code != "100":
            $ Box_Code = renpy.input("Gebe den Zahlencode ein!")
            if Box_Code != "100":
                $ renpy.notify("Code falsch!")
                commander "Mist, das war der falsche Code!"
                menu:
                    "Zurück zum Cockpit?"
                    "Ja":
                        jump Cockpit_Standard
                        window hide
                        $ renpy.pause(hard=True)
                    "Nein":
                        pass
        $ HinweisCheck_state = False
        $ current_label = ""
        $ current_hinweis = ""
        $ EX_Box_state = True
        $ inventory.append(Kopfhoerer)
        commander "Sehr schön, wir haben einen Kopfhörer erhalten!"
        jump Cockpit_Standard
        window hide

    else:
        $ renpy.notify("Box bereits geöffnet!")
    $ renpy.pause(hard=True)
