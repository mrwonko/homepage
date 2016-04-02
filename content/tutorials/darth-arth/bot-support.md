title: Bot Support
author: Darth Arth (Artur L.)
date: 2004-01-01
modified: 2016-04-02
category: multiplayer
type: tutorials/darth-arth
tags: Bots
slug: bot-support


Das mit dem Bot Support ist eigentlich ganz einfach:

1.  Man braucht eine Verknüpfung oder eine Batchdatei (`.bat`) zu der jk2mp.exe, die ungefähr so ausieht:
    
        ">hier dein jk2-Ordner<\GameData\jk2mp.exe" +devmap >mapname< +set bot_wp_edit 1
    
    `>mapname<` ist hier der Name deiner Map.
    
2.  Mit der erstellten BAT-Datei / Verknüpfung JK2-Multiplayer starten
    
3.  Nachdem deine Map geladen wurde, Konsole aufmachen und folgendes eingeben:
    
        /bot_wp_save
    
4.  Dann eine Taste mit dem Befehl zum setzten von "Waypoints" (Wegpunkten) binden, z.B. so:
    
        /bind i "bot_wp_add"
    
    Damit wurde die Taste <kbd>I</kbd> mit dem Befehl `bot_wp_add` belegt. Das heißt, wenn jetzt diese Taste gedrückt wird, entsteht an der Stelle, wo sich der Player gerade befindet, ein "Waypoint".
    
5.  Jetzt durch die Gegend rennen und alle paar Schritte diese Taste drücken (in meinem Beispiel <kbd>I</kbd>). Es werden die Zahlen für die einzelnen "waypoints" angezeigt.
    
    Damit muss man für die Bots einer Art Pfad errichten.
    
    Gut wäre, wenn sich dieser zum Schluss schließt, dass heißt, der letzte Punkt befindet sich in der Nähe des ersten.
    
    Wenn Ihr einen Punkt löschen müsst, dann folgendes eingeben:
    
        /bot_wp_rem
    
    oder
    
        /Bot_wp_rem >point-Nr.<
    
6.  Wenn alle Waypoints gesetzt wurden, einfach noch mal dies eingeben:
    
        /bot_wp_save
        
    Damit wird der erstellte "Waypoints"-Pfad gespeichert.
    
7.  JKII beenden und in dem Ordner `base/botroutes` nach der Bot-Waypoint datei suchen. Die heißt normalerweise `>mapname<.wnt`, wobei `>mapname<` der Name deiner Map ist.

So, das war's eigentlich...

<div class="alert alert-info"><strong>Anmerkung</strong>: Es gibt natürlich viele weiteren Befehle und Optionen für die Erstellung der "Botroutes", diese sollten jedoch nur von erfahrenen Mappern eingesetzt werden. Beschrieben sind diese im Ravens Botsupport-Tutorial aus den Editing Tools.</div>
