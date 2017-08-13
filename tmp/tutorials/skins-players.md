title: Skins selber machen
author: Charmin (Oliver J.) Deluxe
date: 2004-01-01
modified: 2015-04-14
category: models
type: tutorials/darth-arth
tags: Skins, auto-generated
slug: skins-players

**>>
Mapping Academy - Tutorials <<**

 

(c)
2003 [www.darth-arth.net](http://www.darth-arth.net)

----

 

**Skinning-Tutorial für Jedi Knight
2 by Charmin Deluxe**

 

----

[color=black]

[/color]

**1. ****Material**[color=black]

- **[Paintshop Pro](http://www.jasc.com/download_4.asp?)**
[/color] oder ein anderes
Bildbearbeitungsprogramm[color=black]

- **[WinZIP](http://www.winzip.com/ddchomea.htm)**
[/color] und[color=black] **[WinRAR](http://www.winrar.de/)**

- [/color] ein Textbearbeitungsprogramm

**2. Vorbereitung**

- zuerst öffnest du im deinem **Gamedata/base** Ordner die assets0.pk3 mit **WinRAR**.

[color=black]

[/color]
- dann entpackst (**[color=red]nicht rauslöschen![/color]**) du den ganzen Ordner **models/players**
zu einem Ort deiner Wahl.

[color=black]

![image]({filename}./skinning_tut-Dateien/image001.jpg)

[/color]

**3. Das Skin-Verändern**

- Ihr legt einen Ordner an mit dem Namen **models**. In diesen macht ihr
einen neuen Ordner mit Namen **players**. In diesen Ordner kommt ein Ordner
der den Namen eures Skins hat. Bei uns z.b. **Mein_Skin** (**[color=red]Beachte das du
Leerstellen mit einen _ abtrennst[/color]**)

- Nun geht ihr in den von euch extrahierten Ordner und sucht euch dort ein
Model aus. Wir nehmen mal **Gran**. Nun kopiert alle Dateien in Gran in
euren Ordner (bei uns **Mein_Skin**). So da sind jetzt ne Menge Dateien. Um
die Übersicht besser behalten zu können löschen wir erst einmal ein paar die
wir vorerst nicht brauchen. Wir benötigen erstmal nur folgende Dateien (die
benötigten Dateien sind von Model zu Model anders, aber doch leicht zu erkennen).:[color=black]

[/color]
**accessories.jpg

animsounds.cfg

basic_hand.jpg

gran_legs.jpg

head.jpg

icon_default.jpg

l_arm.jpg

model.glm

model_default.skin

r_arm.jpg

sounds.cfg

torso.jpg**[color=black]

![image]({filename}./skinning_tut-Dateien/image002.jpg)

[/color]
(falls du die Dateinamenendungen nicht siehst, geh auf **Systemsteuerung ->
Ordneroptionen -> Ansicht ->** das Häckchen bei "**Dateinamenerweiterungen
bei bekannten Dateitypen ausblenden**" entfernen -> **OK**)

[color=black]

![image]({filename}./skinning_tut-Dateien/image003.jpg)

-[/color] Nun kannst du die Bilddateien beliebig verändern (**[color=red]Achte allerdings darauf
das du die Größe des Bildes nicht verstellst[/color]**).[color=black]

![image]({filename}./skinning_tut-Dateien/image004.jpg)

[/color]
- Nachdem du nun alles verändert hast. Öffne die **model_default.skin**
Datei mit deinem Textbearbeitungsprogramm. jetzt siehst du da verschiedene
Pfade. Die musst du nur noch anpassen. Wenn da z.B. steht: **hips,models/players/gran/gran_legs.tga**
musst du das gran durch den Ordnernamen ersetzen wodrin sich dein Skin
befindet. So das es dann so heißen müsste: **hips,models/players/Mein_Skin/gran_legs.tga**.
Allerdings nicht die Pfade von den ändern die mit deinem Skin nix direkt zu tun
haben, wie z.B. das: **hips_cap_l_leg_off,models/players/stormtrooper/caps.tga**

[color=black]
![image]({filename}./skinning_tut-Dateien/image005.jpg)

[/color]
**4. Den Skin Team-kompatibel machen**[color=black]

[/color]
- Da dieser Skin jetzt aber noch keine Teamfarben hat, macht ihr nun Folgendes:

- kopiert euren **model_default.skin** 2 mal und benennt die Kopien jeweils
in **model_blue.skin** und **model_red.skin** um. Öffnet diese Dateien
mit dem Texteditor und hängt an jede Bilddatei beim Namen für **model_blue.skin**
ein **..._blue** und bei **model_red.skin ..._red**

[color=black]

![image]({filename}./skinning_tut-Dateien/image006.jpg)

[/color]

- kopiert euer **icon_default.jpg** 2 mal und bennent die Kopien jeweils in **icon_blue.jpg**
und **icon_red.jpg** um.

- kopiert eure restlichen Bilddateien ebenfalls 2 mal und benennt eine Hälfte
in **..._blue.jpg** und die anderen in **..._red.jpg** um. Bearbeitet
diese noch mal, wenn ihr wollt.

- es gibt Ausnahmen die ihr nicht in **..._blue** und **..._red**
umbennen müsst. Schaut einfach vorher bei den Modellen, deren Skins ihr
verändern wollt, welche Bilddateien vorher **..._blue** und **..._red**
waren.

- Nun ist euer Skin auch Team-kompatibel.

**5. Den Skin ins Spiel bekommen**

- Dazu erstelle mit **WinZip** eine **ZIP**-Datei. Wir nennen sie bei uns
mal **MeinErsterSkin.ZIP**. Jetzt zippst du unseren models-Ordner mit dem
veränderten Skin drin in diese Datei.

[color=black]

![image]({filename}./skinning_tut-Dateien/image007.jpg)

[/color]

Danach benenne sie von **MeinErsterSkin.ZIP** in **MeinErsterSkin.pk3**
um (**[color=red]normalerweise
kommt dann eine Fehlermeldung. Einfach mit JA bestätigen[/color]**).[color=black]

![image]({filename}./skinning_tut-Dateien/image008.jpg)

[/color]
Diese Datei musst du nur noch in dein **Gamedata/Base** Ordner kopieren.

- Dann starte das Spiel im Multiplayer. Wenn du alles richtig gemacht hast,
kannst du dort deinen Skin auswählen.

**Gratulation! Du hast dein ersten Skin gemacht!**

[color=black]
![image]({filename}./skinning_tut-Dateien/image009.jpg)

[/color]

----

Bei weiteren Fragen oder Verbesserungstipps für dieses Skinning-Tutorial mailt
bitte an **[oliver@mijun.de](mailto:oliver@mijun.de)**
der labert ihn über **ICQ** (**168661509**) an.[color=black][/color]

