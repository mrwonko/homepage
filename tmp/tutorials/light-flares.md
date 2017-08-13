title: Light - Flares
author: Destroyer (Stephan K.)
date: 2004-01-01
modified: 2015-04-14
category: mapping
type: tutorials/darth-arth
tags: Entities, auto-generated
slug: light-flares

**>>
Mapping Academy - Tutorials <<**

 

(c)
2004 [www.darth-arth.de](http://www.darth-arth.de)

----

Light - Flare Tutorial

Author: Destroyer (Stephan K.)

**[u]VORAUSSETZUNG[/u][u]EN[/u]:**

>>
Installation GTK - Radiant ( [Tutorial](../../radiant/gtk_radiant.htm)
)<<

>>
Mein erster Raum ( [Tutorial](../../mapping/firstroom/firstroom.htm)
)<<

 

----

In dieser Lehreinheit (Tutorial) lernen wir Einen
Light - Flare zu machen.

**[u]ACHTUNG!
: Dieses Tutorial ist für JK - JA ausgelegt.[/u]**

----

Du kennst sicher die Map Rift, aus dem SP, aber auch im MP?! Da sind überall 
  so schöne Kristalle anstelle von Lampen an der Wand.

  Wie Du diese Lampen erstellst, und dem ganzen durch Flares einen "Pepp" 
  gibts, erkläre ich Dir in diesem Tutorial.

Legen wir los:

  Zuerst brauchst du natürlich einen kleinen Raum. Ich habe einen Testraum 
  erstellt:

![image]({filename}flares/1.jpg)

Um nun eine Kristall-Lampe wie in Rift Sanctuary zu bekommen musst du 2x Rechtklick 
  im 2D Fenster machen und folgendes wählen:

**misc -> misc_model -> (Im neuen Fenster) map_objects -> rift 
  -> crystal_wall_lamp.md3**

Dann kannst du das Model ausrichten mit "N" und den "key: angle; 
  value: xx".

  Ich habe die Lampe so platziert:

![image]({filename}flares/2.jpg)

So, jetzt sollte man natürlich noch das Model mit einem Clip-Brush einpacken, 
  damit man im Spiel nicht hindruchsprigen kann. - Ich überspringe diesen 
  Teil aber - Was jetzt noch fehlt, ist das Licht, welches die Lampe abstrahlt. 

 
  Dazu erstellt ihr ein Lightentity: Rechtsklick ->

 light.

  Bei

 intensity

 stellst du

 10

 ein (Je nach notwendigkeit). 

 Das Licht plazierst du so, 
  wie du es für am Besten hältst. 

 Ich setzte es mittig! - Jetzt aber 
  kommt der interessante Teil: Die Flares. 

Du selectierst das Light-Entity und drückst "

N". Dann öffnet 
  sich ein neues Fenster "Entities". 

 Unten im Feld **"Key"** 
  gibst du **"_flareshader"** ein. 

 Bei **"Value"** 
  den Pfad zur einen FlareTextur. 

 In unserem Falle liegt **"textures/flares/flare_crystal"** 
  nahe:

![image]({filename}flares/3.jpg)

Jetzt nur noch ein** info_player_start** **einfügen** 
  und **kompilieren** und man erhält folgendes Ergebnis:

![image]({filename}flares/4.jpg)

Ich hoffe, dass euch das Tutorial weiterhilft!

  MfG Destroyer :D

----

Alle
  Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet: 

©
  2000 - 2004 (Artur L.) [www.darth-arth.de](http://www.darth-arth.de)

Nur
  zur privaten Nutzung. Kopieren nicht gestattet. Darth-Arth.de ist ausdrücklich
  nicht für den Inhalt externer Seiten verantwortlich. Es gelten die
  angegebenen Nutzungsbedingungen.

