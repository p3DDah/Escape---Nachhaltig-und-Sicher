label computerWandClicked_Kursberechnung:
    $ renpy.notify("Willkommen in der Kursberechnung")
    $ HinweisCheck_state = False
    $ InventarCheck_state = False
    $ ImageButtonActivate_state = False

    #Informationen aus Cockpit noch nicht erhalten
    if not CP4_CalcPass_state:
        commander "Es wird Zeit endlich wieder auf den richtigen Kurs zurückzukommen!"
        commander "Hierzu müssen wir jedoch erst die Informationen aus dem Cockpit erhalten, um einen sinnvollen Kurs zu berechnen."
        menu:
            "Hast du das Passwort/die Informationen vom Cockpit erhalten?"
            "Ja":
                pass
            "Nein":
                $ HinweisCheck_state = True
                $ current_label = ""
                $ current_hinweis = ""
                $ InventarCheck_state = True
                $ ImageButtonActivate_state = True
                window hide
                $ renpy.pause(hard=True)

        label kursberechnungPasswort_label:
        $ kursberechnungPasswort = ""
        python:
            try:
                kursberechnungPasswort = int(renpy.input("Bitte geben Sie das Passwort aus dem Cockpit ein"))
            except:
                fail = True
        if fail:
            $ fail = False
            "Bitte nur Zahlen eingeben!"
            jump kursberechnungPasswort_label
        $ password = kursberechnungPasswort*10/(year*month*day)

        #Auswahl entsprechend was Cockpit ausgewählt hat
        if kursberechnungPasswort == "3412": #"FuNEJVB!"
            $ CP4_CalcPass_state = True
            #Text Informationen von Cockpit empfangen
            $ CP4_CalcPassText_state = False
            jump kb_Text
        elif kursberechnungPasswort == "4123": #"uwKRg5un"
            $ CP4_CalcPass_state = True
            #Sprach Information von Cockpit empfangen
            $ CP4_CalcPassSound_state = False
            jump kb_Audio
        elif kursberechnungPasswort == "1243": #"0P!&UlZF"
            $ CP4_CalcPass_state = True
            #Video Information von Cockpit empfangen
            $ CP4_CalcPassVideo_state = False
            jump kb_Bild
        else:
            menu:
                "Leider falsch"
                "Passwort erneut eingeben":
                    jump kursberechnungPasswort_label
                "Zurück":
                    $ HinweisCheck_state = True
                    $ current_label = ""
                    $ current_hinweis = ""
                    $ InventarCheck_state = True
                    $ ImageButtonActivate_state = True
                    jump computerWandClicked

        window hide
        $ renpy.pause(hard=True)

label kb_Text:
    if not CP4_CalcPassText_state:
        "Notiere dir den Text!"
        #325365; 27384; 2195; 5,9736·1024; 3,6·10-5; 1:12:35:813
        $ seqKursberechnungText = ["325365", "27384", "2195", "5,9736*10^24", "3,6*10^-5", "1:12:35:813"]
        $ fooo = renpy.random.shuffle(seqKursberechnungText)
        "[seqKursberechnungText[0]]; [seqKursberechnungText[1]]; [seqKursberechnungText[2]];
        [seqKursberechnungText[3]]; [seqKursberechnungText[4]]; [seqKursberechnungText[5]]"
        commander "Es scheint, dass einige Informationen fehlen. Da wollte wohl das Cockpit etwas Ressourcen sparen. Nun haben wir die Rätselarbeit!"
        menu:
            "Hast du dir den Text notiert?"
            "Ja":
                pass
            "Nein":
                jump kb_Text
        $ CP4_CalcPassText_state = True
        menu:
            "Kursberechnung beenden?"
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
        jump kursberechnungAuth

label kb_Audio:
    if not CP4_CalcPassSound_state:
        #der Dialog muss hier evtl. noch angepasst werden
        play sound "audio/morse_code.mp3"
        "Speichere dir den Morse Code ab und füge ihn bei {a=https://morsecode.world/international/translator.html}Übersetzer{/a} ein!"
        $ txt = ".--. .- ... ... .-- --- .-. - ---... / ...-- ..--- ..... ...-- -.... ..... / .- -.- - ..- . .-.. .-.. . / --. . ... -.-. .... .-- .. -. -.. .. --. -.- . .. - ---... / ..--- --... .-.-.- ...-- ---.. ....- / -.- -- -..-. .... / -... . -. ---. - .. --. - . / --. . ... -.-. .... .-- .. -. -.. .. --. -.- . .. - ---... / ..--- .---- ----. ..... / -.- -- -..-. .... / -- .- ... ... . / -.. . .-. / . .-. -.. . ---... / ..... --..-- ----. --... ...-- -.... / -.--. -- .- .-.. -.--.- / .---- ----- -.--. .... --- -.-. .... -.--.- ..--- ....- / -.- --. / . -. - ..-. . .-. -. ..- -. --. / --.. ..- .-. / . .-. -.. . ---... / ...-- --..-- -.... / -.--. -- .- .-.. -.--.- / .---- ----- -.--. .... --- -.-. .... -.--.- -....- ..... / .- . / -.- ..- .-. ... .-.- -. -.. . .-. ..- -. --. ... --.. . .. - ---... / .---- ---... .---- ..--- ---... ...-- ..... ---... ---.. .---- ...--"
        commander "Oh wie cool, ein Morse-Code! Bib Bib Boob Boob Bib ..."
        $ ShowScreen("clipboard")
        "Lasse dir den Morse Code übersetzen."
        $ HideScreen("clipboard")
        menu:
            "Hast du dir den Morse-Code notiert?"
            "Ja":
                pass
            "Nein":
                jump kb_Audio
        $ CP4_CalcPassSound_state = True
        stop sound fadeout 1.0
        menu:
            "Kursberechnung beenden?"
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
        jump kursberechnungAuth

label kb_Bild:
    if not CP4_CalcPassVideo_state:
        "Notiere dir die Werte auf dem Bild!"
        image kursCalcPic = im.FactorScale("images/Objekte/Maschinenraum/kursCalcPic.png", 1.8)
        $ HideScreen("computerWand")
        commander "Seehr schön, eine Bildnachricht, zwar etwas ressourcenhungrig,
        dafür können wir schnell weiterarbeiten. Manchmal muss man eben Kompromisse eingehen!"
        show kursCalcPic at truecenter

        "Notiere die Werte!"

        hide kursCalcPic
        $ ShowScreen("computerWand")
        menu:
            "Hast du dir den Bildinhalt notiert?"
            "Ja":
                pass
            "Nein":
                jump kb_Video
        $ CP4_CalcPassVideo_state = True
        menu:
            "Kursberechnung beenden?"
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
        jump kursberechnungAuth

label kursberechnungAuth:
    $ HinweisCheck_state = True
    $ current_label = "kursberechnungAuth"
    $ current_hinweis = "CP4_kursberechnungAuth_Hinweis"
    commander "Trage nun die richtigen Werte in die .ods"
    commander "Soweit ich weiß, erscheint bei richtiger Eingabe ein Hinweis für einen Schlüssel."
    "Hinweis: Die Datei kann nur mit LibreOffice geöffnet werden!"

    label kursberechnungFinalAuth_label:
    $ kursberechnungFinalAuth= ""
    $ kursberechnungFinalAuth = renpy.input("Trage die Lösung der Frage hier ein:")

    $ tmp = False
    if kursberechnungFinalAuth.lower() == "libreoffice" or kursberechnungFinalAuth.lower() == "gimp":
        $ current_label = ""
        $ current_hinweis = ""
        "Authentifizierung erfolgreich!"
        "Die automatische Kurskorrektur wurde aktiviert. Der Kurs wird in Kürze angepasst."
        commander "Toll, wenn wir so weiter machen, landen wir garantiert sicher auf der Erde!"
        commander "Ach übrigens, LibreOffice und Gimp sind beides OpenSource Projekte. Falls du also ein gutes
        und datensparsames Office Programm benötigst, dann ist LibreOffice die Wahl Nummer 1!"
        commander "Willst du Bilder kostenlos und professionell bearbeiten, dann probier doch mal Gimp aus!"

        $ finishKursberechnung = True
        $ InventarCheck_state = True
        $ ImageButtonActivate_state = True

        $ CP6_UnlockDoor_state += 1

        if CP6_UnlockDoor_state >= 4:
            jump lastScene

        window hide
        $ renpy.pause(hard=True)
    else:
        "Leider falsch, versuche es weiter"
        $ tmp = True
    menu:
        "Kursberechnung beenden?"
        "Ja":
            $ InventarCheck_state = True
            $ current_label = ""
            $ current_hinweis = ""
            $ ImageButtonActivate_state = True
            window hide
            $ renpy.pause(hard=True)
        "Nein":
            pass
    if tmp:
        jump kursberechnungFinalAuth_label
