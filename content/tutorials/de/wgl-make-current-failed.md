title: "wglMakeCurrent failed" Fehler beheben
date: 2008-04-07
type: tutorials
author: Darth Arth (Artur L.)
category: editor
tags: Fehler
modified: 2015-04-12

Betrifft GTKRadiant ab Version 1.3.13.

<pre>ERROR: wglMakeCurrent failed.. Error:[Wert]</pre>

ist normalerweise damit verbunden, dass Antialiasing der Grafikkarte eingeschaltet ist. Auf manchen Systemen führt das zu dem dem Fehler. Dies kann man in dem Control-Pannel der Grafikkarte abschalten. Der Editor verträgt das Antialiasing auf manchen Systemem nicht.



# Wie kann man das fixen?

*   AA im Control-Pannel der Grafikkarte abschalten, sicherstellen, dass es nicht auf "Anwendungsgesteuert" steht.
*   Sollte der Fehler immer noch kommen, ist ev. der Desktop auf 16-bit Farben eingestellt, dann bitte auf 32-bit hochsetzen.
*   Multicore CPUs können auf manchen Systemen auch diesen Fehler verursachen.

    In diesem Fall den Radiant einem Prozessor(kern) zuordnen.  Entweder über den Taskmanager (rechte maustaste > Zugehörigkeit festlegen) oder dauerhaft mit dem Programm "imagecfg.exe" (auf der Windows CD zu finden)

    <pre>CMD-Line:> imagecfg -a 0x1 GtkRadiant-1.4.0.exe</pre>