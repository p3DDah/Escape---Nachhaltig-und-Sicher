#Zusatzaufgabe Flachwitze

label TruheFlach:
    if not EX_Truhe_state:
        $ InventarCheck_state = False
        $ HinweisCheck_state = True
        $ current_label = "TruheFlach"
        $ current_hinweis = "EX_TruheFlach_Hinweis"
        $ Truhe_Code = ""
        commander "Sieht so aus als könnten wir diese Schloss noch öffnen. Lediglich zwei Ziffern fehlen uns!"
        while Truhe_Code != "99":
            $ Truhe_Code = renpy.input("Gebe den Zahlencode ein!")
            if Truhe_Code != "99":
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
        $ EX_Truhe_state = True
        commander "Cool, wir haben einen kleinen Zettel gefunden!"
        jump ZettelStuff
    else:
        $ renpy.notify("Truhe geöffnet!")
        commander "Schauen wir uns den Zettel noch etwas genauer an."
        label ZettelStuff:
            menu:
                "Welchen Inhalt möchtest du dir anschauen?"
                "Mysteriöser Hammer":
                    "Was sagt ein Hammer zu einem Daumen?"
                    "Schön dich mal wieder zu treffen!"
                    commander "HAHA ich hau mich weg!"
                    jump ZettelStuff

                "Monatsrätsel":
                    "Einige Monate haben 30 Tage andere haben 31 Tage. Doch wie viel Monate haben 28 Tage?"
                    "Alle"
                    commander "Oha stimmt."
                    jump ZettelStuff

                "Räumliche Verwirrung":
                    "In welchem Raum stirbt ein normaler Menschen nach wenigen Sekunden, wenn er ihn betritt?"
                    "Im Weltraum"
                    commander "Ein Hoch auf die Technologie! Wir leben noch!!!"
                    jump ZettelStuff

                "Limes":
                    "Womit endet die Unendlichkeit?"
                    "Mit dem Buchstaben \"t\""
                    commander "Och komm schon."
                    jump ZettelStuff

                "Fliegende Fahrt":
                    "Bei welcher Fahrt wird hauptsächlich geflogen?"
                    "Bei der Raumfahrt"
                    commander "Klingt einleuchtend!"
                    jump ZettelStuff

                "Stift Freunde":
                    "Was sagt der große Stift zum kleinen Stift?"
                    "Wachs-mal-stift"
                    commander "Ohhhh coool!"
                    jump ZettelStuff

                "Magneten-Treff":
                    "Treffen sich zwei Magneten. Sagt der Eine:"
                    "Was soll ich bloß anziehen"
                    commander "Hihi ein klassiches Problem."
                    jump ZettelStuff

                "Die Kunst des Werfens":
                    "Wie nennt man jemand der so tut als würde er etwas werfen?"
                    "Einen Scheinwerfer"
                    commander "Der war gut!"
                    jump ZettelStuff

                "Zurück":
                    jump Cockpit_Standard
                    window hide
                    $ renpy.pause(hard=True)
    window hide
    $ renpy.pause(hard=True)

label TruheWhatsapp:
    commander "Da ist ein Zettel drin. Ein kleiner Auszug von den Daten, welche Whatsapp über dich sammelt."
    menu:
        "Möchtest du dir den Zettel anzeigen lassen?"
        "Ja":
            pass
        "Nein":
            jump Cockpit_Standard
            window hide
            $ renpy.pause(hard=True)
    label DatenWhat:
    menu:
        "Diese Daten werden von Whatsapp erhoben:"
        "Telefonnumer":
            jump DatenWhat
        "Verbindungsstatus":
            jump DatenWhat
        "Letzte IP-Adresse":
            jump DatenWhat
        "Gerätetyp, Hersteller, OS":
            jump DatenWhat
        "App-Version":
            jump DatenWhat
        "Profilbild, Datum des Uploads, Profilbesuch":
            jump DatenWhat
        "Beigetretene Gruppen":
            jump DatenWhat
        "Uhrzeit und Bestätigung zur Zustimmung der AGBs":
            jump DatenWhat
        "Mobilfunkbetreiber":
            jump DatenWhat
        "Registrierungsdatum":
            jump DatenWhat
        "App-Einstellungen":
            jump DatenWhat
        "{b}Zurück zum Cockpit{/b}":
            jump Cockpit_Standard
            window hide
            $ renpy.pause(hard=True)
    window hide
    $ renpy.pause(hard=True)
