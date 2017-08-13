title: Eigene NPCs
author: Darth Arth (Artur L.)
date: 2004-01-01
modified: 2015-04-14
category: scripts
type: tutorials/darth-arth
tags: NPCs, auto-generated
slug: custom-npc

**>>
Mapping Academy - Tutorials <<**

 

(c)
2003 [www.darth-arth.net](http://www.darth-arth.net)

----

**NPC Tutorial**

![image]({filename}../buttons/aliendf4.gif)

![image]({filename}../buttons/aliende4.gif)
Erstellung von eigenen Nicht-Player-Charakteren (Non-Player-Characters, NPCs) für Jedi-Knight II - Jedi Outcast.

Um einen neuen, eigenen NPC zu erstellen braucht man eine NPC-Konfigurations-Datei und natürlich das entsprechende Glm-Model samt Skins und Sounds.

Man braucht entweder die "NPCS.CFG" oder einzelne ".npc"- Dateien und die Fähigkeiten der Charaktere zu definieren.

Die Datei "npcs.cfg" befindet sich in dem "ext_data"-Ordner in der assets0.pk3 – Datei.

In dieser Datei sind alle NPC's für JKII-Single Player definiert.

Das mit den zusätzlichen ".npc"-Dateien ist nirgends dokumentiert. Damit kann man neue zusätzliche NPC's definieren, ohne jedes mal die "npcs.cfg" editieren zu müssen.

Der Aufbau ist der Datei gleich wie bei „npcs.cfg“, man kann aber mehrere davon haben.

**[u]
Achtung!:[/u]**

Es funktioniert nicht wenn man vorhandene Charaktere gegen neue tauschen will (z.B. Desann mit Vader vertauschen), dann bleibt nichts anderes übrig als die NPCS.CFG zu editieren, ansonsten gibt es Probleme vor allem bei den Sounds.

![image]({filename}../buttons/aliende4.gif)
Jedi -NPC's, die helle Seite der Macht:

![image]({filename}../buttons/aliendf4.gif)

wenn man gute jedis machen will, muss man den "Jedi"-NPC als Grundlage nehmen.

die NPCs müssen immer heißen:

Jedi_NPCname

genauso die Model-Ordner, sonst funktionieren die NPCs nicht !

Modelname und NPCname müssen gleich sein und mit dem Wort "jedi" anfangen

Es ist sehr wichtig!, sonst funktioniert es nicht.

Beispiel:

![image]({filename}../buttons/aliendf4.gif)

Jedi_yoda

{

playermodel jedi_yoda

saberColor green

rank commander

reactions 5

aim 5

move 5

aggression 5

evasion 5

intelligence 5

hfov 180

vfov 180

scale 55

playerTeam player

enemyTeam enemy

// race human

class jedi

snd yoda

sndcombat yoda

sndextra yoda

sndjedi yoda

yawSpeed 200

walkspeed 60

runspeed 220

health 999

dismemberProbHead 0

dismemberProbArms 0

dismemberProbHands 0

dismemberProbLegs 0

dismemberProbWaist 0

}

![image]({filename}../buttons/aliendf4.gif)

[u]Erklärung:[/u]

rank
 - bedeutet wie gut der NPC ist, (intelligent, Reaktionsvermögen usw.)

Es gibt verschienene Rank-Level (betrifft nur Jedi):

captain
 - der beste

Commander
 - sehr gut

Lt
 - gut

raktion, aim, move, agression, evasion
 - sind Einstellungen für die einzelnen Fähigkeiten

1=schlecht, 5=sehr gut

hfov,vfov
 - ist der Visionsradius (horizontal und vertikal)

"scale" ist die Skalierung des Models, so ist zum Beispiel Desann größer und Yoda kleiner.

[u]Folgendes ist jetzt auch sehr wichtig:[/u]

bei den guten Jedis, muss immer:

PlayerTeam   player

EnemyTeam  enemy

"class
 " muss immer "jedi" sein!

dreht man das um, funktioniert der NPC nicht mehr!

--------------------------------------

"race" ist unwichtig (Überbleibsel von STV-EF)

"snd",
"sndcombat" usw. sind die Ordner für die Sounds unter

"sound/char/modelname"

also wenn man die Sounds unter:

sound/char/Yoda hat

muss es heißen :

snd Yoda

yawSpeed
 ist die Geschwindigkeit mit der sich der
NPC drehen kann

walkspeed
 und
 runspeed
 sind wohl klar (Geh- und
Renngeschwindigkeit)

"health" ist die Gesundheit

**[u]
Bemerkung:[/u]**

was hier die wenigsten wissen, man kann auch Werte
 über 999
 eintragen

so, hat mein Imperator 3000 Health in "The Challenge..."

ok, das waren die guten :D

![image]({filename}../buttons/aliende4.gif) Reborn
NPC's die dunkle Seite der Macht

![image]({filename}../buttons/aliendf4.gif)

hier ist es ähnlich wie bei den guten, nur das statt "Jedi" überall das Wort
"Reborn" vorne stehen muss.

das heißt:

NPCname
Reborn_Vader

Modelname

Reborn_Vader

class

 reborn

und die Playerteams müssen immer umgekehrt, als bei den Jedi's sein.

Was noch bei den "reborns" anders ist, sind die Rank-Stufen.

[u]
Folgende Rank-Stufen gibt es:[/u]

kein rank
 - der normale, dumme Reborn

crewman
 - acrobat

ensign
 - forceuser

ltjg
 - fencer

lt
 - boss

ltcomm
 - shadowtrooper

![image]({filename}../buttons/aliende4.gif)
Die Soldaten NPC's

![image]({filename}../buttons/aliendf4.gif)

Für die Soldaten der dunklen Seite nimmt man "Stormtrooper"
und für die guten "BespinCop"
 als Vorlage.

Der Rest der Einstellungen ist analog zu den beiden beschriebenen Jedi-Klassen.

[u]
Schlussbemerkung:[/u]

Am besten packt man dann alle guten-NPCs in eine ".npc" Datei und die bösen in eine andere.

Das gleiche dann natürlich mit den Soldaten, falls vorhanden.

Oder alternativ kann man eigene  npcs.cfg - Datei erstellen.

Dann die neu definierten Dateien in einen "my_npcs/ext_data" - Ordner kopieren und mit ZIP zusammen packen.

Die erstellte pk3.-Datei dann in ein Mod-Order oder direkt in den "base" Ordner kopieren.

----

Alle
  Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet: 

©
  2000 - 2003 (Artur L.) [www.darth-arth.net](http://www.darth-arth.net)

Nur
  zur privaten Nutzung. Kopieren nicht gestattet. Darth-Arth.Net ist ausdrücklich
  nicht für den Inhalt externer Seiten verantwortlich. Es gelten die
  angegebenen Nutzungsbedingungen.

 
