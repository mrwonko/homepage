title: Shild Floor Unit nicht nur bei CTF
date: 2008-10-17
type: tutorials/darth-arth
author: kaloeffel
category: advanced
tags: Entities, FIXME
modified: 2015-04-12
slug: entity-shield-floor-unit

In diesem Tutorial will ich erklären, wie man diese schönen Kästen im MP auch wärend FFA nutzbar machen kann.

![image]({static}entity-shield-floor-unit-1.png)

Zuerst platzieren wir ein `misc_model_shield_power_converter` und setzen das Model auf `models/items/a_shield_converter.md3`. Das führt dazu, das wir eine Shild Floor Unit haben, die aber nur unten benutzt werden kann und auch nur dort geclippt ist. Um sie oben zu clippen und gleichzeitig nutzbar zu machen, setzen wir oben ein weiteren `misc_model_shield_power_converter` ein. Damit man nun nicht die doppelte Menge Schild beziehen kann, verkleiden wir das ganze noch mit `system/physics_clip`.

Im Radiant sieht es dann so aus:

![image]({static}entity-shield-floor-unit-2.png) ![image]({static}entity-shield-floor-unit-3.png)

Hätten wir unten ein `misc_model` genommen, wäre dieses schwarz.

Download: http://kaloeffel.ka.funpic.de/darth-arth/sfu.pk3 FIXME
