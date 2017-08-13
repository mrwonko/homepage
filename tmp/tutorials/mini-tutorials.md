title: Minitutorials: Firstroom, Caulk, Arena- & pk3-Datei, func_* Brushes, Triggers, Tips und Tricks
author: Ice Dyn4stY™ ( Marc E.)
date: 2004-01-01
modified: 2015-04-14
category: mapping
type: tutorials/darth-arth
tags: Brushwork, Arena, PK3, Entities, auto-generated
slug: mini-tutorials

**>>
Mapping Academy - Tutorials <<**

 

(c)
2004 [www.darth-arth.de](http://www.darth-arth.de)

----

Mini Tutorials

Author: Ice Dyn4stY™ (Marc E.)

**[u]VORAUSSETZUNG[/u][u]EN[/u]:**

>>
GTK Radiant 1.4 downloaden ( [Link](http://www.qeradiant.com/index.php?data=files&files_id=77)
) und installieren ( [Tutorial](../gtk14/install/gtk14.html) ) <<

----

**Mini - Tutorials zu: 
                  

**

-
[ Mein erster Raum](#firstroom) 

- [ Wie caulke ich richtig?](#caulk) 

-
[ 
                  Die Arena Datei](#arena) 

- [ Die pk3 Datei](#pk3) 

-
[ `func_*` Brushes](#func) 

- [ `trigger_*` Brushes](#trigger) 

-
[Tips & Tricks](#tips)

_____________________________________________________________________________________________________________________________________________ 
                  

**Mein erster Raum:**

Also, nachdem ihr den Radiant gestartet habt, geht's 
                  los: In dem 2D Fenster klickt ihr mit der linken Maustaste 
                  drauf, hält die Maustaste 

gedrückt und geht mit der Maus 
                  in eine Richtung; ein Brush wird gezogen. 

![image]({filename}first_room_1.jpg) 

Nach 
                  diesem Muster fertigt ihr nun so viele Bruhes an, bis sie 
                  einen Raum ergeben, dass sollte dann ungefähr so aussehen: 
                  

![image]({filename}first_room_2.jpg)

Wichtig ist dabei, dass sich die Brushes nicht überschneiden, also 
                  sollten nur dort Brushes sein, wo der Spieler sie auch sieht 
                  

(Siehe Bild) Nun habt ihr zwar einen Raum, aber noch 
                  keinen sogenannten "Spawn-Point", an welchem der Spieler 
                  starten kann. Damit ihr 

einen solchen bekommt, drückt ihr 
                  im 2D Fenster mit der rechten Maustaste, dann geht ihr auf
"info", dort auf "info_player_start". 

![image]({filename}first_room_3.jpg) 

Nun 
                  solltet ihr einen roten Klotz sehen, er ist so groß, wie der 
                  Spieler im Spiel selber. Ihr könnt ihn beliebig verschieben, 
                  wichtig 

dabei ist, dass er ** innerhalb** der Map bleibt, und 
                  dass er min. 8 Units (Ein Unit ist so ein Raster in den 2D Fenstern, mehr dazu später) 

oberhalb des Bodens ist. 
                  

Da der Raum jetzt noch ein bisschen langweilig aussieht, 
                  könnnt ihr ihm noch Texturen geben; einfach auf "textures" 
                  dann die gewünschten 

Texturen, z.B. "Korriban" anwählen. 
                  Dann lädt es die Texturen (Kann ne Weile dauern) Wenn es 
                  fertig geladen ist, drückt ihr "T"; nun 

erscheint ein 
                  Fenster, in welchem die Texturen aufgelistet sind. Dann 
                  markiert ihr den Brush mit Shift und der linken Maustaste. 
                  Jetzt 

könnt ihr dem Brush die gewünschte Textur geben. Das ganze sollte nun etwa so aussehen: 

![image]({filename}first_room_4.jpg) 

Dann 
                  speichert ihr die Map in deinem  Gamedata/Base
Verzeichnis in 
                  dem Unterordner namens  maps.
(Standard: C:/Programme/LucasArts/Star Wars Jedi 
                  Knight 

Jedi Academy/GameData/Base/maps) unter dem Namen
"Meine_Map". Dann geht ihr auf "bsp" dann auf "Q3Map2: (single) BSP
-meta". 

 Dies kompiliert
die Map, dass heisst, 
                  es berechnet sie, damit man sie überhaupt spielen kann. Nun 
                  erscheint ein schwarzes Fenster. 

(Die Kompilierungart
berechnet die Map ohne  Licht!, da es nur zum
testen gedacht ist.) 

![image]({filename}first_room_5.jpg)

Sobald es fertig ist, findet ihr in eurem
 maps Ordner 
                  eine neue Datei mit dem Namen "Meine_Map.bsp", diese Datei 
                  wird dann benötigt, um 

sie im Spiel zu spielen. Um sie im 
                  Spiel testen zu können, öffnet ihr im Hauptmenu von JK3 die 
                  Console (**Shift +
^**), dann gebt ihr dort 

ein: "**devmap
meine_map**"; Gross-Kleinschreibung spielt keine Rolle. Dann 
                  lädt es die Map. 

Herzlichen Glückwunsch, ihr habt 
                  euren ersten spielbaren Raum gemacht! 
                  

_____________________________________________________________________________________________________________________________________________ 
                  

Wie caulke ich 
                  richtig?  

Zuerst mal zum caulken 
                  allgemein: Wenn ihr einfach ne Map machen würdet und die ganzen Brushes mit einer 
                  Textur belegen würdet, 

würde das sehr zu Lasten der FPS 
                  gehen (D.h. sie wird unspielbar, wegen Ruckeln), darum 
                  macht man den Brush mit der Caulk Textur; 

 die Caulk Textur 
                  wird von der JK - Engine nicht berechnet, daher schont das auch
die FPS. 

So und nun 
                  zum praktischen: 

Zuerst macht ihr einen Brush/Raum und 
                  belegt ihn mit der Caulk Texur, zu finden in ** system/caulk**. Das 
                  ganze sollte dann so aussehen: 

![image]({filename}caulken1.jpg) 

Danach 
                  drückt ihr "ESC" (Ihr deselektiert den Brush). Nun müsst ihr 
                  die einzelnen Seiten mit der Textur überziehen; dafür markiert 
                  ihr 

den Brush mit "Shift + CTRL +linke Maustaste". Nun 
                  gebt ihr der Brushseite die gewünschte Textur. 

![image]({filename}caulken2.jpg) 

So, 
                  fertig. Vergesst nicht, dies bei jedem Brush eurer Map zu 
                  machen, dass ist wichtig!!! 
                  

_____________________________________________________________________________________________________________________________________________ 
                  

Die Arena Datei:

Um eine Map im Hauptmenu von JK3 sichtbar zu machen, 
                  benötigt ihr eine sogenannte "Arena Datei", sie wird mit einem 
                  einfach Texteditor 

gemacht, z.B. Notpad. 

Eine "Arena 
                  Datei" ist folgendermassenaufgebaut (Einfach eine Textdatei 
                  machen und hineinschreiben): 

{ 

map "meine_map" 
                  

longname "meine_map von mir" 

type "ffa
team-ffa" 

} 
                  

- Bei "map" tragt ihr den exakten Namen eurer Map ein. 
                  

- Bei "longaname" kommt der Namen hin, den ihr gerne im 
                  Hauptmenu angezeigt haben möchtet. 

- Bei "type" tragt ihr 
                  die gewünschten Spieltypes ein (duel, ffa, usw) mehrere 
                  Spieltypen werden durch ein Leerzeichen getrennt. 

Dies 
                  sind die wichtigsten Eigenschaften der Arena Datei, man kann 
                  auch noch "bots" eintragen, dass ist aber unwichtig. 

Nun 
                  benennt ihr die Textdatei in "meine_map.arena" um. In der 
                  PK3 Datei kommt sie in einen Unterordner namens "scripts". 

 
                  (Mehr Infos über die PK3 Datei im nächsten Tut ) 

Herzlichen
Glückwunsch, ihr seid nun in der 
                  Lage, eigene Arena Datei zu schreiben! 
                  

_____________________________________________________________________________________________________________________________________________ 
                  

Die pk3 Datei:

Wenn man eine Map mit Scripts, eigenen Texturen, 
                  eigenen Sounds, etc veröffentlichen will, wäre es schlicht zu 
                  umständlich, alle Files 

einzeln zu veröffentlichen, mit 
                  einer PK3 Datei läuft das viel einfacher. 

Eine PK3 
                  Datei (nur) den notwendigsten Dingen ist so aufgebaut: 
                  

meine_map.pk3 
                  

-meine_map.pk3/scripts/meine_map.arena 
                  

-meine_map.pk3/maps/meine_map.bsp 
                  

-meine_map.pk3/levelshots/meine_map.jpg 

In den 
                  Ordner "scripts" kommt die "Arena Datei", im "maps" Ordner die 
                  kompilierte Map (bsp Datei) Im Ordner "levelshots" findert man 
                  den 

Startscreen, der beim Laden der Map angezeigt wird. 
                  Dies ist eine einfach "*.jpg" Datei 

mit der Auflösung 
                  1024*1024 (Diese Auflösung ist wichtig!) 

 Um eine
"*.**PK3**" Datei 
                  zu machen, macht ihr zunächst eine "*.**zip**" Datei. 

 Da hinein tut ihr folgende Ordner: "maps", "scripts" und
"levelshots". Da tut ihr dann die Dateien hinein, 

wie oben 
                  beschrieben. Wichtig ist, dass die Arena- und Levelshotdatei 
                  jeweilst den Namen der Map haben! 

 So, nachdem ihr alles in die 
                  zip Datei gestopft habt, benennt ihr die `*.zip` Datei in 
                  `*.pk3` um. 

 Schon habt ihr eure Map handlich in eine PK3
                  verpackt, congratulations! 
                  

_____________________________________________________________________________________________________________________________________________ 
                  

**`Func_*`
- Brushes**

`Func_*` verleihen einem Brush eine spezielle 
                  Eigenschaft, lässt ihn z.B. wie eine Tür aufgehen, oder aber 
                  einen Stein zerbrechen.

"Func_*"
erstellt ihr, indem ihr einfach Rechtsklick im 2D Fenster macht, dann auf  func, und dort auf das gewünschte 
                  

anklickt. 

 Die wichtigsten funcs werde ich hier auflisten: 
                  

**func_breakable:**  

Wenn 
                  einem Brush diese Eigenschaft zugewiesen worden ist, dann kann 
                  man ihn zerstören. Weitere Eigenschaften, z.B. wieviel Schaden 
                  der 

Brush verträgt, könnt ihr wie folgt einstellen: Brush 
                  markieren -> "N" drücken -> "KEY: health" "VALUE: 50" - 
                  Das heisst, der Brush geht 

kaputt, nachdem man ihm 50 
                  Schadenspunkte zugefügt hat ![icon_wink.gif]({filename}icon_wink.gif) Man kann auch 
                  das Material des zerstörbaren Brushes angeben, "KEY material" 
                  

"VALUE: 1-9" (Die Bedeutungen stehen oberhalb des 
                  Kästchens, für weitere Bedetungen dieser console, schaut ihr 
                  ins entprechende Tut ![icon_wink.gif]({filename}icon_wink.gif)). 
                  

----

**func_button:**  

Wenn man 
                  eine Tür über einen Schalter öffnen will, ist ein "func_button" genau das richtige. Zuerst macht ihr eine Tür, 
                  also einen Brush 

mit der Eigenschaft "func_door". Danach 
                  macht ihr noch einen Brush mit der Eigenschaft "func_button". 
                  Dann markiert ihr zuerst den 

"func_button", dann den
"func_door" und drückt "**CTRL +
K**". Das war's dann, jetzt 
                  sollten Tür und Schalter mit einer blauen Linie verbunden 
                  

sein. 

![image]({filename}func_button1.jpg) 

So, ihr könnt dem Schalter nun noch eine 
                  Richtung zuweisen, in die er aufgehen soll; "N" drücken, dann 
                  auf den Button unten links klicken 

(90° 180° 270° 360°) - 
                  das musst du einfach ausprobieren, um die richtige Richtung 
                  zu machen. 

![image]({filename}console.jpg) 

----

**func_door:**  

Ein "func_door"
(eine Tür) macht ihr
folgendermassen: Einen Brush, mit "func_door" belegen, dann die Richtung angeben (Wieder die 
                  Grade unten linkes 

in den Entity-Eigenschaften), fertig. 

 Wenn ihr 
                  wollt, dass die Tür nach oben/unten aufgeht, dann macht ihr in 
                  der Mitte unten (In den Entity-Eigenschaften) "up/down" 

und "KEY: lip"
"VALUE: -90". Der - vor 90 muss unbedingt hin, sonst 
                  gehts nicht!!! Bei VALUE wird übrigens die Höhe angegeben, ihr 
                  

könnt sie folgendermaßen herausfinden: 

![image]({filename}func_door.jpg) 

"**Q**" 
                  drücken, dann stehen da Zahlen, welche die Werte der höhe, etc 
                  angeben. Nun könnt ihr für die Höhe bei "VALUE" die Zahl
engeben, die 

da steht, ich würde allerdings empfehlen, 
                  einige Units weniger anzugeben (Wenn da steht 90 z.B. nur 82), 
                  weil sonst die Tür vollständig in 

der Wand verschwindet, 
                  und das komisch aussehen würde. 
                  

_____________________________________________________________________________________________________________________________________________ 
                  

**`Trigger_*`
- Brushes**

Trigger verleihen einem Brush (ähnlich wie `func_*`) 
                  eine spezielle Eigenschaft; der Unterschied besteht darin, 
                  dass beim trigger was 

ausgelöst wird, sobald der Spieler 
                  diesen bestimmten Brush betritt. So kann man zum Beispiel
Teleporter, Jumppads, Türen die per Knopfdruck 

öffnen lasse usw. Wichtig dabei ist, dass alle  Brushes, welche mit 
                  einem trigger belegt werden, die Textur "system/trigger" 
                  

tragen!!! 

 Ich werde hier wieder die häufigsten auflisten:

**trigger_hurt:** 

 

Ein "trigger_hurt" macht dem Spieler Schaden und ist 
                  vergleichweise sehr einfach zu realisieren: Zuerst macht ihr 
                  einen Brush (Mit der 

"system/trigger" Textur), dann 
                  markiert ihn und gebt weist im "trigger" dann "trigger_hurt" 
                  zu. So nun hat der Brush die Eigenschaft, 

aber noch macht 
                  er keinen Schaden. Damit das aber der Fall ist, öffnet ihr die
Entity-Egenschaften mit (Mit "**N**" ) und gebt dort ein: 

 "KEY: dmg" 

"VALUE: 10"

 

dass
heißt, sobald der Spieler den Brush berührt, macht es ihm 10 Schadenspunkte. Das ganze sollte nun etwa 
                  so aussehen: 

(Wenn ihr allerdings wollt, dass der Spieler 
                  (Wie in "ffa_bespin" von JK2) zu Tode stürtzt, dann macht ihr
:

 

 
                  "KEY: dmg"

"VALUE: -1",

dann stirbt der Spieler 
                  sofort.) 

![image]({filename}trigger_hurt.jpg) 

----

**trigger_mutiple:** 

 

Ein
"trigger_multiple" ist nichts anderes als ein Auslöser für 
                  bestimmte Dinge, z.B. für Scripts oder sonstige Vorgänge. Er 
                  kann allerdings 

auch als Schalter für eine Tür benutzt 
                  werden: Dafür macht man zuerst wieder eine Tür mit "func_door", danach macht man einen Schalter. 

Dieser dient 
                  allerdings nur als Atrappe, der Auslöser (Der "trigger_multiple" ) kommt gleich vor den Schalter. Danach
aktiviert ihr beim 

"trigger_multiple" in den Eigenschaften, die "**use_button**"
Option. 

Das bedeutet, die Tür
erst dann aufgeht, wenn jemand 
                  im trigger drin, den "Benutzen-Knopf" drückt. 

Danach 
                  verbindet ihr den trigger wieder mit der Tür (Wieder mit
"CTRL 
                  + K" ). 

 Danach kommt wieder die blaue Linie; das ganze sollte 
                  nun 

etwa so aussehen: 

![image]({filename}trigger_multible.jpg)

----

**trigger_push:**

Ein "trigger_push" ist nichts anderes, als ein
Jumppad; 
                  wenn man auf diesen Jumppad tritt, dann fliegt man durch die 
                  Luft. Diese Jumppads 

sind auch sehr einfach zu realisieren: 
                  

Zuerst macht ihr einen Brush, welcher das Jumppad 
                  darstellt, dann macht ihr einen Brush mit der  trigger Textur 
                  drauf, gebt ihm die 

Eigenschaft "trigger" dann
"trigger_push". Nun fehlt nur noch der Zielort, wo es einem 
                  hintun soll, wenn man auf den trigger tritt. 

Dafür macht 
                  ihr, an einer anderen Stelle, einen "target_position", dafür 
                  geht ihr zuerst auf "target" dann auf "target_position". 

 Nun 
                  markiert ihr zuerst den trigger, dann den target und 
                  drückt "**CTRL +
K**". 

 Nun seht ihr wieder die blaue
Verbindungs-Linie. Nun 
                  habt ihr schon euer erstes Jumppad 

gemacht! 

[u] Sehr wichtig 
                  dabei ist, dass die Linie niemals durch Wände oder 
                  sonstige Hindernisse, welche ihn aufhalten würde gehen darf!!![/u]

![image]({filename}trigger_push.jpg)

----

**trigger_teleport:** 

 

Ein
"trigger_teleport" funktioniert im Prinzip genau gleich, wie 
                  der "trigger_push", mit dem Unterschied, dass er durch Wände 
                  gehen kann. 

Ihr macht also wieder einen Brush mit der 
                  trigger Textur, gebt ihm die Eigenschaft "trigger/trigger_teleport" 

Dann macht ihr, ein bisschen
weiter entfernt davon, einen "target/target_position", 
                  markiert zuerst den trigger, dann den target, drückt "**CTRL +
K**" und fertig. 

![image]({filename}trigger_teleport.jpg)

----

**Tips
& Tricks:**

Was ist ein Raster (Grid) ?

Raster sind die kleinen "Kästchen" in den 2D 
                  Ansichten, sie helfen euch, bei einer Map z.B. die genauen 
                  Masse zu bestimmen.

----

 

Wie mache ich Lichter 
                  farbig? 

Zunächst wählt ihr das Licht an, 
                  drückt "K" und wählt die Farbe aus; OK klicken und fertig
...

----

Wie markiere ich alle Brushes eines 
                  bestimmten Types?? 

Mit diesem Trick kann 
                  man sehr einfach Brushes mit einer besimmten Textur finden. 
                  Man geht ins Texturenmenü "T" und markiert eine 

Textur; 
                  dann "ESC" und nun drückt ihr "STRG + A" und schon werden alle 
                  Brushes mit dem gewählten Texturentyp angezeigt. 
                  

Weitere 
                  folgen...

 

----

Alle
  Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet: 

©
  2000 - 2004 (Artur L.) [www.darth-arth.de](http://www.darth-arth.de)

Nur
  zur privaten Nutzung. Kopieren nicht gestattet. Darth-Arth.de ist ausdrücklich
  nicht für den Inhalt externer Seiten verantwortlich. Es gelten die
  angegebenen Nutzungsbedingungen.

 

