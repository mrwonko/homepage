title: Teleporter
author: SithMaster ( Andreas K.)
date: 2004-01-01
modified: 2015-04-14
category: mapping
type: tutorials/darth-arth
tags: Entities, auto-generated
slug: entity-teleporter

**>> Mapping Academy - 
Tutorials <<**

 

(c) 2004 [http://www.darth-arth.de/](http://www.darth-arth.de/)

----

Teleporter

Author: #jow.SithMaster ( Andreas K.)

**[u]VORAUSSETZUNG[/u][u]EN[/u]:**

>> Mein erster Raum ( [Tutorial](../firstroom/firstroom.htm) 
)

 

----

In dieser Lehreinheit (Tutorial) 
erkläre ich euch, wie ihr einen Teleporter in eure Map setzt.

----

Also als erstes brauchen 
wir einen einfachen Raum.

![image]({static}Raum.jpg)

 

Erstellt an einer freien
Stelle, 
wo ihr den Teleporter haben wollt, einen Brush. Dieser Brush wird zum Teleporter-Bereich.

Nun klickt mit der rechten 
Maustaste auf den Brush und wählt "trigger -->
trigger_teleport". (Der Brush 
**muss** markiert sein!)

 

 

![image]({static}Fenster.jpg)

 

 

Damit der Teleporter-Brush im
spiel unsichtbar 
ist, belegen wir ihn mit der Trigger Textur, in
Textures --> System zu
finden.

 

So, der Teleporter steht schon 
mal, er hat aber noch kein Zielort.

 

Drückt jetzt **ESC** damit bei euch nix 
mehr ausgewählt ist!

 

Als nächsts, drückt da wo ihr den 
Zielort haben wollt, die rechte Maustaste und wählt

target --> 
target_position

 

![image]({static}Fenster2.jpg)

 

Ok, nun habt ihr so einen 
kleinen grünen Target (Zielobjekt).

Schiebt den zurecht, so dass
der dorthin wandert, wo 
ihr ihn haben wollt, bzw. wo ihr nach dem teleportieren herrauskommen 
wollt.

Wenn der Target nun
richtig sitzt, 
hebt alle markierungen auf. (mit **ESC**)

 

Als nächstes müsst ihr eurem 
Teleporter das Ziel zeigen.

Um das zu machen, müsst ihr 
ZUERST den trigger_teleport markieren 
und als ZWEITES den target_position.  

Jetzt 
drückt **Strg + K **und
danach müsstet ihr eine Verbindung zwischen dem Teleporter und dem Zielort sehen.  

 (Hier in grün zu sehen):

 

![image]({static}verbindung.jpg)

 

Speichere alles ab,
kompiliere und lade danach deine Map im 
Spiel.

Wenn man jetzt an die
stelle geht, wo der unsichtbare Teleporter ist, wird man zum Ziel teleportiert.

Um das ganze grafisch ein
wenig besser zu machen, kann man die Teleportstelle mit ein Brushkonstruktion, 

einem LichtStrahl oder
mit etwas anderem erkennbar machen, das hängt jedoch immer von Zweck und Typ
des Teleporters ab.

 

![image]({static}tele1.jpg)

 

![image]({static}tele2.jpg)

 

**Gratuliere!, du hast es geschafft!**

 

**Gruß,**

**Sith**

_______________________________________________________________________________________________________________________________

 

Tutorial-Map 
Download   ([Link](../../downloads/Teleporter.zip))

