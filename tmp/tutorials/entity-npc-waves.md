title: NPC's - Angriffswellen
author: Darth Arth (Artur L.)
date: 2004-01-01
modified: 2015-04-14
category: scripts
type: tutorials/darth-arth
tags: Entities, NPCs, auto-generated
slug: entity-npc-waves

**>>
Mapping Academy - Tutorials <<**

 

(c)
2003 [www.darth-arth.de](http://www.darth-arth.de)

----

**NPC's - Angriffswellen**

**[u]VORAUSSETZUNG[/u][u]EN[/u]:**

>>
Installation JK2 Editing Tools I ( [Tutorial](radiant/jk2_etools1.htm)
)<<

>>
Installation JK2 Editing Tools 2 ( [Tutorial](radiant/jk2_etools2.htm)
)<<

>>
Installation GTK - Radiant ( [Tutorial](radiant/gtk_radiant.htm)
)<<

>> Mein Erster Raum ( [Tutorial](mapping/firstroom/firstroom.htm)
)<<

----

**[u]Vorbereitung:[/u]**

 

**NPC’s
in eine SP Map einfügen**

 

Um
NPC’s in eine SP-Map einzufügen gibt es 2 Möglichkeiten. Die erste Möglichkeit
ist, einen vordefinierten NPC-Namen aus dem Kontextmenu der rechten Maustaste
auszuwählen (rechte Maustaste im 2D-Fenster > NPC > NPC_name).

 

Um
selbsterstellte NPC’s in eine Map einzufügen benötigt man das Entity „NPC_spawner“
(rechte Maustaste im 2D-Fenster > NPC > NPC_spawner). Falls der
NPC_spawner in deiner NPC-Liste nicht verfügbar ist, hast du eine veraltete „sp_entities.def“
- Datei oder einen veralteten Editor. Empfohlen wird der GTKRadiant, ab der
Version ab 2.1.12.

 

Bei
älteren Versionen des GTKRadiant gibt es einen Bug in der NPC_Liste, bei
Bildschirmauflösungen bis 1024 x 768 Pixel, wird die NPC_Liste nicht komplett
dargestellt, so dass man bestimmte NPC’s nicht auswählen kann.

 

Lösung
1: den GTKRadiant ab der
Version 2.1.12 installieren

Lösung
2: Lösche aus der Datei „scripts/sp_entities.def„
alle NPC_Namen außer dem „NPC_spawner“. Du kannst dann alle NPC-Namen aus
der Liste in der „ext_data/npcs.cfg“ - Datei + deine eigenen NPC-Namen
benutzten (selbsterstellte NPC’s laut Tutorial).

 

Falls
in deiner sp_entities.def
- Datei, der NPC_spawner
nicht existiert, füge folgende Definition dort ein:

 

================
**8><** ===================================

 

/*QUAKED
NPC_spawner (1 0 0) (-16 -16 -24) (16 16 32) x x x x DROPTOFLOOR CINEMATIC
NOTSOLID STARTINSOLID SHY

 

CINEMATIC
- Will spawn with no default AI (BS_CINEMATIC)

NOTSOLID
- Starts not solid

STARTINSOLID
- Don't try to fix if spawn in solid

SHY
- Spawner is shy

 

targetname
- name this NPC goes by for targetting

target
- NPC will fire this when it spawns it's last NPC (should this be when the last
NPC it spawned dies?)

 

If
targeted, will only spawn a NPC when triggered

count
- how many NPCs to spawn (only if targetted) default = 1

 

NPC_type
- name of NPC (in NPCs.cfg) to spawn

 

NPC_targetname
- NPC's targetname AND script_targetname

NPC_target
- NPC's target to fire when killed

health
- starting health (default = 100)

playerTeam
- Who not to shoot! (default is TEAM_STARFLEET)

           
TEAM_FREE (none) = 0

           
TEAM_RED = 1

           
TEAM_BLUE = 2

           
TEAM_GOLD = 3

           
TEAM_GREEN = 4

           
TEAM_STARFLEET = 5

           
TEAM_BORG = 6

           
TEAM_SCAVENGERS = 7

           
TEAM_STASIS = 8

           
TEAM_NPCS = 9

           
TEAM_HARVESTER, = 10

           
TEAM_FORGE = 11

enemyTeam
- Who to shoot (all but own if not set)

 

spawnscript
- default script to run once spawned (none by default)

usescript
- default script to run when used (none by default)

awakescript
- default script to run once awoken (none by default)

angerscript
- default script to run once angered (none by default)

painscript
- default script to run when hit (none by default)

fleescript
- default script to run when hit and below 50% health (none by default)

deathscript
- default script to run when killed (none by default)

 

These
strings can be used to activate behaviors instead of scripts - these are checked

first
and so no scripts should be names with these names:

   
default - 0: whatever

           
idle - 1: Stand around,
do abolutely nothing

           
roam - 2: Roam around,
collect stuff

           
walk - 3: Crouch-Walk
toward their goals

           
run - 4: Run toward
their goals

           
standshoot - 5: Stay
in one spot and shoot- duck when neccesary

           
standguard - 6: Wait
around for an enemy

           
patrol - 7: Follow a
path, looking for enemies

           
huntkill - 8: Track
down enemies and kill them

           
evade - 9: Run from
enemies

           
evadeshoot - 10: Run
from enemies, shoot them if they hit you

           
runshoot - 11: Run to
your goal and shoot enemy when possible

           
defend - 12: Defend an
entity or spot?

           
snipe - 13: Stay
hidden, shoot enemy only when have perfect shot and back turned

           
combat - 14: Attack,
evade, use cover, move about, etc.  Full
combat AI - id NPC code

           
medic - 15: Go for
lowest health buddy, hide and heal him.

           
takecover - 16: Find
nearest cover from enemies

           
getammo - 17: Go get
some ammo

           
advancefight - 18: Go
somewhere and fight along the way

           
face - 19: turn until
facing desired angles

           
wait - 20: do nothing

           
formation - 21:
Maintain a formation

           
crouch - 22:
Crouch-walk toward their goals

 

delay
- after spawned or triggered, how many seconds to wait to spawn the NPC

*/

 

================
**8><** ===================================

 

Welcher
NPC durch den NPC_spawner aufgerufen wird, definiert man mit dem KEY „NPC_type“
in den Entity Eigenschaften. Dort kann man sowohl die bereits definierten
NPC-Namen aus der „ext_data/npcs.cfg“
– Datei verwenden oder NPC-Namen von selbsterstellten NPC’s (erweiterung der
npcs.cfg
oder eingene .npc-Dateien,
siehe NPC - Tutorial)

 

[u]**Beispiele:**[/u]

 

Vordefinierter
NPC:

 

KEY:
NPC_type

VALUE:
reborn

 

Oder
eigener NPC:

 

KEY:
NPC_type

VALUE:
jedi_yoda

 

----

 

**Die
erste Angriffswelle:**

 

Wenn
man Angriffswellen programmieren möchte, ist es wichtig, dass die NPC’s beim
laden der Map nicht automatisch erscheinen. Das erreicht man in dem man den
NPC’s einen Zielnamen (targetname)
gibt. Sobald bei einem NPC, der „targetname“ festgelegt ist, erscheint
dieser nicht automatisch im Spiel, sondern muss zuerst per Script oder Trigger,
aktiviert werden.

 

Damit
man auch mehrere NPC’s pro Angriffswelle definieren kann, braucht man noch
eine Möglichkeit die bereits besiegten NPC’s zu zählen. Dafür benötigt man
das Entity „target_counter“
(gibt es nur im SP Modus !)

 

Zum
Erstellen unserer Angriffswelle-Testmap, benötigen wir einen Raum, wie z.B. aus
dem Tutorial „Mein erster
Raum“.

 

Jetzt
platzieren wir in diesem Raum 3 NPC_spawner.
Diese, stellen unsere ersten Gegner dar.

Jetzt
markieren wir alle 3 NPC’s, drücken die „**N**“-Taste 
und fügen folgendes ein:

 

 

KEY:
NPC_type

VALUE:
reborn

 

KEY:
targetname

VALUE:
welle0

 

KEY:
NPC_target

VALUE:
welle1count

 ![image]({filename}npc/waves/Image13.jpg)

Erklärung:

=======

NPC_type
= Name des NPC’s aus einer NPC-Definitionsdatei (in diesem Fall ein „reborn“,
aus der original „npcs.cfg“)

Targetname
= Name der NPC’s, mit dem sie aktiviert werden können. Die aktivierung kann
per Skript mit dem „USE“-Befehl
erfolgen, per „trigger_once“,
„target_relay“
oder mit jedem anderen Entity, das „targets“
(Ziele) aktivieren kann.

NPC_target
= Name eines Ziels, das aktiviert wird, wenn der NPC stirbt. In unserem Fall,
der Name unseres Zählers (target_counter)

 

----

 

Damit
die erste Angriffswelle gleich mit dem Spieler in der Map erscheint benötigen
wir noch einen "target_relay"
,welcher mit dem Spieler-Startpunkt (info_play_start)
verbunden ist. 

Rechte
Maustaste in dem 2D Fenster klicken, dann > target
> target_relay

Jetzt
"**N**"
drücken und dann folgendes eingeben:

 

KEY:
targetname

VALUE:
startwelle0

 

KEY:
target

VALUE:
welle0

 

![image]({filename}npc/waves/Image14.jpg)

 

Jetzt
müssen wir noch unseren Spiele-Startpunkt mit dem target_relay
verbinden.

Drücke
zuerst ESC-Taste um sicher zu gehen, dass nicht mehr markiert ist, markiere dann
das Info_play_start
und drücke "**N**"...

 

...gebe
folgendes ein:

 

KEY:
target

VALUE:
startwelle0

 

![image]({filename}npc/waves/Image10.jpg)

 

So,
wird der Spieler-Startpunkt mit dem "target_relay"
verbunden. 

Dieser
wiederum aktiviert unsere erste Angriffswelle.

 

![image]({filename}npc/waves/Image8.jpg)

 

----

Als
nächstes stellen wir in der Nähe der 3 NPC’s unseren Ziel-Zähler („target_counter“).

Dann
drücken wir „**N**“
und geben folgende Optionen ein:

 

KEY:
targetname

VALUE:
welle1count

 

KEY:
target

VALUE:
welle1

 

KEY:
count

VALUE:
3

 

![image]({filename}npc/waves/Image12.jpg)

 

Erklärung:

=======

targetname
= Name unseres Zählers, über welchen er aktiviert / angestoßen werden kann.

target
= Name eines Ziels, das aktiviert werden soll, wenn unserer Zähler seinen
maximal Wert erreicht. In unserem Fall, die nächste Angrifsswelle.

count
= Dieser Wert definiert, wie oft der Zähler angestoßen werden muss, bevor er
seinen Ziel aktiviert. In unserem Fall 3, da wir 3 Reborns haben, die besiegt werden müssen, bevor die
nächste Angriffs-Welle erscheint.

 

![image]({filename}npc/waves/Image3.jpg)

 

----

 

**die
nächste Angriffswelle **

 

Jetzt
platzieren wir ein wenig von den letzten entfernt, weitere 3 NPC_spawner. 

Diese,
stellen unsere weiteren Gegner dar. Dann markieren wir die 3 NPC’s, drücken
die „**N**“-Taste 
und fügen folgendes ein: 

 

KEY:
NPC_type

VALUE:
rebornacrobat

 

KEY:
targetname

VALUE:
welle1

 

KEY:
NPC_target

VALUE:
welle2count

 

Als
nächstes stellen wir in der Nähe der 3 NPC’s unseren zweiten Ziel-Zähler
(„target_counter“).

Dann
drücken wir „**N**“
und geben folgende Optionen ein:

 

KEY:
targetname

VALUE:
welle2count

 

KEY:
target

VALUE:
welle2

 

KEY:
count

VALUE:
3

 

![image]({filename}npc/waves/Image5.jpg)

 

----

**die
nächste Angriffswelle **

 

Jetzt
wiederholen wir das ganze noch mal, für weitere 3 NPC_spawner. 

Die
3 NPC’s markieren, „**N**“-Taste
drücken und folgendes einfügen: 

 

KEY:
NPC_type

VALUE:
rebornforceuser

 

KEY:
targetname

VALUE:
welle2

 

KEY:
NPC_target

VALUE:
welle3count

 

Als
nächstes stellen wir in der Nähe der 3 NPC’s unseren dritten Ziel-Zähler
(„target_counter“).

Dann
drücken wir „**N**“
und geben folgende Optionen ein:

 

KEY:
targetname

VALUE:
welle3count

 

KEY:
target

VALUE:
welle3

 

KEY:
count

VALUE:
3

 

![image]({filename}npc/waves/Image7.jpg)

 

----

 

**die
letzte Angriffswelle **

 

Jetzt
wiederholen wir das ganze ein letztes mal, weitere 3 NPC_spawner. 

Die
3 NPC’s markieren, „**N**“-Taste
drücken und folgendes einfügen: 

 

KEY:
NPC_type

VALUE:
rebornboss

 

KEY:
targetname

VALUE:
welle3

 

NPC_target
<
wird
nicht mehr benötigt, da keine weiteren Angriffswellen vorhanden >

 

![image]({filename}npc/waves/Image9.jpg)

 

 

Somit,
sind wir mit der Programmierung der Angriffswellen fertig. 

Natürlich
kann man das ganze beliebig oft weitermachen. 

Dieses
Prinzip wird bei den sogenannten "LADDER"-Maps verwendet, um immer
wieder, 

weitere
und schwierigere Gegner erscheinen zu lassen.

 

Jetzt
noch die Map unter dem namen "waves.map"
(Wellen) in dem base/maps
- Ordner speichern, kompilieren und testen.

 

Viel
Spaß !

 

Darth
Arth

 

----

[u][DOWNLOAD
DER TUTORIAL MAP](downloads/waves.zip)[/u]

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

 

