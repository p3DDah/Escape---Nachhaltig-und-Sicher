#Ausgangszustand und Überprüfung, welche Objekte noch aktiv sind bzw angezeigt werden sollen
#zeigt das komplette Cockpit an
label Cockpit_Standard:
    $ InventarCheck_state = True
    $ HinweisCheck_state = True
    $ current_label = ""
    $ current_hinweis = ""
    scene cockpit
    $ renpy.notify("Cockpit")
    #überprüft, ob man das Spiel gerade erst gestartet hat
    if not FirstTime_state:
        $ HideScreen("cockpitDoorPinpad")
        $ HideScreen("gotoCockpitDoor")
        $ FirstTime_state = True

    #überprüfe States von Variablen
    #was soll angezeigt werden
    if not key_L_state:
        $ ShowScreen("key_L")
    if not key_I_state:
        $ ShowScreen("key_I")
    if not key_N_state:
        $ ShowScreen("key_N")
    if not key_U_state:
        $ ShowScreen("key_U")
    if not key_X_state:
        $ ShowScreen("key_X")
    if not key_W1_state:
        $ ShowScreen("key_W1")
    if not key_D_state:
        $ ShowScreen("key_D")
    if not key_O_state:
        $ ShowScreen("key_O")
    if not key_W2_state:
        $ ShowScreen("key_W2")
    if not key_S_state:
        $ ShowScreen("key_S")
    if not key_P_state:
        $ ShowScreen("key_P")
    if not key_E_state:
        $ ShowScreen("key_E")
    if not key_R_state:
        $ ShowScreen("key_R")

    #Schrank ist offen
    if Lockerdoor_state:
        #Monitore wurden entnommen
        if CP2_LockerdoorEmpty_state:
            $ ShowScreen("lockerDoorOpenEmpty")
        else:
            $ ShowScreen("lockerDoorOpen")
    else:
        $ ShowScreen("lockerDoorPinpad") #enables label lockerDoorPinpadClicked

    #überprüft, welcher Monitor ausgewählt wurde
    if MonitorColor_state or MonitorBW_state:
        if MonitorColor_state:
            $ ShowScreen("monitorColor")
        else:
            $ ShowScreen("monitorSW")
    else:
        $ ShowScreen("monitorBroken")

    #überprüft, ob Mikrofon schon angezeigt werden darf
    if micro_state:
        $ ShowScreen("Mikrofon")
    if gps_state:
        $ ShowScreen("GPS")
    if speaker_state:
        $ ShowScreen("Speaker")
    if camera_state:
        $ ShowScreen("Kamera")
    if wifi_state:
        $ ShowScreen("WLAN")

    $ ShowScreen("Box")
    $ ShowScreen("Roboter")
    $ ShowScreen("Schrank")
    $ ShowScreen("Truhe")
    $ ShowScreen("Truhe2")
    $ ShowScreen("Truhe3")
    $ ShowScreen("Truhe4")
    $ ShowScreen("Truhe5")

    #startet einmal Turbulenzen Label, falls es noch nicht besucht worden ist
    if CP5_continue_state:
        jump Turbulenzen #CP5_FunkReparatur.cpy
    $ renpy.pause(hard=True)

#verstecke alle Items, die nicht beim PC angezeigt werden sollen
label HideObejects:
    $ HideScreen("key_L")
    $ HideScreen("key_I")
    $ HideScreen("key_N")
    $ HideScreen("key_U")
    $ HideScreen("key_X")
    $ HideScreen("key_W1")
    $ HideScreen("key_D")
    $ HideScreen("key_O")
    $ HideScreen("key_W2")
    $ HideScreen("key_S")
    $ HideScreen("key_P")
    $ HideScreen("key_E")
    $ HideScreen("key_R")
    $ HideScreen("lockerDoorOpenEmpty")
    $ HideScreen("lockerDoorOpen")
    $ HideScreen("lockerDoorPinpad") #enables label lockerDoorPinpadClicked
    $ HideScreen("monitorColor")
    $ HideScreen("monitorSW")
    $ HideScreen("monitorBroken")
    $ HideScreen("Mikrofon")
    $ HideScreen("GPS")
    $ HideScreen("Speaker")
    $ HideScreen("Kamera")
    $ HideScreen("WLAN")
    $ HideScreen("Box")
    $ HideScreen("Roboter")
    $ HideScreen("Schrank")
    $ HideScreen("Truhe")
    $ HideScreen("Truhe2")
    $ HideScreen("Truhe3")
    $ HideScreen("Truhe4")
    $ HideScreen("Truhe5")

    return

#verstecke alle Objekte vom PC, die nicht beim Cockpit angezeigt werden sollen
label HideObjectsPC:
    $ HideScreen("keyboardBroken")
    $ HideScreen("keyboardFunk")
    $ HideScreen("keyboardDummy")
    $ HideScreen("keyboardNormal")
    $ os_title = ""
    $ HideScreen("choose_OS")
    $ HideScreen("App_Settings")
    $ HideScreen("App_Firefox")
    $ HideScreen("App_Edge")
    $ HideScreen("App_Chrome")
    $ HideScreen("App_Abwurf")
    $ HideScreen("App_Funk")
    $ HideScreen("App_Duesenstart")
    $ HideScreen("BackButton")
    $ HideScreen("BackButtonDummy")
    call Cockpit_Standard from _call_Cockpit_Standard
    return

    #if Keyboard_state:
    #    $ ShowScreen("keyboardNormal")
    #else:
    #    $ ShowScreen("keyboardBroken")
