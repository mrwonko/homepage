title: Leitern
date: 2003-01-01
type: tutorials
author: FallenGuard (Christophe B.)
category: mapping
tags: Leiter
modified: 2015-04-12

# Voraussetzungen

Grundwissen (Brushes erstellen) 

# Tutorial

In diesem Tutorial wird erklärt, wie man Leitern erstellen kann. Obwohl in verschiedenen Spielen, die auf der Quake 3 – Engine basieren, Leitern vorhanden sind (z.B Return to Castle Wolfenstein), sind in Jedi Knight II keine Leitern vorhanden. (Anstatt Leitern werden meistens Lifte benutzt). Doch da die Mapper auch Karten im Mittelalterlichen Stil erstellen, kommt oft die Frage nach einer Leiter auf, die in diesem Tutorial beantwortet werden soll.

## Die Leiter

In Jedi Knight II / Jedi Academy muss man zu einem kleinen Trick greifen, wenn man eine Leiter erstellen möchte. Dabei glaubt der Spieler, er laufe eine Leiter hinauf, jedoch ist diese Leiter nur Staffage. In Wirklichkeit läuft er eine sehr steile Treppe hinauf, die allerdings mit einer unsichtbaren Textur belegt ist, sodass man sie nicht sehen kann.

![image]({filename}leitern-1.jpg)

Dies ist das Bild der Leiter selbst. Sie besteht aus zwei Stangen und mehreren Sprossen. Die Stangen wurden etwas gekippt, damit sie einerseits realistischer aussehen, und andererseits dass man beim herauflaufen so nah wie möglich an den Sprossen bleibt.

Nun folgt die Treppe, worauf der Spieler nach oben läuft.

![image]({filename}leitern-2.jpg)

Die einzelnen Stufen bestehen aus Brushes, die genauso breit wie die Sprossen sind, und (bei Grid 1) 1 Unit breit sind. Die Höhe darf maximal 16 Units betragen, sonst funktioniert die Treppe nicht. Die Brushes werden so aneinander gesetzt, dass sie eine Steil nach oben zeigende Treppe bilden. Sie erhalten eine unsichtbare Textur, wie in diesem Fall `System/Clip`. Da kann man durch schießen und sie wirft keinen Schatten, beides genau was wir wollen.

Nun werden die Leiter und die Treppe zusammen gefügt, so dass ein möglichst geringer Abstand zwischen ihnen liegt.

![image]({filename}leitern-3.jpg)

Hier sieht man die fertige Leiter. 

Treppe und Leiter kommen sich so nah wie möglich, aber berühren sich nicht.

Das war alles. 

Viel Spaß beim Erstellen eurer eigenen Leitern!

[Download der Tutorialmap]({filename}examples/Leiter.zip) (.map - Datei enthalten)
