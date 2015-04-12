title: Aufzug ohne Lip zu kennen
date: 2008-10-11
modified: 2015-04-12
author: kaloeffel
tags: Aufzug, FIXME
type: tutorials
category: mapping

# Voraussetzungen

* http://www.darth-arth.de/tutorials/lift.htm [FIXME]

# Tutorial

Hier nun ein Tutorial, das beschreibt, wie man einen Aufzug baut, ohne den Lip-Wert herauszufinden.

Zuerst brauchen wir einen Raum in dem wir eine Platte auf dem Boden liegen haben. 

Dazu kommt noch ein Brush mit der Textur `systen/nodraw`. 

Diese beiden Brushs machen wir nun zu einer `func_door`, und geben an, dass sie nach oben fahren soll (`angle -1`). 

Zusätzlich geben wir noch `lip 2` an. 

Jetzt brauchen wir eine Stelle, zu der der Aufzug fahren soll, ich klebe einfach eine weitere Platte an die Wand.

Den Nodraw-Brush ziehen wir nun von der Platte aus bis zur gewünschten Höhe. Wenn der Aufzug oben ist, wird das untere Ende des Aufzuges da sein, wo der Nodraw-Brush aufhört. 

Die Lip 2 brauchen wir, da eine Tür immer `eigene Höhe - 2` hoch fährt. Unser Aufzug würde also ein wenig zu tief halten. 

In Radiant sollte es dann etwa so aussehen:

![image]({filename}aufzug-ohne-lip-2d.png)

![image]({filename}aufzug-ohne-lip-3d.png)

Dazu noch ein `trigger_multiple` und schon sollte es wie ein ganz normaler Aufzug funktionieren.

[Download]({filename}examples/lift.pk3)
