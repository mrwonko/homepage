title: Was sind Shader ?, Lava - Shader
author: Darth Arth (Artur L.)
date: 2004-01-01
modified: 2015-04-14
category: texturen
type: tutorials/darth-arth
tags: Shader, auto-generated
slug: shader-intro-lava

**>>
Mapping Academy - Tutorials <<**

 

(c)
2003 [www.darth-arth.net](http://www.darth-arth.net)

----

SHADER: Was sind Shader ?

**[u]VORAUSSETZUNG[/u][u]EN[/u]:**

>>
Installation JK2 Editing Tools I ( [Tutorial](../radiant/jk2_etools1.htm)
)<<

>>
Installation JK2 Editing Tools 2 ( [Tutorial](../radiant/jk2_etools2.htm)
)<<

>>
Installation GTK - Radiant ( [Tutorial](../radiant/gtk_radiant.htm)
)<<

>>
Mein Erster Raum ( [Tutorial](../mapping/firstroom/firstroom.htm) )<<

----

In
dieser Lehreinheit (Tutorial) wird erklärt, was man unter Shader versteht, und
wie man eigene Shader erstellen kann.

----

**_

Was ist ein Shader?

_**

Die Q3-Grafikengine wurde so
entwickelt, dass die Map-Designer und Künstler, direkte Kontrolle über die
Oberflächenqualität von Texturen haben.

Shader sind Spezial-Definitionen
für Texturen. Es sind kleine Text-Skripte, die beschreiben, wie die Oberflächen
im Spiel erscheinen und funktionieren. Konventionell werden die Shader-Dateien,
die diese Skripts enthalten so benannt, wie der Texturen-Set, der die zu
modifizierenden Texturen enthält (z.B.: system, bespin, yavin, etc.). Es gibt
auch spezifische Shader-Dateien, die besondere Effekte behandeln, wie Gewässer,
Nebel, Skyboxen, Special Effekte und Model-Skins.

In Jedi Knight II sind die
Skripte im "GameDate/base/shaders"
zu finden.

Eine Shaderdatei besteht aus
einer Serie von Oberflächenattributen und Render-Befehlen, die mit Klammern
formatiert sind (" {"
und "}"). 

Hier ein Syntax- und
Formatierungsbeispiel für einen Lava-Shader (von mir leicht modifiziert, da der
original Shader einen Bug hat).

<table border="1" width="100%">
 <tr>
  <td style="background-color: #000000" width="28%">
   <font color="#FFFFFF" face="Arial" size="2">
    <b>
     Shader-Bestandteil:
    </b>
   </font>
  </td>
  <td style="background-color: #000000" width="72%">
   <font color="#FFFFFF" face="Arial" size="2">
    <b>
     Beschreibung:
    </b>
   </font>
  </td>
 </tr>
 <tr>
  <td width="28%">
   <font color="#00FF00" face="Arial" size="2">
    textures/imp_mine/lava_neu
   </font>
  </td>
  <td width="72%">
   <font color="#008080" face="Arial" size="2">
    Name des Shaders
      (es muss nicht unbedingt eine Textur mit diesem Namen existieren)
   </font>
  </td>
 </tr>
 <tr>
  <td width="28%">
   <font color="#00FF00" face="Arial" size="2">
    {
   </font>
  </td>
  <td width="72%">
   <font color="#FF0000" face="Arial" size="2">
    Shader -
      Eröffnungs-Klammer
   </font>
  </td>
 </tr>
 <tr>
  <td width="28%">
   <font size="2">
    <font color="#00FF00" face="Arial">
     qer_editorimage
      textures/
    </font>
    <font color="#00FF00" face="Arial" size="2">
     imp_mine/lava2
    </font>
   </font>
  </td>
  <td width="72%">
   <font color="#008080" face="Arial" size="2">
    Textur-Bild, das
      im Editor angezeigt wird
   </font>
   <font color="#C0C0C0" face="Arial" size="2">
    (diese
      Definition fehlt im Original, deswegen wird der Shader nicht richtig
      angezeigt)
   </font>
  </td>
 </tr>
 <tr>
  <td width="28%">
   <font color="#00FF00" face="Arial" size="2">
    surfaceparm lava
   </font>
  </td>
  <td width="72%">
   <font color="#008080" face="Arial" size="2">
    Oberflächen-Definition
   </font>
  </td>
 </tr>
 <tr>
  <td width="28%">
   <font color="#00FF00" face="Arial" size="2">
    deformvertexes
      wave 100 sin 1 1 0 0.25
   </font>
  </td>
  <td width="72%">
   <font color="#008080" face="Arial" size="2">
    Definition zum
      deformieren der Textur-Oberfläche
   </font>
  </td>
 </tr>
 <tr>
  <td width="28%">
   <font color="#00FF00" face="Arial" size="2">
    {
   </font>
  </td>
  <td width="72%">
   <font color="#FF00FF" face="Arial" size="2">
    Eröffnungs-Klammer
      für den ersten Abschnitt (Oberflächenattribut)
   </font>
  </td>
 </tr>
 <tr>
  <td width="28%">
   <font color="#00FF00" face="Arial" size="2">
    map textures/imp_mine/lava2
   </font>
  </td>
  <td width="72%">
   <font color="#008080" face="Arial" size="2">
    Textur-Name für
      den ersten Abschnitt (diese muss vorhanden sein)
   </font>
  </td>
 </tr>
 <tr>
  <td width="28%">
   <font color="#00FF00" face="Arial" size="2">
    blendFunc GL_ONE
      GL_ZERO
   </font>
  </td>
  <td width="72%">
   <font color="#008080" face="Arial" size="2">
    Definition des
      Blende-Effekts
   </font>
  </td>
 </tr>
 <tr>
  <td width="28%">
   <font color="#00FF00" face="Arial" size="2">
    tcMod scroll
      0.01 0.01
   </font>
  </td>
  <td width="72%">
   <font color="#008080" face="Arial" size="2">
    Definition des
      Scroll- (Bewegungs-) Effekts
   </font>
  </td>
 </tr>
 <tr>
  <td width="28%">
   <font color="#00FF00" face="Arial" size="2">
    tcMod turb 1 0.1
      1 0.005
   </font>
  </td>
  <td width="72%">
   <font color="#008080" face="Arial" size="2">
    Definition des Turbulenzen-Effekts
      (bringt ein wenig Unregelmäßigkeit in die Bewegung, damit die Lava
      realistischer wirkt
   </font>
  </td>
 </tr>
 <tr>
  <td width="28%">
   <font color="#00FF00" face="Arial" size="2">
    tcMod stretch
      noise 1 0.01 0 0.05
   </font>
  </td>
  <td width="72%">
   <font color="#008080" face="Arial" size="2">
    Definition des
      Stretch- (Auseinnanderzieh-) Effekts
   </font>
  </td>
 </tr>
 <tr>
  <td width="28%">
   <font color="#00FF00" face="Arial" size="2">
    }
   </font>
  </td>
  <td width="72%">
   <font color="#FF00FF" face="Arial" size="2">
    Abschluss-Klammer
      für den ersten Abschnitt
   </font>
  </td>
 </tr>
 <tr>
  <td width="28%">
   <font color="#00FF00" face="Arial" size="2">
    {
   </font>
  </td>
  <td width="72%">
   <font color="#FF00FF" face="Arial" size="2">
    Eröffnungs-Klammer
      für den zweiten Abschnitt
   </font>
  </td>
 </tr>
 <tr>
  <td width="28%">
   <font color="#00FF00" face="Arial" size="2">
    map $lightmap
   </font>
  </td>
  <td width="72%">
   <font color="#008080" face="Arial" size="2">
    Licht-Map wir
      eingeschaltet. Das bedeutet, die Oberfläche empfängt Schatten- und
      Belichtungs-Effekte.
   </font>
  </td>
 </tr>
 <tr>
  <td width="28%">
   <font color="#00FF00" face="Arial" size="2">
    blendFunc
      GL_DST_COLOR GL_SRC_COLOR
   </font>
  </td>
  <td width="72%">
   <font color="#008080" face="Arial" size="2">
    Definition des
      Blende-Effekts
   </font>
  </td>
 </tr>
 <tr>
  <td width="28%">
   <font color="#00FF00" face="Arial" size="2">
    }
   </font>
  </td>
  <td width="72%">
   <font color="#FF00FF" face="Arial" size="2">
    Abschluss-Klammer
      für den zweiten Abschnitt
   </font>
  </td>
 </tr>
 <tr>
  <td width="28%">
   <font color="#00FF00" face="Arial" size="2">
    }
   </font>
  </td>
  <td width="72%">
   <font color="#FF0000" face="Arial" size="2">
    Abschluss-Klammer
      für den Shader
   </font>
  </td>
 </tr>
</table>

 

Es
ist sehr wichtig, das bei der Erstellung der Shader-Dateien, die Eröffnungs-
und Abschluss-Klammern richtig gesetzt und nicht vergessen werden. 

Da
heißt jeder Shader braucht ein Eröffnungs- und eine Abschluss-Klammer. Das
gleiche betrifft jeden Oberflächen-Attribut (Shader-Anschnitt). 

Aus
diesem Grund ist es ratsam, die Shader so zu schreiben, dass die Attribute ein
wenig eingerückt sind, damit man einen besseren Überblick hat. Vor allem, wenn
in einer Datei, mehrere Shader-Definitionen vorhanden sind.

 

textures/imp_mine/lava_neu

{

     qer_editorimage
textures/imp_mine/lava2

   
surfaceparm lava

   
deformvertexes wave 100 sin 1 1 0 0.25

   
{

   
map textures/imp_mine/lava2

   
blendFunc GL_ONE GL_ZERO

   
tcMod scroll 0.01 0.01

   
tcMod turb 1 0.1 1 0.005

   
tcMod stretch noise 1 0.01 0 0.05

   
}

   
{

   
map $lightmap

   
blendFunc GL_DST_COLOR GL_SRC_COLOR

   
}

}

----

 

Da,
die Shader normale Text-Dateien sind, kann man sie ganz normal mit dem
"Notepad" oder mit jedem anderen Text-Editor erstellen. Diese müssen
jedoch als normaler unformatierter Text gespeichert werden. 

 

Man
kann auch den Shader-Editor zur der Erstellung nutzen, welcher sich in dem GameData/tools
- Ordner befindet. Der ist aber schwer zu bedienen und hat einige nervige Bugs.

 

Nach
dem wir unseren Shader erstellt haben, speichern wir die Datei in den base/shaders
Ordner, unter dem Namen "mylava.shader"
(Es ist wichtig, dass du in Deiner Explorer-Ansicht die Datei-Erweiterungen
eingeblendet hast!)

 

Damit,
die selbst erstellten Shader im Editor angezeigt werden, müssen diese in der
Shader-Liste eingetragen werden. 

Suche
in dem base/shaders
Ordner nach der Datei "shaderlist.txt".
Öffne sie mit dem Notepad und füge am Schluss den Namen unseres neuen Shaders mylava
ein.

 

(**WICHTIG!**:
ohne Datei-Erweiteung, nur den Namen eintragen!)

 

Speichere
dann die Shader-Liste. 

 

Jetzt
kannst du den Editor starten und den neuen Lava-Shader ( "lava_neu"
) unter Textures >
"imp_mine"
finden.

 

![image]({static}lava.jpg)

 

**[u]HINWEIS:[/u]**

Wenn
du selbsterstellte Shader, auch im MP-Modus nutzen möchtest, müssen diese
zusammen mit dem Unterordner "shaders"
in eine pk3-Datei gepackt werden. Die Pk3-Datei muss dann in den base-Ordner
kopiert werden. 

 

Vergiss
nicht die selbsterstellte Shader-Dateien und Texturen mitzuliefern, wenn du
deine Maps veröffentlichen möchtest !

 

----

![image]({static}lava_map.jpg)

 

Im
Anschluss an dieses Tutorial, findest du den neuen Shader zum Download. Folgende
Dateien sind in dem ZIP-Achiv "my_lava.zip"
enthalten:

 

mylava.pk3
= pk3-Datei mit dem Shader für MP - Modus (muss in den base
- Ordner kopiert werden)

lava_test.bsp
= Test-Map für unseren neuen Lava Shader (in den base/maps
Ordner kopieren)

lava_test.map
= Test-Map Quellcode (in den base/maps
Ordner kopieren)

mylava.shader
= Shader-Datei, die in den base/shaders
- Ordner kopiert werden muss ( nicht vergessen, den Namen in die shaderlist.txt
einzutragen! )

 

----

[u][DOWNLOAD
DER TUTORIAL MAP](../downloads/my_lava.zip)[/u]

(.map
- Dateie enthalten)

----

**TIP:**
 In dem "base/shaders"
- Ordner befinden sich die original Shader - Definitionen aus dem JKII - Spiel.
Wenn du einen nuenen speziellen Shader erstellen möchtest, ist es immer ratsam,
sich einen bereits existierenden Shader als Vorlage zu nehmen.

----

Alle
  Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet: 

©
  2000 - 2003 (Artur L.) [www.darth-arth.net](http://www.darth-arth.net)

Nur
  zur privaten Nutzung. Kopieren nicht gestattet. Darth-Arth.Net ist ausdrücklich
  nicht für den Inhalt externer Seiten verantwortlich. Es gelten die
  angegebenen Nutzungsbedingungen.

