title: Aufzug mit Schalter
author: Sentinel (Paul S.)
date: 2004-01-01
modified: 2015-04-14
category: mapping
type: tutorials/darth-arth
tags: Entities
slug: entity-lift

Es gibt grundsätzlich mehrere Arten um einen Aufzug zu erstellen. Dies ist meiner Meinung nach aber die einfachste.

Zuerst erstellt ihr einen Brush, der später der Aufzug sein wird.   

Ich habe mir das in diesem Beispiel so vorgestellt, das der Lift den Spieler auf eine Art Hochstand im Raum befördert.

 ![image]({filename}entity-lift/image001.png)

 

Selektiert diesen Brush und macht ihn zu einem `func_door`. 

Drückt dazu die <kbd>rechte Maustaste</kbd> in der 2d-Ansicht und wählt `func > func_door`.

![image]({filename}entity-lift/image003.png)

Nun geht ihr ins Entity-Menü (<kbd>E</kbd> drücken) und gebt den Brush folgende Werte 

<pre>Key:      angle
Value:    -1</pre>

Das hat zufolge, dass der Aufzug nach oben fährt. Ihr könnt stattdessen auch einfach auf den button `Up` klicken. 

Der Radiant legt dann automatisch diesen Wert fest.

<pre>Key:     lip
Value:   -340 (in unserem Fall)</pre>

 

Hier
wird die Strecke angegeben, die der Aufzug nach oben zurücklegt. Achtet darauf
das vor der Zahl immer ein `-` steht. 

 Die Strecke könnt ihr einfach ausmessen, indem ihr einen Brush an die von euch gedachte Strecke baut.

Um die Werte abzulesen, drückt ihr die Taste <kbd>Q</kbd> und nun könnt ihr die Höhe der Strecke bestimmen. 

In unserem Fall wären das hier 340 Einheiten. Nach dem ablesen löscht ihr den Brush einfach wieder.

![image]({filename}entity-lift/image005.png)

<pre>Key:      wait
Value:    4</pre>

Dies gibt die Zeit (in Sekunden) an, die der Lift, wenn er nach oben gefahren ist, wartet. Nach 4 Sekunden würde unser Lift also wieder runter fahren.

Um einen geeigneten Klang des Liftes zu bekommen, könnt ihr zum Beispiel noch folgende Werte vergeben:

<pre>Key:     soundset
Value:   large_platform</pre>

So, jetzt hätten wir alle Werte für diesen Brush vergeben. Jetzt fehlet noch eine Art Aktivierungs-Schalter für den Lift. Dazu erstellt ihr einen Brush ein kleines bisschen über dem eigentlichen Aufzugsbrush, den wir zuvor erstellt haben. Der neue Brush sollte ungefähr die gleiche Länge und Breite haben wie der Aufzugsbrush . Diesem neuen Brush gebt ihr nun die Textur `system/trigger` und macht ihn zu einem `trigger_multiple` (in 2d-Ansicht <kbd>rechte Maustaste</kbd> > `trigger > trigger_multiple`).

![image]({filename}entity-lift/image007.png)

Jetzt könnt ihr für den Aktivierungsbrush noch folgende Entity-Angaben verwenden.

<pre>Key:     wait
Value:   8</pre>

Das bedeutet, dass man den Lift nur alle 8 Sekunden von diesem Aktivierungsbrush aktiviert werden kann. 

Jetzt deselektiert ihr alles (<kbd>ESC</kbd> drücken). Und dann selektiert ihr zuerst den Aktivierungsbrush und danach den Liftbrush. Drückt <kbd>Strg + K</kbd>, um beide miteinander zu verbinden, sodass diese zusammen wirken können. Wichtig ist, dass ihr die Reihenfolge einhaltet! Nun sollte eine blaue Linie die beiden verbinden.

Zum Schalter:

Um den Lift, wenn ihr an der oberen Station steht und runter wollt, zu euch hoch zu rufen oder holen, müsst ihr noch einen Schalter oben erstellen. 

Formt euch einen Brush zurecht, der dann euer Schalter wird, und gebt ihm irgendeine Textur.

![image]({filename}entity-lift/image009.png)

Nun selektiert den Schalter und gebt ihm die Funktion `func_button` (in der 2d-Ansicht <kbd>rechte Maustaste</kbd> > `func > func_button`). 

Jetzt müssen wir den Schalter noch mit dem Lift in eine Verbindung bringen, dazu selektiert ihr zuerst den Schalter und danach wieder den Liftbrush und drückt <kbd>Strg + K</kbd>.

Es sollte eine blaue Linie die beiden verbinden.

Damit der Schalter bei Berührung vom Spieler auch in die Wand gedrückt wird, könnt ihr auch noch bei den Entity-Eigenschaften folgende Eigenschaft vergeben:

<pre>Key:      angle
Value     90 (in unserem Fall)</pre>

Gibt den Winkel an in dem der Schalter bei Berührung bewegt wird. Also hier bei uns in die Wand. 

Jetzt kannst du kompilieren und den Lift benutzen :D .....