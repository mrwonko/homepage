title: Performance & FPS Optimierung: Hint - Portale
author: Darth Arth (Artur L.)
date: 2004-01-01
modified: 2015-04-14
category: advanced
type: tutorials/darth-arth
tags: Vis, Hintportal, auto-generated
slug: vis-hint

**>>
Mapping Academy - Tutorials <<**

 

(c)
2003 [www.darth-arth.net](http://www.darth-arth.net)

----

Performance , FPS -Optimierung:
Hint-Portale

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

>>
Mein Erster Raum ( [Tutorial](mapping/firstroom/firstroom.htm) )<<

>>
Zwei Räume verbinden, erste Tür ( [Tutorial](mapping/tworooms/tworooms.htm) )<<

>>
Performance, FPS Optinierung:Area-Portale ( [Tutorial](mapping/aportals/aportals.htm) )<<

----

In
dieser Lehreinheit (Tutorial) wird beschrieben, wie man mit Hilfe der Hint-Portale
die FPS-Rate einer Map durch VIS-Blocking mit Hint-Portalen verbessern kann.

----

 

**WAS
SIND HINT-PORTALE ?**

 

Hint
Portale dienen, ähnlich wie die Area-Portale, dem VIS-Blocking. 

Das
bedeutet, dass man mit ihrer Hilfe, die Q3-Engine dran hindern kann, die Teile
der Map zu berechnen, die der Spieler sowieso nicht sehen kann. 

Es gibt jedoch einige
Unterschiede in der Funktion der Hint Portale im Vergleich zu den Area-Portalen:

- Anzahl der Hint-Portale ist
nicht begrenzt (nur durch die Brush-Zahl Begrenzung 32.000)

- Hint-Portale benötigen keine
Türen (wie Area-Portale)

- Hint-Portale funktionieren NUR
in gut verwinkelten Maps (man darf nicht durch sie durchsehen können)

- Hint-Portale können auch in
Outdoor-Maps genutzt werden.

- Hint-Portale funktionieren nur
dann richtig, wenn die Map mit FULLVIS kompiliert wurde.

----

 

**WIE
SETZE ICH HINT-PORTALE ?**

 

Die
Hint Portale müssen an der Stelle, wo sie gesetzt werden, den Raum komplett
Teilen. Das heisst, sie müssen an allen 4 Seiten den Raum abdichten. 

Noch
wichtiger: [u]sie müssen mindestens
8 Einheiten in die angrenzenden Brushes einschneiden[/u],
sonst funktionieren sie nicht!

Man
erstellt einen dünnen Brush (aber mindestens 8 Einheiten), der einen Raum
(überwiegend einen Korridor) abdihtet, Er Sollte von allen 4 Seiten (beide
Wände, Decke und Boden) mindestens mit 8 Einheiten in die anderen Brushes
einschneiden, siehe Bild unten:

![image]({filename}mapping/hinportals/Image8.jpg)

Dann belegt man den Brush mit der
Textur "system/hint".![image]({filename}mapping/hinportals/hint.jpg)

Damit die Hint-Portale ihre
Funktion erreichen, müssen mehre Hint-Brushe den Raum in viele Abschnitte
Teilen. 

![image]({filename}mapping/hinportals/Image1_a.jpg)

Die Sichtbarkeit der einzelnen
Abschnitte entscheidet dann, ob die Hint-Portale funktionieren oder nicht.

Deswegen sind nur gut verwinkelte
Bereiche einer Map für die Hint-Portale geeignet, z.B. Korridore, Räume mit
vielen Winkeln, Cannyons in Außenmaps usw.

![image]({filename}mapping/hinportals/Image1_b.jpg)

Um die richtige Anwendung der
Hint-Portale zu zeigen, habe ich eine Beispiel-Map gebastelt. Ich habe ein
herkömmliches Raum-Prefab genommen und diesen 3 mal reingesetzt. Dann habe ich
die 3 Räume mit 2 Korridoren verbunden, wobei jeder der Durchgänge 2 mal
abgewinkelt wurde. Siehe auf dem Bild unten:

![image]({filename}mapping/hinportals/Image4.jpg)

Hier noch mal, die Sicht auf die gesetzten
Hint-Brushes, im 3D-Fenster:

![image]({filename}mapping/hinportals/Image3.jpg)![image]({filename}mapping/hinportals/Image10.jpg)

----

Um die Wirkung der Hint-Portale
zu zeigen, habe ich 2 Versionen der Map erstellt. Eine Version ist mit den
Hint-Brushes und die andere ohne. 

So sieht die mit Fullvis
kompilierte Map, ohne der gesetzten Hint-Portale. 

Man sieht deutlich, das die
Engine die komplette Map berechnet.

![image]({filename}mapping/hinportals/hint4.jpg)

Und so, sieht die Map-Version mit
den gesetzten Hint-Portalen. 

Man kann gut erkennen, dass
obwohl der Raum keine Tür besitzt, nur der Sichtbare Abschnitt der Map, von der
Q3-Engine, berechnet wird.

![image]({filename}mapping/hinportals/hint3.jpg)

----

Hier noch mal, illustrativ
dargestellt, die Funktionalität der Hint-Portale.

So sieht es aus, so lange wir um
dei Ecke bleiben :

![image]({filename}mapping/hinportals/hint1.jpg)

und so, wenn wir
weitergehen. 

Man erkennt ganz gut, wie die
Hint-Portale ihre Wirkung verlieren, sobald wir durch den unsichtbaren
Hint-Brush durchgehen.

![image]({filename}mapping/hinportals/hint2.jpg)

----

Link zum Download beider Maps
findest du unten in diesem Tutorial. 

Um die Wirkung der Hintportale zu
testen:

1. Starte JKII im SP-Modus

2. Öffne die Konsole und gebe
ein

map nohintportals
(für die Version ohne Hintportale)

map hintportals
(für die Version mit Hint-Brushes)

3. Nach dem die Map geladen
wurde, öffne noch mal die Konsole und gebe ein:

helpusobi 1

r_showtris 1

----

[u][DOWNLOAD
DER TUTORIAL MAP](downloads/hintportals.zip)[/u]

(Beide
.map - Dateien enthalten)

----

**TIP:**
    Plane deine Map, bevor du anfängst sie zu
bauen. Wenn Du Hint-Portale einsetzen möchtest, muss die Map genug
Winkel-Abschnitte besitzen. So kannst du die Wirkung der Hint-Portale optimal nutzen.

----

Alle
  Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet: 

©
  2000 - 2003 (Artur L.) [www.darth-arth.net](http://www.darth-arth.net)

Nur
  zur privaten Nutzung. Kopieren nicht gestattet. Darth-Arth.Net ist ausdrücklich
  nicht für den Inhalt externer Seiten verantwortlich. Es gelten die
  angegebenen Nutzungsbedingungen.

