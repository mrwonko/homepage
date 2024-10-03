title: Target Speaker (Geräusche machen)
author: FexXo (Andreas N.)
date: 2004-01-01
modified: 2015-04-14
category: mapping
type: tutorials/darth-arth
tags: Entities, auto-generated
slug: entity-target-speaker

**>>
Mapping Academy - Tutorials <<**

 

(c) 2006 [http://www.darth-arth.de/](http://www.darth-arth.de/)

----

Sounds an bestimmten
Stellen automatisch und per Knopfdruck erklingen lassen

Author: FexXo (Andreas
N.)

In diesem Tutorial wird
dir erklärt, wie du Musik oder auch Sounds in einem bestimmten
Raum bzw. an einer bestimmten Stelle erklingen lassen kannst.

Ganz zu Anfang brauchen
wir einen Raum, welcher nicht zu riesig sein sollte. Unserer hat ca. 
512 x 512 Einheiten. Und falls du nicht
weißt, wie man einen Raum erstellt, kannst du dieses in Darth
Arth's Tutorial >> "[Mein erster Raum](../../mapping/firstroom/firstroom.htm)" << nachlesen.

Nun sollte es bei euch
so aussehen:

![image]({filename}Schritt-1.JPG)

Ihr braucht nun etwas, das ihr mit Sound
untermalen könnt. Als Beispiel habe ich einen Feuereffekt
verwendet. Diesen Effekt erstellt ihr wie folgt:

Klicke mit der rechten Maustaste auf das
Raster irgendwo in den Raum hinein und wähle '' Fx > Fx_Runner ''
aus.

![image]({filename}Schritt-2.JPG)

Wenn ihr das getan habt,
müsste bei euch so ein kleines, blaues Kästchen erscheinen:

![image]({filename}fx_runner.JPG)

Dieses Kästchen
zeigt euch an, wo der Feuereffekt erscheinen wird. Sprich: Wenn ihr das
Kästchen verschiebt, verschiebt ihr den Feuereffekt. Doch bevor
irgendein Feuerchen erscheinen kann, müsst ihr dem Kästchen
den gewünschten Effekt zuordnen. Das macht ihr, indem ihr das
kästchen mit ''
Shift + linke Maustaste '' anwählt und dann auf 
'' N '' drückt, um in das
Entity-Menü zu kommen. Im Entity-Menü gebt ihr dann folgendes
ein:

<table border="0" cellpadding="0" cellspacing="0" id="AutoNumber1" style="border-collapse: collapse;" width="19%">
 <tr>
  <td width="50%">
   <font color="#c0c0c0" face="Arial" size="2">
    Key:
   </font>
  </td>
  <td width="50%">
   <font color="#c0c0c0">
    FxFile
   </font>
  </td>
 </tr>
 <tr>
  <td width="50%">
   <font color="#c0c0c0" face="Arial" size="2">
    Value:
   </font>
  </td>
  <td width="50%">
   <font color="#c0c0c0">
    Effects/Env/Fire.efx
   </font>
  </td>
 </tr>
</table>

Nun habt ihr euren
Effekt erstellt und es wird im Spiel ein kleines Feuerchen zu sehen
sein. Aber unser Feuer soll ja nicht einsam in dem Raum rumsitzen, das
würde den Effekt verfehlen wie ihr hier seht:

![image]({filename}einsames_feuer.JPG)

Um dem Feuer eine, im
wahrsten Sinne des Wortes, effektive Aufgabe zu geben, werden wir es
nutzen um einen Eingang zu verschönern. Dazu bauen wir eine
Tür mit einem Durchgang, der zu KEINEM weiteren Raum führt.
Wie man eine Tür mit einem Durchgang baut, erfährst du in dem
Tutorial >> 
[
zwei Räume verbinden](../../mapping/tworooms/tworooms.htm) 
<<. Links und rechts von der Tür errichten wir zwei kleine
Podeste, auf die du deinen 
" Fx_Runner " setzt(ganz dicht dran). Um dein
anderes Podest mit dem Effekt zu versehen, kopiere einfach den bereits
erstellten 
( Markieren und '' STRG + C
'' ) und füge
ihn auf dem selben Punkt wieder ein ( Einfach '' STRG + V '' drücken). 

Es sieht dann so
ähnlich bei euch aus:

![image]({filename}Durchgang.JPG)

Nun hast du schonmal
deinen Effekt, jedoch noch keinen passenden Sound, welchen du ja gerne
hören würdest wenn du neben dem Feuer stehst. Für den
Sound benötigst du einen 
" Target_Speaker ". Gehe dafür in's Menü
und wähle 
'' Target >
Target_Speaker ''

![image]({filename}target_speaker.JPG)

Wenn du das gemacht
hast, erscheint in deiner 3D-Vorschau ein weiteres Kästchen,
welches aber rot ist:

![image]({filename}target_speaker_2.JPG)

Nun wählst du den 
" Target_Speaker " an, wir erinnern uns daran wie
wir vorhin den 
" Fx_Runner " angewählt haben und
drücken dann ebenfalls wieder auf 
'' N '' um das Entity-Menü zu
öffnen. Dort gibst du dann folgendes ein:

<table border="0" cellpadding="0" cellspacing="0" id="AutoNumber1" style="border-collapse: collapse;" width="23%">
 <tr>
  <td width="73%">
   <font color="#c0c0c0" face="Arial" size="2">
    Key:
   </font>
  </td>
  <td width="50%">
   <font color="#c0c0c0">
    Noise
   </font>
  </td>
 </tr>
 <tr>
  <td width="73%">
   <font color="#c0c0c0" face="Arial" size="2">
    Value:
   </font>
  </td>
  <td width="50%">
   <font color="#c0c0c0">
    Sound/Effects/Fire_LP.wav
   </font>
  </td>
 </tr>
</table>

Nachdem ihr die Eingaben
mit Enter bestätigt habt, macht ihr einen Haken bei '' Loopen-On
'' >> 
![image]({filename}looped_on.JPG) Platziert nun euren  "
Target_Speaker " über einem
der            
" Fx_Runner-Kästchen ", kopiert den  "
Target_Speaker " und schiebt die Kopie
über euren anderen  " Fx_Runner " , damit der Sound auch da gehört wird, wo das
Feuer ist.

Es sollte in etwa so bei euch aussehen:

![image]({filename}target_speaker_3.JPG)

Wenn du alles richtig
gemacht und befolgt hast, siehst du die Map (wenn du meine Texturen
genommen hast) so wie auf diesem Bild und du hörst eine Art
Knistern des Feuers. Du wirst aucg bemerken, dass das Knistern leiser
wird, wenn du dich von dem Feuer entfernst ;-) In der Beispielmap
hört man es deutlich, wenn man ganz hinten rechts oder linsk in
eine Ecke geht.

Herzlichen
Glückwunsch !!

![image]({static}shot0150.jpg)

Es gibt jedoch noch eine
zweite Möglichkeit, den 
" Target_Speaker " einzusetzen. Und zwar handelt
es sich hierbei um die Benutzung eines 
Buttons, der den Sound dann sozusagen
per Knopfdruck aktiviert und für alle oder nur für den
*Knopfdrückenden* hörbar ist. 

Wie das funktioniert,
erkläre ich euch jetzt:

Wir benutzen dafür
unsere bereits erstellte " Target_Speaker-Map ". Es gibt ja noch genügend Raum zum
Arbeiten.

Zu Anfang erstellen wir
in der Mitte des Raumes einen normalen Brush, der ungefähr doppelt
so groß wie ein 
Info_Player_Spawn - Point ist:

![image]({filename}spawn_doppelt.JPG)

Danach formen wir uns
einen Brush zurecht, der später im Spiel als 
 [u]angeblicher[/u] Schalter dienen soll und setzen
einen Brush mit der Textur 
'' System/Trigger '' davor:

![image]({filename}trigger_multiple_1.JPG)

Jetzt markieren wir den Brush mit der
Triggertextur und geben ihm die Gruppe ''
Trigger_Multiple '' >>

 ![image]({filename}trigger_multiple_2.JPG)

Nachdem du den "
Trigger_Multiple " erstellt hast, klickst
du einmal auf 
'' ESC '' um alles
zu deselektieren. Jetzt ist es an der Zeit den " Target_Speaker " in's
Spiel zu bringen. Markiere dazu einfach einen der bereits erstellten " Target_Speaker " und
kopiere ihn. Nachdem du deinen dritten "
Target_Speaker " hast, schiebst du ihn ein
Stückchen über den Schalter:

![image]({filename}target_Speaker_4.JPG)

Nun markiere den 
" Target_Speaker " erneut und gebe ihm folgende
Werte:

<table border="0" cellpadding="0" cellspacing="0" id="AutoNumber1" style="border-collapse: collapse;" width="33%">
 <tr>
  <td width="87%">
   <font color="#c0c0c0" face="Arial" size="2">
    Key:
   </font>
  </td>
  <td width="50%">
   <font color="#c0c0c0">
    Noise
   </font>
  </td>
 </tr>
 <tr>
  <td width="87%">
   <font color="#c0c0c0" face="Arial" size="2">
    Value:
   </font>
  </td>
  <td width="50%">
   <font color="#c0c0c0">
    Sound/Ambience/Bespin/Bespin_Air.wav
   </font>
  </td>
 </tr>
</table>

Habt ihr das getan,
deselektiert ihr alles durch drücke der 
'' ESC-Taste ''. Nun wählt ihr zuerst den 
" Trigger_Multiple " aus und danach den
Target_Speaker, sodass beide markiert sind. Verbindet die beiden durch
drücken von 
'' STRG + K ''. Drücke noch einmal die 
'' ESC-Taste '' und wähle dann den 
" Trigger_Multiple " und mache ein Häckchen in
das Feld 
>> '' Use_Button ''
<< 
![image]({filename}use_button.JPG)

![image]({filename}multiple_speaker_verbunden.JPG)

Herzlichen Glückwunsch, du hast jetzt
einen Sound der auf Knopfdruck abgespielt wird. Wenn du alles richtig
befolgt hast, wirst du einen Single Player Sound hören, wenn du
vor dem Schalter den 
[u]**'' Use-Button '' **[/u]drückst.  

![image]({static}shot0148.jpg)

Zum Spielen der Map, startet JK2-MP oder SP
und öffnet die Console. Schreibt dort ''
map target_speaker ''
hinein und ihr könnt sehen, wie es im
Spiel ausschaut.

----

[**Tutorial-Map Download**](target_speaker.pk3)

-(.map Datei enthalten)- 

----

Alle Bilder,
Texte, Grafiken, wenn nicht anders gekennzeichnet: 

© 2000 -
2006 (Artur L.) [http://www.darth-arth.de/](http://www.darth-arth.de/)

Nur zur privaten
Nutzung. Kopieren nicht gestattet. Darth-Arth.Net ist ausdrücklich
nicht für den Inhalt externer Seiten verantwortlich. Es gelten die
angegebenen Nutzungsbedingungen. 

 

