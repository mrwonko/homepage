<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="de" xml:lang="de">
<head>
<title>Passwort via Script</title>
<style type="text/css">
body        {background-color:#333333; color:#C0C0C0; font-family:Arial; font-size:12.0pt;}
.title      {font-size:14.0pt; color:white;}
.heading    {text-align:center; color:teal; font-size:20.0pt;}
.copyright  {text-align:center; color:gray; font-size:14pt;}
.copyright2 {text-align:center; font-size:7.5pt; font-family:Verdana; color:teal;}
.needed     {color:yellow;}
</style>
</head>

<body bgcolor="#333333" lang=DE link=blue vlink=blue style='tab-interval:35.4pt'>

<p class="heading"><b>&gt;&gt; Mapping Academy - Tutorials &lt;&lt;</b></p>
<p class="copyright">(c) 2006 <a href="http://www.darth-arth.de" target="_blank">www.darth-arth.de</a></p>

<hr />

<p class="title">Passwort via Script</p>
<p class="needed"><b><u>VORRAUSSETZUNGEN</u>:</b></p>
<p><span style="color:white;">&gt;&gt; Tutorial Scripting - Installation BehavEd (Script-Editor) (<a
href="http://www.darth-arth.de/tutorials/behaved/behaved.htm" target="_blank">hier</a>)<br />
&gt;&gt; Tutorial Mein erster Raum (<a href="http://www.darth-arth.de/tutorials/mapping/firstroom/firstroom.htm" target="_blank">hier</a>)</span></p>

<hr />

<p>In dieser Lehreinheit (Tutorial) Lernen wir, eine Tür mit einem Passworteingabefeld zu bauen.</p>

<hr />

<p>

Zuerst brauchen wir einen Raum mit einem Info_player_start und unseren Passwort-Knöpfen (Ich hab 1-3 genommen):<br /><br />
<img src="images/pic1.jpg" alt="Bild1"/><br /><br />
Die Knöpfe machen wir dann zu Knopf-Entities unserer Wahl, z.B. func_button's.<br /><br />
Außerdem bekommt jeder Knopf noch einen einen target_scriptrunner als target <br />(Rechtsklick -> Target_ -> Target_Scriptrunner, dann erst func_button, dann target_scriptrunner anklicken und strg+k)<br /><br />
<img src="images/pic2.jpg" alt="Bild2"/><br /><br />
Nun gehen wir bei den Scriptrunnern in die Entity-Eigenschaften (N) und stellen ein:<br /><br />
<table border=0>
<tr>
<td>Key</td><td>Value</td><td>Erklärung</td>
</tr>
<tr>
<td>count</td><td>-1</td><td>Wie oft der Scriptrunner benutzt werden kann, -1 steht für unendlich</td>
</tr>
<tr>
<td>usescript</td><td>examples/passwort_*</td><td>Das auszuführende Script, statt * je nach scriptrunner 1, 2 oder 3 einsetzen</td>
</tr>
</table><br /><br />
<img src="images/pic3.jpg" alt="Bild3"/><br /><br />
Nun nehmen wir noch einen Brush, der nicht ans Void (das große Grau) grenzt, und machen ihn zu einem Func_Static.<br />
(Brush markieren und Rechtsklick -> Func_ -> Func_Static)<br />
Dieser Brush wird nachher den Fortschritt im Script speichern.<br /><br />
In seinen Eigenschaften (N) stellen wir noch ein:<br /><br />
<table border=0>
<tr>
<td>Key</td><td>Value</td><td>Erklärung</td>
</tr>
<tr>
<td>script_targetname</td><td>speicher</td><td>Unter welchem Namen man den Brush im Script ansprechen kann</td>
</tr>
</table><br /><br />
<img src="images/pic4.jpg" alt="Bild4"/><br /><br />
Jetzt brauchen wir noch etwas, das passiert, wenn der Spieler alles richtig gemacht hat.<br />
Setzt also einen target_print in die map, und stellt bei ihm ein:<br /><br />
<table border=0>
<tr>
<td>Key</td><td>Value</td><td>Erklärung</td>
</tr>
<tr>
<td>targetname</td><td>richtig</td><td>Unter welchem Namen man ihn benutzt</td>
</tr>
<tr>
<td>message</td><td>gut gemacht!</td><td>Welche Nachricht auf dem Bildschirm erscheinen soll</td>
</tr>
</table><br /><br />
Nun wenden wir uns den Scripts zu. Starten wir also BehavEd.<br /><br />
Ich werd den jetzt hier nicht im einzelnen erklären, sollte etwas unklar sein (z.B. wie füge ich ein Kommando hinzu), guckt bitte in einem der anderen Scripting Tutorials nach.<br /><br />
Als erstes schreiben wir unser passwort_1 Script.<br /><br />
In das Kommentar am Anfang schreiben wir "Script für Knopf 1".<br />
Dann sprechen wir mit Affect unseren Speicher an:<br /><br />
<img src="images/pic5.jpg" alt="Bild5"/><br /><br />
Spätestens jetzt sollten wir uns eine Kombination ausdenken. Sagen wir mal 1 2 3 3 3, denn 1*2*3=3+3.<br /><br />
Wir benutzen jetzt den "Parm1" Wert unseres Speichers zum Speichern des Fortschritts.<br />
Wenn der Spieler Knopf 1 drückt, wird Parm1 also auf 1 gesetzt.<br /><br />
<img src="images/pic6.jpg" alt="Bild6"/><br /><br />
Dieses kurze Script speichern wir nun unter "JKA-Verzeichnis/GameData/Base/Scripts/examples/passwort_1" und drücken auf compile.<br />
Bei der Gelegenheit können wir auch gleich unsere Map mit -meta kompilieren und den Radiant beenden.<br /><br />
Ändern wir jetzt unser Script, sodass es wie folgt aussieht:<br /><br />
<img src="images/pic7.jpg" alt="Bild7"/><br /><br />
Das If-Kommando testet, ob eine Bestimmung zutrifft.<br />
In diesem Fall, ob Parm1 = 1 ist.<br /><br />
Wenn Parm1 = 1 ist, wird Parm1 auf 12 gesetzt. (Das wurde nämlich dann gedrückt)<br /><br />
Wenn Parm1 nicht = 1 ist, wird das Kommando im Else-Teil ausgeführt. (können auch mehrere Kommandos sein)<br />
Das heißt, dass Parm1 auf "error" gesetzt wird, weil der Spieler einen Fehler gemacht hat.<br /><br />
Nun speichert ihr das ganze unter ".../examples/passwort_2" (save as) und Kompiliert es (compile).<br /><br />
Fehlt nur noch das dritte, und komplizierteste script, denn hier wird der gleiche Knopf mehrmals gedrückt.<br /><br />
Eigentlich könntet ihr das schon alleine schreiben. Versucht das doch einfach mal.<br id="unten" /><br />

<?php

if($_GET['spoiler']==1)
{
	echo'
	<img src="images/pic8.jpg" alt="Bild8"/><br /><br />
	Erklärung:<br />
	Erst wird geguckt, ob parm1 = 12 ist.<br />
	Wenn ja, wird parm1 auf 123 gesetzt.<br />
	Wenn nein, wird geguckt, ob parm1 auf 123 steht.<br />
	Wenn ja, wird parm1 auf 1233 gesetzt.<br />
	Wenn nein, wird geguckt, ob parm1 auf 1233 steht.<br />
	Wenn ja, wird "richtig" benutzt.<br />
	Und parm1 wird auf "error" gestellt, denn egal ob parm1 vorher 1233 war oder nicht, nun ist das script fertig und parm1 wird zurückgesetzt.<br /><br />
	';
}
else
	echo '<a href="index.php?spoiler=1#unten">Klickt hier, falls ihr es nicht hinbekommt. (Aber erst versuchen, sonst lernt ihr ja nix)</a><br /><br />';

?>
Eines noch: Vor dem Laden der Map müsst ihr noch "sv_pure 0" in die Konsole eingeben, sonst funktionieren die Scripts nicht.<br /> <br />
Und nicht vergessen die Scripts nachher in der pk3 mitzuliefern!<br /><br /><br />
mfG Mr. Wonko
<br />

<hr />

<p>Download der Sourcefiles: <a href="downloads/source.zip">Download</a></p>

<hr />

<p class="copyright2">Alle Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet:<br /><br />
© 2000 - 2006 (Artur L.) <a href="http://www.darth-arth.de"
target="_blank">www.darth-arth.de</a><br /><br />
Nur zur privaten Nutzung. Kopieren nicht gestattet. Darth-Arth.De
ist ausdrücklich nicht für den Inhalt externer Seiten verantwortlich. Es gelten
die angegebenen Nutzungsbedingungen.</p>

</body>

</html>
