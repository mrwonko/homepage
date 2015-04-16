title: Richtlinien für Texturen
date: 2008-01-25
type: tutorials/darth-arth
author: mrwonko
category: texturen
tags: Textur
modified: 2015-04-12
slug: textures-richtlinien

Da das Thema im Forum immer wieder auftaucht, hier einige Dinge, die man beim Erstellen neuer Texturen beachten sollte.

# Größe

Die Textur muss als Höhe und Breite Zweierpotenzen haben.

Zweierpotenz bedeutet z.B.

*   `2*2 = 4`
*   `2*2*2 = 8`
*   `2*2*2*2*2*2*2*2 = 256`

d.h. als Größe z.B. 256 Pixel mal 512 Pixel.

Die meisten Texturen in Jedi Knight habe eine Größe von `512*512`, kleinere wie Lampen auch mal `128*128` und große auch mal `1024*1024` - größer wird es aber nicht.

# Format

Möglich sind:

*   **JPG**
    
    klein, aber ohne Alphakanal (d.h. Informationen über Transparenz) - beim Speichern nicht progressiv einstellen. (Progressiv das ist eine spezielle Art von JPG, mit der Jedi Knight nicht umgehen kann, und wenn ihr die beim Speichern nicht auswählen könnt, sollte sie aus sein)

*   **TGA**
    
    unkomprimiert, also groß, hat aber einen Alphakanal, also Format der Wahl für Dinge wie Gitter

*   **PNG**
    
    wie TGA, nur Komprimiert, also klein, macht aber soweit ich weiß Probleme mit Lightmaps(=Beleuchtung) bei Transparenz - also gut für Sachen wie Menüs, die ja nicht beleuchtet werden

# die Textur ins Spiel bekommen

Bei normalen Texturen ohne irgendwelche speziellen Eigenschaften wie Transparenz kommt man ohne Shader aus - dann muss man die Textur einfach nur in <code><em>Jedi Knight Verzeichnis</em>/GameData/Base/Textures/<em>ordner</em>/</code> speichern.

<div class="alert alert-warning"><strong>Achtung</strong>: Weder der Texturname noch der Ordnername dürfen Leerzeichen enthalten.</div>

Dann den Radiant starten, bei Bedarf unter `Textures` das Häkchen bei <code>Shaderlist.txt only</code> ausmachen und die Textur laden.

<div class="alert alert-info">Im Allgemeinen sollte <code>shaderlist.txt only</code> jedoch aktiviert sein, damit keine Texturen aus fremden Maps angezeigt werden.</div>

Wenn ihr noch spezielle Dinge wie Transparenz oder bewegte Texturen haben wollt, braucht ihr einen Shader - siehe entsprechende Tutorials.
