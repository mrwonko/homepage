title: ICARUS-Manual Deutsch
author: mrwonko
date: 2004-01-01
modified: 2015-04-14
category: scripts
type: tutorials/darth-arth
tags: Scripting, auto-generated
slug: script-icarus-manual-de

**[color=teal]>> [/color]****[color=teal] - Tutorials <<[/color]**

 

[color=gray](c) 2006[/color][color=silver] [/color][color=silver][www.darth-arth.de](http://www.darth-arth.de)[/color]

----

[color=white]ICARUS Manual
(deutsche Version)[/color]

**[u][color=yellow]VORAUSSETZUNGEN[/color][/u]****[color=yellow]:[/color]**

[color=white]>>
Tuturial Scripting - Installation BehavEd (Scripts-Editor) ([/color][color=white][hier](../../behaved/behaved.htm)[/color][color=white])[/color]

 

----

 

[u][color=white]BehavEd benutzen[/color][/u]

[color=white]BehavEd ist ein drag & drop Programm zum
erstellen von Scripts.  Links siehst du ne Liste
mit verfügbaren ICARUS Kommandos. Rechts ist eine Reihe von Knöpfen die
für BehavEd Funktionen wie das Laden und Speichern der Scripts, Beenden, Kopieren
und Einfügen usw. da sind.[/color]

[color=white] [/color]

[u][color=white]BehavEd Kommando Knöpfe[/color][/u]

[color=white] [/color]

[u][color=white]Actions[/color][/u]

[color=white]Add
– Fügt das aktuell ausgewählte Kommando zum Script hinzu (du kannst auch
doppelt drauf klicken)[/color]

[color=white]Delete
– Löscht die ausgewählte Zeile aus dem Script (du kannst auch entfernen
drücken)[/color]

[color=white]Edit
– Editiert die ausgewählte Zeile des Scripts (du kannst die Zeile auch doppelt
anklicken)[/color]

[color=white]Clone
– Kopiert die selektierte Zeile in die nächste Zeile[/color]

[color=white]Copy
– Kopiert die selektierte Zeile in den Zwischenspeicher (es geht natürlich auch
strg+c)[/color]

[color=white]Paste
– Fügt die Zeile(n) aus dem dem Zwischenspeicher ein (es geht auch strg+v)[/color]

[color=white] [/color]

[u][color=white]File[/color][/u]

[color=white]New
– Erstellt ein neues Script[/color]

[color=white]Open
– Öffnet ein existierendes Script[/color]

[color=white]Append
– Fügt ein bestehendes Script am Ende des aktuellen ein[/color]

[color=white]Save
– Speichert das aktuelle Script unter dem momentanen Namen[/color]

[color=white]Save
As… - Speichert das Script unter einem anderen Namen[/color]

[color=white] [/color]

[u][color=white]Application[/color][/u]

[color=white]Preferences
– Eine Liste von Verzeichnissen und Einstellungen die BehavEd nutzt (hier wird
es auch eingerichtet)[/color]

[color=white]About…
- Einige Informationen über BehavEd[/color]

[color=white]Exit
– Beendet BehavEd (Aber das wolln wir im Moment ja nicht :P
)[/color]

[color=white] [/color]

[u][color=white]Treeview Options[/color][/u]

[color=white]Show
Types – Schaltet das Anzeigen der Arten von allen Strings und Values an[/color]

[color=white]%g
floats – Zeigt alle Dezimalstellen an, also am Ende noch Nullen (normalerweise
werden nur genutzte angezeigt)[/color]

[color=white] [/color]

[color=white]Compile!
– Kompiliert das Script, damit es im Spiel von ICARUS genutzt werden kann[/color]

[color=white] [/color]

[u][color=white]Das Feedback Fenster[/color][/u]

[color=white]Alle
Errors und Nachrichten werden hier angezeigt.  Wenn ein Script erfolgreich
kompiliert wurde steht da “OK”.  Andernfalls steht da der Error.[/color]

[color=white] [/color]

[u][color=white]ICARUS Kommando Liste[/color][/u]

[color=white]Du
kannst ein Kommando zu deinem Script (im großen Fenster in der Mitte
dargestellt) entweder durch doppelt drauf klicken oder durch Reinziehen
hinzufügen. Wenn du ein Kommando nur anklickst erscheinen über dem Feedback
Fenster Informationen darüber.[/color]

[color=white] [/color]

_[color=white]Key:[/color]_

[color=white]{}
– Zeigt an das ein Kommando andere Kommandos beinhalten kann.[/color]

[color=white]e
– Ein normales Kommando[/color]

[color=white][]
– Ein Makro, eine Gruppe von Kommandos.[/color]

[color=white] [/color]

_[color=white]Kommandos:[/color]_

[color=white](Für
detaillierte Beschreibung siehe unten)[/color]

[color=white]flush[/color][color=white]     if          loop      affect    run       wait      sound   move    rotate    use       (kill)      remove[/color]

[color=white]print[/color][color=white]      rem      declare free       get       random set       camera task      do        wait      dowait[/color]

[color=white](walkTo runTo)[/color]

[color=white] [/color]

[color=white] [/color]

[color=white] [/color]

[u][color=white]Die Kommandos editieren[/color][/u]

[color=white] [/color]

[color=white]Wenn du einmal ein Kommando zu deinem Script
hinzugefügt hast, musst du es richtig einstellen. Dies kannst du entweder
durch Doppelklicken auf das Kommando oder durch erst das Kommando an-, und dann
'edit' klicken tun.[/color]

[color=white]Du wirst mit einer Reihe von Boxen und Feldern
belohnt werden.[/color]

[color=white] [/color]

[color=white]Manche sind einfache Eingabefelder wo du was
eintippen musst (/kannst). Diese sind meistens dadurch gekennzeichnet, das
darunter steht welcher Typ benötigt wird, string, float, vector, usw.. [/color]

[color=white]Andere sind Drop-Down-Menüs, in denen du aus
vorgegeben Möglichkeiten eine auswählen musst. Diese Drop-Down-Menüs
verändern gelegentlich Eigenschaften von Feldern, du musst nach dem ändern dann
'Re-Evaluate' anklicken, damit die anderen Felder entsprechend eingestellt
werden.[/color]

[color=white]Neben den Eingabefeldern ist ein “Helper” Knopf.
Wenn du ihn anklickst, kannst du das “get” Kommando (siehe unten)
benutzen. Nur die Felder die den richtigen Typ haben sind
möglich. Wenn die benötigte Eingabe ein Float ist kannst du auch die
“random” Funktion (noch mal siehe unten) benutzen. Dann trag einfach die
kleinste und die größte mögliche Zahl ein. Wenn du dich entscheidest, doch
keine der Helper-Funktionen zu nutzen, klick “revert” an, um zur normalen
Eingabebox zurück zu kommen.[/color]

[color=white] [/color]

[color=white]Wenn
du fertig bist, klick 'ok' oder klick auf 'cancel' falls du die Änderungen
nicht übernehmen willst.[/color]

 

[color=white]

[/color]

[u][color=white]"Script-Fluss" Kommandos[/color][/u][u][/u]

[color=white](flush, loop,
wait, if, affect, run)[/color]

[color=white]Dies sind Kommandos, die den Ablauf des Scripts
kontrollieren. In anderen Worten, sie sagen, wann und wie ein Kommando
ausgeführt wird.[/color]

[color=white] [/color]

**[color=white]rem[/color]**[color=white] – Dieses Kommando kontrolliert nicht wirklich den Ablauf des
Scripts, es ist nur ein Kommentar. Du kannst hier Notizen für dich rein schreiben,
oder es für andere einfacher machen dein Script zu verstehen usw. Es ist
eine gute Idee, an den Anfang des Scripts ein 'rem' zu stellen, und hinein
schreiben, wozu das Script da ist.[/color]

[color=white] [/color]

**[color=white]flush[/color]**[color=white] – Dieses Kommando entfernt alle laufenden oder noch
durchzuführende Kommandos vom Entity. Es ändert keine Einstellungen am Entity,
sondern löscht nur die noch nicht ausgeführten Kommandos, wie zum Beispiel „geh
zum Baum“.[/color]

[color=white] [/color]

[color=white]Als
Beispiel, du hast dieses Script einem weglaufenden Gegner zugewiesen:[/color]

[color=white] [/color]

[color=white]set ( “SET_BEHAVIORSTATE”, “BS_DEFAULT” )[/color]

[color=white]set ( “SET_LOOK_FOR_ENEMIES”, “false” )[/color]

[color=white]set ( “SET_WALKING”, “true” )[/color]

[color=white]set ( “SET_NAVGOAL”, “walk1” )[/color]

[color=white]wait
( 3000 )[/color]

[color=white]print
( “Hello!” )[/color]

[color=white] [/color]

[color=white]Aber
dann: nachdem die ersten zwei Kommandos ausgeführt wurden wird ein anderes
Script auf dem Gegner ausgeführt:[/color]

[color=white] [/color]

[color=white]flush()[/color]

[color=white]set ( “SET_LOOK_FOR_ENEMIES”, “true” )[/color]

[color=white]set ( “SET_WALKING”, “false” )[/color]

[color=white]print( “I kill you!” [/color][color=white])[/color]

[color=white] [/color]

[color=white]Das
“flush” Kommando entfernt alle Befehle vom Entity, die noch nicht ausgeführt
wurden. Wenn also die ersten beiden Kommandos ausgeführt wurden, kommt das
zweite Script, wodurch er in den Angriff übergeht und “I kill you!”
ausgibt. Er wird niemals drei Sekunden warten und “Hello” sagen – diese Kommandos
wurden “geflushed”.[/color]

[color=white] [/color]

[color=white]Flushs
sind nützlich um ein vorheriges Script zu stoppen, das in einer Schleife lief.
Der Flush stoppt dann die Schleife.[/color]

[color=white] [/color]

**[color=white]loop[/color]**[color=white] – Ist ein einfaches Kommando, um Kommandos zu wiederholen.
Also kannst du an Stelle von:[/color]

[color=white]wait ( 3000 )[/color]

[color=white]print ( “Hello World!” )[/color]

[color=white]wait ( 3000 )[/color]

[color=white]print ( “Hello World!” )[/color]

[color=white]wait ( 3000 )[/color]

[color=white]print ( “Hello World!” )[/color]

[color=white]wait ( 3000 )[/color]

[color=white]print ( “Hello World!” )[/color]

[color=white] [/color]

[color=white]einfach machen:[/color]

[color=white] [/color]

[color=white] ( 4 )[/color]

[color=white]{[/color]

[color=white]wait ( 3000 )[/color]

[color=white]print ( “Hello
World!” [/color][color=white])[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]Wenn
du eine Schleife sich für immer wiederholen lassen willst, tipp als Nummer “-1”
ein.[/color]

[color=white] [/color]

[color=white]Loop ( -1 )[/color]

[color=white]{[/color]

[color=white]wait ( 3000 )[/color]

[color=white]print ( “Hello
World!” [/color][color=white])[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]Das
lässt das Script für immer, oder bis es geflushed wurde, weiter laufen.[/color]

[color=white] [/color]

**[color=white]Wait[/color]**[color=white] – Ist ein Kommando um ein Script für [so viele wie du
willst] Millisekunden zu pausieren.  1000
Millisekunden sind eine Sekunde. Und 60 Sekunden sind eine Minute. Und 60
Minuten eine Stunde. Und so weiter.[/color]

[color=white] [/color]

[color=white]Als
Beispiel:[/color]

[color=white] [/color]

[color=white]print(
“Hello…” )[/color]

[color=white]wait(
1000 )[/color]

[color=white]print(
“World!”)[/color]

[color=white] [/color]

[color=white]Das
lässt das Script “Hello…”ausgeben, dann eine Sekunde warten und dann “World!”
ausgeben.[/color]

[color=white] [/color]

**[color=white]if[/color]**[color=white] – Dieses Kommando prüft eine Bedingung, die erfüllt sein muss,
damit der Teil in den geschweiften Klammern ausgeführt wird.[/color]

[color=white] [/color]

[color=white]Das
einfache Format ist:[/color]

[color=white] [/color]

[color=white]if
( Wert1 = Wert2 )[/color]

[color=white]{[/color]

[color=white]print( “Hello World!” )[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]Werte
die du überprüfen kannst, sind Variablen und Werte, die du mit 'get' geholt
hast.[/color]

[color=white] [/color]

[color=white]Als Beispiel:[/color]

[color=white] [/color]

[color=white]if ( get(FLOAT, “health”) > 0 )[/color]

[color=white]{[/color]

[color=white]print( “Hello World!” )[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]Mehr
zum 'get' Kommando später...[/color]

[color=white] [/color]

[color=white]Du
kannst auch einen “else” Block dahinter setzen, der ausgeführt wird wenn die
'if' Bedingung nicht zutrifft.:[/color]

[color=white] [/color]

[color=white]if ( get(FLOAT, “health”) > 0 )[/color]

[color=white]{[/color]

[color=white]print( “Hello
World!” )[/color]

[color=white]}[/color]

[color=white]else[/color]

[color=white]{[/color]

[color=white]print( “Hey, I’m
dead!” [/color][color=white])[/color]

[color=white]}[/color]

[color=white] [/color]

**[color=white]affect[/color]**[color=white] – Dieses Kommando sendet eine Reihe von Befehlen an ein
anderes Entity als das, welches das Script ausführt. [/color][color=white]Zum
Beispiel:[/color]

[color=white] [/color]

[color=white]Print( “Hello, Fred!”)[/color]

[color=white] [/color]

[color=white]Affect ( “Fred”, FLUSH )[/color]

[color=white]{[/color]

[color=white]           
wait( 1000 )[/color]

[color=white]           
print( “Leave me alone!” [/color][color=white])[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]Im
Beispiel oben sagt das das Script ausführende entity “Hello, Fred!” und sagt
fred das er eine Sekunde warten soll und dann “Leave me alone!” sagt.[/color]

[color=white] [/color]

[color=white]Der
Name (“Fred”) den du angibst muss der script_targetname des zu 'benutzenden'
Entitys sein. Für NPCs kannst du auch NPC_targetname nehmen. Bei allen
anderen Entitys musst du script_targetname nehmen falls du sie irgendwann per
script ansprechen willst.[/color]

[color=white] [/color]

[color=white]Das
zweite “affect” Parameter entscheidet, wie das Entity die Befehle auführt. Zur
Auswahl stehen:[/color]

[color=white] [/color]

[color=white]FLUSH
– Wie das “flush” Kommando, flushed Fred und lässt ihn den “affect” Block
ausführen.[/color]

[color=white] [/color]

[color=white]INSERT
– Was immer Fred gerade macht, er fügt die Kommandos ein und macht hinterher
weiter damit. Wenn Fred also rum sitzt, isst und sich um sieht, wird er “Leave
me alone!” sagen und hinterher weiter sitzen, essen und sich umsehen.[/color]

[color=white] [/color]

[color=white]Es ist wichtig, daran zu denken, dass das Affect
Kommando die Befehle nur an das Entity sendet, jedoch wird nicht darauf
gewartet, dass das "affectete" Entity mit den Befehlen fertig ist.[/color]

[color=white] [/color]

[color=white]Als
Beispiel:[/color]

[color=white] [/color]

[color=white]Print(
“Hello, Fred!”)[/color]

[color=white] [/color]

[color=white]Affect ( “Fred”, FLUSH )[/color]

[color=white]{[/color]

[color=white]           
wait( 1000 )[/color]

[color=white]           
print( “Leave me alone!” )[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]print( “Damn you to Hell, Fred!” [/color][color=white])[/color]

[color=white] [/color]

[color=white]Dieses
Script wird _nicht_ warten, bis Fred fertig ist und dann “Damn you to Hell,
Fred!” sagen. Es wird etwas wie das Passieren:[/color]

[color=white] [/color]

[color=white]“Hello,
Fred!”[/color]

[color=white]“Damn
you to Hell, Fred!”[/color]

[color=white] [/color]

[color=white]Dann,
eine Sekunde später sagt Fred:[/color]

[color=white] “Leave
me alone!”[/color]

[color=white] [/color]

[color=white]Das
passiert weil “affects” die Befehle sofort und auf ein Mal an das Entity (Fred)
sendet. Wenn du willst, das gewartet wird, bis Fred gesprochen hat, musst du so
was machen.[/color]

[color=white] [/color]

[color=white]Print( “Hello, Fred!”)[/color]

[color=white] [/color]

[color=white]Affect ( “Fred”, FLUSH )[/color]

[color=white]{[/color]

[color=white]           
wait( 1000 )[/color]

[color=white]           
print( “Leave me alone!” )[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]wait( 2000 )[/color]

[color=white]print( “Damn you to Hell, Fred!” [/color][color=white])[/color]

[color=white] [/color]

[color=white]Du
wartest _zwei_ Sekunden weil ja beim affect eine Sekunde ist und noch eine
mehr gewartet wird.[/color]

[color=white] [/color]

[color=white]Das
ist eine wichtige Regel und leicht zu vergessen. Also merke: _affects
werden nicht vom das Script ausführenden Entity ausgeführt, sondern an ein
anderes Gesendet!_[/color]

[color=white] [/color]

**[color=white]run[/color]**[color=white] – dieses Kommando starten ein anderes Script vom aktuellen Script
aus.[/color]

[color=white] [/color]

[color=white]Sagen
wir mal du hast so ein Script:[/color]

[color=white] [/color]

[color=white]print( “Hello World!” )[/color]

[color=white]run( “test/response” )[/color]

[color=white]wait( 1000 )[/color]

[color=white]print( “Oh well, I give up.” [/color][color=white])    [/color]

[color=white] [/color]

[color=white]und
ein Script namens “test/response” wie dieses:[/color]

[color=white] [/color]

[color=white]wait( 1000 )[/color]

[color=white]print( “I said Helloooo World!” [/color][color=white])[/color]

[color=white] [/color]

[color=white]Wenn
du das erste Script laufen lässt, passiert folgendes:[/color]

[color=white] [/color]

[color=white]“Hello World!”[/color]

[color=white](1 sek. Pause) [/color]

[color=white]“I said Helloooo World!” [/color]

[color=white](noch 1 sek. Pause) [/color]

[color=white]“Oh well, I give up.”[/color]

[color=white] [/color]

[color=white]Also
fügt ein “run” Kommando einfach nur da wo es steht eine Reihe von Befehlen ein.
Das ist nützlich wenn du eine Reihe von Befehlen von verschiedenen Scripts
benutzen willst. Wenn du diese in ein einzelnes Script schreibst kannst du sie
von jedem beliebigen Script “runnen”. Das spart Zeit weil du die Befehle nicht
immer wieder neu Einfügen musst. Außerdem hilft diese Art des Einfügens die
Behebung von Fehlern, da du später nicht alle Scripts ändern musst.[/color]

[color=white] [/color]

**[color=white]

[/color]**

**[color=white] [/color]**

**[color=white]Makros[/color]**

[color=white](walkTo,
runTo, usw.)[/color]

[color=white]Makros
sind einfache Blöcke von Befehlen, die der Einfachheit halber zusammen
geschlossen sind. Dies kann ein Script übersichtlicher machen.[/color]

[color=white] [/color]

**[u][color=white]Tasks[/color][/u]**

[color=white](task,
do, wait, dowait)[/color]

[color=white] [/color]

[color=white]Tasks sind eine Gruppe von Befehlen, auf die man
das Script warten lassen kann. Dies ist in allen möglichen Situationen
nützlich. Wenn du z.B. willst, dass ein NPC zu einem Schalter läuft und ihn
drückt, muss das Script darauf warten, dass er da ist, ehe er denn Schalter
drückt. Auch wenn ein NPC erst eine Animation oder eine Zeile in einem Dialog
beenden soll, brauchst du einen task.[/color]

[color=white] [/color]

[color=white]Das
Format des tasks ist folgendes:[/color]

[color=white] [/color]

[color=white]task
( “TASKNAME” )[/color]

[color=white]{[/color]

[color=white]           
Kommandos…[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]Den
Tasknamen kannst du frei wählen, aber es sollte (darf) nicht zwei gleiche
Tasknamen geben.[/color]

[color=white] [/color]

[color=white]Um
einen Task ausführen zu lassen lassen, benutzt du:[/color]

[color=white] [/color]

[color=white]do** **( “TASKNAME” )[/color]

[color=white] [/color]

[color=white]Das
startet den task mit dem namen TASKNAME.[/color]

[color=white] [/color]

[color=white]Wenn
ein Script warten soll, bis ein task fertig ist, benutzt du:[/color]

[color=white] [/color]

[color=white]wait
( “TASKNAME” )[/color]

[color=white] [/color]

[color=white]Das
Script wird nicht fort fahren, ehe nicht alle Kommandos des tasks ausgeführt
sind. MERKE: _Wenn du “wait” ohne “do”
verwendest, wird das Script NIEMALS BEENDET! In anderen Worten: tu das nicht._[/color]__

[color=white] [/color]

[color=white]Oft
will man erst ein "do” und dann ein “wait” verwenden, um ein Script den
task ausführen und auf ihn warten zu lassen. In diesem Fall, um Zeit zu sparen,
kannst du folgendes benutzen:[/color]

[color=white] [/color]

[color=white]dowait
( “TASKNAME” )[/color]

[color=white] [/color]

[color=white]Dies
startet den task und pausiert den Rest des Script augenblicklich, bis der task
ausgeführt ist.[/color]

[color=white] [/color]

[color=white]Es ist wichtig, zu wissen, das es einige
Kommandos gibt, die einige Zeit benötigen (z.B. zu einem navgoal zu gehen oder
eine Zeile eines Dialogs beenden), während die meisten Befehle sofort
ausgeführt sind (z.B. der print Befehl). In diesem Dokument sind alle Befehle
die einige Zeit brauchen, mit einem Sternchen (*) gekennzeichnet. Wenn du einen
task machst, muss er mindestens eins von diesen Kommandos beinhalten, oder er
ist fertig, sobald du ihn gestartet hast.[/color]

[color=white] [/color]

[color=white]Das wichtigste, was du dir merken solltest,
ist: _Ein task ist nur für das Entity für das er definiert ist._ Das
heißt, wenn du einen task auf einem Entity definiert hast, und dann von einem
anderen aus, z.B. per affect, darauf zugreifen willst, bekommst du einen
"cannot find task block TASKNAME” Fehler.[/color]

[color=white] [/color]

[color=white]Als Beispiel:[/color]

[color=white] [/color]

[color=white]task ( “Go to the door” )[/color]

[color=white]{[/color]

[color=white]           
commands…[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]affect ( “Fred”, FLUSH )[/color]

[color=white]{[/color]

[color=white]           
dowait ( “Go to the door”);[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]Ist
falsch. “Fred” hat keine Ahnung, was zum Teufel denn “Go to the door” sein
soll, _weil der task von einem Entity definiert wurde, der "Fred" [u]affected[/u]
hat_, und nicht "Fred" selber![/color]

[color=white] [/color]

[color=white]Die
richtige Art:[/color]

[color=white] [/color]

[color=white]affect
( “Fred”, FLUSH )[/color]

[color=white]{[/color]

[color=white]task ( “Go to the
door” )[/color]

[color=white]{[/color]

[color=white]           
commands…[/color]

[color=white]}[/color]

[color=white]           
dowait ( “Go to the door”);[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]Zu
Anfang ist das ein normaler Fehler, aber du wirst es mit der Zeit lernen.[/color]

[color=white]           
Als letztes ist es wichtig, das man einen task nur ein Mal definieren kann,
jedoch beliebig oft ausführen.[/color]

[color=white] [/color]

[color=white]Als Beispiel:[/color]

[color=white] [/color]

[color=white]loop ( 50 )[/color]

[color=white]{[/color]

[color=white]task ( “Go to the
door” )[/color]

[color=white]{[/color]

[color=white]           
commands…[/color]

[color=white]}[/color]

[color=white]           
dowait ( “Go to the door”);[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]Ist
Falsch. Es definiert den task 50 mal! [/color][color=white]Was du willst
ist:[/color]

[color=white] [/color]

[color=white]task ( “Go to the door” )[/color]

[color=white]{[/color]

[color=white]           
commands…[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]loop ( 50 )[/color]

[color=white]{[/color]

[color=white]           
dowait ( “Go to the door”);[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]Das
definiert den task einmal, aber führt in 50 Mal aus, wie du wolltest.[/color]

[color=white] [/color]

**[color=white]

[/color]**

**[color=white] [/color]**

[u][color=white]Sound Kommando[/color][/u][u][/u]

[color=white]sound([/color][color=white] CHANNEL, dateiname )[/color]

[color=white]           
[/color][color=white]Mit dem
Sound Kommando spielt man einen Sound. (wer hätte das
gedacht :D ) Es gibt verschiedene Kanäle auf denen du den Sound abspielen
lassen kannst. Wenn du einen Sound in einem noch gebrauchten Kanal spielst,
wird der vorherige Sound ausgemacht.[/color]

[color=white] [/color]

[color=white]CHAN_AUTO         ??      Sucht sich einen ungenutzten
Kanal und spielt da den Sound[/color]

[color=white]CHAN_LOCAL              Menü Sounds usw.[/color]

[color=white]CHAN_WEAPON          Spielt im Waffen Kanal ab[/color]

[color=white]CHAN_VOICE               Lässt den NPC seinen Mund bewegen[/color]

[color=white]CHAN_VOICE_ATTEN   Lässt den NPC seinen Mund bewegen, benutzt
den normalen Sound-Falloff (wird leiser)[/color]

[color=white]CHAN_ITEM                 Spielt den Sound auf dem Item
Kanal[/color]

[color=white]CHAN_BODY               Spiel auf dem Körper Kanal
(Fußstapfen, Aufkomm-Sounds usw.)[/color]

[color=white]CHAN_AMBIENT          Für ambiente Sounds[/color]

[color=white]CHAN_LOCAL_SOUND Chat Nachrichten etc[/color]

[color=white]CHAN_ANNOUNCER    Ansagen etc, werden global abgespielt[/color]

[color=white]CHAN_LESS_ATTEN    gibt den Sound wie chan_voice aus, aber
benutzt die CHAN_AUTO-leeren-Kanal-such-Funktion[/color]

[color=white]CHAN_MENU1             Menüsachen etc.[/color]

[color=white]CHAN_VOICE_GLOBAL            Lässt den NPC den Mund bewegen und
ist wie Announcer global[/color]

[color=white] [/color]

[color=white]Wenn
ein Sound fertig sein soll ehe das Script weiterläuft, wird das so gemacht:[/color]

[color=white] [/color]

[color=white]task(
“say hello” )[/color]

[color=white]{[/color]

[color=white]           
sound( [/color][color=white]CHAN_VOICE,
“sound/voice/test/helloworld.wav” )[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]print(
“Hello yourself! )[/color]

[color=white] [/color]

[color=white]Man
kann auch auf Sounds auf den Kanälen CHAN_VOICE_ATTEN und CHAN_VOICE_GLOBAL
warten, aber auf die andern nicht.[/color]

[color=white] [/color]

[color=white] [/color]

[u][color=white]Brush-Manupulation-Kommandos[/color][/u][u][/u]

[color=white](move, rotate)[/color]

[color=white]Das **move** Kommando bewegt einen Brush von einer festgelegten
Position in einer Anzahl Millisekunden zu einer anderen, etwa so:[/color]

[color=white] [/color]

[color=white]move (<0 0 0>, <0 0 1000>, 1000 )[/color]

[color=white] [/color]

[color=white]Der Brush bewegt sich vom Zentrum (bei <0 0 0>) aus 1000 map
units höher als das Zentrum.[/color]

[color=white] [/color]

[color=white]Du kannst auch das get-, und das tag-Kommando benutzen um die
Koordinaten zu bestimmen, also so:[/color]

[color=white] [/color]

[color=white]move ( tag(“spot1”, ORIGIN), tag(“spot2”,
ORIGIN), 1000 )[/color]

[color=white] [/color]

[color=white]move ( get(VECTOR, “parm1”), get(VECTOR,
“parm2”), 1000 )[/color]

[color=white] [/color]

[color=white]Mehr zum tag und get Kommando später…[/color]

[color=white]Man kann auch den mittleren Wert auslassen, dann wird der Brush zu
diesem Punkt bewegt.[/color]

[color=white] [/color]

[color=white]Das **rotate** Kommando dreht den brush um einen festgelegten
Winkel in eine Zeit in Millisekunden:[/color]

[color=white] [/color]

[color=white]rotate( <0 90 0>, 1000 )[/color]

[color=white] [/color]

[color=white]dreht den brush um 90° um die Z-Achse.[/color]

![image]({static}images/rotate_script_xyz.jpg)

Quelle: www.map-review.com

[color=white] [/color]

[color=white]Merke: die Zeitangabe 0 dreht den brush augenblicklich.[/color]

[color=white] [/color]

[color=white][/color]

[color=white][/color]

[u][color=white]Use[/color][/u]

[u][color=white][/color][/u]

[color=white]Mit
dem Use Kommando kann man Entities in der Map benutzen.[/color]

[color=white]Use(
“Targetname“ );[/color]

[color=white]Targetname
ist der targetname eines (oder mehrerer) Entitys im Radiant.[/color]

[color=white][/color]

[u][color=white]Remove[/color][/u]

[color=white]Mit remove werden Entities gelöscht.[/color]

[color=white]Remove([/color][color=white] “targetname“ );[/color]

[color=white]targetname[/color][color=white] ist dabei der Name des Entitys. Heißt z.B. ein NPC Fred, hat also
NPC_targetname Fred, so wäre das script um ihn zu löschne[/color]

[color=white]Remove([/color][color=white] “Fred“ );[/color]

[color=white][/color]

[u][color=white]Print[/color][/u]

[color=white]Mit print gibt man einen Text aus.[/color]

**[color=white]

[/color]**

**[color=white] [/color]**

[u][color=white]CAMER[/color][/u][u][color=white]A Kommandos[/color][/u][u][/u]

[color=white](enable, disable, move, pan, zoom, roll,
follow, track, distance, fade, shake, path)[/color]

[color=white]Die camera Kommandos werden für Cutscenes
genutzt: gescriptete Ereignisse, in denen die Kameraperspektive sich ändert und
es schwarze Balken gibt.[/color]

[color=white] [/color]

[u][color=white]Enable[/color][/u][color=white] – Dies aktiviert den Kamera Modus. Die Sicht des Spiele wird zu
der der Kamera.[/color]

[color=white] [/color]

[u][color=white]Disable[/color][/u][color=white] - Dies deaktiviert den Kamera Modus und der Spieler kehrt in die
normale Sicht zurück.[/color]

[color=white] [/color]

[u][color=white]Move[/color][/u][color=white] – Das wird benutzt um die Kamera zu einem bestimmten Punkt oder
bestimmten Koordinaten zu bewegen. Hierzu gibt es drei Möglichkeiten:[/color]

[color=white] [/color]

[color=white]camera(
MOVE, <0 0 0>, 0 )[/color]

[color=white] [/color]

[color=white]Bewegt
die Kamera zu den Koordinaten <0 0 0>, dem Mittelpunkt der Map[/color]

[color=white] [/color]

[color=white]camera( MOVE, tag( “cameraSpot1”, ORIGIN
), 0 )[/color]

[color=white] [/color]

[color=white]bewegt
die Kamera zu dem ref_tag in der Map, der “cameraSpot1” heißt.[/color]

[color=white] [/color]

[color=white]camera( MOVE, get( VECTOR, “SET_ORIGIN” ),
0 )[/color]

[color=white] [/color]

[color=white]Bewegt
die Kamera an die Position des aktuellen Entitys (oder was immer für'n Vector
im set Feld geholt wird bzw. welche Variable du "gettest").[/color]

[color=white] [/color]

[color=white]Der
letzte Parameter gibt an, wie lange die Kamera (in Millisekunden) für die
Bewegung braucht. Wenn du Null eingibst, springt die Kamera sofort zum
Ausgangspunkt. Wenn du 1000 eingibst, wird die Kamera sich so schnell bewegen,
dass sie exakt 1000 Millisekunden (eine Sekunde) braucht, um am Ziel
anzukommen.[/color]

[color=white] [/color]

[u][color=white]Pan[/color][/u][color=white] – Damit drehst du die Kamera. Du kannst sie nach links, rechts,
oben oder unten gucken lassen, und wenn du willst kannst du sie sich um die
eigene Achse drehen lassen (also schief stellen).[/color]

[color=white] [/color]

[color=white]Camera
( PAN, Drehung, Schwenk, Dauer )[/color]

[color=white] [/color]

[color=white]Das
Format ist:[/color]

[color=white]Camera(
PAN, <0 0 0>, <0 0 0>, 0 )[/color]

[color=white] [/color]

[color=white]Die
benutzten Werte sind: <pitch yaw roll>[/color]

[color=white] [/color]

[color=white]Da
ich den Originaltext hier nicht so recht verstanden hab, beschreib ich mal das,
was ich tu.[/color]

[color=white]Im
1. Feld  werden
die gewünschten Endwerte eingegeben, da ich das mit dem Schwenken a) nicht
brauche und es b) nicht verstanden habe lass ich das 2. immer auf <0 0 0>,
im 3. steht die Dauer.[/color]

[color=white](Originaltext: The destinationAngle is the
final angle you intend to finish at.  The panDirection is the direction
you wish each axis to move in.  Any value is valid, but it will only look
to see if each axis’ direction is positive or negative.  A value of zero
will make the camera find the shortest direction to pan in to reach the
destinationAngle.)[/color]

[color=white]Und,
wie beim Move Kommando, kann man die Werte auf drei Arten einstellen[/color]

[color=white] [/color]

[color=white]camera( PAN, <0 0 0>, <1 1 1>,
0 )[/color]

[color=white]camera( PAN, tag( “cameraSpot1”, ORIGIN ),
<1 1 1>, 0 )[/color]

[color=white]oder[/color]

[color=white]camera( PAN, get( VECTOR, “SET_ORIGIN” ),
<1 1 1>, 0 )[/color]

[color=white] [/color]

[color=white]Eine
Dauer von Null dreht die Kamera augenblicklich, bei mehr als Null wird sie
geschwenkt.[/color]

[color=white] [/color]

[u][color=white]Zoom[/color][/u][color=white] – Verändert die Linsengröße, hat den Effekt eines Zooms.[/color]

[color=white] [/color]

[color=white]Camera(
ZOOM, 80, 0 )[/color]

[color=white] [/color]

[color=white]Der
zweite Wert  80 ist die Linsengröße die benutzt werden soll. 80 ist die
normale Linsengröße, 1 ist der maximale Zoom und 120 der größte mögliche Wert.
Der letzte Wert ist die Dauer, bei Null wird augenblicklich der neue Zoom
angenommen, ansonsten dauert es [X] Millisekunden.[/color]

[color=white] [/color]

[u][color=white]Roll[/color][/u][color=white] – Hiermit kann man die Kamera kippen.[/color]

[color=white] [/color]

[color=white]Camera(
ROLL, 45, 0 )[/color]

[color=white] [/color]

[color=white]Ein
positiver Wert dreht die Kamera nach rechts, ein negativer nach links. Der
letzte Wert ist die Dauer.[/color]

[color=white] [/color]

[u][color=white]Follow[/color][/u][color=white] – Lässt die Kamera
einer Gruppe Entities folgen.[/color]

[color=white] [/color]

[color=white]camera( FOLLOW, “cameraGroup”, speed,
initialLerp )[/color]

[color=white] [/color]

[color=white]Das
“cameraGroup” ist eine Zeichenkette (String). Jedes Entity, dass dieser
“cameraGroup” angehört, wird Teil der “Szene”. Die Kamera sucht sich
automatisch die Mitte der “Schauspieler”. Das ist nicht nur nützlich, um
die Kamera NPCs folgen zu lassen, sondern auch, um eine die Kamera richtig
einzustellen, um alle NPCs ins Bild zu kriegen. Um die “cameraGroup” von einem
Entity einzustellen, benutze das [/color][SET_CAMERA_GROUP](#camGroup) [color=white]Kommando (mehr zum
Set-Kommando steht in der Set-Sektion).[/color]

[color=white] [/color]

[color=white]Der
zweite Wert ist die Drehgeschwindigkeit der Kamera. Je höher diese ist,
desto schneller reagiert die Kamera. Der Wert 0 entspricht dem Standardwert
(100).[/color]

[color=white]“initialLerp”
ist ein wahr/falsch (0/1) Kommando, mit dem man einstellt, ob die Kamera erst
langsam (bzw. schnell, je nach “speed”) in Richtung der “cameraGroup” schwenkt
oder Augenblicklich die Richtung ändert. [/color]

[u][color=white]Track[/color][/u][color=white] – Lässt die Kamera einem Pfad folgen[/color]

[color=white] [/color]

[color=white]Camera( TRACK, “trackName”, speed,
initialLerp )[/color]

[color=white] [/color]

[color=white]Der
“trackName” ist der targetname des ersten path_corners aus einer Reihe
selbiger. Die funktionieren wie bei einer func_train.[/color]

[color=white] [/color]

[color=white]Der
“speed” Wert stellt ein, wie schnell sich die Kamera bewegt.[/color]

[color=white] [/color]

[color=white]Wenn
“InitialLerp” gleich 1 ist, bewegt sich die Kamera erst von ihrer
aktuellen Position zum ersten path_corner mit der in “speed“ eingestellten
Geschwindigkeit, wenn es gleich 0 ist kommt sie sofort da hin.[/color]

[color=white]Wenn
die Kamera einen path_corner erreicht, sieht sie nach, ob beim nächsten ein
speed eingestellt ist, und benutzt ggf. diesen. Damit kann man die Kamera in
verschiedenen geschwindigkeiten fahren lassen.[/color]

[color=white] [/color]

[color=white]Distance
– Stellt die Mindestentfernung der Kamera zur “cameraGroup” ein.[/color]

[color=white] [/color]

[color=white]Camera(
DISTANCE, distance, initialLerp )[/color]

[color=white] [/color]

[color=white]Dieses
Kommando funktioniert mit dem “FOLLOW”Kommando, und moistens auch mit “TRACK”.
Die eingestellte “distance” bremst die Kamera ab, so dass eine
Mindestentfernung zur “cameraGroup” erhalten wird. Wenn die Kamera gerade einem
“TRACK“ folgt, wird der “speed“ angeglichen, so dass die Kamera weit genug von
der “cameraGroup“ entfernt ist.[/color]

[color=white]Mit
“initialLerp” kann man die Kamera schneller werden lassen, damit sie auf die
gewünschte “distance“ kommt, statt einer sofortigen Positionsänderung.[/color]

[color=white] [/color]

[u][color=white]Fade[/color][/u][color=white] – Lässt die Kamera ihre RGB (Rot Grün Blau) Farbe und Transparenz
ändern.[/color]

[color=white] [/color]

[color=white]Camera( FADE, startRGB, startOpacity,
endRGB, endOpacity, duration )[/color]

[color=white] [/color]

[color=white]Um
einen Fade-to-Black (bildschirm wird Schwarz) über 2 sekunden zu machen,
benutzt man das:[/color]

[color=white] [/color]

[color=white]Camera(
FADE, <0 0 0>, 0, <0 0 0>, 1, 2000 )[/color]

[color=white] [/color]

[color=white]Man
kann das Schwarz auch wieder ausblenden, und zu Weiß oder irgendeiner anderen
Farbe wechseln.[/color]

[color=white] [/color]

[u][color=white]Shake[/color][/u][color=white] – Rüttelt die Kamera für eine angegebene Zeit.[/color]

[color=white] [/color]

[color=white]Camera(
SHAKE, intensity, duration )[/color]

[color=white] [/color]

[color=white]Die
“intensity” (Intensität) wird in Zahlen von 1 bis 16 angegeben.[/color]

[color=white] [/color]

[color=white]Die
“duration” (Dauer) wird in Millisekunden angegeben. (1 sek = 1000 milisek)[/color]

**[color=white] [/color]**

**[color=white]Path* - [/color]**[color=white]Lässt die Kamera einem ROF Pfad folgen.[/color]

[color=white] [/color]

[color=white]Stellt einen ROF Pfad ein, dem die Kamera folgt.
Dies ist ein Kommando, auf dessen Vollendung gewartet werden kann
(task+dowait).[/color]

[color=white] [/color]

[color=white]Camera(
PATH, “roff/bob.rof” )[/color]

[color=white] [/color]

[color=white] [/color]

[u][color=white]Get[/color][/u][u][/u]

[color=white]Get( FLOAT/VECTOR/STRING, “” )[/color]

[color=white]           
[/color][color=white]Alles was
man “setten” kann, kann man auch “getten”. Get wird benutzt, um einen Wert aus
einem Set-Feld in ein anderes zu kopieren, oder für IF-Abfragen.[/color]

[color=white] [/color]

[color=white]set(“SET_PARM1”, “Fred”)[/color]

[color=white] [/color]

[color=white]if( get(STRING, “SET_PARM1”) = “Fred” )[/color]

[color=white]{[/color]

[color=white]           
print(“Hello World!”)[/color]

[color=white]}[/color]

[color=white]  [/color]

[color=white]           
In BehavEd kann man “Get” benutzen, wenn man auf den “helper” button im
Kommando Editieren Dialog klickt.[/color]

[color=white] [/color]

[color=white] [/color]

[color=white] [/color]

[u][color=white]Variablen[/color][/u]

[color=white](global/local)[/color]

[color=white]Alle Variablen müssen deklariert (eingerichtet)
warden, ehe man sie benutzen kann. Dabei muss der Typ und der Name der Variable
eingestellt werden.[/color]

[color=white] [/color]

[color=white]declare( FLOAT, “zaehler” )[/color]

[color=white]declare( VECTOR, “position” )[/color]

[color=white]declare(
STRING, “meinName” )[/color]

[color=white] [/color]

[color=white]Und
so werden Variablen eingestellt:[/color]

[color=white]set(
“meinName”, “Fred” )[/color]

[color=white] [/color]

[color=white]Jetzt
kann man Variablen jedenzeit “getten”, z.B. in IF-Abfragen:[/color]

[color=white] [/color]

[color=white]If ( get(STRING, “meinName”) = “Fred” )[/color]

[color=white]{[/color]

[color=white]           
print( “Hello, World!” )[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]Wenn
man eine Variable nicht mehr braucht, kann man sie “löschen”:[/color]

[color=white] [/color]

[color=white]free(
“meinName” )[/color]

 

[color=white]Alle
Variablen werden gelöscht, wenn das Level zu Ende ist, aber vielleicht willst
du sie ja selber während das Level läuft löschen, weil maximal 32 Variablen pro
Typ pro Level erlaubt sind[/color]

[color=white] [/color]

[color=white]Natürlich
kann man Variablen auch bei Set benutzen:[/color]

[color=white] [/color]

[color=white]set( “SET_NAVGOAL”, get(STRING,
“globalNavGoal”) )[/color]

[color=white] [/color]

[color=white]So
kann man in einem Script einen globalen “Navgoal” (Punkt, zu dem ein NPC laufen
soll) einstellen, und diesen immer benutzen. Das Einstell-Script sähe dann so
aus:[/color]

[color=white] [/color]

[color=white]set(
“globalNavGoal”, “FredsHome” )[/color]

[color=white] [/color]

[color=white]Oder,
wenn das Script vielseitiger sein soll:[/color]

[color=white] [/color]

[color=white]set( “globalNavGoal”, get(STRING,
“SET_PARM1”) )[/color]

[color=white] [/color]

[color=white]So
kann man 50 Entities das Script immer anders ausführen lassen, je nachdem, was
ihr parm1 ist.[/color]

[color=white] [/color]

[color=white] [/color]

[u][color=white]Random[/color][/u][u][/u]

[color=white]Random(
minNumber, maxNumber )[/color]

[color=white]           
Mit dieser Variablen-Funktion kann man ein wenig Zufall in seine Scripts
kriegen. Gib das einfach dort ein, wo eigentlich ne Nummer stehen sollte, und
es wird eine zufällige ermittelt.[/color]

[color=white] [/color]

[color=white]random[/color][color=white]( 0, 3.5 )[/color]

[color=white] [/color]

[color=white]Hier
wird dann eine zufällige Nummer zwischen 0 und 3,5 benutzt.[/color]

[color=white] [/color]

[color=white]Man
kann Random nur über den “helper” Button erreichen. [/color]

[color=white] [/color]

[u][color=white]TAGs[/color][/u]

[color=white]TAG( “targetname”, ORIGIN/ANGLE )[/color]

[color=white]           
Im Radiant kann man entities namens Ref_tag platzieren. Bei denen wird dann ein
targetname, und durch a) angles oder b) einen info_notnull/target_position die
Richtung eingestellt. Diese ref_tags kann man dann in Scripts benutzen, um
Koordinaten einzustellen, ohne umständlich die Koordinaten einzustellen. (Außerdem
wird das script dadurch flexibler)[/color]

[color=white] [/color]

[color=white]Beispiel:[/color]

[color=white] [/color]

[color=white]camera[/color][color=white]( MOVE, tag(“cameraSpot1”, ORIGIN), 0 )[/color]

[color=white] [/color]

[color=white]Hiermit
wird die Kamera zum ref_tag mit dem targetname “cameraSpot1” bewegt.[/color]

[color=white] [/color]

[color=white]Man
kann auch die Richtung der Kamera via ref_tag einstellen:[/color]

[color=white] [/color]

[color=white]camera( PAN, tag(“cameraSpot1”, ANGLES),
<1 1 1>, 0 )[/color]

[color=white] [/color]

[color=white]In
BehavEd kann man tag unter “helper” auswählen.[/color]

**[color=white]

[/color]**

**[color=white] [/color]**

[u][color=white]Set Kommando[/color][/u][u][/u]

[color=white]set( SET_TABLE, value )[/color]

[color=white] [/color]

[color=white]           
[/color][color=white]Das “set”
Kommando ist sicherlich das nützlichste einzelne Kommando. Man kann damit
eigentlich “nur” den Wert von einer beliebigen Variable aus der Set Liste (in
BehavEd ein Dropdown Menü) setzen. Allerdings ist der dadurch erreichte Effekt
(teilweise) ziemlich groß, was dieses Kommando sehr mächtig macht.[/color]

[color=white] [/color]

[color=white]Beispiel:[/color]

[color=white] [/color]

[color=white]set(
“SET_BEHAVIORSTATE”, “BS_WANDER” )[/color]

[color=white] [/color]

[color=white]Dieses
Kommando sagt einem NPC, dass er zufällig durch das Waypoint-Netz des Levels
wandern soll. (Vorrausgesetzt es gibt Waypoints ;) )[/color]

[color=white] [/color]

[color=white]In
der nächsten Sektion steht die Liste sämtlicher SET Variablen mitsamt
Erklärung.[/color]

[color=white] [/color]

[color=white]Kurz noch was zu den SET_PARM Variablen:[/color]

[color=white] [/color]

[color=white]Es
gibt 16 davon – SET_PARM1 bis SET_PARM16. Es sind Strings, Nummern oder
Vektoren, die man im Radiant bei den Entities (in den Einstellungen, via Key:
Parm1 Value: meinWert) einstellt. Damit kann man das Script flexibler machen.[/color]

[color=white] [/color]

[color=white]Ein
einfaches Beispiel:[/color]

[color=white] [/color]

[color=white]In
deiner Map gibts einen NPC, der zwischen 3 waypoints hin und her laufen soll,
die “nav1”, “nav2” und “nav3” 
heißen. Normalerweise würdest du jetzt so ein Script schreiben:[/color]

[color=white] [/color]

[color=white]set(
“SET_BEHAVIORSTATE”, “BS_DEFAULT” )[/color]

[color=white]set([/color][color=white] “SET_WALKING”, “true” )[/color]

[color=white]Loop( -1 )[/color]

[color=white]{[/color]

[color=white]task( “walk to
nav1” )[/color]

[color=white]{[/color]

[color=white]           
set( “SET_NAVGOAL”, “nav1” )[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]task( “walk to
nav2” )[/color]

[color=white]{[/color]

[color=white]           
set( “SET_NAVGOAL”, “nav2” )[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]task( “walk to
nav3” )[/color]

[color=white]{[/color]

[color=white]           
set( “SET_NAVGOAL”, “nav3” )[/color]

[color=white]}[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]So,
und nun läuft dein NPC für immer diese 3 Navgoals ab.[/color]

[color=white] [/color]

[color=white]Aber jetzt setzt du einen andern NPC in die map,
der 3 ganz andere Navgoals, nämlich “point1”, “point2” und “point3” ablaufen
soll, ablaufen soll, in die Map. Tja, jetzt musst du noch ein Script schreiben.
“Was?!?”, denkst du jetzt bestimmt, “das muss doch einfacher gehn!” Recht hast
du. Denn jetzt kommen die parms. [/color]

[color=white] [/color]

[color=white]Beim
ersten NPC, der die 3 “nav” Navgoals ablaufen soll, stellst du jetzt ein:[/color]

[color=white] [/color]

[color=white]parm1              
nav1[/color]

[color=white]parm2              
nav2[/color]

[color=white]parm3              
nav3[/color]

[color=white] [/color]

[color=white]Und
beim zweiten, der die 3 “point”s nehmen soll:[/color]

[color=white] [/color]

[color=white]parm1              
point1[/color]

[color=white]parm2              
point 2[/color]

[color=white]parm3              
point 3[/color]

[color=white] [/color]

[color=white]Und
dann kriegen beide NPCs das selbe script, dieses:[/color]

[color=white] [/color]

[color=white]set( “SET_BEHAVIORSTATE”, “BS_DEFAULT” )[/color]

[color=white]set( “SET_WALKING”, “true” )[/color]

[color=white]Loop( -1 )[/color]

[color=white]{[/color]

[color=white]task( “walk to
nav1” )[/color]

[color=white]{[/color]

[color=white]           
set( “SET_NAVGOAL”, get( STRING, “SET_PARM1” ) )[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]task( “walk to
nav2” )[/color]

[color=white]{[/color]

[color=white]           
set( “SET_NAVGOAL”, get( STRING, “SET_PARM2” ) )[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]task( “walk to
nav3” )[/color]

[color=white]{[/color]

[color=white]           
set( “SET_NAVGOAL”, get( STRING, “SET_PARM3” ) )[/color]

[color=white]}[/color]

[color=white]}[/color]

[color=white] [/color]

[color=white]Hier
werden dann ,von den get Kommandos, parm1, parm2 und
parm3 als Navgoals genommen.[/color]

[color=white] [/color]

[color=white]So
kann du das selbe Script immer und immer wieder benutzen. Vielleicht sieht das
auf den ersten Blick nach mehr Arbeit aus, vor allem wenn du nur 2 NPCs hast,
aber wenn du dann anfängst, an die 50 NPCs zu haben, wirst du schnell merken,
dass auf diese Weise doch einfacher gewesen wäre.[/color]

[color=white] [/color]

[color=white]Eine
Sache solltest du beachten: Wenn du dieses Script änderst, werden alle NPCs davon
betroffen sein. Aber falls du genau das willst (oder musst), dann brauchst du
nur ein Script ändern, und nicht 50 [/color]

[color=white][/color]

[color=white][/color]

**[color=white] [/color]**

[u][color=white]SET Kommando Variablen(Set Liste):[/color][/u][u][/u]

[color=white] [/color]

[color=white]Hier
ist eine Liste von allen Set Variablen im Spiel. Jede hat im Spiel eine
spezielle Funktion.[/color]

[color=white]Wenn
du NPCs einstellen willst, sind die Behavior Sets und Behavior States von
großer Bedeutung:[/color]

[color=white] [/color]

[color=white]Behavior
Sets (spawnscript, usescript, awakescript, etc.) – Das ist ein Script, dass der
NPC ausführt, wenn eine bstimmte Situation eintrifft. (Beschreibung im
Einzelnen s.u.) [/color]

[color=white]Behavior
States – Hier wird das Verhalten des NPC eingestellt – welche KI benutzt werden
soll. Siehe die Behavior State Liste weiter unten. [/color]

[color=white]Noch mal zur Erinnerung:
Alles mit einem vorangehenden Sternchen (*) wird das Script pausieren, bis es
fertig ausgeführt ist.[/color]

[color=white]Mit Targetname ist bei
NPCs meistens NPC_targetname gemeint.[/color]

[color=white] [/color]

[color=white]Alle [/color]**[color=gray]eingegrauten[/color]** [color=white]Kommandos/Listeneinträge
sind nicht eingebaut und funktionieren folglich nicht.[/color]

[color=white] [/color]

##[color=white]Behavior Sets
:[/color]

[color=white] [/color]

###[color=white]Set Field Name                         Typ
des Werts  Beschreibung        &nbsp[/color]

