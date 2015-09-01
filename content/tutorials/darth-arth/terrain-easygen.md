title: Terrain Erstellung mit EasyGen
date: 2003-01-01
type: tutorials/darth-arth
author: Darth Arth (Artur L.)
category: advanced
tags: Terrain
modified: 2015-04-12
slug: terrain-easygen

# Voraussetzungen

*   [Installation GTK - Radiant]({filename}installation-1.4.md)
*   [EasyGen]({filename}terrain-easygen/EasyGen_v142.zip)

# Tutorial

In dieser Lehreinheit (Tutorial) erstellen wir einen Terrain für JKII mit Hilfe von EasyGen.

EasyGen ist ein Programm zum Erstellen von Terrains für auf Q3-Engine basierte Spiele. EasyGen ist sehr einfach zu bedienen, wenn man weiß worauf es ankommt. Mit EasyGen kann man sehr schöne Landschaften erstellen und diese dann für eigene Maps benutzen. Die hier erstellten Terrains sind ohne Blending, das heißt, es gibt nur eine Textur und nicht mehrere mit weichem Übergang.

## Installation

1.  Die ZIP-Datei in einen Ordner entpacken

2.  `EasyGen.exe` starten

3.  Beim ersten Start des Programms wird man nach ein paar Einstellungen gefragt:

![image]({filename}terrain-easygen/prefs.gif)

Bei den Einstellungen ist die Angabe des `Work mod`-Pfades wichtig. Hier muss der Pfad zu deinem Jedi-Knight2 `base`-Ordner stehen. Die `Bitmaps` Ordner sind zweitrangig, diese müssen nur existent sein. `Player size` definiert die Größe des Spielers. Die Angaben stimmen mit den von JKII überein. Der Rest ist nicht besonders wichtig. 

Wenn du möchtest, kannst du noch, unter `Ignore brushes with shaders`, die Q3-`common`-Shaders gegen die `system`-Shaders aus JKII austauschen, dies ist aber nicht zwingend notwendig..

## Erklärungen zu EasyGen

Nach dem du EasyGen installiert und konfiguriert hast, starte das Programm. 

Zuerst ein paar Erklärungen zu den Grid Einstellungen:

<dl>
    <dt>Divisions</dt><dd>Anzahl der Zellen in welche das Terrain aufgeteilt wird</dd>
    <dt>Widths</dt><dd>Breite und Länge des Terrains in Map-Einheiten. Entspricht genau den Einheiten aus dem Radiant-Editor</dd>
    <dt>Div.Widr.</dt><dd>Breite und Länge einer einzelnen Zelle im Terrain. (je kleiner die Zellen, desto feiner das Terrain. Geht jedoch auch kosten der Performance, da viel mehr Brushes erstellt werden müssen. Man sollte keine Zellen definieren, die kleiner sind als 64-Einheiten)</dd>
</dl>

In dem 3D-Fenster bewegt man sich wie folgt:

*   <kbd>linke Maustaste</kbd> = 3D Rundumsicht
*   <kbd>rechte Maustaste</kbd> = vorwärts, rückwärts, nach links, nach rechts
*   <kbd>beide Maustasten</kbd> = nach oben oder nach unten bewegen

![image]({filename}terrain-easygen/Image33.gif)

Bevor wir unser Terrain formen, müssen wir noch ein Paar Einstellungen vornehmen. In diesem Tutorial arbeiten wir ja nicht mit Alpha-Map Terrains, wir müssen aber trotzdem ein Paar Kleinigkeiten festlegen, sonst kann die Export-Funktion nicht benutzt werden.

## EasyGen konfigurieren

Klicke jetzt auf `Alphamap`.

![image]({filename}terrain-easygen/Image32.gif) ![image]({filename}terrain-easygen/Image3.gif)

Dann in dem Pallete-Raster auf das kleine Quadrat oben links und wähle ein Farbe, z.B. Dunkel-Blau, Klicke dann auf OK.

![image]({filename}terrain-easygen/Image31.gif)

Als nächstes müssen wir einen Texturen-Ordner auswählen. Geh ins Menu auf `Textures > Add folder`

![image]({filename}terrain-easygen/Image30.gif)

Jetzt wählen wir einen Texturen-Ordner. Dieser ist für uns unwichtig, da wir ja diese Funktion, sowieso nicht nutzten wollen. 

Das Programm braucht jedoch die Einstellungen, um die Export-Funktion durchführen zu können (Q3-bedingt).

Wähle am besten einen kleinen Texturen-Ordner, wie z.B. `common`, da das Laden der Texturen eine Weile dauern kann.

![image]({filename}terrain-easygen/Image6.gif)

Nach dem die Texturen geladen wurden, klicke unten links (in dem Texturen-Fenster), eine der Texturen an. 

Z.B. `common/mp_blue`.

![image]({filename}terrain-easygen/Image29.gif)

## Terrain-Erstellung

Nachdem wir unsere minimalen Alphamap-Einstellungen vorgenommen wurden, können wir uns der Formung unseres Terrains widmen.

Klicke jetzt auf `Modifier` und wähle `Cone`. In der Mitte des Terrains erscheint der Modifier (Modifikator, eine rote Draht-Box). Man erkennt, wie sich an dieser Stelle das Terrain verformt hat. 

Den Modifikator kann man bewegen, in dem man die Taste <kbd>Strg</kbd> festhält und die <kbd>linke Maustaste</kbd> benutzt. 

![image]({filename}terrain-easygen/Image28.gif)

Mit der <kbd>Leertaste</kbd> kann man dann an der Stelle, wo sich der Modifikator gerade befindet, die Änderung des Terrains zuordnen. Wenn du mehrmals auf der gleichen Stelle die Leertaste drückst, wächst der Hügel entsprechend höher.

![image]({filename}terrain-easygen/Image13.gif)

Wenn du die Taste <kbd>Shift</kbd> (Umschalttaste) festhältst und dann die <kbd>rechte Maustaste</kbd> benutzt, kannst du die Breite des Modifikators ändern:

![image]({filename}terrain-easygen/Image24.gif) ![image]({filename}terrain-easygen/Image25.gif)

Mit der Taste <kbd>Strg</kbd> und der <kbd>rechten Maustaste</kbd> kannst du die Höhe des Modifikators ändern.

![image]({filename}terrain-easygen/Image26.gif) ![image]({filename}terrain-easygen/Image27.gif)

Probiere die einzelnen Modifikatoren durch, um deren Wirkung zu testen. Einige, wie z.B. `Smooth`, dienen dazu, das Terrain wieder abzuflachen. Versuche einfach, ein wenig mit allen zu arbeiten, um ein Gefühl für die Wirkung zu bekommen.

Nach dem du das Terrain fertig geformt hast, sollten wir es speichern.

![image]({filename}terrain-easygen/Image2.gif)

Geh ins Menü und wähle `File > save`.

![image]({filename}terrain-easygen/Image23.gif)

Gebe dann einen Dateinamen ein, z.B. `terrain1` und klicke auf `Speichern`. Dieser Schritt ist sehr wichtig, falls du später an dem Terrain noch Änderungen vornehmen möchtest. 

![image]({filename}terrain-easygen/Image15.gif)

## Exportieren

Jetzt können wir das Terrain exportieren. Gehe ins Menü und wähle `File > Export > Terrain entity (.map)`

![image]({filename}terrain-easygen/Image22.gif)

Dann erscheint eine Dialogbox, in der man verschiedene Export-Einstellungen vornehmen kann.

In dem Bereich `Save what` (was speichern), wähle nur `Save the map`. 

Bei `General/Wolrdspawn` wählen wir noch zusätzlich `Insert into a skybox` und `Add an info_player_start`. Damit wird unser Terrain gleich in eine Skybox verpackt und auch den Player-Startpunkt gesetzt bekommen. 

![image]({filename}terrain-easygen/Image17.gif)

Unter `Shader` stellen wir jetzt die Texturen ein, die unser Terrain aufgelegt bekommt. Da wir keine Alphamap-Terrains nutzen, müssen wir hier andere Texturen eintragen. 

Unter `top` trage bitte die Textur ein, die als Oberfläche des Terrains dient, z.B. `yavin/grass`. Unter `botton, sides` (die unsichtbaren Wände), trage bitte `system/caulk` ein. 

Die Einstellung `common/caulk` kommt von Q3, denn dort sind die system-shader alle im `common`-Ordner gespeichert. Bei JKII liegen diese jedoch im `textures/system`. Deswegen müssen wir `common/caulk` gegen `system/caulk` tauschen.

Wenn du mal zukünftig ein neu erstelltes Terrain in eine Map einfügen möchtest, kannst du die 2 Optionen bei `General/Worldspawn` auch weg lassen. Damit werden die Skybox und `info_player_start` nicht unnötig erstellt.

![image]({filename}terrain-easygen/Image20.gif)

Nach dem alle Export-Einstellungen vorgenommen wurden, speichern wir unser Terrain als Map. Klicke in dem Export-Optionen Fenster auf `Continue >>`. Gib jetzt als Dateinamen `terrain1` ein und klicke auf `Speichern`.

![image]({filename}terrain-easygen/Image19.gif)

Wenn die Map gespeichert wurde, können wir EasyGen beenden.

## Feintuning im GTK Radiant

Jetzt werden wir unser Terrain im Editor laden. Da wir das Terrain samt Skybox und "info_player_start" exportiert haben, können wir es wie eine normale Map öffnen. Gehe ins menu und wähle `File > Open` und lade unsere `terrain1.map`.

![image]({filename}terrain-easygen/gtk/Image25.gif)

Ups, was ist das denn ? unsere Skybox ist rot !?. Hmm..., na ja, das EasyGen hat zwar für unser Terrain den `system/caulk` shader benutzt, so wie wir es eingegeben haben. Für die Skybox hat EasyGen jedoch den Q3-Shader benutzt. Das ist aber nicht weiter schlimm, wir tauschen einfach den nicht existierenden Shader gegen den richtigen aus.

![image]({filename}terrain-easygen/gtk/Image28.gif)

Gehe ins Menü und wähle `Textures > Find/Replace` (Suchen/Ersetzen).

![image]({filename}terrain-easygen/gtk/Image24.gif)

Klicke jetzt mit der Maus in das obere Eingabefeld `Find`, 

![image]({filename}terrain-easygen/gtk/Image5.gif)

dann im Texturen-Fenster auf den roten Shader `caulk` ![image]({filename}terrain-easygen/gtk/Image26.gif).

`textures/common/caulk` erscheint unter `Find` (Suche)

![image]({filename}terrain-easygen/gtk/Image6.gif)

Jetzt klicke mit der Maus in das untere Eingabefeld,

![image]({filename}terrain-easygen/gtk/Image7.gif)

und dann in dem Texturenfenster auf den lila Shader `caulk` ![image]({filename}terrain-easygen/gtk/Image27.gif).

In unterem Eingabefeld erscheint `textures/system/caulk`.

![image]({filename}terrain-easygen/gtk/Image8.gif)

Um den Q3-Shader durch den richtigen zu ersetzen, klicke jetzt auf `Apply`.

![image]({filename}terrain-easygen/gtk/Image10.gif)

Man könnte natürlich die Namen der Texturen auch per Hand eintragen, da diese jedoch oft sehr lang sind, verschreibt man sich gerne. Daher ist diese Methode sicherer und bequemer. 

Klicke jetzt auf `Close`, um das Fenster zu schliessen.

![image]({filename}terrain-easygen/gtk/Image23.gif)

Jetzt ist unsere Skybox mit der richtigen Caulk-Textur belegt.

![image]({filename}terrain-easygen/gtk/Image22.gif)

So kann es aber nicht bleiben, da wir dann im Spiel hässliche Grafikfehler hätten.

Markiere jetzt die inneren Seiten der Skybox-Brushes, in dem du sie mit <kbd>Strg</kbd> + <kbd>Alt</kbd> + <kbd>Shift</kbd> und der linken Maustaste anklickst.

![image]({filename}terrain-easygen/gtk/Image21.gif)

Geh jetzt ins Menü und lade die Skies-Texturen  ( `Textures > Skies` )

Suche dann einen Sky-Shader mit dem Namen `Yavin` ![image]({filename}terrain-easygen/gtk/Image20.gif) und klicke ihn an.

![image]({filename}terrain-easygen/gtk/Image19.gif)

So, jetzt ist unsere Skybox perfekt :D

Drücke jetzt die <kbd>Esc</kbd>-Taste und markiere unser Terrain-Entity. Hier müssen wir nämlich noch ein paar Änderungen vornehmen.

![image]({filename}terrain-easygen/gtk/Image18.gif)

Nachdem unser Terrain markiert ist, drücke die <kbd>N</kbd>- Taste um die Entity-Eigenschaften anzuzeigen.

Lösche jetzt alles raus (Eigenschaft mit der Maus anklicken und dann auf `Del Key/Pair` klicken), außer `classname func_group`

![image]({filename}terrain-easygen/gtk/Image16.gif)![image]({filename}terrain-easygen/gtk/Image17.gif)

Drücke dann die <kbd>Esc</kbd>-Taste.

Danach speichern wir unsere Map und kompilieren sie mit `FastVis (nolight)` (im GTK Radiant ab Version 1.4 erst `-meta` dann `-vis -fast`)

Im Spiel sieht das ganze dann so aus:

![image]({filename}terrain-easygen/shot0295.jpg)

Gratuliere, du stehst auf deinem eigenem Terrain :D

## Download

[Download der Tutorial Map]({filename}examples/easygen.zip) (`.map` - Datei enthalten)

## Tip

Wenn du an dem Terrain was verändern möchtest, mache es bitte im EasyGen und exportiere es noch mal. Ändere das Terrain-Entity nicht im GTKradiant, vor allem schneide nichts raus mit der `SCG-Subtract` Funktion und verschiebe keine Vertexe. 

Wenn du es tust, kriegst du im Spiel merkwürdige Grafikfehler und komische Schatten. Wenn du die Oberfläche zum Teil mit einer anderen Textur belegen möchtest, benutzte immer die <kbd>Strg + Alt + Shift</kbd> Tasten-Kombination, um die einzelnen Faces zu markieren. Passe immer auf, dass du nicht aus Versehen die inneren Caulk-Seiten des Terrains mit einer normalen Textur belegst!