title: NPC's als Schauspielen in Cutscenes
author: Darth Arth (Artur L.)
date: 2004-01-01
modified: 2015-04-14
category: scripts
type: tutorials/darth-arth
tags: Entities, NPCs, auto-generated
slug: script-cutscenes-npcs

**>>
Mapping Academy - Tutorials <<**

 

(c)
2003 [www.darth-arth.de](http://www.darth-arth.de)

----

**NPC's - als Schauspieler**

**[u]VORAUSSETZUNGEN[/u]:**

>> Kamera
Modus ( [Tutorial](cutscenes/cam1/camera1.htm) ) <<

>> Die erste
Kamerafahrt ( [Tutorial](cutscenes/cam2/camera2.htm) ) <<

>>
Konfiguration BehavEd ( [Tutorial](behaved/behaved.htm) ) <<

----

**Der
Filmset****:**

 

Zuerst
benötigen wir einen Raum, wie z.B.. den aus dem Tutorial "[Meine erster
Raum](mapping/firstroom/firstroom.htm)".

Dort
setzten wir ein "info_player_start"
rein, falls noch nicht vorhanden. 

Jetzt
"N" drücken um die Entity Eigenschaften anzuschauen und folgendes
eingeben:

 

KEY:
target

VALUE:
startwelle0

 

Damit
verbinden wir den Startpunkt mit einem "target_relay",
der dann automatisch unsere "Reborn-Schauspieler" erscheinen lässt.

 

![image]({filename}npc/cutscenes/Image2.jpg)

 

Jetzt
erstellen wir den "target_relay"
(rechte Maustaste in der 2D-Ansincht > target > target_relay ).

Dann
gehen wir in die Eigenschaften von diesem Entity ("N" Taste) und geben
folgendes ein:

 

KEY:
target

VALUE:
welle0

 

target
(Ziel) legt fest, was angestartet werden soll. 

In
unserem Fall sind es die Reborns, die alle später den targetnamen "welle0"
erhalten.

 

KEY:
targetname

VALUE:
startwelle0

 

targetname
(wie heisse ich, falls mich jemand als target
benutzten will).

Hier
wird die Verbindung zu dem "info_player_start"
hergestellt ( info_player_start/target
> target_relay/targetname)

 

![image]({filename}npc/cutscenes/Image4.jpg)

 

----

**Die
Schauspieler****:**

 

So...,
jetzt erstellen wir unsere 3 Schauspieler. 

Wir
setzen in unseren Raum, drei "NPC_spawner"
rein.

 

In
die Entity-Eigenschaften muss jeweils folgendes eingetragen werden:

 

KEY:
targetname

VALUE:
welle0

 

KEY:
NPC_type

VALUE:
reborn

 

KEY:
spawnscript

VALUE:
go1               
(go2
für den zweiten, go3
für den dritten NPC )

 

Spawnscript
legt fest, welches Script
abgearbeitet werden soll, bei dem Erscheinen eines NPC's.

Deswegen
ist es wichtig, dass diese NPC's nicht mit der Map geladen werden, 

sondern
über den "targetnamen"
aufgerufen werden (mit trigger
oder target_relay,
usw.).

 

 

![image]({filename}npc/cutscenes/Image12.jpg)

 

**[u]ACHTUNG:[/u]**

 

Es
ist wichtig, dass die NPC's, die als Schauspieler für Cutscenes benutzt werden,
in den

"CINEMATIC"
Modus gesetzt werden, ansonsten gehorchen sie den Animationsbefehlen nicht!

 

Da,
der eigentliche Player, im Kamera-Modus nicht sichtbar ist, sollte man einen
Fake hinstellen.

Wir
machen es so, dass wir in der nähe des "Info_player_start"
noch einen "NPC_Kyle"
setzen.

 

![image]({filename}npc/cutscenes/Image14.jpg)

----

 

**Die
Kameras:**

 

Jetzt
"montieren" wir unsere Kameras in die Scene. 

Wir
plazieren 3 "ref_tag"'s
die jeweils folgende Eigenschaften besitzen:

 

Kamera
1:

![image]({filename}npc/cutscenes/Image6.jpg)

 

Kamera
2:

![image]({filename}npc/cutscenes/Image8.jpg)

 

Kamera
3:

![image]({filename}npc/cutscenes/Image10.jpg)

 

Die
Richtung und den Winkel, in die eine Kamera schauen soll, definieren wir mit
jeweils einem endsprechenden

"info_not_null"
, wie in dem "Erste Kamera-Fahrt" - Tutorial beschrieben.

 

Die
Info_notnull
Entities, heißen dann jeweils "cam1point",
"cam2point",
"cam3point"

 

![image]({filename}npc/cutscenes/Image18.jpg)

 

----

 

**Die
Wegpunkte****:**

 

Damit
unsere Schauspieler wissen, wo sie entlang laufen sollen, müssen wir sogenannte
"waypoints"
(Wegpunkte) setzen.

 

Rechte
Maustaste im 2D-Fenster > waypoint
> waypoint_navgoal

 

![image]({filename}npc/cutscenes/Image16.jpg)

 

Wir
setzten für jeden Reborn jeweils 2 Wegpunkte die entsprechend heißen (targetname):

 

Reborn1:

Wegpunkt1:

 

KEY:targetname

VALUE:
p1_1

 

Wegpunkt2:

 

KEY:targetname

VALUE:
p1_2

=============================

 

Reborn2:

Wegpunkt1:

 

KEY:targetname

VALUE:
p2_1

 

Wegpunkt2:

 

KEY:targetname

VALUE:
p2_2

=============================

 

Reborn3:

Wegpunkt1:

 

KEY:targetname

VALUE:
p3_1

 

Wegpunkt2:

 

KEY:targetname

VALUE:
p3_2

=============================

 

Wenn
alle Entities gesetzt sind, sollte es ungefähr so aussehen wie auf dem Bild
unten.

Wenn
alles stimmt , kann die Map gespeichert werden, z.B. unter dem Namen "cutscene_test.map"

Da
es sich hier um eine Test-Map handelt, kann diese ruhig mit Fastvis/Nolight
kompiliert werden.

 

![image]({filename}npc/cutscenes/Image20.jpg)

 

----

**Die
Anweisungen****:**

 

Jetzt
kommt der schwierigster Teil der Arbeit, die Ausarbeitung der Scripts.

Jeder
unserer 3 Schauspieler benötigt einen eigenen Script, da sie unterschiedliche Wege
gehen.

Fangen
wir mit dem ersten mal an.

 

Erstellt
folgendes Script:

 

//Generated by BehavEd

rem ( "comment" );

camera ( /*@CAMERA_COMMANDS*/ ENABLE );

wait ( 1000.000 );

camera ( /*@CAMERA_COMMANDS*/ MOVE, $tag( "cam1", ORIGIN)$, 0 );

camera ( /*@CAMERA_COMMANDS*/ PAN, $tag( "cam1", ANGLES)$, < 0.000 0.000 0.000 >, 0 );

camera ( /*@CAMERA_COMMANDS*/ ZOOM, 90.000, 0 );

set ( /*@SET_TYPES*/ "SET_WALKING", /*@BOOL_TYPES*/
"true" );

set ( /*@SET_TYPES*/ "SET_WALKSPEED",
 80 );

set ( /*@SET_TYPES*/ "SET_NAVGOAL",
"p1_1" );

wait ( 4000.000 );

set ( /*@SET_TYPES*/ "SET_NAVGOAL",
"p1_2" );

wait ( 4000.000 );

camera ( /*@CAMERA_COMMANDS*/ MOVE, $tag( "cam2", ORIGIN)$, 2000 );

camera ( /*@CAMERA_COMMANDS*/ PAN, $tag( "cam2", ANGLES)$, < 0.000 0.000 0.000 >, 2000 );

wait ( 7000.000 );

camera ( /*@CAMERA_COMMANDS*/ MOVE, $tag( "cam3", ORIGIN)$, 3000 );

camera ( /*@CAMERA_COMMANDS*/ PAN, $tag( "cam3", ANGLES)$, < 0.000 0.000 0.000 >, 3000 );

wait ( 4000.000 );

camera ( /*@CAMERA_COMMANDS*/ ZOOM, 50.000, 2000 );

wait ( 5000.000 );

camera ( /*@CAMERA_COMMANDS*/ DISABLE );

 

Mit
dem SET_WALKING
= true, zwingen wir den NPC zu gehen und mit "WALKSPEED"
kann man die Gehgeschwindigkeit festlegen.

 

Mit
dem Befehl "SET_NAVGOAL"
setzten wir fest, entlang welcher Punkte, der NPC laufen soll.

Wichtig
ist, dass man einen WAIT
- Befehl zwischen den einzelnen Gehpunkten setzt, so dass dem NPC genug Zeit
bleibt von einem Punkt zum anderen zu gehen bevor er den nächsten Befehl
erhält.

Ansonsten
kann passieren, dass die Ausführung des Scriptes unterbrochen wird, der NPC
einfach stehen bleibt oder dumm durch die gegen hüpft.

 

Wir
nutzen dieses erste Script gleichzeitig dafür, die Kameras entsprechend zu
steuern. Man könnte zwar dafür ein eigenes Script erstellen, dann ist es
jedoch schwieriger, alles gut zu "timen"
(Zeitliche Abstimmung des Ablaufs).

Das
"Timing"
erfolgt durch richtig gesetzte "WAIT"
Befehle und gehört zu den schwierigsten Aufgaben des "Regissers"
(Scripters)

Das
Timing in diesem Script ist genau auf die, hier befindliche "Beispiel-Map"
abgestimmt. 

Falls
ihr das Script mit eure eigene Map ausprobieren wollt, müssen die WAIT-Befehle
eventuell noch angepasst werden.

 

Jetzt
speichern wir dieses Script in den "base/scripts"
- Ordner unter dem Namen "go1.txt". 

Dann
sollte dieses Script mit dem BehavEd-Editor kompiliert werden.

 

![image]({filename}../buttons/aliendf4.gif)

 

Für
den zweiten Reborn erstellen wir folgendes Script:

 

//Generated by BehavEd

rem ( "comment" );

wait (
10000.000 );

set ( /*@SET_TYPES*/ "SET_WALKING", /*@BOOL_TYPES*/ "true" );

set ( /*@SET_TYPES*/ "SET_WALKSPEED",  80 );

set ( /*@SET_TYPES*/ "SET_NAVGOAL", "p2_1" );

wait ( 5000.000 );

set ( /*@SET_TYPES*/ "SET_NAVGOAL", "p2_2" );

Hier
benötigen wir keine Kamera-Steuerbefehle, da dies schon von dem ersten Script
erledigt wird.

Mit
diesem Script erteilen wir dem zweiten NPC lediglich die Befehle zum Durchlaufen
der Wegpunkte.

Wichtig
hier, ist der erste "WAIT"-Befehl,
welcher den NPC zwingt zu warten, bis der erste Schauspieler seinen Weg gelaufen
ist und die Kamera, die richtige Position erricht hat.

 

Jetzt
speichern wir dieses Script in den "base/scripts"
- Ordner unter dem Namen "go2.txt". 

Dann
sollte dieses Script mit dem BehavEd-Editor kompiliert werden.

 

![image]({filename}../buttons/aliendf4.gif)

 

Für
unseren dritten Schauspieler erstellen wir folgendes Script:

 

//Generated by BehavEd

rem ( "comment" );

wait (
15000.000 );

set ( /*@SET_TYPES*/ "SET_WALKING", /*@BOOL_TYPES*/ "true" );

set ( /*@SET_TYPES*/ "SET_WALKSPEED",  80 );

set ( /*@SET_TYPES*/ "SET_NAVGOAL", "p3_1" );

wait ( 5000.000 );

set ( /*@SET_TYPES*/ "SET_NAVGOAL", "p3_2" );

 

Dieses
Script unterscheidet sich nur geringfügig von dem zweiten. 

Der
NPC läuft über andere Wegpunkte und muss ein wenig länger warten, da er als
letzter dran ist :)

 

Dieses
Script speichern wir in den "base/scripts"
- Ordner unter dem Namen "go3.txt". 

und
kompillieren es, wie die anderen mit dem BehavEd-Editor.

 

----

**Die
Cutscene (Zwischensequenz) Testen****:**

 

Nach
dem die Map Fehlerfrei kompiliert wurde und alle 3 Scripte in dem base/scripts
- Ordner liegen und zu IBI
- Dateien kompiliert wurden, kann unsere Zwischensequenz getestet werden.

 

Starte
Jedi-Knight2 im SP Modus, öffne die Konsole, gebe ein

 

map
cutscene_test

 

und
genieße deine erste richtige Cutscene incl. Schauspieler ;)

 

Falls
die Kameras nicht ganz Synchron mit deinen Schauspielern laufen, müssen ev. die
WAIT-Befehle
noch angepasst werden.

Dies
ist jedoch, wie bereits erwähnt, das schwierigste und zeitaufwändigste beim
erstellen von Cutscenes ...

 

 

----

[u][DOWNLOAD
DER TUTORIAL MAP](downloads/cutscene_test.zip)[/u]

(
.map - Datei enthalten)

 

----

Alle
  Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet: 

©
  2000 - 2003 (Artur L.) [www.darth-arth.de](http://www.darth-arth.de)

Nur
  zur privaten Nutzung. Kopieren nicht gestattet. Darth-Arth.de ist ausdrücklich
  nicht für den Inhalt externer Seiten verantwortlich. Es gelten die
  angegebenen Nutzungsbedingungen.

 

