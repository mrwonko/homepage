title: Mein erster Raum
author: Darth Arth (Artur L.)
date: 2004-01-01
modified: 2015-09-01
category: mapping
type: tutorials/darth-arth
tags: Brushwork
slug: brushwork-first-room

# Voraussetzungen

* Installation JK2 Editing Tools I ([Tutorial]({filename}installation-jk2-editing-tools.md))
* Installation JK2 Editing Tools 2 ([Tutorial]({filename}installation-jk2-editing-tools-2.md))
* Installation GTK - Radiant ([Tutorial](installation-1.4.md))

# Tutorial

In dieser Lehreinheit (Tutorial) lernen wir, einen Einfachen Raum mit einem Spieler-Startpunkt zu erstellen.

Zuerst schalte deine 2D-Ansicht im Editor auf "Draufsicht von oben". Um das zu erreichen, klicke in der Symbol-Leiste auf dieses Symbol ![image]({static}brushwork-first-room/xyz.jpg) "Change Views" (Ansicht wechseln) oder drücke auf <kbd>Strg</kbd> + <kbd>Tab</kbd> so lange, bis die Achsen-Darstellung so aussieht:

![image]({static}brushwork-first-room/z_view.jpg)

oder geh ins Menu und wähle `View > Layout > XY (Top)`

![image]({static}brushwork-first-room/view_top.jpg)

Als nächstes schalten wir den Grid auf 32-Einheiten um. Die Wände von Räumen, vor allem wenn sie groß sind, sollten immer mindestens 16 Einheiten dick sein, ansonsten können im Spiel komische Grafik-Fehler auftreten. Geh ins Menu und wähle `Grid > Grid32` oder drücke die Taste <kbd>6</kbd>.

![image]({static}brushwork-first-room/grid32.jpg)

Jetzt brauchen wir eine spezial Textur (Shader) mit dem Namen "Caulk". Um diese zu finden gehen wir ins Menü und wählen: `Textures > system`. Finde diese Textur und klicke sie an, so dass sie rot umrahmt ist. 

![image]({static}brushwork-first-room/caulk.jpg)

<div class="alert alert-warning"><strong>ACHTUNG</strong>: Bitte nicht verwechseln mit "Caulk_nonsolid"!</div>

Jetzt erstellen wir in dem 2D-Fenster einen rechteckigen Brush, der mindestens 1000 Einheiten breit und 1000 Einheiten lang ist. Klicke einfach auf die <kbd>linke
Maustaste</kbd> halte sie fest und ziehe dann einen Rechteck. Wenn dieser groß genug ist, lasse die Maustaste los. 

![image]({static}brushwork-first-room/firstbrush.jpg)

Du kannst die Größe des Brushes korrigieren, indem du außerhalb des Brushes mit der <kbd>linken Maustaste</kbd> klickst, sie festhältst und dann bewegst.

Wenn der Brush erstellt ist, schalten wir die Sicht jetzt auf Seitenansicht um, damit wir die Höhe des Brushes verändern können. 

Klicke auf die Sichtänderung ![image]({static}brushwork-first-room/xyz.jpg) oder geh ins Menu und wähle `View > Layout > YZ`.

![image]({static}brushwork-first-room/view_side1.jpg)

Klicke jetzt mit der <kbd>linken Maustaste</kbd> oberhalb des Brushes und ziehe ihn mindestens 1000 Einheiten hoch.

![image]({static}brushwork-first-room/firstbrush_hight.jpg)

Das ganze sieht dann so aus:

![image]({static}brushwork-first-room/firstbrush_hight2.jpg)

<div class="alert alert-warning"><strong>ACHTUNG</strong>: Wenn du in deiner 3D-Ansicht den Würfel nicht sehen kannst, dann liegt es wahrscheinlich daran, dass du dich innerhalb des Würfels befindest. Benutze einfach das Scrollrad deiner Maus oder die Pfeiltasten, um aus dem Würfel herauszukommen.</div>

Jetzt haben wir einen großen Würfel. Was wir aber brauchen, ist eine Box. 

Um aus dem Würfel eine Box zu machen, klicke auf das Symbol (Hollow) ![image]({static}brushwork-first-room/button_hollow.jpg) oder geh ins Menu und wähle `Selection > CSG > Make Hollow`.

![image]({static}brushwork-first-room/make_hollow.jpg)

Danach sieht das ganze dann so aus:

![image]({static}brushwork-first-room/firstbrush_hollow.jpg)

Wie dick die Wände nach Ausführung dieser Funktion bleiben, hängt von der aktuellen "Grid"-Einstellung ab.

So nützlich diese Funktion auch ist, doch hat sie einen Fehler. Das heißt, die jetzt neu erstellten 6 Brushes, die unsere Box darstellen, überschneiden sich an den Kanten. Und dies sollte man beim Level-Aufbau möglichst vermeiden. Denn Überscheidungen bei den Brushes verlängern erheblich die Kompilierzeit und produzieren im Spiel die merkwürdigsten Grafik-Fehler.

Um das Problem bei unserer Box zu lösen, benutzen wir die mächtige Funktion "CSG Substract". Wenn man diese Funktion bei einem selektierten Brush durchführt, werden alle anderen ihn überlappenden Brushes an den Überlappungsstellen abgeschnitten und wenn notwendig geteilt. Aus diesem Grund sollte man diese Funktion nur mit äußerster Vorsicht und Überlegung benutzen. Und wirklich nur dann, wenn man weißt, was als Ergebnis herauskommt.

Zuerst aber müssen wir die Selektierung aller 6 Brusehes aufheben in dem wir auf <kbd>Esc</kbd> drücken.

Jetzt bewegen wir uns in der 3D-Ansicht in das Innere unserer Box, um die Wände passend zu schneiden. 

Markiere jetzt den oberen und unteren Brush (Decke und Boden). Benutze <kbd>Shift</kbd> (Umschalttaste) und die <kbd>linke Maustaste</kbd>.

![image]({static}brushwork-first-room/firstbrush_substract.jpg)

Klicke dann auf ![image]({static}brushwork-first-room/button_csg_substract.jpg) (CSG-Substract) oder geh über's Menu auf `Selection > CSG > CSG Substract`.

![image]({static}brushwork-first-room/csg_substract.jpg)

Alle 4 Wände werden oben und unten abgeschnitten. In der Console sollte dann erscheinen:

```
Substracting...

done. (created 4 fragments out of 4 brushes)
```

Jetzt drücke noch mal <kbd>Esc</kbd>, um die Markierung aufzuheben. 

Markiere jetzt 2 gegenüberliegende Wände:

![image]({static}brushwork-first-room/firstbrush_substract2.jpg)

und klicke noch mal auf ![image]({static}brushwork-first-room/button_csg_substract.jpg) (CSG-Substract).

Die anderen 2 Wände werden an den Seiten geschnitten. In der Console sollte dann erscheinen:

```
Subtracting...

done. (created 2 fragments out of 2 brushes)
```

Jetzt drücke noch mal <kbd>Esc</kbd>.

Unsere Box ist perfekt. :D

Jetzt suchen wir uns ein paar passende Texturen, um unseren ersten Raum ein wenig zu verschönern. Geh ins Menu auf `Textures > kejim`. 

Nachdem die Texturen geladen wurden, markiere die obere Seite des Boden-Brushes, indem du die Tasten <kbd>Shift</kbd> + <kbd>Strg</kbd> + <kbd>Alt</kbd> festhältst und mit der <kbd>linken Maustaste</kbd> drauf klickst (im 3D-Fenster). Es ist wichtig, dass du nur die eine Seite und nicht den ganzen Brush markierst!

Suche nun die Textur "floor02" und klicke drauf. Die Textur wird unserem Boden zugeordnet.

![image]({static}brushwork-first-room/firstroom_floor.jpg)

Drücke <kbd>Esc</kbd>, um die Markierung aufzuheben.

Markiere auf die gleiche Weise (mit <kbd>Shift</kbd> + <kbd>Strg</kbd> + <kbd>Alt</kbd>) die untere Seite des Decken-Brushes. 

Suche eine Textur mit dem Namen "bigwall02" und klicke darauf. Drücke dann <kbd>Esc</kbd>.

![image]({static}brushwork-first-room/firstroom_ceiling.jpg)

Unsere Decke hat jetzt auch eine Textur.

Als nächstes markiere mit der gleichen Methode die inneren Seiten aller 4 Wände. Suche dann die Textur "kej_wall" und klicke sie an.

![image]({static}brushwork-first-room/firstroom_walls.jpg)

Falls die Texturen nicht ganz auf die Wände passen, drücke <kbd>S</kbd> für den "Surface-Inspector" und passe die Wand-Texturen an.

![image]({static}brushwork-first-room/surface_insp.jpg)

Nachdem die Texturen angepasst sind, klicke im Surface-Inspector auf "Apply" und dann auf "Done".

Drücke dann <kbd>Esc</kbd>.

Nun ist unser Raum komplett texturiert.

![image]({static}brushwork-first-room/firstroom_textured.jpg)


Als letztes setzen wir noch einen Spieler-Starpunkt in diesen Raum, damit wir unsere Map kompilieren und ausprobieren können.

Stell das 2D-Fenster auf die TOP-Ansicht (`View > Layout > XY (Top)`).

Klicke <kbd>rechte Mauste</kbd> ( irgendwo im Inneren der Box) und wähle `info > info_player_start`.

![image]({static}brushwork-first-room/info_player_start.jpg)

Schalte jetzt das 2D-Fenster auf die Seitenansicht und bewege das Entity so, dass es knapp über dem Boden steht.

![image]({static}brushwork-first-room/info_player_start2.jpg)

**Gratuliere!, du hast deinen ersten Raum erstellt !**

Da die Map jetzt fertig ist, sollten wir sie speichern. Geh auf Menu `File > Save as...` und gib "firstroom" als Namen ein.

Jetzt nur noch die Map schnell kompilieren. Im Menü: `BSP > FastVis (nolight)` und wir können sie im Spiel ausprobieren:

1.  Starte Jedi Knight 2 im SP oder MP Modus
2.  Öffne die Console und tippe ein: `map firstroom`

![image]({static}brushwork-first-room/firstroom_shot.jpg)

Und nun befindest du dich in deinem ersten Raum...

[Download der Tutorialmap]({static}brushwork-first-room/firstroom.zip) (.map-Datei enthalten)

<div class="alert alert-info"><strong>TIP</strong>: Benutze immer die "Caulk" Textur für Brush-Seiten, die der Spieler sowieso nicht sehen kann. Das spart Kompilier-Zeit, hält die Dateigröße kleiner und steigert die Geschwindigkeit deiner Map im Spiel.</div>