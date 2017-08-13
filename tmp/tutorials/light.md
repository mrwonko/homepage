title: Licht
author: Killermic (Michael S.)
date: 2004-01-01
modified: 2015-04-14
category: mapping
type: tutorials/darth-arth
tags: Beleuchtung, auto-generated
slug: light

**>>
Mapping Academy - Tutorials <<**

 

(c)
2004 [www.darth-arth.de](http://www.darth-arth.de)

----

Licht

Author: Killermic ( Michael S.)

**[u]VORAUSSETZUNG[/u][u]EN[/u]:**

>>
Installation GTK - Radiant ( [Tutorial](../../radiant/gtk_radiant.htm)
)<<

>>
Mein erster Raum ( [Tutorial](../../mapping/firstroom/firstroom.htm)
)<<

>>
Kompilieren mit Q3map2 ( [Tutorial](../../q3map2.htm)
)<<

 

----

In dieser Lehreinheit (Tutorial) lernen wir in unserem ersten Raum ein Licht zu setzen. 

Später auch ein paar Tricks um
das Licht schöner aussehen zu lassen.

Dieses Tutorial ist für JK - JA ausgelegt.

----

Nachdem wir unseren ersten Raum erstellt haben möchten wir ein richtiges Licht
reinsetzen.

Zuerst rufen wir unseren ersten Raum
im Editor auf.

**Der sieht jetzt ungefähr so aus:**

![image]({filename}firstroom1.jpg)

Jetzt setzen wir erst einmal unser erstes Licht.

Mit einem Rechtsklick auf das Raster bekommen wir das Entity-Menü und klicken
"**Light**" an.

![image]({filename}entlight.jpg)

Auf der Map erscheint jetzt das Light-Entity und eine Box, wo die Stärke des Licht
abgefragt wird.

**ACHTUNG:** 100 ist ein mäßig starkes Licht, jedoch 300 ist schon ein sehr intensives Licht. Aber die Beleuchtung
hängt immer von dem Typ eurer Map an. Benutzt ihr sehr helle Texturen, so fällt Stärke 100 fast nicht auf. Doch benutzt ihr dunkle Texturen, fällt Stärke 100 schon ziemlich gut auf. Auch auf die Fläche die beleuchtet werden soll, kommt es sehr stark an.

Da wir eine große Fläche beleuchten wollen nehmen wir 4 Lichter, mit jeweils der Stärke 500.

![image]({filename}light1.jpg)

Jetzt schieben wir noch die Light-Entities dort hin, wo wir die Quellen des Lichts haben wollen.

Dazu halten wir **SHIFT** gedrückt und klicken das Light-Entity an. Danach
das Entity einfach mit der Maus an den gewünschten ort schieben.

Jetzt setzen wir die Kenntnisse aus dem Tutorial "[Kompilieren mit Q3map2](../../q3map2.htm)" ein.

Kompiliert mit genau den selben Einstellungen von Q3map2, wie in den Optionen, dann ergibt es ein für den Anfang gutes Licht.

![image]({filename}ingame1.jpg)

Jetzt sehen wir unser erstes Licht im
Spiel:)

----

**[u]Realistische Lichtquellen[/u]** (für etwas Fortgeschrittene)

Realistische Lichtquellen sind oft das Etwas, was eine gute Map ausmacht. Darum wollen wir das jetzt herstellen.

Dazu löschen wir die Lichter die wir vorher gesetzt haben, und machen eine (simple) Konstruktion, die eine Lampe darstellen soll. Darunter habe ich ein Light-Entity gesetzt, mit der Stärke 300:

![image]({filename}lampe1.jpg)

Nachdem wir kompiliert haben, fällt es schon auf:

Es ist zu dunkel! Aber wenn wir das Licht noch heller machen, sieht es wieder unrealistisch aus. Auch eine zweite Lichtquelle sähe nicht gut aus.

Jetzt nutzen wir eine Einstellung im "Worldspawn" aus. Im Worldspawn werden Einstellungen gemacht, die für die **ganze** Map gelten.

Um Einstellungen am "Worldspawn" zu machen, klicken wir einen einfachen Wand-,
Decken- oder Boden-Brush und drücken die Taste "**N"**:

![image]({filename}light4.jpg)

Und zwar tragen wir einen "ambient" - Wert ein. Wir geben folgendes ein:

**KEY:** ambient

**VALUE:** 40

![image]({filename}light5.jpg)

**ACHTUNG:** Ein "ambient"-Wert sollte sehr klein bleiben! 40 ist schon ziemlich hoch. Für eine gut beleuchtete Map sollte ein "ambient"-Wert von 10 reichen, um die schwarzen Flächen, wo kein Licht hinkommt, ein wenig aufzuhellen.
Es kommt immer auf die Atmosphere und die Art eurer Map an, für helle Outdoor (aussengelände)
Maps , kann man sehr hohe Ambient-Werte benutzen, wogegen für gut beleuchtete
Indoor (Innenraum) Maps ein kleiner Wert ausreicht. Meistens heißt es einfach
"ausprobieren" und den richtigen Wert selbst herausfinden.

![image]({filename}ingame2.jpg)

Glückwunsch! Jetzt stehst du in deinem ersten Raum mit realistischer Lichtquelle. (Auf dem Screenshot sieht es etwas dunkel aus, aber im Spiel ist es in Ordnung)

----

**[u]Generelle Fragen[/u]**

Jetzt wollen wir nachträglich von dem Light-Entity die Stärke ändern. Aber wir machen kein Neues und löschen das Alte, sondern wählen das Alte einfach an mit **SHIFT** + Anklicken und drücken daraufhin **>N. Das ruft das **Entity-Menü** auf. Das sollte so aussehen:

![image]({filename}light2.jpg)

Nun klicken wir "light 300" an und ändern unten, in den Eingabefeldern folgendes:
**

Key: light

Value: 350

![image]({filename}light3.jpg)

Und drücken **>ENTER

Jetzt ist das Licht etwas stärker.

**

----

**Farbiges Licht**

Ein rotes Licht machen? Kein Problem!

Wir wählen einfach unser Licht an und drücken **>K

Jetzt erscheint ein Menü, in dem man die Farbe wählen kann.

Jetzt stellen wir dort Rot ein.

![image]({filename}light6.jpg)

Jetzt ist nach einem Klick auf "OK" euer Licht rot. Hier kann man natürlich auch alle möglichen Einstellungen vornehmen um Lichter farbig zu machen :)

**

----

Alle
  Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet: 

©
  2000 - 2004 (Artur L.) [www.darth-arth.de](http://www.darth-arth.de)

Nur
  zur privaten Nutzung. Kopieren nicht gestattet. Darth-Arth.de ist ausdrücklich
  nicht für den Inhalt externer Seiten verantwortlich. Es gelten die
  angegebenen Nutzungsbedingungen.

 

