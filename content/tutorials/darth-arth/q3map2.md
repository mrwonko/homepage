title: Kompilieren mit Q3map2 und Q3Map2Build
author: Darth Arth (Artur L.)
date: 2004-01-01
modified: 2016-04-24
category: general
type: tutorials/darth-arth
tags: q3map2
slug: q3map2

# Voraussetzungen

* [Installation JK2 Editing Tools I]({filename}installation-jk2-editing-tools.md)
* [Installation JK2 Editing Tools 2]({filename}installation-jk2-editing-tools-2.md)
* [Installation GTK - Radiant]({filename}installation-1.4.md)

# Vorbereitung

* Download Q3Map2 (aktuelle Version Teil des [GTK Radiant](http://icculus.org/gtkradiant/downloads.html), ältere Versionen auf der [Q3Map2 Website](http://q3map2.robotrenegade.com/))
* Download [Q3Map2build]({static}q3map2/q3map2build_win32.rar)

Entpacke  Q3Map2build und die
aktuelle Version von  Q3Map2 in einen Ordner deiner Wahl.

Starte dann Q3Map2build.

# Konfiguration

Als nächstes müssen einige
Einstellungen festgelegt werden.

![image]({static}q3map2/Image1.jpg)

Unter `Game executable location` muss der vollständiger Pfad zu der `jk2sp.exe` oder `jk2mp.exe` angegeben werden, ja nach dem, welche Art von Maps du erstellst. Diese Einstellung ist wichtig, falls du deine Map nach dem Kompilieren direkt ausprobieren möchtest.

Unter `Q3Map2.exe location` wird angegeben, wo die q3map2.exe zu finden ist. 

`Bspc.exe location` kann leer gelassen werden.

Unter `Game` muss `jk2`
angegeben werden, nicht `jkii`, wie fälschlicherweise in der
Beschriftung des Eingabe-Feldes sichtbar.

Dann auf `Save` klicken.



Jetzt sollten die "Logging Options" festgeleget
werden. 

Logging bedeutet "Protokollieren",
das heißt, dass alle Meldungen während des Kompilier-Vorgangs aufgezeichnet
werden. 

Dies ist vor allem bei Fehlersuche sehr wichtig!

![image]({static}q3map2/Image2.jpg)

Klicke auf `Logging Options`. 

Unter `Log Directory` sollte der Ordner angegeben werden, in dem die Kompilier-Protokolle (log-files) gespeichert werden sollen.

Die restlichen Einstellungen sollten in dieser Dialogbox unverändert bleiben.

Dann auf `Save` klicken.

Jetzt noch unter `Options` das Häckchen bei `Use Logging` einschalten.

Wenn
man möchte, dass die Map nach dem Kompilieren direkt im Game getestet
wird, kann man auch ein Häckchen bei `Play after build` setzten. 

Diese Option ist jedoch unter Umständen nicht sinnvoll, vor allem, wenn man während
des Kompilierens andere Arbeiten ausführt, da die Gefahr besteht, dass man dadurch in einer wichtigen Tätigkeit unterbrochen wird, was manchmal auch zu Datenverlust führen kann.

# Kompilier-Einstellungen

Als nächstes sollten noch ein
paar Einstellungen zum Kompiliervorgang vorgenommen werden.

Bitte bei `BSP`, `VIS`, `LIGHT` von
`Normal`
auf `Custom`
umstellen und überall das Häckchen bei `Pause`
herausnehmen.

![image]({static}q3map2/Image3.jpg)

Bei den Einzelnen
Kompilierschritten sollten die Einstellungen wie folgt aussehen:

Bei `BSP` bitte `-meta` und `-v`
einstellen.

![image]({static}q3map2/Image4.jpg)

Bei `VIS` bitte `-fast`
und `-v`
einstellen.

![image]({static}q3map2/Image5.jpg)

Bei `LIGHT` bitte `-fast`
und `-v`
einstellen.

![image]({static}q3map2/Image6.jpg)

Diese
Einstellungen entsprechen dem `FastVis
(1/2)` Kompiliervorgang,
welcher am
besten zum Testen von Maps geeignet ist.

Für `Novis/Nolight`
sollte man `VIS` und `LIGHT` auf `None`
stellen (z.B. bei LEAK-Suche).

Für
eine `FullVis`
Kompilierung sollte bei `VIS` und `LIGHT` der Parameter `-fast`
ausgeschaltet werden.

<div class="alert alert-info">Bitte beachten, dass eine
FullVis Kompilierung von mehreren Stunden bis zu mehreren Tagen dauern kann, je
nach Komplexität und Größe einer Map.</div>

Für weitere Optionen und
Parameter zum dem Kompilier-Vorgang bitte die Q3map2-Dokumentation
konsultieren.

# Kompilieren

Sind alle Einstellungen korrekt,
werden unter Maps alle `.map`-Dateien
angezeigt.

Jetzt kann man die gewünschte
Map auswählen und mit einem Klick auf `Build`
kompilieren.

Unter `Logging Info`
erscheint dann: `Status: connected (127.0.0.1), mapname.log`.

Hier kann man jede Zeit (auch
während des Kompilierens) auf `View`
klicken und sich den aktuellen Stand der Log-Datei anzeigen lassen (wichtig bei
Fehlersuche).

![image]({static}q3map2/Image7.jpg)

<div class="alert alert-warning"><b>Achtung:</b>

Leider hat Q3map2build einen
kleinen Bug. Nach dem Kompiliervorgang muss das Programm beendet werden, denn
sonst wird beim nächsten Kompilieren die Log-Datei nicht erstellt. Das heißt,
man muss vor jeder Kompilierung das Programm neu starten, was aber nur
unwesentlich die Funktionalität des sehr guten Tools beeinträchtigt.</div>

# Tips

Speichere deine Maps öffters unter einen neuen Versions-Namen, so dass du im Fall eines
schwerwiegenden Fehlers auf die letzte funktionsfähige Version zugreifen
kannst.

Nutze
bei Q3map2 nur die Optionen und Parameter, deren Funktionalität dir völlig
klar ist, ansonsten sind unerwünschte Effekte, Große BSP-Dateien und lange
Kompilierzeiten angesagt.

 

Kompiliere
deine Maps regelmäßig und kontrolliere genau die Log-Dateien, um rechtzeitig
Fehler zu entdecken und beheben zu können. Ansammlungen von Fehlern sind schwer
zu korrigieren und kosten viel Zeit und Nerven. Unter Umständen kann die Map sogar
unbrauchbar werden.
