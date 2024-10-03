title: Richtiges Licht in Outdoor-Maps
author: Shooter ( Oliver M.)
date: 2004-01-01
modified: 2015-04-14
category: advanced
type: tutorials/darth-arth
tags: Beleuchtung, auto-generated
slug: light-sun

**>> 
  Mapping Academy - Tutorials << **

(c) 2003 [http://www.darth-arth.de](http://www.darth-arth.de)

----

**Outdoor-Mapping 
  - Das richtige Licht
( Tutorial by Shooter )**

**VORRAUSSETZUNGEN**

>> Installation JK2 
  Editing Tools I ( [ Tutorial](radiant/jk2_etools1.htm) )<<

  >> Installation JK2 Editing Tools 2 ( [ Tutorial](radiant/jk2_etools2.htm) )<<

  >> Installation GTK - Radiant ( [ Tutorial](radiant/gtk_radiant.htm) )<<

  >> Terrain-Entities mit [ EasyGen](mapping/easygen/easygen.htm)

----

In diesem Tutorial werden 
  wir das Setzen von Licht in freier Wildbahn (Outdoor) kennen lernen. Ihr braucht 
  dazu eine Map mit einer schon vorhandenen Skybox und einem Gelände, auf 
  dem ihr euch bewegen könnt. Falls ihr diese Sachen noch nicht haben solltet 
  und auch nicht wisst, wo ihr so etwas herbekommt, dann absolviert unbedingt 
  erst das Tutorial "Terrain-Entities mit EasyGen" von der Mapping Academy.

----

Im Gegensatz zur Beleuchtung 
  in abgeschlossenen Räumen verwenden wir im Landschaftsbereich keine Punktlichter 
  zur Beleuchtung. Viele Punklichter erzeugen unwirkliche Schatten und Lichtverhältnisse, 
  da es in der Natur nun einmal nur eine einzige Lichtquelle gibt und das ist 
  eine Sonne bzw. ein Mond. Wir wollen daher einen echten Schattenwurf der Modelle 
  haben und somit helle beschienene und dunkle schattige Plätze erstellen. 
  Die Beleuchtung selbst setzt sich aus zwei Teilen zusammen: Ambientes Licht 
  & Direktes Licht

----

**1. Ambientes Licht**

Unter ambienten Licht versteht 
  man die Grundhelligkeit einer Gegend. Selbst wenn im Freien keine Sonne scheint, 
  ist es am Tage immer hell, da die Athmosphäre und die Wolken das Licht 
  einer Sonne indirekt weitergeben. Nachts ist dagegen das ambiente Licht fast 
  Null, wenn nicht gerade zB. der Vollmond scheint. Wichtig ist das ambiente Licht 
  vor allem für die Schattenbereiche, wo es sonst stockdunkel wäre. 
  Beginnen wir mit der Arbeit:

Öffnet im GTK eure 
  Map, die ihr belichten wollt. Bevor ihr weiter macht, kontrolliert bitte, ob 
  ihr alle Punktlichter oder sonstige Lichtquellen gelöscht habt. Drückt 
  dafür "L" im GTK, es erscheint folgendes Fenster

![image]({static}outdoor_light/screens/1.jpg)

Wenn ihr den Eintrag "light" 
  seht, dann müsst ihr das Licht selektieren und anschließend löschen. 
  (Select -> Close -> Backspace -> "L") Erst wenn kein Eintrag 
  für "light" mehr vorhanden ist, bekommt ihr das gewünschte 
  Ergebnis am Ende. Wenn ihr kein Licht mehr habt, schließt das Fenster 
  mit "Close".
  

----

Jetzt markieren wir einen
normalen Brush und drücken die Taste 
  "**N**", für das Entity-Fenster.
  

![image]({static}outdoor_light/screens/2.jpg)

Achtet darauf, dass im oberen 
  Fenster "worldspawn" markiert ist. Jetzt tragt ihr bei
"**Key**" den Schlüssel 
  "ambient" ein und bei "**Value**" den Wert "80". Die Höhe 
  der Werte müsst ihr selber herausbekommen, was zu eurer Map am besten passt. 
  Die Helligkeit hängt von der Tageszeit und den Wetterbedingungen (Wolken) 
  ab. An einem herrlichen Sonnentag ist es selbst im Schatten ziemlich hell, so 
  dass Werte bis 140 vorkommen können. In der Nacht hingegen kann das ambiente 
  Licht schnell gegen 0 gehen, aber zu dunkel darf man es auch nicht machen, da 
  man sonst nix mehr erkennt.

Der zweite wichtige Aspekt 
  beim Licht ist die Farbe. Bei einem warmen rötlich-gelbem Licht denkt man 
  an einen Sonnenuntergang, während der Mond nahezu weißes kaltes Licht 
  ausstrahlt. Bei Regen oder schlechten Wetter sind bläuliche Farben von 
  Vorteil.

  Um die Farbe des ambienten Lichtes einzustellen, schließt ihr das Entity-Fenster 
  und drückt danach "**K**".

![image]({static}outdoor_light/screens/3.jpg)

Mit der Maus könnt 
  ihr nun direkt den kleinen Kreis bewegen um die gewünschte Lichtfarbe einzustellen. 
  Natürlich geht es auch durch die Eingabe der Werte rechts im Fenster. Wenn 
  ihr die richtige Farbe gefunden habt (ihr könnt es jeder Zeit wieder ändern) 
  drückt "**OK**"

  Ein Druck auf die "N"-Taste öffnet wieder das bekannte Entity-Fenster 
  und siehe da, der color-Wert hat sich automatisch eingetragen:

![image]({static}outdoor_light/screens/4.jpg)

Das war schon alles zum
Thema ambientes Licht.

----

**1. Sonnenlicht**

Kommen wir nun zum zweiten 
  Teil des Licht-Tutorials - das Sonnenlicht. 

 Dazu benötigen wir einen Shader. 
  Wer schon eine eigene Shader-Datei hat, kann diese benutzen, ansonsten legen 
  wir uns nun einen Sonnenshader an.

  Im Ordner GameData\base\shaders befinden sich die bereits vorhandenen
Shader-Dateien. 
  Öffnet Euren Texteditor ( z.B. Notepad) und kopiert folgenden Text in die leere 
  Datei:

// skyparms work like this:

  // q3map_sun <red> <green> <blue> <intensity> <degrees> 
  <elevation>

  // color will be normalized, so it doesn't matter what range you use

  // intensity falls off with angle but not distance 100 is a fairly bright sun

  // degree of 0 = from the east, 90 = north, etc. altitude of 0 = sunrise/set, 
  90 = noon

textures/system/sonnenshader

  {

  qer_editorimage textures/skies/sky.tga

  q3map_surfacelight 10

  sun 1.00 0.82 0.42 300 80 45

  surfaceparm sky

  surfaceparm noimpact

  surfaceparm nomarks

  q3map_nolightmap

  skyParms textures/skies/yavin 512 -

  }

Dann speichert ihr die Textdatei 
  in dem Verzeichnis GameData\base\shaders mit dem Namen _sonnenshader.shader_ 
  ab. Jetzt müsst ihr im gleichen Verzeichnis die Datei _shaderlist.txt_ 
  öffnen._ _Am Ende der Datei tragt ihr unter den anderen Namen jetzt 
  eure eigene shaderdatei _sonnenshader _ein. (ohne
  die Endung ".shader" ) 

Dann bitte Abspeichern und
Schließen.

----

**Zur Erklärung der 
  Datei:**

In den ersten 5 Zeilen findet 
  ihr die originale Beschreibung eines Sonnenlichtes. Das es sich nur um Kommentare 
  handelt, erkennt man an den  // - Zeichen am Anfang der Zeile

textures/system/sonnenshader

  In dieser Zeile wird der Effekt bezeichnet (Name des Shaders). Ihr findet den Shader dann im GTK-Radiant 
  im Ordner "textures/system" mit dem Namen
sonnenshader.

qer_editorimage textures/skies/sky.tga

gibt an, welches Bild im 
  GTK für den Shader angezeigt werden soll. In diesem Fall ist es das kleine 
  graue Quadrat, wo ** SKY** draufsteht.

sun  1.00 0.82 0.42
 300  80
 45

Hier nun der wichtige Teil 
  des Shaders. Die ersten drei Zahlen (1.00 0.82 0.42) bestimmen die Farbe des 
  Sonnenlichtes. Diese Zahlen sind genau die gleichen wie im GTK wenn ihr "**K**" 
  drückt. Ihr könnt also im GTK euch die Farbe raussuchen und dann die 
  Zahlen in der Textdatei eingeben.

  Die vierte Zahl ist die  Leuchtstärke der Sonne.
Der Wert "300" entspricht einer guten
Nachmittagssonne, ein Mond würde dagegen mit "100" ausreichend leuchten.

die fünfte Zahl (80) ist die Richtung aus der das Licht kommt. Wenn ihr zum Beispiel 
  auf eurem Himmel eine Sonne habt oder im Nachhimmel einen Mond, ist es sinnvoll, 
  wenn das Licht auch aus dieser Richtung kommt. Angegeben ist in Grad, also 1
- 360°.

  Die letzte Zahl (45) ist der Winkel, wie hoch die Sonne/Mond
steht (1bis
90). Dies hat 
  entscheidenden Einfluss auf die Schatten in der Map. Mittags sollten es 
  kurze Schatten sein, also bis zu  90°. Lange Schatten wie bei einem Sonnenaufgang 
  bekommt man mit Werten um die  20°.

skyParms textures/skies/yavin 512 -

In dieser Zeile wird beschrieben, 
  welche Himmelbilder benutzt werden. In diesem Fall ist es der Himmel von Yavin. 
  Die Bilder findet ihr in dem Verzeichnis textures/skies. Wenn ihr einen anderen 
  Himmel wollt, müsst ihr statt  yavin euren gewünschten Namen eintragen. 
  Beachtet bitte, dass eine Himmelstextur immer aus ** 6 Bildern** besteht (Oben, Unten, 
  Vorn, Hinten, Links, Rechts) Diese Dateien heißen im Dateinamen immer 
  am Anfang gleich und unterscheiden sich durch die Kürzel nach dem "**_**" 
  Zeichen (yavin_dn,  yavin_rt ...). In diese Zeile schreibt ihr aber nur den gemeinsamen 
  Namen, der Teil vor dem "**_**" im Dateinamen, also
  **yavin**. Die zahl "512"
  gibt die Größe den einzelnen Skybox-Teile in Pixel an (in diesem Fall 512
  x 512). Wenn Ihr Skyboxbilder benutzen wollt, die andere Größe haben,
  dann müsst Ihr diese Zahl dementsprechend anpassen. Zulässig sind : 256,
  512, 1024, 2048 

Die Bedeutung der anderen 
  Einträge könnt ihr den Shader-Tutorials entnehmen, da sie hier keine 
  Rolle spielen.

----

Um die neue Shaderdatei 
  nutzen zu können, müsst ihr den GTK neu starten. Also Map speichern 
  und alles neu laden.

  Nun müssen wir den Sonnenshader unserer Skybox zuweisen. Dazu markiert 
  ihr die Innenseiten eurer Skybox mit der Kombination ** STRG + SHIFT + ALT** +
** Linke 
  Maustaste** im 3D-Fenster. 

![image]({static}outdoor_light/screens/5.jpg)

Wenn ihr alle 4 Wände 
  und die Decke markiert habt, öffnet euren Texturen-Ordner und wählt 
  das Verzeichnis "system". Unter den Texturen sollte sich unser
sonnenshader 
  verstecken.

![image]({static}outdoor_light/screens/6.jpg)

Wählt diesen nun aus, 
  und eure Skybox ist nun mit unserem Sonnenshader belegt. 

Jetzt noch die Map
speichern und kompilieren, aber bitte mit Licht! ** ;)**

----

**Tutorial
by Shooter, **

 thx to Darth 
  Arth

----

Alle
  Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet: 

©
  2000 - 2003 (Artur L.) [www.darth-arth.de](http://www.darth-arth.de)

Nur
  zur privaten Nutzung. Kopieren nicht gestattet. Darth-Arth.de ist ausdrücklich
  nicht für den Inhalt externer Seiten verantwortlich. Es gelten die
  angegebenen Nutzungsbedingungen.

 

 

