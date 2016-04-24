title: Menü Coding - Die fortgeschrittenen Befehle  
author: BiKi (Benjamin K.)
date: 2004-01-01
modified: 2016-04-24
category: scripts
type: tutorials/darth-arth
tags: Menu
slug: menu-advanced

# Voraussetzungen

* [Menü Coding - Die ersten Schritte]({filename}menu-basics.md)
* einen installierten Editor (wie Notepad oder Wordpad)
* WinRAR ([download](http://winrar.de)) oder vergleichbar (7-Zip etc.)

# Einführung

In dieser Lehreinheit (Tutorial) lernen wir ein paar fortgeschrittene Befehle und ihre Funktionen.

Am Ende dieses Tutorials solltet ihr dann in der Lage sein, ohne Probleme euer eigenes Menü zu erstellen! 

# Kapitel 1 - die onXXX Befehle

Die wohl am häufigsten genutzten fortgeschrittenen Befehle sind die on-Befehle. Damit löst man etwas aus, sobald etwas passiert, ähnlich wie bei if. Wer schon Erfahrung mit JavaScript hat, wird sich sicher nicht allzu fremd vorkommen:

![die on-Befehle]({filename}menuimages/menuadvanced1.jpg)

Hier sieht man einmal alle on-Befehle aufgelistet... und nun die Erklärung.. (Ja ich weiß... aber es geht nicht ohne :P ):

- `onOpen` - Sobald ein Menü geöffnet wird, werden alle Befehle innerhalb des onOpen Blocks ausgeführt! 
- `onESC` - Sobald man die ESC Taste drückt (bzw. das Menü geschloßen wird) werden die Befehle im Block ausgeführt!
- `onClick` - Sobald der Button (in unserem Beispiel) gedrückt wird geschiet etwas! Das ist wohl in 99,9% der Fälle, dass sich ein neues Menü öffnet!
- `onEnter` - Löst ein Ereignis aus, sobald man mit der Maus über den Button fährt.
- `onExit` - Löst ein Ereignis aus, sobald man mit der Maus den Button verlässt!

Eigentlich sind die Befehle ja ganz logisch, man muss nur ein bisschen logisch denken ;)

Nun zeige ich euch mal ein komplexeres Beispiel dieser on-Befehle:

![die on-Befehle]({filename}menuimages/menuadvanced2.jpg)

Ich bin sicher, das ihr das meiste schon versteht ;) Jedoch sind wieder ein paar neue Befehle hinzugekommen:

- `open` - Öffnet ein Menü... als value muss der Name angegeben werden, der im Header definiert ist (Nicht der Name der `.menu` Datei!!)
- `show` - Blendet etwas ein, was zwar in der .menu Datei definiert ist, jedoch bei `visible` die value `0` hat.
- `hide` - Blendet etwas aus, was entweder bei `visible` `1` stehen hat, oder was vorübergehend durch `show` eingeblendet wurde!

So, das war's erstmal hierzu. 

# Kapitel 2 - Befehle, Befehle, Befehle

Na, alles behalten? Hier nochmal eine kleine Auflistung vieler (nützlichen) Befehle:

<table class="table">
 <tr><th>Befehl    </th><th>Beschreibung</th></tr>
 <tr><td>name      </td><td>Definidert den Namen der .menu Datei, wie man es vom Spiel aus ansprechen kann!</td></tr>
 <tr><td>group     </td><td>Gruppiert Blöcke, um sie zusammen ansprechen zu können!</td></tr>
 <tr><td>style     </td><td>Gibt den Style des Blocks an... wichtig zur Identifizierung!</td></tr>
 <tr><td>type      </td><td>Gibt den Typ an... ein Button, Text, usw!</td></tr>
 <tr><td>rect      </td><td>Gibt die Position des Buttons, des Textes... an!</td></tr>
 <tr><td>text      </td><td>Gibt den Text an, der erscheinen soll!</td></tr>
 <tr><td>descText  </td><td>Gibt den Text an, der unten als Beschreibung erscheinen soll</td></tr>
 <tr><td>font      </td><td>Gibt die Schriftart an... Values 1 - 4!</td></tr>
 <tr><td>textscale </td><td>Die Größe des Textes!</td></tr>
 <tr><td>textalign </td><td>Die Ausrichtung des Textes!</td></tr>
 <tr><td>forecolor </td><td>Ändert die Farbe des Textes, Buttons...</td></tr>
 <tr><td>visible   </td><td>Gibt an, ob der Block standartmäßig erscheinen soll, oder ob er Nachträglich erscheinen soll!</td></tr>
 <tr><td>decoration</td><td>Falls diese Zeilte als letztes in einem Block steht, kann nicht mit der Maus drüber gefahren werden!</td></tr>
 <tr><td>onOpen    </td><td>Gibt den Pfad zu einem Bild an!</td></tr>
 <tr><td>onESC     </td><td>siehe oben...</td></tr>
 <tr><td>onEnter   </td><td>siehe oben...</td></tr>
 <tr><td>onExit    </td><td>siehe oben...</td></tr>
 <tr><td>onClick   </td><td>siehe oben...</td></tr>
</table>

Das war's wieder erstmal. Bei weiteren Fragen: Mail, Foren-PM oder per ICQ anschreiben!

MFG
