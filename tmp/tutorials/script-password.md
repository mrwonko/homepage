title: Passworteingabefeld via Script
author: mrwonko
date: 2004-01-01
modified: 2015-04-14
category: scripts
type: tutorials/darth-arth
tags: Scripting, auto-generated
slug: script-password

**>> Mapping Academy - Tutorials <<**

(c) 2006 [www.darth-arth.de](http://www.darth-arth.de)

----

Passwort via Script

**[u]VORRAUSSETZUNGEN[/u]:**

[color=white]>> Tutorial Scripting - Installation BehavEd (Script-Editor) ([hier](http://www.darth-arth.de/tutorials/behaved/behaved.htm))

>> Tutorial Mein erster Raum ([hier](http://www.darth-arth.de/tutorials/mapping/firstroom/firstroom.htm))[/color]

----

In dieser Lehreinheit (Tutorial) Lernen wir, eine Tür mit einem Passworteingabefeld zu bauen.

----

Zuerst brauchen wir einen Raum mit einem Info_player_start und unseren Passwort-Knöpfen (Ich hab 1-3 genommen):

![Bild1]({static}images/pic1.jpg)

Die Knöpfe machen wir dann zu Knopf-Entities unserer Wahl, z.B. func_button's.

Außerdem bekommt jeder Knopf noch einen einen target_scriptrunner als target 

(Rechtsklick -> Target_ -> Target_Scriptrunner, dann erst func_button, dann target_scriptrunner anklicken und strg+k)

![Bild2]({static}images/pic2.jpg)

Nun gehen wir bei den Scriptrunnern in die Entity-Eigenschaften (N) und stellen ein:

<table border="0">
 <tr>
  <td>
   Key
  </td>
  <td>
   Value
  </td>
  <td>
   Erklärung
  </td>
 </tr>
 <tr>
  <td>
   count
  </td>
  <td>
   -1
  </td>
  <td>
   Wie oft der Scriptrunner benutzt werden kann, -1 steht für unendlich
  </td>
 </tr>
 <tr>
  <td>
   usescript
  </td>
  <td>
   examples/passwort_*
  </td>
  <td>
   Das auszuführende Script, statt * je nach scriptrunner 1, 2 oder 3 einsetzen
  </td>
 </tr>
</table>

![Bild3]({static}images/pic3.jpg)

Nun nehmen wir noch einen Brush, der nicht ans Void (das große Grau) grenzt, und machen ihn zu einem Func_Static.

(Brush markieren und Rechtsklick -> Func_ -> Func_Static)

Dieser Brush wird nachher den Fortschritt im Script speichern.

In seinen Eigenschaften (N) stellen wir noch ein:

<table border="0">
 <tr>
  <td>
   Key
  </td>
  <td>
   Value
  </td>
  <td>
   Erklärung
  </td>
 </tr>
 <tr>
  <td>
   script_targetname
  </td>
  <td>
   speicher
  </td>
  <td>
   Unter welchem Namen man den Brush im Script ansprechen kann
  </td>
 </tr>
</table>

![Bild4]({static}images/pic4.jpg)

Jetzt brauchen wir noch etwas, das passiert, wenn der Spieler alles richtig gemacht hat.

Setzt also einen target_print in die map, und stellt bei ihm ein:

<table border="0">
 <tr>
  <td>
   Key
  </td>
  <td>
   Value
  </td>
  <td>
   Erklärung
  </td>
 </tr>
 <tr>
  <td>
   targetname
  </td>
  <td>
   richtig
  </td>
  <td>
   Unter welchem Namen man ihn benutzt
  </td>
 </tr>
 <tr>
  <td>
   message
  </td>
  <td>
   gut gemacht!
  </td>
  <td>
   Welche Nachricht auf dem Bildschirm erscheinen soll
  </td>
 </tr>
</table>

Nun wenden wir uns den Scripts zu. Starten wir also BehavEd.

Ich werd den jetzt hier nicht im einzelnen erklären, sollte etwas unklar sein (z.B. wie füge ich ein Kommando hinzu), guckt bitte in einem der anderen Scripting Tutorials nach.

Als erstes schreiben wir unser passwort_1 Script.

In das Kommentar am Anfang schreiben wir "Script für Knopf 1".

Dann sprechen wir mit Affect unseren Speicher an:

![Bild5]({static}images/pic5.jpg)

Spätestens jetzt sollten wir uns eine Kombination ausdenken. Sagen wir mal 1 2 3 3 3, denn 1*2*3=3+3.

Wir benutzen jetzt den "Parm1" Wert unseres Speichers zum Speichern des Fortschritts.

Wenn der Spieler Knopf 1 drückt, wird Parm1 also auf 1 gesetzt.

![Bild6]({static}images/pic6.jpg)

Dieses kurze Script speichern wir nun unter "JKA-Verzeichnis/GameData/Base/Scripts/examples/passwort_1" und drücken auf compile.

Bei der Gelegenheit können wir auch gleich unsere Map mit -meta kompilieren und den Radiant beenden.

Ändern wir jetzt unser Script, sodass es wie folgt aussieht:

![Bild7]({static}images/pic7.jpg)

Das If-Kommando testet, ob eine Bestimmung zutrifft.

In diesem Fall, ob Parm1 = 1 ist.

Wenn Parm1 = 1 ist, wird Parm1 auf 12 gesetzt. (Das wurde nämlich dann gedrückt)

Wenn Parm1 nicht = 1 ist, wird das Kommando im Else-Teil ausgeführt. (können auch mehrere Kommandos sein)

Das heißt, dass Parm1 auf "error" gesetzt wird, weil der Spieler einen Fehler gemacht hat.

Nun speichert ihr das ganze unter ".../examples/passwort_2" (save as) und Kompiliert es (compile).

Fehlt nur noch das dritte, und komplizierteste script, denn hier wird der gleiche Knopf mehrmals gedrückt.

Eigentlich könntet ihr das schon alleine schreiben. Versucht das doch einfach mal.

	Erklärung:

	Erst wird geguckt, ob parm1 = 12 ist.

	Wenn ja, wird parm1 auf 123 gesetzt.

	Wenn nein, wird geguckt, ob parm1 auf 123 steht.

	Wenn ja, wird parm1 auf 1233 gesetzt.

	Wenn nein, wird geguckt, ob parm1 auf 1233 steht.

	Wenn ja, wird "richtig" benutzt.

	Und parm1 wird auf "error" gestellt, denn egal ob parm1 vorher 1233 war oder nicht, nun ist das script fertig und parm1 wird zurückgesetzt.

	';
}
else
	echo '[Klickt hier, falls ihr es nicht hinbekommt. (Aber erst versuchen, sonst lernt ihr ja nix)](index.php?spoiler=1#unten)

';

?>
Eines noch: Vor dem Laden der Map müsst ihr noch "sv_pure 0" in die Konsole eingeben, sonst funktionieren die Scripts nicht.

 

Und nicht vergessen die Scripts nachher in der pk3 mitzuliefern!

mfG Mr. Wonko

----

Download der Sourcefiles: [Download](downloads/source.zip)

----

Alle Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet:

© 2000 - 2006 (Artur L.) [www.darth-arth.de](http://www.darth-arth.de)

Nur zur privaten Nutzung. Kopieren nicht gestattet. Darth-Arth.De
ist ausdrücklich nicht für den Inhalt externer Seiten verantwortlich. Es gelten
die angegebenen Nutzungsbedingungen.

