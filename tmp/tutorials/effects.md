title: Editieren von Effekten
author: Charmin (Oliver J.) Deluxe
date: 2004-01-01
modified: 2015-04-14
category: models
type: tutorials/darth-arth
tags: Effekte, auto-generated
slug: effects

**>>
Mapping Academy - Tutorials <<**

 

(c)
2003 [www.darth-arth.net](http://www.darth-arth.net)

 

----

 

**EffectsEd-Tutorial für Jedi Knight
2 by Charmin Deluxe**

 

----

[color=black]

**1.Material**[/color]

- **[JK2 Editing-Tools 1&2](http://plasmaskins.jediknightii.net/files/resources/programs.html)**

- **[4 Bilddateien](downloads/4Bilddateien.zip)**

- **[WinRAR](http://www.winrar.de/)**

**2. Vorbereitung**

- Installier die **JK2 Editing-Tools 1&2** in dein **Gamedata**
Ordner.

- Extrahier den Inhalt von **4Bilddateien.zip** in deinen **Gamedata/Tools**
Ordner.

- Zuerst öffnest du im deinem **Gamedata/base** Ordner die assets0.pk3 mit **WinRAR**.

- Dann entpackst (**[color=red]nicht rauslöschen![/color]**) du den **gfx** und **effects** Ordner
in dein **Gamedata/base** Ordner.

[color=black]

![image]({filename}./effectsed_tut-Dateien/image001.jpg)

[/color]

**3. Das Editieren der Effekte**

- Startet **EffectsEd** (Er befindet sich nach dem Installieren im **Gamedata/Tools**
Ordner.)

- Wenn ihr ihn das erste Mal startet, müsst ihr die Pfade angeben. Stellt
einfach bei **Default game path** den Pfad zu eurem **Gamedata/base**
Ordner. Klickt dann auf **OK**

[color=black]

![image]({filename}./effectsed_tut-Dateien/image002.jpg)

[/color]

- Nun öffnet ihr über **File -> Open** z.b. **Gamedata/base/effects/env/fire.efx**.
Wenn nach dem Öffnen oben in der Leiste auf das grüne Dreieck drückt, wird der
Effekt abgespielt.

[color=black]

![image]({filename}./effectsed_tut-Dateien/image003.jpg)

[/color]

- Außerdem findet ihr rechts ein Fenster mit **Generation, Origin/Size,
Motion, Physics** und **Color**. Unten links sind die Partikel angezeigt.

- Klickt unten auf **Unnamed Particel 0** und dann auf **Color**. Jetzt
ändern wir die Farbfelder mal auf grün. Drückt nach dem Editieren auf **Apply**.
Wenn ihr jetzt wieder auf **Play Effect** drückt, müsste das Feuer grün
sein. Ihr könnt noch die Größe usw. einstellen. Probiert einfach mal rum.

[color=black]

![image]({filename}./effectsed_tut-Dateien/image004.jpg)

[/color]

- Zum Schluss speichert euren Effekt unter **Gamedata/base/effects/meineeffekte/feuer_gruen.efx**
ab.

**4. Den Effekt ins Game bekommen**

- Dazu erstellt ihr in eurem Radianten einen **fx_runner**, indem ihr
rechtsklickt und dann auf **fx -> fx_runner** klickt. Lasst den **fx_runner**
makiert und drückt **n**. Jetzt gebt ihr ihm als **Key: fxFile** und **Value:
effects/meineeffekte/feuer_gruen.efx**. Bestätigt mit Enter.

[color=black]

![image]({filename}./effectsed_tut-Dateien/image005.jpg)

[/color]

- Dann starte deine Map mit deinem Effekt. Wenn du alles richtig gemacht hast,
siehst du dort deinen Effekt.

**Gratulation! Du hast dein ersten Effekt gemacht!**

[color=black]

[/color]**[color=red]Bedenke
aber, dass du diesen Effekt in deiner pk3 mitlieferst, falls du deine Map zum
Download stellst.[/color]**[color=black]

![image]({filename}./effectsed_tut-Dateien/image006.jpg)
[/color]

----

Bei weiteren Fragen oder Verbesserungstipps für dieses EffectsEd-Tutorial mailt
bitte an **[oliver@mijun.de](mailto:oliver@mijun.de)**
der labert ihn über **ICQ** (**168661509**) an.[color=black][/color]

