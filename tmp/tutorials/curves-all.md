title: Der effiziente Umgang mit Curves und Patches
author: Chux (Mike H.S.)
date: 2004-01-01
modified: 2015-04-14
category: mapping
type: tutorials/darth-arth
tags: Curves, auto-generated
slug: curves-all

**>> Mapping Academy - 
Tutorials <<**

 

(c) 2004 [http://www.darth-arth.de](http://www.darth-arth.de)

----

Der effiziente Umgang mit Curves und 
Patches

Autor: Chux ( Mike H.S.)

**[u]VORAUSSETZUNGEN[/u]:**

>> Installation JK2 
Editing Tools I ( [Tutorial](../../radiant/jk2_etools1.htm) 
)<<

>> Installation JK2 
Editing Tools 2 ( [Tutorial](../../radiant/jk2_etools2.htm) 
)<<

>> Installation GTK - 
Radiant ( [Tutorial](../../gtk14/install/gtk14.html) 
)<<

>> Mein Erster Raum ( [Tutorial](../firstroom/firstroom.htm) 
)<<

----

In dieser Lehreinheit (Tutorial) wird 
der effiziente Umgang mit Curves 
& Patches beschrieben.

----

**
**

[Was sind 
Curves und Patches](#about)

[Erklärung 
der einzelnen Untermenü-Punkte](#menu)

[Der 
Bereich Cylinder](#section_cylinder)

[Der 
Bereich End Cap & Bevel](#section_endcap_bevel)

[Der 
Bereich Cone](#section_cone)

[Der 
Bereich Simple Patch](#section_simple_patch)

[Der 
Bereich Columns](#section_columns)

[Der 
Bereich Matrix](#section_matrix)

[Der 
Bereich Cap Selection](#section_cap_selection)

[Der 
Bereich Cycle Cap Texture](#section_cycle_cap_texture)

[Der 
Bereich Overlay](#section_overlay)

[Der 
Bereich Thicken](#section_thicken)

[Die 
Bearbeitung von Patch-Texturen](#textures)

[Ein 
Simple Patch Mesh](#simple_patch_mesh)

[Einen 
Torbogen erstellen](#torbogen)

----

**Was sind Curves und Patches**

Curves sind im Grunde genommen das Selbe wie Patches, sodass ich hier für 
beide Begriffe zusammen eine Erklärung schreiben werde:

Es handelt sich hierbei um editierbare Flächen, denen man durch Punktsysteme beliebige Formen zuweisen kann. Da Curves keine Dichte oder Dicke haben, muss man 
aus mehreren Curves eine Simulation eines dreidimensionalen Objektes erstellen. 
Das bedeutet, dass man z.B. für einen Würfel sechs Curves erstellen müsste, von 
denen jedes eine Seite darstellen würde.

In diesem Tutorial werde ich euch erklären, wie genau man effiezient mit 
Curves arbeitet und selber eigene Formen erstellen kann.

----

**Erklärung der einzelnen 
Untermenü-Punkte** 

**Der Bereich Cylinder**

Der Bereich Cylinder im 
Untermenü Curve beinhaltet einen 
Menüpunkt, nämlich Cylinder, und 
ein weiteres Untermenü, nämlich More 
Cylinders, welches wiederum drei weitere Menüpunkte enthält, nämlich 
Dense Cylinder, Very Dense Cylinder und Square Cylinder.

Ein Klick auf den Punkt Cylinder macht einen zuvor markierten Brush zu einem zylinderförmigen
Patch mit drei vertikalen und drei horizontalen 
Steuerungspunkten.

Ein Klick auf den Punkt Dense 
Cylinder macht einen zuvor markierten Brush zu einem zylinderförmigen Patch mit fünf vertikalen und drei horizontalen 
Steuerungspunkten.

Ein Klick auf den Punkt Very Dense 
Cylinder macht einen zuvor markierten Brush zu einem zylinderförmigen Patch mit neun vertikalen und drei horizontalen 
Steuerungspunkten.

Ein Klick auf den Punkt Square 
Cylinder macht einen zuvor markierten Brush zu einem quaderförmigen Patch 
mit drei vertikalen und drei horizontalen Steuerungspunkten.

Hier noch mal in der Übersicht:

![image]({filename}pic8.gif)

**Der Bereich End Cap & Bevel**

Der Bereich End Cap & 
Bevel im Untermenü Curve 
beinhaltet zwei Menüpunkte, nämlich End 
Cap und Bevel, und ein 
weiteres Untermenü, nämlich More End Caps, 
Bevels, welches wiederum zwei weitere Menüpunkte enthält, nämlich Square End Cap und Square Bevel.

Ein Klick auf den Punkt End 
Cap macht einen zuvor markierten Brush zu einem halbkreisförmigen Patch 
mit drei vertikalen und drei horizontalen Steuerungspunkten - Ende 
geöffnet.

Ein Klick auf den Punkt Bevel macht einen zuvor markierten Brush zu einem 
viertelkreisförmigen Patch mit drei vertikalen und drei horizontalen 
Steuerungspunkten - Ende geöffnet.

Ein Klick auf den Punkt Square End 
Cap macht einen zuvor markierten Brush zu einem halbkreisförmigen Patch 
mit drei vertikalen und drei horizontalen Steuerungspunkten - Ende 
geschlossen.

Ein Klick auf den Punkt Square 
Bevel macht einen zuvor markierten Brush zu einem viertelkreisförmigen 
Patch mit drei vertikalen und drei horizontalen Steuerungspunkten - Ende 
geschlossen.

Hier noch mal in der Übersicht:

![image]({filename}pic9.gif)

**Der Bereich Cone**

Der Bereich Cone im 
Untermenü Curve beinhaltet lediglich
einen Menüpunkt, nämlich Cone.

Ein Klick auf den Punkt Cone 
macht einen zuvor markierten Brush zu einem zylinderförmigen Patch mit drei 
vertikalen und drei horizontalen Steuerungspunkten - nach oben spitz 
zulaufend.

Hier ein kleines Bild:

![image]({filename}pic10.gif)

**Der Bereich Simple Patch**

Der Bereich Simple Patch im 
Untermenü Curve beinhaltet lediglich
einen Menüpunkt, nämlich Simple 
Patch Mesh....

Ein Klick auf den Punkt Simple 
Patch Mesh... macht einen zuvor markierten Brush zu einem 2-dimensionalen 
Simple Patch (standardmäßig mit drei vertikalen und drei horizontalen 
Steuerungspunkten, Zeilen und Spalten allerdings 
konfigurierbar).

**Der Bereich Columns**

Der Bereich Columns 
beinhaltet zwei Untermenüs, nämlich Insert und Delete. 
Das Untermenü Insert beinhaltet 
vier Menüpunkte, nämlich Insert (2) 
Columns, Add (2) Columns, 
Insert (2) Rows und Add (2) Rows. Das Untermenü Delete beinhaltet vier Menüpunkte, 
nämlich Delete First (2) Columns, 
Delete Last (2) Columns, Delete First (2) Rows und Delete Last (2) Rows.

**Insert**

Insert (2) Columns - Fügt 
eine Spalte an den Anfang (links) des Simple Patches.

Add (2) Columns - Fügt eine 
Spalte ans Ende (rechts) des Simple Patches.

Insert (2) Rows - Fügt eine 
Zeile an den Anfang (oben) des Simple Patches.

Add (2) Rows - Fügt eine 
Zeile ans Ende (unten) des Simple Patches.

**Delete**

Delete First (2) Columns - 
Löscht die Spalte am Anfang (links) des Simple Patches.

Delete Last (2) Columns - 
Löscht die Spalte am Ende (rechts) des Simple Patches.

Delete First (2) Rows - 
Löscht die Zeile am Anfang (oben) des Simple Patches.

Delete Last (2) Rows - 
Löscht die Zeile am Ende (unten) des Simple Patches.

**Der Bereich Matrix**

Der Bereich Matrix 
beinhaltet ein Untermenü, nämlich Matrix. Das Untermenü Matrix beinhaltet drei Menüpunkte, nämlich Invert, Re-Disperse und Transpose.

Matrix - Kehrt die 
Texturfläche eines Simple Patches, sowie eines Komplex Patches auf die 
gegenüberliegende Seite.

Der Rest ist erstmal nicht notwendig.

**Der Bereich Cap Selection

**

Der Bereich Cap Selection 
beinhaltet lediglich einen Menüpunkt, nämlich Cap Selection.

Cap Selection 
- Bei Cylinder- und Cone-Patches wird automatisch eine Art 
Deckel oben und unten generiert. Bei Bevels und End Caps erscheint folgendes 
Fenster:

![]({filename}pic11.gif)

#Bei einem zuvor markierten [color=rgb(51,255,255)]Bevel[/color] wird hier nun entweder der Punkt 
[color=rgb(51,255,255)]Bevel[/color] oder der Punkt [color=rgb(51,255,255)]Inverted Bevel[/color] 
ausgewählt.Bei einem zuvor markierten [color=rgb(51,255,255)]End Cap[/color] wird hier nun entweder der Punkt 
[color=rgb(51,255,255)]End Cap[/color] oder der Punkt Inverted 
[color=rgb(51,255,255)]End Cap[/color] ausgewählt.

Wenn man 
sich das Fenster oben genau ansieht, erkennt man neben den Auswahlpunkten 
jeweils eine kleine Grafik. Diese zeigt mithilfe des blauen Bereiches, welcher 
Form der zu generierende Deckel später haben wird. Aber soetwas musst du selber 
ausprobieren, es lässt sich schwer mit Worten erklären.

**

Der 
Bereich Cycle Cap Texture

**

Der Bereich Cycle Cap Texture beinhaltet lediglich einen 
Menüpunkt, nämlich Cycle Cap 
Texture.

Cycle Cap 
Texture -  Verändert die Ausrichtung der Textur 
eines Patches

Diesen Punkt wirst du wahrscheinlich nicht sehr oft 
brauchen, daher erkläre ich ihn nicht näher.

**Der Bereich 
Overlay

**

Der Bereich Overlay beinhaltet lediglich ein Untermenü, nämlich Overlay, mit zwei Untermenüpunkten, 
nämlich Set und Clear.

Diese Menüpunkte wirst du 
genauso kaum benötigen. Deshalb sind sie hier erst mal nicht weiter erklärt.

**

Der Bereich 
Thicken

**Der Bereich Thicken beinhaltet lediglich einen Menüpunkt, nämlich Thicken....

Thicken... - Ein Klick auf 
diesen Punkt öffnet folgendes Fenster:

![]({filename}pic6.gif)

In 
dem Eingabefeld Amount 
wird ein Wert angegeben. Dieser steht für die Anzahl an 
Units, die ein Simple Patch, sowie ein Complex Patch nach der Bestätigung 
"vertieft" wird.

Mit "vertieft" meine ich die Tiefe im 3-dimensionalen 
Raum.

----

**Die Bearbeitung von 
Patch-Texturen

**Texturen auf Patches bearbeitet man 
ähnlich, wie die Texturen auf simplen Brushes - Nur nicht mir dem [color=rgb(51,255,255)]Surface Inspector[/color], sondern mit den [color=rgb(51,255,255)]Patch Properties[/color]. Folgendes Fenster wird 
geöffnet, wenn du die Tastenkombination [color=rgb(51,255,255)]Shift + S[/color] drückst. Vorher allerdings 
solltest du einen Patch markiert haben:

![]({filename}pic12.gif)

Wie 
du siehst, ähnelt dieses Fenster sehr dem Surface Inspector. Auch die Funktionen 
der Auswahl- und Eingabefelder sind ähnlich:

[color=rgb(51,255,255)]Horizontal Shift Step[/color] - Bestimmt die 
horizontale Lage der Textur auf dem Patch.

[color=rgb(51,255,255)]Vertical Shift Step[/color] - Bestimmt die 
vertikale Lage der Textur auf dem Patch.

[color=rgb(51,255,255)]Horizontal Stretch Step[/color] - Bestimmt den 
Grad der horizontalen Verzerrung der Textur auf dem 
Patch.

[color=rgb(51,255,255)]Vertical 
Stretch Step[/color] - Bestimmt den Grad der vertikalen Verzerrung der Textur auf 
dem Patch.

[color=rgb(51,255,255)]Rotate Step[/color] - 
Bestimmt den Winkel, um den die Textur auf dem Patch gedreht wird.

----

**

Ein Simple Patch 
Mesh**

Ein Simple Patch Mesh ist, wie im obigen Kapitel erklärt, eine einzelne Patch-Fläche, der eine beliebige 
Form zugewiesen werden kann. Wie man ein Simple Patch Mesh erstellt und es dann 
editiert, erkläre ich euch jetzt.

Als erstes erstellt ihr einen einfachen Brush. Markiert den Brush und 
klickt unter dem Menüpunkt Curve 
auf Simple Patch 
Mesh...:

![image]({filename}pic1.gif)

Dann dürfte sich ein Fenster öffnen, das wie Folgendes 
aussieht:

![image]({filename}pic2.gif)

In dem Fenster befinden sich zwei Eingabefelder: Width und Height - In diese Felder wird die Anzahl der vertikalen und 
horizontalen Punkte auf dem späteren Curve eingegeben. Momentan befinden sich 
die Werte 3 und 3 in den Feldern. Für eine simple Form reichen neun 
Punkte (3 mal 3) allemal aus. Klicke auf Ok. Aus deinem ehemaligen Brush sollte nun eine 2-dimensionale 
Fläche geworden sein, wie das folgende Bild zeigt:

![image]({filename}pic3.gif)

Während das Curve noch markiert ist, drücke die Taste V, um somit die einzelnen Punkte des Curves frei zu 
legen und das Curve bearbeiten zu können. Das Ergebnis sollte dann so 
aussehen:

![image]({filename}pic4.gif)

Wie du siehst, befinden sich nun in der Vertikalen je drei Punkte, sowie 
in der Horizontalen je drei Punkte, sodass die Form des Curves insgesamt von 
neun Punkten gesteuert wird. Klicke nun einen der äußeren Punkte an und 
verschiebe ihn noch weiter nach außen. Du wirst sehen, dass sich die Form des 
Curves mit der Position des Punktes verändert. Verschiebe noch ein paar Punkte, 
sodass irgendwann eine kurvige und egale Form entsteht:

![image]({filename}pic5.gif)

Wie unschwer zu erkennen ist, ist das Curve nach wie vor nur 
2-dimensional. Um das zu ändern, klicke bei markiertem Curve unter dem Menüpunkt 
Curve auf Thicken oder drücke einfach die Tastenkombination 
STRG + T. Es sollte sich nun ein 
Fenster öffnen, das wie Folgendes aussieht:

![image]({filename}pic6.gif)

In dem Fenster befindet sich lediglich ein Eingabefeld. Dieses definiert,
wie viele Units der simulierte Körper nach dem Klick auf Ok dick sein soll. Standard-Wert ist hier 8. Da 
dieser Wert dir fürs Erste wahrscheinlich etwas dünn ist, gib einen beliebigen 
höheren Wert an. Im Beispiel sind es 300 Units. Klicke nach der Eingabe auf 
Ok. Es sollte ungefähr Folgendes in 
der 3D Anzeige zu sehen sein:

![image]({filename}pic7.gif)

Wenn das geklappt hat, ein herzlicher Glückwunsch von mir zu deinem 
ersten selbst gebauten Curve-Gebilde! Es ist zwar noch sinnlos, aber nun kannst 
du all deine Ideen und Vorstellungen darauf anwenden!

----

**Einen Torbogen erstellen

**In diesem 
Abschnitt möchte ich erläutern, wie du schnell, einfach und effizient einen 
Torbogen mit simplen Brushes und einigen Patches erstellen kannst.

Anfänglich 
benötigen wir ein Grundgerüst für den Torbogen. Es besteht aus drei einfachen 
Brushes. Es sollte ungefähr wie folgt aussehen:

![]({filename}pic13.gif)

Nun 
erstellst du einen weiteren kleinen Brush, markierst ihn und machst ihn zu einem 
Bevel, indem du auf [color=rgb(51,255,255)]Curve >> 
Bevel[/color] klickst. Drehe ihn dir zurecht und setze ihn so, dass das Ganze wie 
folgt aussieht:

![]({filename}pic14.gif)

Nun 
markierst du lediglich den Bevel-Patch und klickst auf [color=rgb(51,255,255)]Curve >> Cap Selection[/color]. Es sollte 
sich nun ein Fenster öffnen, das wie Folgendes aussieht:

![]({filename}pic11.gif)

Klicke 
hier [color=rgb(51,255,255)]Inverted Bevel[/color] an und bestätige 
mit [color=rgb(51,255,255)]Ok[/color]. Nun sollte die Lücke 
zwischen Bevel und Brush-Gerüst-Ecke durch zwei Simple Patches ausgefüllt sein, 
wie auf dem folgenden Bild zu sehen ist:

![]({filename}pic15.gif)

Bearbeite 
die Textur des Bevels so, dass sie sich mit dem Rest des Torbogens verbindet, 
kopiere dann das Bevel mit seinen zwei Simple Patches und kopiere es mit der 
[color=rgb(51,255,255)]Leertaste[/color]. Spiegel es, indem du auf 
folgendes Symbol klickst:

![]({filename}pic17.gif)

Nun 
setze es noch an die entgegengesetzte Stelle und dein Torbogen ist fertig. Das 
Ergebnis sollte ungefähr so aussehen:

![]({filename}pic16.gif)

Herzlichen 
Glückwunsch zu deinem ersten richtigen Torbogen!

 

----

Alle Bilder, 
Texte, Grafiken, wenn nicht anders gekennzeichnet: 

© 2000 -
  2004 
(Artur L.) [www.darth-arth.de](http://www.darth-arth.de)

Nur zur 
privaten Nutzung. Kopieren nicht gestattet. Darth-Arth.de ist ausdrücklich 
nicht für den Inhalt externer Seiten verantwortlich. Es gelten die angegebenen 
Nutzungsbedingungen. 

  
