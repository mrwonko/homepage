title: Performance & FPS Optimierung: Area - Portale
author: Darth Arth (Artur L.)
date: 2004-01-01
modified: 2015-04-14
category: advanced
type: tutorials/darth-arth
tags: Vis, Areaportal, auto-generated
slug: vis-area-portals

**>>
Mapping Academy - Tutorials <<**

 

(c)
2003 [www.darth-arth.net](http://www.darth-arth.net)

----

Performance , FPS -Optimierung:
Area-Portale

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

>>
Zwei Räume verbinden, erste Tür ( [Tutorial](../tworooms/tworooms.htm) )<<

 

----

In
dieser Lehreinheit (Tutorial) wird beschrieben, wie man mit Hilfe der
Area-Portale auch große Maps spielbar machen kann.

----

Als erstes, benötigen wie einen
einfachen Raum, wie in dem Tutorial >> "[Mein
erster Raum](../firstroom/firstroom.htm)" << beschrieben. Nur sollte er nicht ganz so groß
sein, max. 1000 x 1000 Map - Einheiten.

Bitte ESC-Taste drücken um
sicher zu gehen, dass nichts markiert ist. Dann, legen wir in der 2D-Ansicht
einen Brush um den kompletten Raum, siehe Bild unten:

![image]({filename}../tworooms/Image39.jpg)

Jetzt klicken wir auf ![image]({filename}../tworooms/Image40.jpg)
um den ganzen Inhalt zu markieren.

![image]({filename}../tworooms/Image38.jpg)

Jetzt kopieren (Leertaste) wir
diesen Raum 16 mal, und legen die Räume dicht bei einander, aber so, dass da
noch jeweils ein Gang dazwischen passt. Jetzt müssen wir noch zwischen den
Räumen Durchgänge bauen, 

so wie es im Tutorial >> [zwei
Räume verbinden](../tworooms/tworooms.htm) << beschreiben wurde. 

[u]Tip:[/u] Erstelle zuerst den Brush
zum Ausschneiden der Wände und mache überall Löscher rein, wo später ein
Gang rein kommt. Baue dann, einen Durchgang mit mindestens 1 Tür, kopiere den
15 mal und baue an den entsprechenden Stellen wieder ein. So sparst du Zeit und
Arbeit :D

![image]({filename}../tworooms/Image21.jpg)

Zum Schluss solltest du einen
Raumkomplex haben, der ungefähr so, wie auf dem Bild unten, aussieht und genau
16 Durchgänge, sowie 17 Räume hat.

Das "info_player_start"
sollte sich im ersten Raum befinden, und in den anderen Räumen solltest du
mindestens 1 Gegner positionieren , wenn möglich in die Nähe einer Tür :D

![image]({static}Image51.jpg)

Wenn du fertig bist, speichere
die Map unter dem Namen: "rooms_noaportals"
und kompiliere mit "Fastvis
(nolight)".

Starte dann JKII-SP Modus, öffne
Konsole und gebe ein:

map rooms_noaportals

nach dem die Map geladen wurde,
öffne noch mal die Konsole und gebe ein

helpusobi
1

cg_drawfps
1

r_showtris
1

![image]({static}Image52.jpg)

Du siehst, die Q3-Engine
berechnet auch die Räume hinter der geschlossen Tür und die FPS-Rate ist auch
nicht besonders berauschend, obwohl unsere Map noch kaum Details beinhaltet.
Jetzt stell dir vor, es wäre eine riesige und sehr detaillierte Map mit vielen
Gegnern. Solche Maps sind ohne Area-Portale nicht spielbar egal ob MP- oder
SP-Modus. Und wenn der Entwickler keine Möglichkeiten offen gelassen hat, noch
Türen einzubauen und die Räume durch Area-Portale abzudichten, dann ist so
eine Map meistens verloren, oder es muss viel Arbeit in den Umbau rein gesteckt
werden. Hier ist eine große Frust vorprogrammiert.

![image]({static}Image54.jpg)

Dann fangen wir doch mal an,
unsere Räume mit Türen und Area-Portalen abzudichten. Area-Portale sind so was,
wie eine unsichtbare Blockade für die Q3-Engine, damit diese nicht den
unsichtbaren Teil der Map unnötig berechnet und so, sehr negativ die FPS-Rate
beeinflusst. 

Wie baut man Area Portale ein?
Area-Portale funktionieren nur in Verbindung mit Türen und die Räume die abschottet
werden, dürfen keine sonstigen Öffnungen oder duschsichtbare Fenster besitzen.
Am besten eignen sich einfache Türen die aus max. 4 Bruches bestehen und sich durch
einen einzigen Brush exakt überdecken lassen. Erstelle jetzt in jedem Durchgang
einen Brush, der genauso groß ist wie die Tür (nur 1 Tür pro Durchgang) 
und ganz genau die gleiche Breite hat und somit die komplette Tür überdeckt.
Wähle jetzt die Textur system/areaportal und ordne sie diesem Brush zu. 

[u]ANMERUNG:[/u]
Falls du auf die Idee kommst, einfach die Tür zu kopieren, dann achte bitte
darauf, dass der Area.Portal Brush keine "func_door"
funtionalität besitzen darf. Um die aus dem Brush zu löschen, klicke rechte
Maustaste und wähle "ungroup
Entity" (die kopierte
Tür, muss zu diesem Zeitpunkt markiert sein)

Wenn du jetzt fertig bist,
überprüfe noch mal, ob beide Brushes richtig sind (Tür-Brush = "func_door"
& Tür-Textur, AreaPortal = Worldspawn & Areaportal-Textur, wenn nötig
verschiebe sie ein wenig, um sie auseinander halten zu können) und wenn alles
OK ist, bringe beide wieder in die richtige Position. [u]Die
beiden Brushes müssen sich komplett überdecken![/u]
Das heißt, die Tür und der Area-Portal Brush, sollen exakt die gleiche Größe
und Position haben.

![image]({static}Image49.jpg)

Wiederhole diese Tätigkeit für
alle anderen Türen, aber nur ein mal pro Gang, denn du musst daran
denken: 

man darf nur **max.
16 Area-Portale** pro Map
nutzen!

![image]({static}Image50.jpg)

Wenn du fertig bist, speichere
die Map unter einem neuen Namen: "rooms_aportals"
und kompiliere sie mit "Fastvis
(nolight)".

Starte dann JKII-SP Modus, öffne
Konsole und gebe ein:

map rooms_aportals

nach dem die Map geladen wurde,
öffne noch mal die Konsole und gebe ein

helpusobi
1

cg_drawfps
1

r_showtris
1

Jetzt kann man die Funktion der
Area-Portale gut erkennen. Die Q3-Engine berechnet nur den Raum, in dem wir uns
befinden, die Räume dahinter werden nicht mehr berechnet. Das wirkt sich
natürlich auch sehr gut auf unsere FPS-Rate.

![image]({static}Image55.jpg)

Wirkung des Area-Portals in der
Tür, **Tür geschlossen: 52
FPS**

![image]({static}Image56.jpg)

Wirkung des Area-Portals in der
Tür, **Tür offen: 14 FPS**

Ups!,
da stimmt doch was nicht !, sollten die anderen Area-Portale nicht die anderen
Räume auch abdichten ? 

Wieso
kann man die dann sehen ?.

Ja...,
ich bin fies und habe dich absichtlich, einen Fehler in die Map einbauen lassen
um die Wirkung noch ein wenig zu verstärken. 

Es
sind die Gegner, die zu dicht an der Tür stehen und dafür sorgen, dass diese
nicht geschlossen werden kann  :D

So, du hast aber jetzt genug
gelernt und geschuftet. Also Los!, geh und sorge dafür, dass die Türen alle
wieder zu sind :D

P.S. die komische 
Drahtmodel-Sicht kannst du mit "r_showtris
0" wieder ausschalten.

![image]({static}Image57.jpg)

----

[u][DOWNLOAD
DER TUTORIAL MAP](../../downloads/aportals.zip)[/u]

(Beide
.map - Dateien enthalten)

----

**TIP:**
    Setze die
Area-Portale mit Bedacht ein und plane deine Map, bevor du anfängst sie zu
bauen. So kannst du die Wirkung der Area-Portale optimal nutzen.

----

Alle
  Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet: 

©
  2000 - 2003 (Artur L.) [www.darth-arth.net](http://www.darth-arth.net)

Nur
  zur privaten Nutzung. Kopieren nicht gestattet. Darth-Arth.Net ist ausdrücklich
  nicht für den Inhalt externer Seiten verantwortlich. Es gelten die
  angegebenen Nutzungsbedingungen.

 

