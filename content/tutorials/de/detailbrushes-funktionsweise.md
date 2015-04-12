title: Detailbrushes - Funktionsweise
date: 2007-12-13
type: tutorials
author: mrwonko
category: advanced
tags: Detail, FIXME
modified: 2015-04-12

# Voraussetzungen

* [Mein erster Raum](www.darth-arth.de/tutorials/mapping/firstroom/firstroom.htm) FIXME

# Tutorial

Beim Kompilieren werden u.a. aus den Brushes einzelne Dreiecke gemacht, sogenannte Tris. Im Spiel kann man diese, wenn die maps mit cheats gestartet wurde (`devmap mapname`) und, falls es im mp ist, `developer 1` eingestellt wurde, mit `r_showtris 1/2` anzeigen.

Jedenfalls, wie brushes zerschnitten werden, hängt davon ab, welchen Typ sie haben. Im Radiant sieht das ganze z.B. noch so aus:

![image](wonko822.wo.funpic.de/downloads/detailbrushes/images/radiant.jpg)

Wenn alles Structural-Brushes sind, man also keine Detailbrushes benutzt, sieht es im Spiel so aus:

![image](wonko822.wo.funpic.de/downloads/detailbrushes/images/game_structural.jpg)

Ist jedoch der Quader ein Detail-Brush, so zerschneidet er die Fläche nicht und es sieht so aus:

![image](wonko822.wo.funpic.de/downloads/detailbrushes/images/game_detail.jpg)

[color=red]Möglicherweise sind die Bilder falsch und Detailbrushes haben darauf überhaupt keine Auswirkung. Diskussion siehe [hier](darth-arth.de/forum/viewtopic.php?p=38752)[/color] FIXME



Das heißt, es werden weit weniger Dreiecke erstellt und die Grafikkarte hat demnach weniger zu tun. 

Zum Anderen und **vor Allem** werden durch Detailbrushes keine "Portale" erstellt, das spart dem Compiler Arbeit und so geht das -vis Kompilieren schneller. Das ist jetzt sehr stark verkürzt, man kann das schöner sehen, wenn man beim -vis Kompilieren -saveprt angibt, und die dadurch entstehende .prt mit dem prt-Viewer Plugin des Radiant anschaut.

# Anmerkung

Detailbrushes werden vom Compiler gewissermaßen ignoriert ,das heißt, wenn sie den Map-Innenraum mit dem Void (das "große Grau") verbinden, gibt es ein Leak. Daher sollte man sie bei der Leaksuche im Radiant mit `Strg + D` ausblenden.

# Schlusswort

So, ich hoffe, ich konnte euch Detailbrushes ein wenig näher bringen. Wenn ihr sie geschickt einsetzt, könnt ihr zum einen die Performance eurer Map verbessern und zum anderen ein paar böse Fehler vermeiden. Vor allem bei vielen Brushes auf kleinem Raum, z.B. bei einem Gitter, sollten Detailbrushes verwendet werden.

Euer Mr. Wonko