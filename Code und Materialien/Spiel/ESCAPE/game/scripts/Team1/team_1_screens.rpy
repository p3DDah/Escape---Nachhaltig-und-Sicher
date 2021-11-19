#Klasse, um bestimmte Objekte klickbar zu machen und dahingehend eine Funktion auszuführen
init:
    transform arrowSize:
        zoom 0.5

    transform keycardSize:
        zoom 0.2

screen Schrank():
    imagebutton:
        xalign 0.28
        yalign 0.3
        idle "Objekte/Cockpit/Schrank.png"
        action []
        at transform:
            zoom 0.8

screen Truhe():
    imagebutton:
        xalign 0.28
        yalign 0.34
        idle "Objekte/Cockpit/Truhe.png"
        hover "Objekte/Cockpit/Truhe_Hover.png"
        action [Notify("Schloss kaputt!")]
        at transform:
            zoom 0.28

screen Truhe2():
    imagebutton:
        xalign 0.33
        yalign 0.41
        idle "Objekte/Cockpit/Truhe.png"
        hover "Objekte/Cockpit/Truhe_Hover.png"
        action [Notify("Truhe geöffnet!"), Call("TruheWhatsapp")]
        at transform:
            zoom 0.2

screen Truhe3():
    imagebutton:
        xalign 0.289
        yalign 0.275
        idle "Objekte/Cockpit/Truhe.png"
        hover "Objekte/Cockpit/Truhe_Hover.png"
        action [Notify("Schloss kaputt!")]
        at transform:
            zoom 0.24

screen Truhe4():
    imagebutton:
        xalign 0.352
        yalign 0.32
        idle "Objekte/Cockpit/Truhe.png"
        hover "Objekte/Cockpit/Truhe_Hover.png"
        action [Notify("Schloss kaputt!")]
        at transform:
            zoom 0.16
            rotate -30

screen Truhe5():
    imagebutton:
        xalign 0.353
        yalign 0.36
        idle "Objekte/Cockpit/Truhe.png"
        hover "Objekte/Cockpit/Truhe_Hover.png"
        action [Notify("Verschlossen"), Call("TruheFlach")]
        at transform:
            zoom 0.15

screen Roboter():
    imagebutton:
        xalign 0.17
        yalign 0.52
        idle "Objekte/Cockpit/Roboter.png"
        hover "Objekte/Cockpit/Roboter_Hover.png"
        action [Call("RobotSpricht")]
        at transform:
            zoom 2.5

screen Box():
    imagebutton:
        xalign 0.93
        yalign 0.65
        idle "Objekte/Cockpit/Box.png"
        hover "Objekte/Cockpit/Box_Hover.png"
        action [Call("FindeKopfhoerer")]
        at transform:
            zoom 2.5

screen gotoCockpitDoor():
    imagebutton:
        xalign 0.5
        yalign 0.4172
        idle "Objekte/door.png"
        hover "Objekte/door_hover.png"
        action Call("cockpitDoorClicked")

screen cockpitKeycard():
    imagebutton:
        xalign 0.1
        yalign 0.9
        idle "Objekte/keycard.png"
        action [Notify("Schlüsselkarte gefunden"), Hide("cockpitKeycard"), Play("sound", "audio/item_found.mp3"), SetVariable("tookKeycard", True), AddToSet(inventory, cockpitKeycard)]
        at keycardSize

screen cockpitDoorPinpad():
    imagebutton:
        xalign 0.68
        yalign 0.4
        idle "Objekte/pinpad.png"
        hover "Objekte/pinpad_hover.png"
        action Call("cockpitPinpadClicked")

screen key_L():
    imagebutton:
        xalign 0.4
        yalign 0.8
        idle "Objekte/Cockpit/key_L.png"
        action [Notify("Taste gefunden"), Hide("key_L"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, key_L), SetVariable("key_L_state", True)]
        at transform:
            zoom 0.7

screen key_I():
    imagebutton:
        xalign 0.35
        yalign 0.75
        idle "Objekte/Cockpit/key_I.png"
        action [Notify("Taste gefunden"), Hide("key_I"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, key_I), SetVariable("key_I_state", True)]
        at transform:
            zoom 0.7

screen key_N():
    imagebutton:
        xalign 0.65
        yalign 0.85
        idle "Objekte/Cockpit/key_N.png"
        action [Notify("Taste gefunden"), Hide("key_N"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, key_N), SetVariable("key_N_state", True)]
        at transform:
            zoom 0.7

screen key_U():
    imagebutton:
        xalign 0.85
        yalign 0.62
        idle "Objekte/Cockpit/key_U.png"
        action [Notify("Taste gefunden"), Hide("key_U"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, key_U), SetVariable("key_U_state", True)]
        at transform:
            zoom 0.7

screen key_X():
    imagebutton:
        xalign 0.27
        yalign 0.53
        idle "Objekte/Cockpit/key_X.png"
        action [Notify("Taste gefunden"), Hide("key_X"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, key_X), SetVariable("key_X_state", True)]
        at transform:
            zoom 0.7

screen key_W1():
    imagebutton:
        xalign 0.8
        yalign 0.98
        idle "Objekte/Cockpit/key_W.png"
        action [Notify("Taste gefunden"), Hide("key_W1"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, key_W1), SetVariable("key_W1_state", True)]
        at transform:
            zoom 0.7

screen key_D():
    imagebutton:
        xalign 0.4
        yalign 0.88
        idle "Objekte/Cockpit/key_D.png"
        action [Notify("Taste gefunden"), Hide("key_D"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, key_D), SetVariable("key_D_state", True)]
        at transform:
            zoom 0.7

screen key_O():
    imagebutton:
        xalign 0.5
        yalign 0.7
        idle "Objekte/Cockpit/key_O.png"
        action [Notify("Taste gefunden"), Hide("key_O"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, key_O), SetVariable("key_O_state", True)]
        at transform:
            zoom 0.7

screen key_W2():
    imagebutton:
        xalign 0.81
        yalign 0.58
        idle "Objekte/Cockpit/key_W.png"
        action [Notify("Taste gefunden"), Hide("key_W2"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, key_W2), SetVariable("key_W2_state", True)]
        at transform:
            zoom 0.7

screen key_S():
    imagebutton:
        xalign 0.7
        yalign 0.7
        idle "Objekte/Cockpit/key_S.png"
        action [Notify("Taste gefunden"), Hide("key_S"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, key_S), SetVariable("key_S_state", True)]
        at transform:
            zoom 0.7

screen key_P():
    imagebutton:
        xalign 0.69
        yalign 0.71
        idle "Objekte/Cockpit/key_P.png"
        action [Notify("Taste gefunden"), Hide("key_P"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, key_P), SetVariable("key_P_state", True)]
        at transform:
            zoom 0.7

screen key_E():
    imagebutton:
        xalign 0.3
        yalign 0.8
        idle "Objekte/Cockpit/key_E.png"
        action [Notify("Taste gefunden"), Hide("key_E"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, key_E), SetVariable("key_E_state", True)]
        at transform:
            zoom 0.7

screen key_R():
    imagebutton:
        xalign 0.33
        yalign 0.85
        idle "Objekte/Cockpit/key_R.png"
        action [Notify("Taste gefunden"), Hide("key_R"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, key_R), SetVariable("key_R_state", True)]
        at transform:
            zoom 0.7

screen Mikrofon():
    imagebutton:
        xalign 0.33
        yalign 0.85
        idle "Objekte/Cockpit/mic.png"
        action [Notify("Mikrofon gefunden"), Hide("Mikrofon"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, micro), SetVariable("micro_state", False)]
        at transform:
            zoom 0.7

screen GPS():
    imagebutton:
        xalign 0.2
        yalign 0.55
        idle "Objekte/Cockpit/gps.png"
        action [Notify("GPS gefunden"), Hide("GPS"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, gpsModule), SetVariable("gps_state", False)]
        at transform:
            zoom 0.7

screen Speaker():
    imagebutton:
        xalign 0.31
        yalign 0.7
        idle "Objekte/Cockpit/speaker.png"
        action [Notify("Lautsprecher gefunden"), Hide("Speaker"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, speaker), SetVariable("speaker_state", False)]

screen Kamera():
    imagebutton:
        xalign 0.85
        yalign 0.6
        idle "Objekte/Cockpit/cam.png"
        action [Notify("Kamera gefunden"), Hide("Kamera"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, camera), SetVariable("camera_state", False)]

screen WLAN():
    imagebutton:
        xalign 0.91
        yalign 0.66
        idle "Objekte/Cockpit/wlanmodul.png"
        action [Notify("WLAN-Modul gefunden"), Hide("WLAN"), Play("sound", "audio/item_found.mp3"), AddToSet(inventory, wlanModule), SetVariable("wifi_state", False)]

screen MikrofonPlaced():
    imagebutton:
        xalign 0.2
        yalign 0.58
        idle "Objekte/Cockpit/mic.png"
        action []
        at transform:
            zoom 0.7

screen GPSPlaced():
    imagebutton:
        xalign 0.2
        yalign 0.55
        idle "Objekte/Cockpit/gps.png"
        action []
        at transform:
            zoom 0.7

screen SpeakerPlaced():
    imagebutton:
        xalign 0.18
        yalign 0.57
        idle "Objekte/Cockpit/speaker.png"
        action []

screen KameraPlaced():
    imagebutton:
        xalign 0.27
        yalign 0.52
        idle "Objekte/Cockpit/cam.png"
        action []

screen WLANPlaced():
    imagebutton:
        xalign 0.2
        yalign 0.52
        idle "Objekte/Cockpit/wlanmodul.png"
        action []

screen lockerDoorPinpad():
    imagebutton:
        xalign 0.732
        yalign 0.497
        idle "Objekte/Cockpit/lockerDoorPinpad.png"
        hover "Objekte/Cockpit/lockerDoorPinpad_hover.png"
        action Call("lockerDoorPinpadClicked")

screen lockerDoorOpen():
    imagebutton:
        xalign 0.715
        yalign 0.5
        idle "Objekte/Cockpit/lockerDoorOpen.png"
        hover "Objekte/Cockpit/lockerDoorOpen_hover.png"
        action [Notify("Monitore gefunden"), Hide("lockerDoorOpen"), Play("sound", "audio/item_found.mp3"), Call("MonitorsFound")]

screen lockerDoorOpenEmpty():
    imagebutton:
        xalign 0.715
        yalign 0.5
        idle "Objekte/Cockpit/lockerDoorOpenEmpty.png"
        hover "Objekte/Cockpit/lockerDoorOpenEmpty.png"
        action [Hide("lockerDoorOpenEmpty"), Call("MonitorsFound")]

screen monitorBroken():
    imagebutton:
        xalign 0.045
        yalign 0.48
        idle "Objekte/Cockpit/monitorBroken.png"
        action Call("brokenMonitorClicked")

screen monitorSW():
    imagebutton:
        xalign 0.045
        yalign 0.5
        idle "Objekte/Cockpit/monitorWhite.png"
        action [Jump("ComputerSzene")]

screen monitorColor():
    imagebutton:
        xalign 0.045
        yalign 0.5
        idle "Objekte/Cockpit/monitorBlack.png"
        action [Jump("ComputerSzene")]

screen keyboardBroken():
    imagebutton:
        xalign 0.495
        yalign 0.9
        idle "Objekte/Cockpit/keyboardBroken.png"
        hover "Objekte/Cockpit/keyboardBroken_hover.png"
        action Call("keyboardBrokenClicked")

screen keyboardNormal():
    imagebutton:
        xalign 0.495
        yalign 0.9
        idle "Objekte/Cockpit/keyboard.png"
        hover "Objekte/Cockpit/keyboard_hover.png"
        action Call("keyboardClicked")

screen keyboardDummy():
    imagebutton:
        xalign 0.495
        yalign 0.9
        idle "Objekte/Cockpit/keyboard.png"
        action []

screen keyboardFunk():
    imagebutton:
        xalign 0.495
        yalign 0.9
        idle "Objekte/Cockpit/keyboard.png"
        hover "Objekte/Cockpit/keyboard_hover.png"
        action [Call("KeyboardFunkClicked"), Hide("keyboardFunk"), Show("keyboardDummy")]

screen App_Settings():
    imagebutton:
        xalign 0.21
        yalign 0.05
        idle "Objekte/Cockpit/App_Settings.png"
        action [Call("EditSettings")]

screen App_Duesenstart():
    imagebutton:
        xalign 0.21
        yalign 0.05
        idle "Objekte/Cockpit/App_Settings.png"
        action [Call("chapter6_Duesenstart")]

screen App_Firefox():
    imagebutton:
        xalign 0.27
        yalign 0.05
        idle "Objekte/Cockpit/App_Firefox.png"
        action [Call("OpenFirefox")]

screen App_Edge():
    imagebutton:
        xalign 0.33
        yalign 0.05
        idle "Objekte/Cockpit/App_Edge.png"
        action [Call("OpenEdge")]

screen App_Chrome():
    imagebutton:
        xalign 0.39
        yalign 0.05
        idle "Objekte/Cockpit/App_Chrome.png"
        action [Call("OpenChrome")]

screen App_Funk():
    imagebutton:
        xalign 0.51
        yalign 0.05
        idle "Objekte/Cockpit/App_Funk.png"
        action [Call("FunkApp")]

#screen App_Abwurf_Settings():
#    imagebutton:
#        xalign 0.21
#        yalign 0.05
#        idle "Objekte/Cockpit/App_Settings.png"
#        action [Call("OpenAbwurfSettings")]

screen App_Abwurf():
    imagebutton:
        xalign 0.45
        yalign 0.05
        idle "Objekte/Cockpit/App_Abwurf.png"
        action [Call("OpenAbwurfSettings")]

screen BackButton():
    imagebutton:
        xalign 0.95
        yalign 0.91
        idle "Objekte/Cockpit/BackButton.png"
        hover "Objekte/Cockpit/BackButton_Hover.png"
        action [Hide("BackButton"), Jump("HideObjectsPC")]

screen BackButtonDummy():
    imagebutton:
        xalign 0.95
        yalign 0.91
        idle "Objekte/Cockpit/BackButton.png"
        action []

screen choose_OS:
    label "Betriebssystem wählen" xalign 0.5 yalign 0.2 text_color "#fff" text_size 40

screen os_title:
    label str(os_title) xalign 0.515 yalign 0.2 text_color "#fff" text_size 40

screen os_title_black:
    label str(os_title) xalign 0.515 yalign 0.2 text_color "#000" text_size 40

screen App_Abwurf_Settings_Title:
    label "Einstellungen für automatischen Abwurf" xalign 0.5 yalign 0.05 text_color "#fff" text_size 40
    label "__________________________________________" xalign 0.5 yalign 0.1 text_color "#fff" text_size 40

screen App_Abwurf_Title:
    label "Aktivierung des automatischen Abwurfs" xalign 0.5 yalign 0.05 text_color "#fff" text_size 40
    label "__________________________________________" xalign 0.5 yalign 0.1 text_color "#fff" text_size 40
    label "Dazu musst du das Spiegelrätsel lösen" xalign 0.5 yalign 0.15 text_color "#fff" text_size 40

screen App_Funk_Title:
    label "Kommunikationsapp" xalign 0.5 yalign 0.05 text_color "#fff" text_size 40
    label "__________________________________________" xalign 0.5 yalign 0.1 text_color "#fff" text_size 40

screen Check_Encryption_Title:
    label "Funkgerät" xalign 0.5 yalign 0.05 text_color "#fff" text_size 40
    label "__________________________________________" xalign 0.5 yalign 0.1 text_color "#fff" text_size 40
    label "Verschlüsselung" xalign 0.5 yalign 0.2 text_color "#fff" text_size 40

screen choose_mic:
    label "Mikrofonzugriff" xalign 0.5 yalign 0.2 text_color "#fff" text_size 40

screen choose_cam:
    label "Kamerazugriff" xalign 0.5 yalign 0.2 text_color "#fff" text_size 40

screen choose_wlan:
    label "WLAN" xalign 0.5 yalign 0.2 text_color "#fff" text_size 40

screen choose_gps:
    label "Standortzugriff" xalign 0.5 yalign 0.2 text_color "#fff" text_size 40

screen choose_zeitpunkt:
    label "Abwurfzeitpunkt" xalign 0.5 yalign 0.135 text_color "#fff" text_size 40

screen Sicherheitsprotokoll:
    label "Sicherheitsprotokoll" xalign 0.5 yalign 0.05 text_color "#fff" text_size 40
    label "__________________________________________" xalign 0.5 yalign 0.1 text_color "#fff" text_size 40
    label "[title]" xalign 0.5 yalign 0.15 text_color "#fff" text_size 40

screen countdown:
    timer 1 repeat True action [If(set_time > 0, true=[SetVariable('set_time', set_time - 1)], false=[Hide('countdown'), Jump(timer_jump)]),
    #Zeige 20s Earth Sequenz an
    If((set_time > 0 and CP4_EarthImage20_state), true=[Show("Earth"+str(set_time))], false=[SetVariable('CP4_EarthImage20_state', False)]),
    #Zeige 60s Earth Sequenz an
    If((set_time > 0 and CP4_EarthImage60_state and set_time % 3 == 0), true=[Show("Earth"+str(set_time/3))], false=[])]
    label "[countdown_title]" xalign 0.5 yalign 0.18 text_color "#fff" text_size 40
    label "noch " + str(set_time) + " s" xalign 0.5 yalign 0.23
