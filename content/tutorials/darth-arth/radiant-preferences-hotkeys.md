title: GTK Radiant Hotkeys und Eigenschaften
author: Darth Norman (Norman P.)
date: 2004-01-01
modified: 2015-04-14
category: editor
type: tutorials/darth-arth
tags: Radiant
slug: radiant-preferences-hotkeys

In diesem Tutorial werde
ich euch die für Mapper besten Einstellungen, sowie die meisten und wichtigsten
HOTKEYS im GTK Radiant nennen und erklären. 



# Einstellungen

Nachdem ihr den GTK Radiant
installiert und gestartet habt (siehe [Tutorial: GTK Radiant – Installation]({filename}installation-1.4.md)),
könnt ihr nun in den `Preferences` (<kbd>P</kbd> drücken) den
Radiant auf eure Wünsche zurechtschneiden.

![image]({static}radiant-preferences-hotkeys/image001.jpg)

-   Game settings: hier müsst ihr das Spiel wählen, für das ihr später mappen wollt.
-   2D Display/Rendering: Grundeinstellungen so lassen
-   3D View: bezieht sich auf das 3D-Fenster im Editor, hier ist es von Vorteil die beiden Regler ganz nach links zu schieben. Sie sind für die Mausgeschwindigkeit zuständig; je langsamer sich die Kamera bewegt, desto genauer kann man in alle Winkel manövrieren.
-   Texture Settings: Grundeinstellungen so lassen
-   Layout: hier stellt man die Gliederung der einzelnen Fenster ein.

    Ich persönlich bevorzuge das erste: ![image]({static}radiant-preferences-hotkeys/image002.gif) mit ihm lässt es sich am besten mappen.
    
-   Mouse: hier darauf achten, dass `3 button` angeklickt ist; vorausgesetzt, man hat eine 3-Tastenmaus :)

-   Editing: Grundeinstellungen so lassen

-   Startup/Autosave: hier kann man unter `Load last map on open` dem Radi befehlen, er soll bei jedem Start die letzte Map, die bearbeitet wurde, öffnen. Das bringt nur was, wenn man immer an ein und derselben Map arbeitet (ich finde es auf die Dauer nervig -.-)

    Des Weiteren kann man noch die  **Autosave-Funktion**  bestimmen, sie gibt an, nach welcher Zeit der Editor die gerade in Bearbeitung befindliche map in `autosave.map` speichern soll. **5 Minuten mindestens, wenn nicht noch weniger**, sollte es schon sein, gerade bei komplexen Bauten ist es immer gut zu speichern; wenn man es selber mal vergisst und einen Fehler in der Map hat, kann man sich sicher sein, dass der Editor eine Kopie gemacht hat.

-   Paths: kann leer bleiben
-   Misc: Grundeinstellungen so lassen
-   BSP Monitoring: ist unwichtig, da ihr mit [q3map2build]({filename}q3map2.md) kompilieren solltet!



# Editor

![image]({static}radiant-preferences-hotkeys/image004.jpg)

So sieht das dann aus. 

Noch schnell eine kurze Erläuterung der Oberfläche (siehe Bild):

<ol>
    <li>Die Menüleisten, mit denen ihr alle wichtigen Aktionen durchführen könnt. (mehr bei Hotkeys)</li>
    <li>Das 3D Fenster, hier wird eure map in 3D und Farbe :P dargestellt.</li>
    <li>Das Texturen Fenster, hier zeigt euch der Editor alle geladenen Texturen an, die ihr über: <code>Menüleiste > Textures > <em>irgendein textur-verzeichnis</em></code> aufrufen könnt.</li>
    <li>
        Das 2D Fenster, hier wird eure map in einer der 3 Ansichten dargestellt, entweder:
        <ul>
            <li>von Oben</li>
            <li>von der Seite</li>
            <li>oder von Vorn</li>
        </ul>
        Die Ansicht wechselt ihr über diesen Button in der Menüleiste: <img alt="image" src="{static}radiant-preferences-hotkeys/image005.jpg"/>
    </li>
    <li>Dieses Fenster zeigt die Höhe eurer Brushes; an ich weiß aber nicht was es noch kann, ist auch nicht so wichtig -> könnt ihr getrost ausblenden, um mehr Platz zu schaffen.</li>
    <li>Die Statusleiste zeigt an, was der Editor gerade macht, also welche Befehle er ausführt. (kann auch ausgeblendet werden)</li>
    <li>Eine 2. Statusleiste zeigt neben der Cursor-Position auch die Anzahl der nichtmarkierten Brushes und Entities an. (lieber nicht ausblenden)</li>
</ol>



# Hotkeys

Hotkeys im Allgemeinen sind
dazu da, die Arbeit am Programm zu erleichtern, und was noch viel wichtiger
ist, zu beschleunigen. Es ist nicht wichtig, alle Hotkeys zu beherrschen, weil
grundsätzlich gilt, dass all diese Funktionen auch durch die Buttons oder Menüs
in der Menüleiste aktiviert werden können.

Also es gibt jede Menge
Hotkeys beim GTK, zuerst einmal die wichtigsten allgemeinen, die jeder kennen
sollte (die sind auch in anderen Programmen und Windows einsetzbar):

<kbd>Shift</kbd> = <kbd>Umschalt</kbd> = Taste
zum Großschreiben :ugly:

<table class="table table-striped table-sm-nowrap-col1">
    <thead>
        <tr><th>Tasten</th><th>Effekt</th></tr>
    </thead>
    <tbody>
        <tr><td><kbd>Strg</kbd> + <kbd>N</kbd></td><td><strong>n</strong>eue map (<strong>n</strong>ew)</tr>
        <tr><td><kbd>Strg</kbd> + <kbd>O</kbd></td><td>map öffnen (<strong>o</strong>pen)</td></tr>
        <tr><td><kbd>Strg</kbd> + <kbd>S</kbd></td><td>speichern (<strong>s</strong>ave)</td></tr>
        <tr><td><kbd>Strg</kbd> + <kbd>A</kbd></td><td>alles markieren (<strong>a</strong>ll)</td></tr>
        <tr><td><kbd>Strg</kbd> + <kbd>X</kbd></td><td>ausschneiden (e<strong>x</strong>tract)</td></tr>
        <tr><td><kbd>Strg</kbd> + <kbd>C</kbd></td><td>kopieren (<strong>c</strong>opy)</td></tr>
        <tr><td><kbd>Strg</kbd> + <kbd>V</kbd></td><td>einfügen (neben c)</td></tr>
        <tr><td><kbd>Strg</kbd> + <kbd>Z</kbd></td><td>rückgängig (<strong>z</strong>urück)</td></tr>
    </tbody>
</table>

So jetzt alle, die mit dem Editor zu tun haben samt Erklärung

<table class="table table-striped table-sm-nowrap-col1">
    <thead>
        <tr><th>Tasten</th><th>Effekt</th></tr>
    </thead>
    <tbody>
        <tr><td><kbd>N</kbd></td><td>öffnet den E<strong>n</strong>tity-Editor</td></tr>
        <tr><td><kbd>S</kbd></td><td>öffnet den <strong>S</strong>urfaceinspector</td></tr>
        <tr><td><kbd>K</kbd></td><td>öffnet das Farbwählfenster (für Lichter)</td></tr>
        <tr><td><kbd>L</kbd></td><td>öffnet das Entity-Übersichts Fenster: listet alle in der map befindlichen Entities akribisch auf</td></tr>
        <tr><td><kbd>M</kbd></td><td>zeigt die <strong>M</strong>apübersicht zu der Anzahl aller Brushes und Entities an</td></tr>
        <tr><td><kbd>I</kbd></td><td>selektiert alle Brushes in der map (nochmaliges Benutzen: Deselektion)</td></tr>
        <tr><td><kbd>D</kbd> / <kbd>C</kbd></td><td>bewegen die Kamera nach oben bzw. unten</td></tr>
        <tr><td><kbd>,</kbd> / <kbd>.</kbd></td><td>bewegen die Kamera nach links bzw. rechts</td></tr>
        <tr><td><kbd>Q</kbd></td><td>zeigt Höhe, Breite und Tiefe des derzeit selektierten Brushes</td></tr>
        <tr><td><kbd>H</kbd></td><td><strong>H</strong>ide-Funktion versteckt alle selektierten Brushes (<kbd>Shift</kbd> + <kbd>H</kbd>: Umkehrung)</td></tr>
        <tr><td><kbd>P</kbd></td><td>öffnet <strong>P</strong>references</td></tr>
        <tr><td><kbd>E</kbd></td><td>markiert alle <strong>E</strong>cken eines Brushes, die man dann individuell verziehen kann (Bauen von Schrägen)
        <tr><td><kbd>V</kbd></td><td>(funktioniert bei Brushes wie „e“ aber) : bevorzugt bei curves eingesetzt; man erhält ein Gittermodel des selektierten curve (Zylinder, Patch etc.) die entstehenden Punkte lassen sich verziehen, sodass man den Zylinder z.B. in die gewünschte Form bringen kann. Die Buttons in der Menüleiste <img alt="image" src="{static}radiant-preferences-hotkeys/image006.gif"/> helfen dabei, größere Haufen zu drehen</td></tr>
        <tr><td><kbd>R</kbd></td><td>aktiviert die Free<strong>R</strong>otation-Funktion; mit der kann man Brushes in jede Richtung drehen (nicht zu empfehlen, weil es dadurch zu Verzerrungen der Texturen kommt)</td></tr>
        <tr><td><kbd>J</kbd></td><td>schaltet zwischen 4 Varianten der  Brushmarkierung um:
            <ol>
                <li>rote Unterlegung + weiße Kanten (Standard und das Beste!)</li>
                <li>nur rote Unterlegung</li>
                <li>keinerlei Markierung</li>
                <li>nur weiße Kanten</li>
            </ol>
        </td></tr>
        <tr><td>Zahlen <kbd>1</kbd>-<kbd>9</kbd></td><td>verändern die Rastergröße (Grid) im 2D Fenster; <kbd>1</kbd> = kleinste, <kbd>9</kbd> = größte, <kbd>0</kbd> = Raster verschwindet</td></tr>
        <tr><td><kbd>Backspace</kbd> (Über <kbd>Enter</kbd>)</td><td>löscht selektierten Brush/Entity o.ä.</td></tr>
    </tbody>
</table>

Kommen wir zu den Tastenkombos:

(<kbd>LMT</kbd> = linke Maustaste; <kbd>MMT</kbd> = mittlere Maustaste (Rad drücken); <kbd>RMT</kbd> = rechte Maustaste)

<table class="table table-striped table-sm-nowrap-col1">
    <thead>
        <tr><th>Tasten</th><th>Effekt</th></tr>
    </thead>
    <tbody>
        <tr><td><kbd>Shift</kbd> + <kbd>LMT</kbd></td><td>            selektiert bzw. deselektiert Brushes/Entities o.ä. (nur im 3D Fenster zu empfehlen)</td></tr>
        <tr><td><kbd>Shift</kbd> + <kbd>S</kbd></td><td>                öffnet “Patch Property” – Fenster funktioniert wie der <strong>S</strong>urface Inspector, ist aber für curves und patches gedacht</td></tr>
        <tr><td><kbd>Shift</kbd> + <kbd>P</kbd></td><td>                macht aus einem neuen Brush einen <strong>P</strong>atch</td></tr>
        <tr><td><kbd>Shift</kbd> + <kbd>U</kbd></td><td>                löst die Ausschneid-Funktion aus (Subtract)</td></tr>
        <tr><td><kbd>Shift</kbd> + <kbd>B</kbd></td><td>                öffnet Surface Inspector</td></tr>
        <tr><td><kbd>Shift</kbd> + <kbd>R</kbd></td><td>                bewirkt, dass die Textur, die auf dem Brush ist, nicht mehr „fest klebt“ und bei Verschiebungen sich stete verändert</td></tr>
        <tr><td><kbd>Shift</kbd> + <kbd>T</kbd></td><td>                behebt das Problem von eben wieder</td></tr>
        <tr><td><kbd>Shift</kbd> + <kbd>C</kbd></td><td>                fügt auf Zylinder Deckel- und Grundfläche und bei Bevels bzw. End caps Seiten hinzu (Torbogen)</td></tr>
        <tr><td><kbd>Leertaste</kbd></td><td>                kopiert den derzeit selektierten Brushes/Entities o.ä. samt Textur und allen Einstellungen</td></tr>
        <tr><td><kbd>Strg</kbd> + <kbd>LMT</kbd></td><td>             verzerrt den selektierten Brush (unwichtig)</td></tr>
        <tr><td><kbd>Strg</kbd> + <kbd>K</kbd></td><td>                verbindet Entities miteinander (z.B. für: Teleporter, Türen oder Spotlights)</td></tr>
        <tr><td><kbd>Strg</kbd> + <kbd>I</kbd></td><td>                 bewirkt, dass die Textur eines Zylinders z.B., die normalerweise Außen angebracht ist, nun auf der entgegenliegenden Seite, also Innen, ist</td></tr>
        <tr><td><kbd>Strg</kbd> + <kbd>T</kbd></td><td>                Thicken-Funktion (Nein nicht das Wort mit „f“!) einfach ausprobieren! – ist gut für Rohre und son Zeugs</td></tr>
        <tr><td><kbd>Strg</kbd> + <kbd>3</kbd> - <kbd>9</kbd></td><td>              legt die Anzahl der Ecken eines Brushes fest (also 3,4,5… oder 9 Ecken; man sollte
es nicht übertreiben (32!), sondern dann lieber Zylinder nehmen!!!)</td></tr>
        <tr><td><kbd>Strg</kbd> + <kbd>Shift</kbd> + <kbd>LMT</kbd></td><td>  selektiert immer nur eine Seite eines Brushes</td></tr>
        <tr><td><kbd>Strg</kbd> + <kbd>Shift</kbd> + <kbd>Alt</kbd> + <kbd>LMT</kbd></td><td>man kann mehrere Seiten selektieren/deselektieren</td></tr>
    </tbody>
</table>

# Bewegung und Aktion im 3D Fenster

Jo da haben wir’s – das 3D Fenster das GTK Radiant

![image]({static}radiant-preferences-hotkeys/image007.jpg)

Um sich im 3D Fenster frei
bewegen zu können, klickt man mit der  RMT in das Fenster; es erscheint ein
weißes Fadenkreuz (siehe Bild).

Wir können und nun mit der
Maus frei umsehen. Wenn ihr nun noch die Pfeiltasten und das Mausrad benutzt,
könnt ihr euch eure map von jedem Winkel aus betrachten und schon im Editor
nach Fehlern suchen.

Man kann aber auch das 3D
Fenster noch zu anderen Zwecken verwenden:

<table class="table table-striped table-sm-nowrap-col1">
    <thead>
        <tr><th>Tasten</th><th>Effekt</th></tr>
    </thead>
    <tbody>
        <tr><td><kbd>MMT</kbd></td><td>            wenn man einen selektierten Brush hat und bei einen anderen, nichtselektierten Brush auf eine Seite mit der <kbd>MMT</kbd> klickt, nimmt der selektierte Brush die gleiche Textur an, die auch der nichtselektierte Brush hat (sehr praktisch und schneller, als immer die Textur aus dem Textur-Fenster herauszusuchen)</td></tr>
        <tr><td><kbd>Alt</kbd> + <kbd>LMT</kbd></td><td>     verschiebt die Textur auf dem Brush</td></tr>
        <tr><td><kbd>Strg</kbd> + <kbd>LMT</kbd></td><td>   verzerrt den selektierten Brush</td></tr>
        <tr><td><kbd>LMT</kbd></td><td>             verschiebt die selektierten Brushes in der map umher (ungenau! -nicht zu empfehlen)</td></tr>
    </tbody>
</table>

Joa, das war’s auch schon, ich hoffe ihr habt viel gelernt und Spaß dabei gehabt, alle Tastenkombos auszuprobieren und, dass eure Maps nun noch schneller fertig werden!

MfG

Darth NormaN