title: Installation - GTK Radiant 1.4 (Raven)
date: 2004-01-01
type: tutorials
author: Killermic (Michael S.)
category: editor
tags: FIXME
modified: 2015-04-12

# Voraussetzungen

* [GTK Radiant 1.4](http://eliteforce2.filefront.com/file/GTKRadiant;26097)

# Tutorial

In dieser Lehreinheit (Tutorial) lernen wir, den GTK Radiant 1.4 zu installieren.

Dieses Tutorial ist für JK - JA und JK - JK2 ausgelegt.

Als erstes rufen wir die `GtkRadiantSetup-1.4.0-raven.exe` (wenn nicht umbenannt) auf.

Nach einer kleinen Wartezeit kommt dieser Bildschirm:

![image]({filename}installation-1.4/step1.jpg)

Wir klicken auf `Next` und stimmen, mit einem klick auf `Yes`, auch den Lizenzvereinbarungen zu.

Der darauf folgende Dialog ist nur eine kleine Information, was der Radiant alles für Spiele unterstütz, also wieder auf `Next`.

<div class="alert alert-info">Ab hier fangen die potentiellen Fehlerquellen an, also bitte alles genau nach dem Tutorial machen.</div>

Auf dem nächsten Bildschirm wird abgefragt wohin der GTK Radiant installiert werden soll.

Dies ist noch ziemlich egal, daher würde ich die Standart Einstellung nehmen. (Ihr könnt natürlich hier noch einen anderen Ordner nehmen.)

<div class="alert alert-warning"><strong>ACHTUNG</strong>: <strong>Nicht</strong> in <code>/GameData</code> oder untergeordnete Ordner installieren!</div>

![image]({filename}installation-1.4/step2.jpg)

Jetzt wird abgefragt wo Jedi Knight 2 - Jedi Outcast installiert ist.

Hier könnt ihr natürlich eintragen wo euer JK2 installiert ist, aber ich mache das hier in dem Tutorial nicht, dafür gibt es nämlich das Tutorial [Installation - GTK Radiant 1.2]({filename}installation-1.2.md) von Darth Arth.

Der nächste Bildschirm wird auch in diesem Tutorial nicht beachtet, da es immer noch für JK2 ist ;)

Auf dem darauf folgenden Bildschirm wird gefragt wo wir Star Trek Voyager : Elite Force installiert haben. 

Dies wird abgefragt, damit man mit einer heruntergeladenen Installations-Datei den Map-Editor auch für andere Q3-Engine basierte Spiele installieren kann. 

Wenn du eins oder mehrere der Spiele nicht besitzst, einfach auf `Next` klicken.

Auch dies wird im Tutorial ignoriert. Ebenso wie der darauf folgende Dialog.

Danach kommt noch Soldiers of Fortune II - Double Helix, was hier auch ingoriert wird. (und die darauf folgende Abfrage ebenso...)

Und endlich wird nach *Jedi Knight - Jedi Academy* gefragt!

![image]({filename}installation-1.4/step3.jpg)

Hier klicken wir auf `Browser...`. Dann erscheint dieses Fenster:

![image]({filename}installation-1.4/step4.jpg)

Hier müssen wir jedoch etwas einstellen.

Wir müssen den Ort angeben, wo **Jedi Academy** installiert ist.

Bei dem Beispiel ist es unter `C:\\Programme\LucasArts` installiert.

in diesem Feld muss man aber angeben, wo sich der richtige Ordner `/GameData` befindet.

<div class="alert alert-warning"><strong>ACHTUNG</strong>: es <em>muss</em> dein richtiger <code>.../GameData</code> Ordner angegeben werden!</div>

![image]({filename}installation-1.4/step5.jpg)

Jetzt wieder auf `Next` klicken.

Der darauf folgende Dialog bestimmt den Namen, den der Ordner haben wird, der in `/GameData` erstellt wird. Das ist auch egal.

<div class="alert alert-warning"><strong>ACHTUNG</strong>: Den Ordner Namen nicht nachträglich ändern!</div>

Also wieder auf `Next`.

Jetzt wird gefragt ob wir "**Custom**" oder "**Full Install**" haben wollen.

Das muss jeder für sich selbst entscheiden, aber ich würde "Full Install" empfehlen. (Natürlich nicht, wenn man eine kleine Festplatte hat, oder nur noch sehr wenig Speicher!)

Jetzt wird nur noch gefragt, wie der Ordner in eurem Startmenü heißen soll. Das entscheidet jeder selbst oder einfach auf `Next` klicken.

Nach einem klick auf `Next` wird noch mal in einer Zusammenfassung angezeigt, was alles installiert wird.

Wieder auf `Next` und euer GTK Radiant wird installiert!

Nachdem der Balken bis auf 100% gewandert ist, drücken wir auf `Finish`.


**Glückwunsch! Jetzt ist dein GTK Radiant 1.4 installiert!**

Doch hier endet das Tutorial nicht, denn wir müssen überprüfen, ob alles richtig installiert wurde.

Dazu rufen wir den GTK Radiant auf.

In dem kleinen Dialog-Fenster, welches beim aufrufen erscheint, stellen wir folgendes ein:

![image]({filename}installation-1.4/step6.jpg)

Nach einem klick auf "OK" startet der GTK Radiant. Jetzt sieht das ganze so aus:

![image]({filename}installation-1.4/step7.jpg)

Um zu testen ob die Installation erfolgreich war klicken wir auf `Menu > Textures`

Danach auf `Desert`

![image]({filename}installation-1.4/step8.jpg)

(Nicht wundern, wenn bei euch manche Menü-Punkte unter `Textures` nicht so sind wie bei mir. Das kommt durch Custom-Maps wo eigene Texturen dabei sind)

Nachdem wir auf `Desert` geklickt haben, sollte der Editor die Texturen laden. 

Unten in der Status-Leiste sollten wir das ablesen können:

<pre>Loaded 100 shaders and created default shader for 70 orphan textures.</pre>

Wenn jetzt im Texturen-Fenster es so aussieht, dann sollte alles stimmen:

![image]({filename}installation-1.4/step9.jpg)

Wenn hier etwas nicht stimmt, solltest du noch mal das Tutorial durchgehen und überprüfen, ob du alles richtig gemacht hast.

Und jetzt **VIEL** Spaß beim Mappen!

Ich würde empfehlen mit den Tutorial [Mein erster Raum](www.darth-arth.de/tutorials/mapping/firstroom/firstroom.htm) FIXME anzufangen. 
