title: Animierte MD3 Modelle mit Milkshape
author: Seb (Crea)
date: 2004-01-01
modified: 2015-04-14
category: models
type: tutorials/darth-arth
tags: Modelling, Milkshape 3D, auto-generated
slug: model-md3-milkshape

**>>
Mapping Academy - Tutorials <<**

 

(c)
2003 [www.darth-arth.de](http://www.darth-arth.de)

----

**[u]Jedi Knight 2 - Animierte Map Objekte Tutorial by 
Seb(Crea)[/u]**

Zuerst was benötigt ihr dazu:

Milkshape 3D

GTK 
Radiant

 

 

Zunächst 
einmal ist es nötig ein model zu entwerfen nutzt dazu Milkshape 3D, ich habe mal 
ein Test Model gemacht ladet es hier herunter

-->
[model_test](downloads/model_test.zip)

 

Nachdem 
wir das Model fertig haben muss man ein Skellet für das model entwerfen. Dazu 
sucht in Milkshape den Menüpunkt Model und 

wählt 
dort Joint an. Jetzt setzt ihr den ersten Skellet punkt am besten wie im 
Bild.

 

![image]({filename}sebcrea-Dateien/bild1.jpg)

 

Geht 
nun auf den Menüpunkt Joints und nennt dort den Punkt z.b. Anfang dies ist 
wichtig um später einen überblick zu behalten.

 

![image]({filename}sebcrea-Dateien/bild2.jpg)

 

Als 
nächste benutzt ihr die Select funktion und wählt als Select Option Joint und 
klick dann den ersten Punkt an sodass dieser Rot wird.

Jetzt 
auf Joint in den Tools klicken und eine neuen setzen. Siehe Bild:

 

![image]({filename}sebcrea-Dateien/bild3.jpg)

 

So 
setzt man an alle Stellen welche man später animieren will einen Joint sodass es 
so aussieht:

 

![image]({filename}sebcrea-Dateien/bild4.jpg)

 

Ihr 
könnt dabei jedem Joint einen Namen geben wie ihr das schon mit dem Anfangs 
Joint gemacht habt. Als nächste muss man die Joints

mit 
den einzelnen Model teilen verbinden. Hierzu wählz im Menüpunkt Joints einen 
Joint an z.b. r_arm und jetzt sollte der Joint grün werden.

Danach 
geht in den Menüpunkt Groups und wählt dort den arm aus der dazu gehört.

 

![image]({filename}sebcrea-Dateien/bild5.jpg) 

 

Danach 
lasst ihr beides selektiert und geht in den Menüpunkt Joints und klick dort auf 
Assign. Jetzt ist der Joint mit dem Arm verbunden

und 
kann animiert werden allerdings sollte man erst das ganze Model mit den dazu 
gehörigen Joints verbinden wie oben genannt.

Wenn 
ihr damit fertig seit müsst ihr das model animieren. Geht dazu ganz unten auf 
den Menüpunkt Anim dort stehen jetzt Zahlen wie 1

und 
30. Dies sind die Frames mit dem das Model animiert wird. 1 ist die Anfangsframe 
und 30 die Endframe man kann für 30 auch 15 oder jede andere Zahl schreiben. Je 
höher die Zahl desto weicher und langsamer wird die Bewegung. 

 

In 
diesem Tutorial animieren wir nur ein Arm zum Test aber ihr könnt natürlich 
alles animieren z.b. Beine , Kopf .

Wenn 
ihr euch für eine Frame Anzahl entsclossen habt gehts ans animieren hierzu wählt 
in der Frame leiste die 2 Frame an.

 

![image]({filename}sebcrea-Dateien/bild6.jpg)

 

Nun 
geht in den Menü Punkt Joints und wählt den Arm an. Nun auf Model und dann könnt 
ihr wählen Rotate, Move nehmt am besten Rotate für Gliedmaßen. Nun können sieh 
den arm über den dazu gehörigen Joint bewegen bestimmen sie nun die Anfangs 
position des Armes. Wie im Bild:

![image]({filename}sebcrea-Dateien/bild7.jpg)

 

Danach 
geht in die Menü Leiste auf Animate und dann auf Set Keyframe. Über den Animate 
MenüPunkt kann man auch Frames einzeln oder 

alle 
Frames löschen.

 

Jetzt 
wählt eure nächste Frame aus z.b. 15.

 

Jetzt 
müsst ihr wie oben den Arm mit Rotate. Neu plazieren z.B. so

 

![image]({filename}sebcrea-Dateien/bild8.jpg)

 

Wenn 
ihr das gemacht habt geht wieder auf Set Keyframe.

Jetzt 
könnt ihr mit der unteren Leiste nachprüfen ob der Arm sich richtig bewegt. Ich 
hab nun die Animation abgeschlossen nun muss es Exportiert werden und zwar so 
das die Frames nicht verloren gehen. Geht hierzu auf Tools Quake III Arena 
---> Generate Control File...

Wählt 
nun einen Name z.b. model_ani.

Jetzt 
erscheint dieses Fenster:

 

![image]({filename}sebcrea-Dateien/bild9.jpg)

 

Belasst 
allen Werte so wie vorgegeben.

Da 
sich dieses Tutorial auf Animation fixiert haben wir keine Texturen definiert. 
Aber das brauchen wir nicht zum Testen. Danach Exportiert ihr das model als md3. 
Achtung es muss den selben Namen wie der Control File haben.Damit wäre die 
Arbeit mit Milkshape abgeschlossen.

Jetzt 
geht in base Ordner und dann auf models---> map_objects .Dort erstellt ihr 
einen ordner und nennt diesen z.B. Model_test. In diesen

Ordner 
verschiebt ihr die Md3 die ihr gerade erstellt habt. 

Nun 
startet ihr den GTK Radiant, erstellt einen Raum. Danach benutzt die rechte 
Maustaste und wählt misc--->misc_model_breakable,

lasst 
es markiert und drückt n. Danach öffnet sich ein Fenster, klickt hier auf model 
und wählt das erstellte Model aus. Danach kommt das wichtigste man muss außerdem 
in diesem Fenster noch den Punkt auto animate anwählen. Nun noch einen 
info_player_start setzen und kompilen. Die Animation wird jetzt immer wieder 
Wiederholt.

 

 

 

 

Herrlichen 
Glückwunsch ihr habt euer erstes Animiertes Map_Object erstellt.

 

 

by
Seb(crea).

 

 

----

Alle
  Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet: 

©
  2000 - 2003 (Artur L.) [www.darth-arth.de](http://www.darth-arth.de)

Nur
  zur privaten Nutzung. Kopieren nicht gestattet. Darth-Arth.de ist ausdrücklich
  nicht für den Inhalt externer Seiten verantwortlich. Es gelten die
  angegebenen Nutzungsbedingungen.

 

