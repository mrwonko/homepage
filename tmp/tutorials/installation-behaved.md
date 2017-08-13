title: Scripting - Installation: BehavEd (Script-Editor)
author: Darth Arth (Artur L.)
date: 2004-01-01
modified: 2015-04-14
category: scripts
type: tutorials/darth-arth
tags: Installation, auto-generated
slug: installation-behaved

**>>
Mapping Academy - Tutorials <<**

 

(c)
2003 [www.darth-arth.net](http://www.darth-arth.net)

----

Konfiguration des BehavEd -
Script Editors

**[u]VORAUSSETZUNG[/u][u]EN[/u]:**

>>
Installation JK2 Editing Tools I ( [Tutorial](../radiant/jk2_etools1.htm)
)<<

>>
Installation JK2 Editing Tools 2 ( [Tutorial](../radiant/jk2_etools2.htm)
)<<

 

----

Der BehavEd-Editor hilft bei der
Erstellung von Icarus-Scripten. Die Scripte werden benötigt um Cutscenes (Im
Spiel gemachte Filme) und verschiedene Events im Single-Player Modus von JK2 zu
programmieren.

Nach der Installation von
Editing-Tools, ist der Editor jedoch noch nicht ganz arbeitsbereit. Damit man
mit dem Scripte-Erstellen beginnen kann, müssen vorher noch ein paar Einstellungen
angepasst werden.

----

**Die Konfiguration:**

Starte deinen BehavEd ( der
befindet sich in deinem GameData/Tools
- Ordner )

Wenn dein BehavEd nicht richtig
konfiguriert ist, stehen in dem Status Fenster eine ganze menge Fehler:

![image]({filename}behaved_errors.jpg)

Diese bedeuten, dass der Editor
seine Game-Ressoucen nicht finden kann, weil die Pfade nicht richtig eingestellt
sind.

Im das zu ändern, klicke auf der
rechten Seite des Editor-Fensters auf "Prefs"
in dem "Applikation"
- Bereich:

![image]({filename}behaved_prefs.jpg)

Jetzt erscheint das
Konfigurations-Fenster in dem alle relevanten Pfade angezeigt werden.

![image]({filename}behaved_prefs2.jpg)

Wichtig sind folgende Pfade:

<table border="1" height="120" width="72%">
 <tr>
  <td height="16" style="background-color: #000000" width="34%">
   <font color="#FFFFFF" face="Arial" size="2">
    Pfad-Bezeichnung
   </font>
  </td>
  <td height="16" style="background-color: #000000" width="66%">
   <font color="#FFFFFF" face="Arial" size="2">
    Beschreibung
   </font>
  </td>
 </tr>
 <tr>
  <td height="17" width="34%">
   <font color="#C0C0C0" face="Arial" size="2">
    Script
      Path
   </font>
  </td>
  <td height="17" width="66%">
   <font color="#C0C0C0" face="Arial" size="2">
    Der
      komplette Pfad zu deinem
   </font>
   <font color="#00FFFF" face="Arial" size="2">
    base/scripts
   </font>
   <font color="#C0C0C0" face="Arial" size="2">
    - Ordner
   </font>
   <p>
    <font color="#00FFFF" face="Arial" size="2">
     &lt;dein
      JK2-Installationspfad&gt;/GameData/
    </font>
    <font color="#00FFFF" face="Arial" size="2">
     base/scripts
    </font>
   </p>
  </td>
 </tr>
 <tr>
  <td height="19" width="34%">
   <font color="#C0C0C0" face="Arial" size="2">
    Location
      of IBIZE.EXE
   </font>
  </td>
  <td height="19" width="66%">
   <font color="#C0C0C0" face="Arial" size="2">
    Hier
      wird angegeben wo sich der Script-Kompiler befindet. Der sollte in deinem
   </font>
   <font color="#00FFFF" face="Arial" size="2">
    GameData/Tools
   </font>
   <font color="#C0C0C0" face="Arial" size="2">
    - Ordner liegen.
   </font>
   <p>
    <font color="#C0C0C0" face="Arial" size="2">
     Die Angabe sollte dann so
      aussehen:
    </font>
   </p>
   <p>
    <font color="#00FFFF" face="Arial" size="2">
     &lt;dein
      JK2-Installationspfad&gt;/GameData/Tools/IBIze.exe
    </font>
   </p>
  </td>
 </tr>
 <tr>
  <td height="19" width="34%">
   <font color="#C0C0C0" face="Arial" size="2">
    Command
      Description File
   </font>
  </td>
  <td height="19" width="66%">
   <font color="#C0C0C0" face="Arial" size="2">
    Die Beschreibung
      der Script-Befehle.
   </font>
   <font color="#C0C0C0" face="Arial" size="2">
    Befindet
      sich in deinem
   </font>
   <font color="#00FFFF" face="Arial" size="2">
    GameData/Tools
   </font>
   <font color="#C0C0C0" face="Arial" size="2">
    - Ordner
   </font>
   <p>
    <font color="#C0C0C0" face="Arial" size="2">
     Die richtige Eingabe:
    </font>
   </p>
   <p>
    <font color="#00FFFF" face="Arial" size="2">
     &lt;dein
      JK2-Installationspfad&gt;/GameData/Tools/behavEd.bhc
    </font>
   </p>
  </td>
 </tr>
 <tr>
  <td height="19" width="34%">
   <font color="#C0C0C0" face="Arial" size="2">
    Source
      Files path
   </font>
  </td>
  <td height="19" width="66%">
   <font color="#C0C0C0" face="Arial" size="2">
    Der
      Pfad zu Spiel-Beschreibungen. Die Standard-Angaben zu diesem Pfad sind
      meistens falsch!
   </font>
   <p>
    <font color="#C0C0C0" face="Arial" size="2">
     Die richtige Einstellung
      lautet:
    </font>
   </p>
   <p>
    <font color="#00FFFF" face="Arial" size="2">
     &lt;dein
      JK2-Installationspfad&gt;/GameData/Tools/gamesource
    </font>
   </p>
  </td>
 </tr>
</table>

Falls einer der Pfade nicht
richtig ist, klicke auf "Browse..."
und finde den richtigen Pfad.

----

Nach dem du alle Pfade eingestellt hast, klicke auf **<OK>**.

Wenn alle Angaben richtig
sind, sollte dann im Status-Fenster folgendes erscheinen:

![image]({filename}behaved_ready.jpg)

Die eine übrig gebliebene
Fehlermeldung, kann ignoriert werden...

----

**Gratuliere, du hast jetzt
einen funktionsfähigen Script-Editor!**

----

Alle
  Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet: 

©
  2000 - 2003 (Artur L.) [www.darth-arth.net](http://www.darth-arth.net)

Nur
  zur privaten Nutzung. Kopieren nicht gestattet. Darth-Arth.Net ist ausdrücklich
  nicht für den Inhalt externer Seiten verantwortlich. Es gelten die
  angegebenen Nutzungsbedingungen.

   

