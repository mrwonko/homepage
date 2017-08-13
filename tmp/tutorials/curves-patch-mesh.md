title: Curves & Patches - Torbogen / archway
author: Darth Arth (Artur L.)
date: 2004-01-01
modified: 2015-04-14
category: mapping
type: tutorials/darth-arth
tags: Curves, auto-generated
slug: curves-patch-mesh

**>>
Mapping Academy - Tutorials <<**

 

(c)
2003 [www.darth-arth.net](http://www.darth-arth.net)

----

Curves & Patches: Tor-Bogen

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
dieser Lehreinheit (Tutorial) wird beschrieben, wie man einen Tor-Bogen mit
Hilfe von Simple Patches
und Curves
erstellt.

----

Zuerst brauchen wir zwei Säulen
(aus 2 normalen, 4-eckigen Brushes). Zwischen den Säulen werden wir unseren
Torbogen bauen.

![image]({filename}Image2.jpg)

Da, es im Editor recht schwierig
ist, runde Formen zu erstellen, benötigen wir ein Hilfsmittel. Wir basteln
einen rechteckigen Brush zwischen den beiden Säulen und zwar so hoch, dass die
obere Kante des Brushes ungefähr dahin kommt, wo unserer spätere Bogen, seine
oberste Kante haben wird.

![image]({filename}Image3.jpg)

Jetzt müssen wir diesen Brush
Rund machen. Um das zu erreichen gehen wir auf "Menu"
> "Brush"
> "Arbitrary sided".

In dem Dialog-Feld tragen wir 32
ein, damit der Brush annähernd rund wird.

![image]({filename}Image4.jpg)   ![image]({filename}Image5.jpg)

----

Nach dem unser Hilfs-Brush fertig
ist, können wir mit dem Bau des Torbogens beginnen. Zuerst erstelle einen
weiteren Brush, wie auf diesem Bild:

![image]({filename}Image6.jpg)

Jetzt müssen wir diesen Brush zu
einem "Patch" konvertieren. Dafür gehen wir ins Menü "Curve"
> "Simple  Patch
Mesh" und tragen jeweils
5
für die Breite (Width) und Höhe (Hight) des Patches. Diese Zahlen legen fest,
wie komplex der Patch sein wird. Generell gilt für Patches un Curves, je größer
die Figur, desto komplexer sollte der Patch sein. Denn sonst kann die Struktur
nicht solide "Löcher" bekommen.

![image]({filename}Image7.jpg)  ![image]({filename}Image8.jpg)

Nach dem unser Patch da ist,
sollten wir prüfen, ob seine sichtbare Seite in die richtige Richtung zeigt.
Wenn es nicht der Fall ist, dass heißt, die sichtbare Seite zeigt nach innen
unseres zukünftigren Bogens (wie auf dem Bild unten), dann müssen wir den
Patch umdrehen.

![image]({filename}Image9.jpg)

Um die Sichtbaren Seiten zu wechseln,
geht man ins Menü "Curve"
> "Matrix"
> "Invert"

![image]({filename}Image10.jpg)

----

Jetzt können wir damit anfangen
unseren Patch zu "verbiegen". Drücke auf die Taste "V",
es erscheinen viele farbigen Punkte. Diese helfen uns, den Patch in die richtige
Form zu biegen.

![image]({filename}Image11.jpg)

Zuerst klicke den Punk unten,
zwischen der Säule und unserem Hilfsbrush. Ziehe den Punkt dann nach unten, wie
auf dem Bild, bis der ungefähr in der Mitte zwischen unserem Hilfsbrush und der
Säule ist.

![image]({filename}Image12.jpg)

Dann versuche die anderem Punkte
nach unten zu ziehen, so dass die untere Kante des Patches, sich mit der runden
Kante des Hilfsbrushes deckt. Wenn du feststellst, dass du zu wenig Punkte hast,
um richtig runde Form zu erreichen, musst du welche hinzufügen. ( weiter unter
dem Bild )

![image]({filename}Image13.jpg)

Um noch paar Punkte hinzufügen,
markiere einen der existierenden Punkte in der Nähe (wie auf dem Bild oben,
blau) und wähle aus dem Menu > "Curve"
> "Insert"
> "add (2) Columns"
oder "add (2) Rows",
je nach dem, was du benötigst. Du brauchst keine Angst zu haben, dass etwas
daneben geht. Du kannst immer, deinen letzten Schritt, durch das Drücken von STRG
+ "Z" ,
rückgängig machen.

![image]({filename}Image14.jpg)

 

Mit den zusätzlichen Punkten,
lässt sich der Patch besser bearbeiten und zu Recht biegen.

![image]({filename}Image15.jpg)

Wenn du mit dem Formen, fertig
bist, drücke ein mal die ESC
- Taste, um den Bearbeitungs-Modus zu beenden.

![image]({filename}Image16.jpg)

Unserer Patch hat jetzt zwar die
richtige Form, ist noch aber viel zu Flach. Bevor wir den Patch dicker machen,
brauchen wir die richtige Breite. 

![image]({filename}Image17.jpg)

Falls, du Dich nicht mehr dran
erinnern kannst, schalte deine 2D-Sicht auf "top" und klicke eine der
Säulen, um die Maße zu sehen.

Wenn es in deinem Editor nicht
angezeigt wird, kannst du es im Menü einstellen, unter "Edit"
> "Preferences",
dann unter "2D Display/Renderin"
> "Display Size Info"
anklicken.

![image]({filename}Image18.jpg)

----

Jetzt drücke ESC und markiere
wieder unseren Patch. 

Da wir jetzt die Maße kennen,
können wir unserem Patch, die richtige Breite verpassen

![image]({filename}Image17.jpg)

Gehe ins Menü > "Curve"
> "Thicken...",
in der Dialogbox gebe dann die Breite an. In unserem Fall, die 32 (Einheiten).

![image]({filename}Image19.jpg)   ![image]({filename}Image20.jpg)

Als Ergebnis, bekommen wir die
Hälfte unseres Torbogens. Jetzt müssen wir, diese Figur nur noch kopieren.

![image]({filename}Image21.jpg)

Um dies zu tun, drücke einfach
auf die Leertaste.

![image]({filename}Image22.jpg)

So, jetzt haben wir die andere
Hälfte unseres Bogens, nur leider falsch rum.

![image]({filename}Image23.jpg)

Um die Kopie zu drehen, geh ins
Menü "Selection"
> "Rotate"
> "Arbitrary rotation".
In dem Dialogfeld, gebe unter "Z",
180
ein und klicke "Apply"
um die Figur zu drehen. Klicke dann auf OK

![image]({filename}Image24.jpg)    ![image]({filename}Image25.jpg)

Jetzt muss alles noch ein wenig
zu Rech geschoben werden und wir sind auch fast mit dem Bauen fertig.

![image]({filename}Image26.jpg)

Da unser Bogen steht, können wir
den Hilfsbrush löschen. Markiere den runden Hilfsbrush und drücke die Taste
"Back-Space"

![image]({filename}Image27.jpg)

Gratuliere, du hast deinen
Torbogen fertiggestellt.

![image]({filename}Image28.jpg)

----

**TIP:**
    Wenn man
Figuren und Objekte aus Curves und Patches baut, sollte man sie immer mit der
Funktion "func_group" zusammen binden. Denn Curves und Patches sind
nur von einer Seite sichtbar und falls etwas verschoben, gedreht oder gelöscht
werden muss, könnten Konstruktions-Teile übrig bleiben.

----

Alle
  Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet: 

©
  2000 - 2003 (Artur L.) [www.darth-arth.net](http://www.darth-arth.net)

Nur
  zur privaten Nutzung. Kopieren nicht gestattet. Darth-Arth.Net ist ausdrücklich
  nicht für den Inhalt externer Seiten verantwortlich. Es gelten die
  angegebenen Nutzungsbedingungen.

 

