title: Zwei Räume verbinden, erste Tür
author: Darth Arth (Artur L.)
date: 2004-01-01
modified: 2015-04-14
category: mapping
type: tutorials/darth-arth
tags: Brushwork, Entities, Tür, auto-generated
slug: brushwork-first-door

**>>
Mapping Academy - Tutorials <<**

 

(c)
2003 [www.darth-arth.net](http://www.darth-arth.net)

----

2 Räume verbinden, erste Tür

**[u]VORAUSSETZUNG[/u][u]EN[/u]:**

>>
Installation JK2 Editing Tools I ( [Tutorial](../../radiant/jk2_etools1.htm)
)<<

>>
Installation JK2 Editing Tools 2 ( [Tutorial](../../radiant/jk2_etools2.htm)
)<<

>>
Installation GTK - Radiant ( [Tutorial](../../radiant/gtk_radiant.htm)
)<<

>>
Mein Erster Raum ( [Tutorial](../firstroom/firstroom.htm) )<<

----

In
dieser Lehreinheit (Tutorial) wird beschrieben, wie man auf einfachste Weise 2
Räume miteinander verbinden kann und wie erstellt man eine einfache Tür.

----

Als erstes, benötigen wie einen
einfachen Raum, wie in dem Tutorial >> "[Mein
erster Raum](../firstroom/firstroom.htm)" << beschrieben. Nur sollte er nicht ganz so groß
sein, max. 1000 x 1000 Map - Einheiten.

![image]({static}Image41.jpg)

Bitte ESC-Taste drücken um
sicher zu gehen, dass nichts markiert ist. Dann, legen wir in der 2D-Ansicht
einen Brush um den kompletten Raum, siehe Bild unten:

![image]({static}Image39.jpg)

Jetzt klicken wir auf ![image]({static}Image40.jpg)
um den ganzen Inhalt zu markieren.

Es sieht danach später so aus, wie auf
diesem
Bild:

![image]({static}Image38.jpg)

Jetzt bitte die "Leertaste
drücken um den ganzen Raum zu kopieren. Die Kopie setzen wir neben dem Original,
aber nicht direkt, sondern mit ein wenig Entfernung, damit wir einen schönen
Gang dazwischen bauen können.

![image]({static}Image37.jpg)

Beim erstellen von Türem Gängen
usw., sollte man sehr auf die Größen-Verhältnisse achten. Denn, falsche
Maßstäbe haben schon so manchen Mapper zur Verzweiflung getrieben. Deswegen
ist es immer wichtig, ein Bezugsobjekt zu finden, an dessen Größe man sich
orientieren kann. Bei JKII eignet sich "Info_player_start"
sehr gut zu diesem Zweck, denn das Entity ist genauso groß, wie der Player im
Spiel . Wir setzen jetzt ein "Info_player_start"
nah an die Stelle wo unser Durchgang gebaut wird.

![image]({static}Image36.jpg)

Jetzt in der 2D-Sicht (Top)
erstellen wir einen Brush der die beiden Räume verbindet. Die beiden Seiten,
die in das Innere der Räume zeigen, sollten ein wenig länger sein (16-32
Einheiten), das wird dann unser Tür-Rahmen :D Der Brush soll nicht breiter als
4 x Player-Breite sein.

![image]({static}Image35.jpg)

Als nächstes schalten wir in die
Seitenansicht und ziehen den Brush hoch, aber nur so, dass er maximal 2 x so
hoch ist, wie der Player.

![image]({static}Image33.jpg)

Wenn alles passend eingestellt
ist, sind wir bereit ein Loch in beide Wände zu schneiden. Benutze dafür den
"CSG - Substract" Befehl.

![image]({static}Image30.jpg)

Die zwei Wände werden in jeweils
3 Teile zerschnitten.

![image]({static}Image29.jpg)

Jetzt wandeln wir unseren Brush
in eine Box. Nutze dafür den "Make Hollow" Befehl ![image]({filename}../firstroom/button_hollow.jpg).

![image]({static}Image32.jpg)

damit aus unserer Box ein Gang
wird, müssen wir die beiden Seiten im Inneren der Räume löschen. Markiere die
Seiten und drücke "Backspace"

![image]({static}Image31.jpg)

Wir wissen aus den vorherigen
Tutorials, dass der "Make
Hollow" - Befehl, Boxen
erstellt, deren wände sich gegenseitig überschneiden. Da wir bereits 2 von 6
Wänden gelöscht haben, brauchen wir nur noch 2 zu schneiden. Markiere den
Gangboden und -Decke und klicke wieder auf "CSG
- Substract" ![image]({static}Image30.jpg)

![image]({static}Image27.jpg)

Unser Durchgang ist fertig. Jetzt
bauen wir noch eine Tür. Erstelle einen Brush im Durchgang und zwar so, dass er
auf der Höhe der Wand ist, aber ein wenig schmaler, damit die Tür beim
Aufmachen, keine Grafik-Fehler verursacht, sondern komplett in der Wand
verschwindet. Der Brush darf auch keine der Gang-Wände überschneiden. Jetzt
noch eine Passende Textur drauf legen, z.B.. "kejim/blastdoor_onoff"
und mit Surface Ispector ("S" drücken) anpassen.

![image]({static}Image26.jpg)

Danach müssen wir, dem Brush
noch die Tür-Funktionalität geben. Klicke in der 2D-Ansicht auf rechte
Maustaste (der Brush muss markiert sein! ) und wähle:

func >
func_door.

![image]({static}Image25.jpg)

Als nächstes sollten wir
festlegen, in welche Richtung die Tür aufgeht, wenn wir uns ihr nähern.
Drücke die "N"-Taste und klicke auf "UP", damit die Tür
nach oben aufgeht. In der Key-liste wird dann eingetragen: KEY angle, VALUE -1.

![image]({static}Image24.jpg)

Jetzt kannst du noch die Tür
kopieren (Leertaste) und die Kopie in die Wand des anderen Raumes setzen. 

![image]({static}Image23.jpg)

Damit haben wir einen schönen
Durchgang geschaffen, der von beiden Seiten jeweils eine Tür hat :D

![image]({static}Image22.jpg)

Danach, können wir in dem
anderen Raum noch einen Gegner setzten, damit das Testen nicht ganz so
langweilig wird. 

Drücke rechte Maustaste in der
2D Ansicht (innerhalb des zweiten Raumes) und wähle "NPC"
> "NPC_Reborn"

Jetzt kannst du noch, in dem Gang
ein paar passende Texturen setzen und dann speichern. Die Map speichern wir
unter dem Namen "tworooms"

![image]({static}Image21.jpg)

Jetzt JKII im SP-Modus starten, Konsole
aufmachen und angeben "map tworooms"

Und im Spiel sieht das ganze dann
so aus:

![image]({static}Image42.jpg)

so, das innere des Ganges:

![image]({static}Image44.jpg)

und da kommt auch schon unser
Gegner, ... AUA !!!  :D

![image]({static}Image43.jpg)

 

----

 

[u][DOWNLOAD
DER TUTORIAL MAP](../../downloads/tworooms.zip)[/u]

(.map
- Datei und enthalten)

----

**TIP:**
 Beim Verbinden von
Räumen und Bauen vor Durchgängen achte darauf, dass keine undichten Stellen
entstehen. Denn sonst hast du ein LEAK (ein Leck, siehe Fehlerliste) und die Map
lässt sich nicht mehr kompilieren. Vor allem beim Umgang mir der "CSG
- Substract" Funktion
sollte man sehr vorsichtig sein und sie nur dann benutzten, wenn man ganz genau weißt,
was als Ergebnis herauskommt.

----

Alle
  Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet: 

©
  2000 - 2003 (Artur L.) [www.darth-arth.net](http://www.darth-arth.net)

Nur
  zur privaten Nutzung. Kopieren nicht gestattet. Darth-Arth.Net ist ausdrücklich
  nicht für den Inhalt externer Seiten verantwortlich. Es gelten die
  angegebenen Nutzungsbedingungen.

 

