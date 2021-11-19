#diese Datei dient dazu, um den aktuellen Stand des Spielers einsehen zu können, sodass ein
#paralleler Spielbetrieb möglich ist

init python:
    #Cockpit
        password = 0
        fail = False

        #Extra Aufgaben
        EX_Box_state = False
        EX_Truhe_state = False

        #Random Generator
        import time
        year, month, day, hour, minute, second, dow, doy, dst = time.localtime()
        renpy.random.Random(seed=dow)

        #sperre Inventar/Hinweise innerhalb einer Aufgabe
        InventarCheck_state = False
        HinweisCheck_state = False

        #Hinweise
        HinweiseAnzahl_state = 3
        Hinweis1_state = False
        Hinweis2_state = False
        Hinweis3_state = False
        current_label = ""
        current_hinweis = ""
        Hinweis1Label_state = ""
        Hinweis2Label_state = ""
        Hinweis3Label_state = ""

        #Variable zum Sperren
        mussWarten = False

        #Freiliegende Objekte
        key_L_state = False
        key_I_state = False
        key_N_state = False
        key_U_state = False
        key_X_state = False
        key_W1_state = False
        key_D_state = False
        key_O_state = False
        key_W2_state = False
        key_S_state = False
        key_P_state = False
        key_E_state = False
        key_R_state = False

        micro_state = False
        gps_state = False
        speaker_state = False
        camera_state = False
        wifi_state = False

        #stehende Objekte
        MonitorColor_state = False
        MonitorBW_state = False

        Lockerdoor_state = False

        Keyboard_state = False

        #Sonstiges
        FirstTime_state = False

        #Chapter 2
        CP2_LockerDoor_state = False
        CP2_LockerdoorEmpty_state = False

        CP2_tmpD_state = True #um zu merken, welche Taste man gedrückt hatte
        CP2_tmpE_state = True
        CP2_tmpI_state = True
        CP2_tmpL_state = True
        CP2_tmpN_state = True
        CP2_tmpO_state = True
        CP2_tmpP_state = True
        CP2_tmpR_state = True
        CP2_tmpS_state = True
        CP2_tmpU_state = True
        CP2_tmpW1_state = True
        CP2_tmpW2_state = True
        CP2_tmpX_state = True
        CP2_tmpText = ""

        CP2_KeyboardBroken_state = False

        CP2_OsWahl_state = False
        CP2_OpenOs_state = False
        CP2_OS_state = False
        CP2_Computer_state = False
        isWindows = False
        isLinux = False

        CP2_Verbindung_state = False

        CP2_EditedSettings_state = False

        #Chapter 3
        CP3_BrowserWahl_state = False
        CP3_Browser = ""

        CP3_Kursberechnung24_state = False
        CP3_Kreuz_state = False
        CP3_Cipher_state = False

        #Chapter 4
        CP4_AbwurfPartI_state = False
        CP4_EarthImage20_state = False
        CP4_EarthImage60_state = False
        tmp_stati = 0.2

        CP4_AbwurfPartII_state = False
        CP4_Spiegel_state = False

        #Chapter 5

        CP5_continue_state = False
        CP5_FunkAppNo_state = False #kein Empfang
        CP5_VarSelect_state = False

        CP5_UsedMic = False
        CP5_UsedCam = False
        CP5_UsedGPS = False
        CP5_UsedSpeaker = False
        CP5_UsedWLAN = False

        CP5_KommTest_state = False
        CP5_StandortTest_state = False

        CP5_FunkAppYes_state = False #wieder Empfang

        #chapter 6, gilt auch für Maschinenraum
        Frage1_state = True
        Frage2_state = True
        Frage3_state = True
        Frage4_state = True
        Frage5_state = True
        Frage6_state = True
        Frage7_state = True
        Frage8_state = True
        Frage9_state = True
        Frage10_state = True
