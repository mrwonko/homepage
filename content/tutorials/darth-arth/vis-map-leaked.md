title: Visibility / Map Leaked
date: 2008-05-01
type: tutorials/darth-arth
author: mrwonko
category: advanced
tags: Vis
modified: 2015-04-12
slug: vis-map-leaked


*Map Leaked* - die meisten kennen diesen Fehler, denn er kann leicht auftreten: sobald irgendwo in der Map ein Loch ist, kommt er. Als Folge funktioniert das -vis Kompilieren nicht, wodurch die Performance in den Keller geht.

Wie löst man dieses Problem? Wer nicht lange auf Lochsuche gehen will, baut einen großen Kasten um seine Karte, und behebt damit das Symptom (den Fehler), nicht jedoch das eigentliche Problem (geringe Performance).

Wieso nicht die Folge? Wieso ist die Performance immer noch unten?

Um das zu verstehen, muss man wissen, wie die Performance-Optimierung in Jedi Knight bzw. der Quake 3 Engine allgemein funktioniert:

Beim `-vis` Kompilieren wird die Map in Blöcke aufgeteilt. Die Größe ist im Worldspawn mit `_blocksize` festgelegt, das kann einem aber zu Anfang erstmal egal sein, ich habe das bisher auch noch nie umgestellt.

Nun wirkt jeder Brush (außer Detailbrushes, Entities und Patches) auf den Block, in dem er sich befindet, wie ein Messer - der Block wird in mehrere aufgeteilt.

Anschließend wird berechnet, von welchem Block aus welche anderen sichtbar sind - nur diese werden dann berechnet, wenn der Spieler sich in diesem Block befindet.

Um den Berechnungsaufwand gering zu halten, sollte man daher nur die nötigsten Brushes zur Berechnung mit einbeziehen, und die anderen zu Detailbrushes machen (Rechtsklick -> `make Detail` oder <kbd>Strg</kbd> + <kbd>M</kbd>), damit für kleine Details wie z.B. Gitter keine zig Blöcke erstellt werden.

Die Blöcke kann man übrigens sehen, wenn man bei `-vis` mit `-saveprt` kompiliert und die entstehende `*levelname*.prt` mit dem GTK-Radiant-Plugin prtviewer lädt.

Wenn wir nun Löcher in der Map haben und zum "_Beheben_" eine große Box um die Map gebaut haben, kann es sein, dass 2 Räme, die eigentlich an unterschiedlichen Enden der Map sind und sich nie sehen könnten, sich durch diese Löcher doch sehen. Schnell kann es passieren, dass stets die gesamte Map berechnet wird. Mal ganz davon abgesehen, das Spieler womöglich aus der Map hinausfallen könnten.

Daher sollte man Löcher beheben, indem man sie stopft. Wenn man vom Radiant aus kompiliert, zeigt einem eine rote Linie den Weg zum Loch. Dabei sollte man via <kbd>Strg</kbd> + <kbd>D</kbd> Detailbrushes, via <kbd>Strg</kbd> + <kbd>P</kbd> Patches und via <kbd>Alt</kbd> + <kbd>2</kbd> Entities ausblenden, weil diese ja für `-vis` nicht relevant sind. Hat man das Loch dann gefunden, so muss es nur noch geschlossen werden.