title: Detailbrushes - Einsatz
date: 2008-04-05
type: tutorials/darth-arth
author: mrwonko
category: advanced
tags: Detail, Vis
modified: 2015-04-12
slug: vis-detailbrushes-einsatz

# Voraussetzungen

* [Mein erster Raum]({filename}brushwork-first-room.md)
* ([Detailbrushes - Funktionsweise]({filename}vis-detailbrushes-funktionsweise.md))

# Tutorial

Alles mit Ausnahme der Wände sollte zu Detailbrushes gemacht werden, sodass man hinterher nur noch die groben Raumformen hat.

Denn während der Vis-Phase (vis steht für visibility, also Sichtbarkeit) wird berechnet, von wo aus man was von der Map sieht, und im Spiel alles andere ausgeblendet.

Dazu wird die Map in Abschnitte unterteilt, deren Größe im Worldspawn via `_blocksize` eingestellt werden kann. Nun zerschneiden Structuralbrushes, also die, die nicht Detail sind, diese Abschnitte, sodass mehrere entstehen.

Das ist an sich klug, denn so bekommen zwei Räume, die eigentlich in einem Abschnitt sind, zwei eigene Abschnitte. Wenn man nun z.B. eine Tür mit Areaportal oder einen verwinkelten Gang mit Hint-Brushes (siehe entsprechende Tutorials) dazwischen setzt, wird wenn möglich der eine Abschnitt ausgeblendet. Wäre alles Detailbrushes, gäbe es nur einen Abschnitt, und beide Räume würden immer berechnet.

Wenn wir nun aber viele kleine Details haben, z.B. Gitter oder auch einfach Säulen, dann werden sehr viele kleine Bereiche erstellt. Allerdings sind diese z.T. immer sichtbar, z.B. die Löcher in einem Gitter, jedes Loch wird ein einzelner Bereich, aber von beiden Seiten aus sind alle Sichtbar. nur, wenn man in einem der Löcher wäre, könnte man die anderen nicht sehen, aber das wird wohl nicht passieren ;)

Daher sagen wir dem Compiler, dass er bei der Berechnung bitte das Gitter ignorieren soll - wir machen es (z.B. durch Markieren und das Kürzel <kbd>Strg</kbd> + <kbd>M</kbd>) zu Detail.

Hier nochmal ein Beispiel:

![image]({static}vis-detailbrushes-einsatz-1.jpg)

mit ausgeblendeten Details (<kbd>Strg</kbd> + <kbd>D</kbd>):

![image]({static}vis-detailbrushes-einsatz-2.jpg)

Wie man sieht habe ich alles, was nur Verzierung ist und nicht zur grundlegenden Struktur des Raumes gehört, zu Detailbrushes gemacht.


Kleiner Tip noch: Wenn ihr beim vis kompilieren den parameter `-saveprt` angebt, wird eine mapname.prt erstellt, die ihr hinterher im Radiant über `plugins/prtview/load portal file` anschauen könnt, um zu schauen, wo die Portale, also Grenzen der Bereiche, erstellt wurden.
