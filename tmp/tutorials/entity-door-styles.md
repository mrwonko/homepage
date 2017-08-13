title: Verschiedene Türarten
author: Guard (Christophe B.)
date: 2004-01-01
modified: 2015-04-14
category: mapping
type: tutorials/darth-arth
tags: Tür, Entities, auto-generated
slug: entity-door-styles

**_

>>
Mapping Academy - Tutorials <<

 

(c)
2003 [www.darth-arth.de](http://www.darth-arth.de)

----

_
**_[u][/u]_

Tutorial:

Verschiedene Türarten
by Guard (Christophe B.)

Vorraussetzungen:

Grundwissen (Räume erstellen)

Basiswissen der `func_****`
(Türen erstellen)

----

Einführung

In diesem Tutorial werden verschiedene Möglichkeiten vorgestellt, eine Tür zu öffnen. Da in den verschiedenen JK2-Editingforn immer wieder solche Fragen auftachen, sollte diese Tutorial manchen Leuten weiterhelfen. 

Hintergrundwissen

Um die Türen richtig in den Spielfluss der Map einzubetten, muss man verschiedene Grundsätze beachten: Den Stil der Map, die Bauweise und die Geschwindigkeit.

[u][/u]

Den Stil der Map: Texturen tragen neben der Beleuchtung wesentlich zur Gesamtatmosphäre einer Map bei. Imperiale Doppeltüren passen halt nicht in einen alten, verfallenen Tempel. Dagegen würden Steintüren in einer Imperialen Basis wohl sehr lächerlich aussehen und die Atmosphäre zerstören. Deshalb auf die Umgebung achten, in der sich die Tür befinden soll.

Auch die Öffnungsmöglichen sollten bedacht werden. Automatische Türen sind meistens in imperialen Basen anzutreffen, aber auch an anderen Stellen, an denen sich viele Leute aufhalten. Manuelle Türen findet man in Lagerräumen, Gefängnissen usw...

[u][/u]

Die Bauweise: Neben den Texturen ist die Bauweise der Tür selbst mitentscheidend. Die Bauweise sollte immer dem Stil der Map angepasst sein. Imperiale Türen sind meistens gut gepanzert, und bestehen aus maximal 2 Hälften. In manchen urbanen Empfangsräumen können Türen vorkommen, die ein Sehr hohes Detail-level besitzen (Eingelegtes Glas, Verzierungen, Gitter) und aus mehreren beweglichen Teile bestehen.  In Tempelanlagen (wie das Lichtschwertraining im Singelplayer) sind meistens Schwere Steintüren zu finden.

[u][/u]

Die Gescwindigkeit: Auch die Spielgeschwindigkeit trägt einiges zum Design der Türen bei. Ein Saberonly-Match spielt sich langsamer als ein Waffengame, welches sich wieder von CTF/CTY unterscheidet. Schwere, langsame Türen in einer CTF-Map behindern den Spieler und sorgen unter Umständen für Verärgerung. Andererseits können solche Türen, wenn sie wohlplaziert sind, einiges an Taktik in das Spiel bringen. Für Weaponmatches sind schnelle Türen ein wichtiges Element, da sie nur zur visuellen Abdeckung dienen, und nicht zum Abschließen eines Areals.

----

Türarten

Es gibt mehrere Möglichkeitein, Türen zu öffnen. Automatisch, per Knopfdruck oder mit dem Use-Button. Dazu gibt es noch einige Besonderheiten, wie Kraftfelder usw.... Die Eignung der verschiedenen Arten wurde schon oben beschrieben. Im folgenden Kapitel sehen wir uns das Erstellen näher an.

1. Automatische Türen

Automatische Türen sind nichts anderes als func_door, wie sie in [Dart Arth’s Tutorial](mapping/tworooms/tworooms.htm) beschrieben werden. Sie öffnen sich automatisch, sobald der Spieler in die Nähe kommt.

2. Türen mit Schalter

Diese Art von Tür wird über einen Schalter (func_button) geöffnet. Ingame muss der Spieler gegen einen solchen func_button laufen, um die Tür zu öffnen. Der func_button kann in beliebiger Entfernung angebracht werden.

Wenden wir uns dem eigentlichen Aufbau zu. Als erstes brauchen wir eine einfache Tür, wie sei bei Punkt 1 beschrieben wird. Dann benötigen wir den Schalter. Dazu erstellen wir einen Brush, belegen ihn mit einer Schaltertextur (z.B.
cairn/door_display) und machen ihn per Entity-Menü (N) zu einem func_button.

![image]({filename}doors/Image1.gif)

Dort stellen wir auch ein, in welche Richtung sich der Button bewegen soll, wenn ein Spieler dagegen läuft. Mit den Angle-Buttons wird die Richtung festgelegt. (Die Richtung bezieht sich auf die 2D-Draufsicht). Dann noch den func_button mit der Tür verknüpfen (STRG + K) und fertig.

****

TIPP:  Da es etwas seltsam aussieht, wenn sich der Schalter bewegt, kann man einen kleinen Trick anweden. Man erstellt einen normalen Brush, der die Schaltertextur besitzt, und darunter einen kleineren, flachen Brush, der dann die func_button-Funktion übernimmt. Diesen kleineren Brush belegt man dann mit einer unsichtbaren Textur (System/Caulk oder System/Nodraw).

![image]({filename}doors/Image2.gif)

Im Spiel läuft der Spieler dann gegen den unsichtbaren Brush. Dieser bewegt sich, aber weil der unsichtbar ist, sieht man das nicht und meint, man würde gegen den Brush mit der Schaltertextur laufen.

3. Türen mit „Benutzen"

Eine weitere Türart sind Türen, die sich öffnen, sobald man in einem bestimmten Bereich die Benutzen-Taste drückt. Um diese Art Tür zu erstellen benötigen wir eine func_door (wie in Kapitel 1 beschrieben), einen trigger_multiple, und einen Brush mit Schaltertextur(oder etwas ähnliches um den Bereich, in dem man die Benutzen-Taste drücken soll, kennzeichnet).

![image]({filename}doors/Image3.gif)

Als erstes konstruieren wir die func_door, und stellt Angle, Geschwindigkeit usw. ein. Danach sollte ein Blickfang, wie Schalter, Markierung oder ähnliches, erstellt werden, damit der Spieler später weiß, wo er die Benutzen-Taste drücken soll. In diesem Bereich erstellen wir nun einen Brush und geben ihm die triggertextur (system/trigger). Dann öffnen wir das Entity-Menü, und wählen aus der oberen Liste trigger_multiple aus. Im Menü aktivieren wir die Checkbox Use_Button, damit sich die Tür erst öffnet, wenn der Spieler sich im trigger_multiple befindet und die Benutzen-Taste drückt.

Besonderheit: Kraftfelder

Eine Besonderheit sind Kraftfelder. Diese blau leuchtenden Barrieren werde dort eingesetzt, wo normale Türen nicht ausreichen würden, wie z.B Gefängniszellen, besonders gesicherte Zugänge usw. Typisch für Kraftfeldersind ausserdem die ovalen Durchgänge, die innen durch die weiß leuchtenden Projektoren erhellt werden. In Jedi Knight 2 werden Kraftfelder wie Türen eingesetzt und versperren dem Spieler bestimmte Wege. Aber im unterschied zu normalen Türen kann man durch Kraftfelder hindurchsehen, was in bestimmten Situationen sehr nützlich ist. Kraftfelder werden wie folgt aufgebaut.

Als erstes benötigen wir einen geeigneten „Rahmen" für das Kraftfeld, um die Glaubwürdigkeit zu steigern.

![image]({filename}doors/Image4.gif)

Der in diesem Bild verwendete Rahmen besteht aus einfachen Brushes und vier "Endcaps", die innen mit einer Textur belegt sind, die die Kraftfeld-Projektoren darstellen soll.

Als nächstes benötigen wir das Kraftfeld selbst. Dazu erstellen wir einen Brush, der die dem Rahmen entsprechende Größe besitzt und geben ihm eine Kraftfeld-Textur (z.B doomgiver/forcefield). Diesen Brush definieren wir per Entity-Menü als func_useable.

Im Menü kann man wählen, on das Kraftfeld beim Spielstart aktiviert ist und auf Knopfdruck ausgeschaltet wird, oder umgekehrt. (start_off).

![image]({filename}doors/Image5.gif)

Um das Kraftfeld realistischer zu gestalten, empfiehlt es sich, target_speaker mit Kraftfeld-Geräusch (zu finden in sound/movers/doors) einsetzt.

So, das wars dann schon. Für weitere Fragen:

[Darth Arth's Mapping Academy](http://www.darth-arth.de/)

[Jedi-Knight2.de](http://www.jedi-knight2.de/)

[Fiesling's Place](http://www.fieslingsplace.de/)

----

[u][DOWNLOAD
DER TUTORIAL MAP](downloads/BSPMap_Tueren.zip)[/u]

(
.map - Datei enthalten)

 

----

Alle
  Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet: 

©
  2000 - 2003 (Artur L.) [www.darth-arth.de](http://www.darth-arth.de)

Nur
  zur privaten Nutzung. Kopieren nicht gestattet. Darth-Arth.de ist ausdrücklich
  nicht für den Inhalt externer Seiten verantwortlich. Es gelten die
  angegebenen Nutzungsbedingungen.

