title: Eigene Schwertgriffe erstellen
author: Charmin (Oliver J.) Deluxe
date: 2004-01-01
modified: 2015-04-14
category: models
type: tutorials/darth-arth
tags: Modelling, Milkshape 3D, auto-generated
slug: model-saber-milkshape

**>>
Mapping Academy - Tutorials <<**

 

(c)
2003 [www.darth-arth.net](http://www.darth-arth.net)

----

**Saberhilt
Modelling-Tutorial für Jedi Knight 2 by Charmin Deluxe**

----

[color=black]

[/color]
**Voraussetzungen für
die Nutzung dieses Tutorials:**

- Ihr habt das Tutorial auf **[Gargamel.de](http://www.gargamel.de)** schon gemacht!

- Ihr habt **Dateinamenerweiterung an** (falls du die Dateinamenendungen
nicht siehst, geh auf Systemsteuerung -> Ordneroptionen -> Ansicht ->
das Häckchen bei **"Dateinamenerweiterungen bei bekannten Dateitypen
ausblenden" entfernen -> OK** (s. **[Skinning-Tutorial](skinning_tut.htm)**)).[color=black]

[/color]
**1. Material**[color=black]

- **[Milkshape](http://www.swissquake.ch/chumbalum-soft/ms3d/download.html)**

- **[JK2 Editing-Tools 1](http://plasmaskins.jediknightii.net/files/resources/programs.html)**

- **[Lith Unwrap](downloads/LithUnwrap.zip)**

- **[Paintshop Pro](http://www.jasc.com/download_4.asp?)**
[/color] oder ein anderes
Bildbearbeitungsprogramm

- **[WinZIP](http://www.winzip.com/ddchomea.htm)** und **[WinRAR](http://www.winrar.de/)**

[color=black]

[/color]
**2. Vorbereitung**

- Installier die **JK2 Editing-Tools 1** in dein Gamedata Verzeichnis.

- zuerst öffnest du im deinem **Gamedata/Base** Ordner die assets0.pk3 mit **WinRAR**.

- dann entpackst (**[color=red]nicht rauslöschen![/color]**) du den Ordner **models/weapons2/saber**
zu einem Ort deiner Wahl.[color=black]

![image]({filename}./saberhilt_modeling_tut-Dateien/image001.jpg)

[/color]
**3. Das Saber-Erstellen**

- Starte **Milkshape**

- Geh auf  **File -> Import -> Ghoul2 Model Glm**[color=black]

![image]({filename}./saberhilt_modeling_tut-Dateien/image002.jpg)

[/color]
- Dann öffnet sich ein Fenster und er fragt, was ihr alles importieren wollt.
Macht einfach überall ein Häckchen.

[color=black]

![image]({filename}./saberhilt_modeling_tut-Dateien/image003.jpg)

-[/color] Jetzt habt ihr da den Standard-Saberhilt. Den könnt ihr löschen wenn ihr
wollt, doch behaltet ihn lieber so lange drinne bis die Größe eures Saberhilts
mit dem Saberhilt übereinstimmt (kann auch größer sein, nur is es dann im Game
natürlich auch dementsprechend größer).

- Jetzt modellt einfach drauf los. Ich mach hier einfach mal eine Röhr mit 2
Scheiben an den Enden.[color=black]

![image]({filename}./saberhilt_modeling_tut-Dateien/image004.jpg)

-[/color] Nachdem ich die alten beiden Saberteile gelöscht habe (**w_saber** und **w_handle**)
sind nur noch mein Model, ***flash** und ***parent** vorhanden. Falls
euer Model aus mehreren Einzelteilen besteht (wie bei mir die 3 Cylinder)
regroupt die einfach und benennt den Regroup dann in **w_saber** um.
Außerdem benennt ihr ***flash** und ***parent** noch in **tag_flash**
und **tag_parent** um. Dann müsste es so aussehen:

[color=black]

![image]({filename}./saberhilt_modeling_tut-Dateien/image006.jpg)

[/color]
- Den **tag_flash** müsst ihr jetzt noch mit **Rotate** auf der X-Achse
um 270° drehen und so verschieben, das es ungefähr so aussieht:

[color=black]

![image]({filename}./saberhilt_modeling_tut-Dateien/image007.jpg)

- [/color] Zum Schluss weist ihr eurem **w_saber** die Textur **saber.jpg**, die
sich in eurem **models/weapons2/saber** Ordner befindet, zu.

- OK, euer Model is dann soweit fertig. Speichert es irgendwo unter dem Namen **saber_w.ms3d**
ab.

**4. Das Texturieren**

- Wie man Modelle texturiert ist auf **[Gargamel.de](http://www.gargamel.de)** schon
beschrieben. Doch bei komplexeren Saberhilts brauch man **Lith Unwrap**.
Leider gibt es jetzt nur noch **Ultimate Unwrap** und die Demo davon ist
nutzlos. Ich konnte aber glücklicherweise noch irgendwo ein altes **Lith
Unwrap** auftreiben, das auch das ms3d-Format unterstützt.

- Startet **Lith Unwrap**

- Geh auf **File -> Model -> Open** und öffnet eure gespeicherte **saber_w.ms3d**

- Nun müsste es so oder so ähnlich aussehen:

[color=black]

![image]({filename}./saberhilt_modeling_tut-Dateien/image008.jpg)

-[/color] Jetzt drückt **Strg + A** und geht dann auf **Tools -> UVMapping**.
Hier findet ihr verschiedene Arten euer Model auf eine Bilddatei auszubreiten.
Ich bevorzuge für Saberhilts: **Tools -> UVMapping -> Planar (Z-Achse)**.[color=black]

![image]({filename}./saberhilt_modeling_tut-Dateien/image009.jpg)

-[/color] Ein Tipp: Probiert auch einmal **Tools -> Optimize Model**. Es (wer
wäre draufgekommen) optimiert euer Model, indem es z.b. unnütze Vertexe
entfernt.

[color=black]

![image]({filename}./saberhilt_modeling_tut-Dateien/image010.jpg)

[/color]
- Wenn ihr euer Model UV-gemappt hat, könnt ihr es unter **File -> UV Map
-> Save** als Tga unter dem Namen **saber.tga** in euerm **models/weapons2/saber**
Ordner abspeichern (**[color=red]Achtet darauf, dass die Auflösung immer aus diesen Zahlen besteht:
64, 128, 256, 512, 1024. Also eure Auflösung darf 256x256 oda 64x512 usw. sein,
aber nich 83x145 oder so![/color]**).[color=black]

![image]({filename}./saberhilt_modeling_tut-Dateien/image012.jpg)

[/color]
- Danach müsst ihr euer Model auch nochmal abspeichern. Geht dafür auf **File
-> Model -> Save** und speichert es als **saber_w.ms3d** ab.

- Danach könnt ihr **Lith Unwrap**  schließen.

- Jetzt
öffnet die **saber.tga** z.b. mit **Paintshop Pro** und bearbeitet das
Muster beliebig.

![image]({filename}./saberhilt_modeling_tut-Dateien/image013.jpg)

- Speichert es als **saber.jpg** in eurem **models/weapons2/saber**
Ordner ab.

- Nun hat euer Model eine Textur

**5. Den Saberhilt ins Spiel bekommen**

- Startet **Milkshape**

- Öffnet eure **saber_w.ms3d**

- Wenn ihr jetzt im 3D-Fenster rechtsklickt und dann auf **Textured** geht,
seht ihr euer Model mit Textur.

![image]({filename}./saberhilt_modeling_tut-Dateien/image014.jpg)

- Nun geht ihr auf **Tools -> Quake III Arena -> Generate Control File
...**. Speichert diese datei unter dem Namen **saber_w.qc** in eurem **models/weapons2/saber**
Ordner ab.

- Es öffnet sich ein Fenster:

![image]({filename}./saberhilt_modeling_tut-Dateien/image015.jpg)[color=black]

[/color]
- Schreibt sie so um, dass sie so aussieht:

[color=black]

![image]({filename}./saberhilt_modeling_tut-Dateien/image016.jpg)

[/color]
- Nach dem Speichern geht ihr wieder zurück in **Milkshape**. Dort geht ihr
auf **File -> Export -> Quake III Arena MD3** und speichert euer Model
als **saber_w.md3** in eurem **models/weapons/saber** Ordner ab.

[color=black]

![image]({filename}./saberhilt_modeling_tut-Dateien/image017.jpg)

- [/color] Jetzt könnt ihr **Milkshape** schließen.

- Kopiert euren **models** ordner mit eurem Saberhilt drin nach **Gamedata/base**.
Jetzt könnt ihr euer **saber_w.md3** mit **MD3View** öffnen (**MD3View**
findet ihr nach dem Installieren der **JK2 Editing-Tools 1** in eurem **Gamedata/Tools**
Ordner. Einfach starten und über **File -> Open** euer **saber_w.md3**
öffnen.)

- Dort geht ihr auf **File -> Export as GLM (Ghoul 2)** Jetzt kommen eine
Reihe von Meldungen. Einfach mit **OK** bestätigen.

[color=black]

![image]({filename}./saberhilt_modeling_tut-Dateien/image018.jpg)

[/color]
- Jetzt müsstet ihr in eurem **models/weapons2/saber** Ordner folgende
Dateien haben:

**saber.jpg

saber.tga

saber_w.glm

saber_w.md3

(saber_w.ms3d)

saber_w.qc

saber_w_1.md3**

- Löscht **saber.tga, saber_w.md3, (saber_w.ms3d), saber_w.qc** und **saber_w_1.md3**.

[color=black]
![image]({filename}./saberhilt_modeling_tut-Dateien/image019.jpg)

[/color]
- Jetzt müsst ihr euer Saberhilt nur noch in eine pk3 tun. Dazu erstelle mit **WinZip**
eine **ZIP**-Datei. Wir nennen sie bei uns mal **MeinErsterSaberhilt.ZIP**.
Jetzt zippst du unseren **models**-Ordner mit dem Saberhilt drin in diese
Datei.

[color=black]
![image]({filename}./saberhilt_modeling_tut-Dateien/image020.jpg)

[/color]
Danach benenne sie von **MeinErsterSaberhilt.ZIP** in **MeinErsterSaberhilt.pk3**
um (**[color=red]normalerweise
kommt dann eine Fehlermeldung. Einfach mit JA bestätigen[/color]**).

[color=black]
![image]({filename}./saberhilt_modeling_tut-Dateien/image021.jpg)

[/color]
Diese Datei musst du nur noch in dein **Gamedata/Base** Ordner kopieren
(Wenn sie das nicht schon ist).

- Dann starte das Spiel im Multiplayer. Wenn du alles richtig gemacht hast,
kannst du dort deinen Saberhilt anstatt des Standard-Saberhilts sehen.

**Gratulation! Du hast dein ersten Saberhilt gemacht! Ihr könnt das selbe mit
den anderen Waffen machen, nur lauten da die tags und Dateinamen geringfügig
anders!**

[color=black]

[/color]**[color=red]Zur
Information! NEIN, so kann man KEINE Player-Modelle erstellen![/color]**[color=black]

![image]({filename}./saberhilt_modeling_tut-Dateien/image022.jpg)

[/color]

----

Bei weiteren Fragen oder Verbesserungstipps für dieses Saberhilt Modelling-Tutorial
mailt bitte an **[oliver@mijun.de](mailto:oliver@mijun.de)** oder labert
ihn über **ICQ**
(**168661509**) an.

