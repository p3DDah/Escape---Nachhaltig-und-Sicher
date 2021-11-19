#diese Datei dient dazu, um den aktuellen Stand des Spielers einsehen zu können, sodass ein
#paralleler Spielbetrieb mögich ist

init python:
    #Maschinenraum
        #deaktiviere ImageButtons
        ImageButtonActivate_state = True

        #Zusatzaufgabe
        EX_Tresor_state = False

        #Chapter 2
        CP2_browserChoice_state = False

        CP2_browserConfig_state = False

        CP2_browserFrage1_state = False
        CP2_browserFrage2_state = False
        CP2_browserFrage3_state = False
        CP2_browserFrage4_state = False

        #Chapter 3
        CP3_Bauplan_state = False

        CP3_CookieChoice_state1 = False
        CP3_CookieChoice_state2 = False

        CP3_Systemcheck_state = False

        #Chapter 4
        CP4_CalcPass_state = False
        CP4_CalcPassText_state = True
        CP4_CalcPassSound_state = True
        CP4_CalcPassVideo_state = True

        #Chapter 5
        CP5_Reparatur_state = False

        #chapter 6
        CP6_UnlockDoor_state = 0
