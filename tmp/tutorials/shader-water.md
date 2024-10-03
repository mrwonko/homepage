title: Wasser - Shader
author: Darth Arth (Artur L.)
date: 2004-01-01
modified: 2015-04-14
category: texturen
type: tutorials/darth-arth
tags: Shader, auto-generated
slug: shader-water

**>>
Mapping Academy - Tutorials <<**

 

(c)
2003 [www.darth-arth.net](http://www.darth-arth.net)

----

SHADER: Wasser

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

>>
Shader: Was sind Shader ? ( [Tutorial](shader1.htm) )<<

 

----

In
dieser Lehreinheit (Tutorial) wird erklärt, wie man einen Wasser - Shader
erstellen kann.

----

Wasser-Shader gehören zu den
sehr komplizierten und sehr komplexen Shader - Definitionen. 

Sie enthalten mehrere
Oberflächen-Parameter und verschiedene Optionen. 

Anhand von folgendem Beispiel,
versuche ich zu erklären, wie ein Wasser-Shader zusammengebaut ist:

<table border="1" bordercolor="#808080" bordercolordark="#808080" bordercolorlight="#C0C0C0" style="border-collapse: collapse; mso-border-alt: solid windowtext .5pt; mso-padding-alt: 0cm 3.5pt 0cm 3.5pt; border-style: none; border-width: medium" width="998">
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="background-color: #000000; border: .5pt solid #000000; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#FFFFFF" face="Arial" size="2">
     <b>
      Shader-Bestandteil:
     </b>
    </font>
    <span style='font-size:10.0pt;font-family:"Courier Neu"'>
     <o:p>
     </o:p>
    </span>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="background-color: #000000; border: .5pt solid #000000; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#FFFFFF" face="Arial" size="2">
    <b>
     Beschreibung:
    </b>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="border: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span style="font-size: 10.0pt">
      textures/yavin/wasser01
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="border: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#008080" face="Arial">
    <span style="font-size: 10.0pt">
     Name
      des Shaders
    </span>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span style="font-size: 10.0pt">
      {
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span style="font-size: 10.0pt">
      <span style="mso-tab-count:
  1">
      </span>
      qer_editorimage
      <span style="mso-tab-count:1">
      </span>
      textures/yavin/wasser01
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#008080" face="Arial">
    <span style="font-size: 10.0pt">
     Bild
      Im Editor
    </span>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span style="font-size: 10.0pt">
      <span style="mso-tab-count:
  1">
      </span>
      surfaceparm
      <span style="mso-tab-count:1">
      </span>
      nonsolid
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#008080" face="Arial">
    <span style="font-size: 10.0pt">
     Oberflächen-Parameter:
      macht den Brush nonsolid (damit man nicht auf dem Wasser steht)
    </span>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span style="font-size: 10.0pt">
      <span style="mso-tab-count:
  1">
      </span>
      surfaceparm
      <span style="mso-tab-count:1">
      </span>
      nonopaque
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font size="2">
    <font color="#008080" face="Arial">
     <span style="font-size: 10.0pt">
      Oberflächen-Parameter:
      Lichtdurchlässig
     </span>
    </font>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span style="font-size: 10.0pt">
      <span style="mso-tab-count:
  1">
      </span>
      surfaceparm
      <span style="mso-tab-count:1">
      </span>
      water
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font size="2">
    <font color="#008080" face="Arial">
     <span style="font-size: 10.0pt">
      Oberflächen-Parameter:
      Wasser-Brush
     </span>
    </font>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span style="font-size: 10.0pt">
      <span style="mso-tab-count:
  1">
      </span>
      surfaceparm
      <span style="mso-tab-count:1">
      </span>
      trans
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font size="2">
    <font color="#008080" face="Arial">
     <span style="font-size: 10.0pt">
      Oberflächen-Parameter:
      Durchsichtig
     </span>
    </font>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span style="font-size: 10.0pt">
      <span style="mso-tab-count:
  1">
      </span>
      qer_trans
      <span style="mso-tab-count:1">
      </span>
      0.9
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font size="2">
    <font color="#008080" face="Arial">
     <span style="font-size: 10.0pt">
      Oberflächen-Parameter:
      Stufe der Transparenz (Durchsichtigkeit 0 - 1)
     </span>
    </font>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span style="mso-tab-count: 1; font-size: 10.0pt">
     </span>
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      surfaceparm
      <span style="mso-tab-count:1">
      </span>
      fog
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font size="2">
    <font color="#008080" face="Arial">
     <span style="font-size: 10.0pt">
      Oberflächen-Parameter:
      Nebel (definier die innere Umgebung des Wassers)
     </span>
    </font>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-tab-count:1">
      </span>
      fogparms
      <span style="mso-tab-count:1">
      </span>
      ( 0.462464 0.571832 0.967132 ) 1024.0
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#008080" face="Arial" size="2">
    <span style="font-size: 10.0pt">
     Nebel-Parameter:
      ( R-Farbenanteil G-Farbenanteil B-Farbenanteil ) sichtweite
    </span>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-tab-count:1">
      </span>
      q3map_material
      <span style="mso-tab-count:1">
      </span>
      Water
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font size="2">
    <font color="#008080" face="Arial">
     <span style="font-size: 10.0pt">
      Oberflächen-Parameter:
      Wasser (Q3-Engine)
     </span>
    </font>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-tab-count:1">
      </span>
      q3map_nolightmap
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font size="2">
    <font color="#008080" face="Arial">
     <span style="font-size: 10.0pt">
      Oberflächen-Parameter:
      Empfängt keine Schatten
     </span>
    </font>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-tab-count:1">
      </span>
      q3map_onlyvertexlighting
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font size="2">
    <font color="#008080" face="Arial">
     <span style="font-size: 10.0pt">
      Oberflächen-Parameter:
      nur Vertex-Belichtung
     </span>
    </font>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-tab-count:1">
      </span>
      cull disable
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font size="2">
    <font color="#008080" face="Arial">
     <span style="font-size: 10.0pt">
      Oberflächen-Parameter:
      Beide Seiten einer Wand sind sichtbar
     </span>
    </font>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-spacerun: yes">
      </span>
      {
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-spacerun: yes">
      </span>
      <span style="mso-tab-count:
  1">
      </span>
      map textures/yavin/wasser01
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#008080" face="Arial">
    <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
     Erste
      Textur für die Wasser-Oberfläche
    </span>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-spacerun: yes">
      </span>
      <span style="mso-tab-count:
  1">
      </span>
      blendFunc GL_ONE
      GL_ONE_MINUS_SRC_ALPHA
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#008080" face="Arial">
    <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
     Blend-Funktion:
      Leichte Durchsichtigkeit
    </span>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-spacerun: yes">
      </span>
      <span style="mso-tab-count:
  1">
      </span>
      rgbGen exactVertex
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#008080" face="Arial">
    <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
     definiert
      Vertex-Belichtung (ist nicht unbedingt notwendig)
    </span>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-spacerun: yes">
      </span>
      <span style="mso-tab-count:
  1">
      </span>
      alphaGen const 0.5
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#008080" face="Arial" size="2">
    <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
     generiert
      Alpha-Channel (für Durchsichtigkeit)
    </span>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-spacerun: yes">
      </span>
      <span style="mso-tab-count:
  1">
      </span>
      tcMod turb 0 0.08 0.04
      0.08
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#008080" face="Arial" size="2">
    <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
     generiert
      Oberflächen Turbulenzen
    </span>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-spacerun: yes">
      </span>
      <span style="mso-tab-count:
  1">
      </span>
      tcMod scroll -0.05 -0.001
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#008080" face="Arial" size="2">
    <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
     generiert
      Oberflächen Bewegung X Y
    </span>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-spacerun: yes">
      </span>
      <span style="mso-tab-count:
  1">
      </span>
      tcMod scale 3 3
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#008080" face="Arial">
    <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
     skaliert
      die Textur X Y
    </span>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="mso-spacerun: yes; font-size: 10.0pt; mso-ansi-language: EN-US">
     </span>
     <span style="font-size: 10.0pt">
      }
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span style="font-size: 10.0pt">
      <span style="mso-spacerun:
  yes">
      </span>
      {
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span style="font-size: 10.0pt">
      <span style="mso-spacerun:
  yes">
      </span>
      <span style="mso-tab-count:1">
      </span>
      map textures/yavin/wasser01
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#008080" face="Arial" size="2">
    <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
     Zweite
      Textur für die Wasser-Oberfläche (ist nicht notwendig, sieht aber besser
      aus :D )
    </span>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span style="font-size: 10.0pt">
      <span style="mso-spacerun:
  yes">
      </span>
      <span style="mso-tab-count:1">
      </span>
     </span>
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      blendFunc
      <span style="mso-spacerun: yes">
      </span>
      GL_DST_COLOR GL_ONE
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#008080" face="Arial" size="2">
    <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
     Blend-Funktion:
      stärkere Durchsichtigkeit
    </span>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-spacerun: yes">
      </span>
      <span style="mso-tab-count:
  1">
      </span>
      alphaGen const 0.5
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#008080" face="Arial" size="2">
    <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
     generiert
      Alpha-Channel (für Durchsichtigkeit)
    </span>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-spacerun: yes">
      </span>
      <span style="mso-tab-count:
  1">
      </span>
      tcMod turb 0 0.08 0.04
      0.08
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#008080" face="Arial" size="2">
    <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
     generiert
      Oberflächen Turbulenzen
    </span>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-spacerun: yes">
      </span>
      <span style="mso-tab-count:
  1">
      </span>
      tcMod scroll 0.05 0.001
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#008080" face="Arial" size="2">
    <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
     generiert
      Oberflächen Bewegung X Y
    </span>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-spacerun: yes">
      </span>
      <span style="mso-tab-count:
  1">
      </span>
      tcMod scale 3 3
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
   <font color="#008080" face="Arial" size="2">
    <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
     skaliert
      die Textur X Y
    </span>
   </font>
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      <span style="mso-spacerun: yes">
      </span>
      }
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
  </td>
 </tr>
 <tr>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="559">
   <p class="MsoNormal" style="mso-layout-grid-align:none;text-autospace:none">
    <font color="#00FF00" face="Arial">
     <span lang="EN-US" style="font-size: 10.0pt; mso-ansi-language: EN-US">
      }
      <o:p>
      </o:p>
     </span>
    </font>
   </p>
  </td>
  <td bordercolordark="#808080" bordercolorlight="#C0C0C0" style="mso-border-top-alt: solid windowtext .5pt; border-left: .5pt solid windowtext; border-right: .5pt solid windowtext; border-top-style: none; border-top-width: medium; border-bottom: .5pt solid windowtext; padding-left: 3.5pt; padding-right: 3.5pt; padding-top: 0cm; padding-bottom: 0cm" valign="top" width="822">
  </td>
 </tr>
</table>

 

Ich
habe auf diese Weise, mit Hilfe von 4 neuen Texturen, 4 neue Wasser Shader
gebastelt. 

Wobei
diese verschiedene Eigenschaften besitzen, vor allem was die Farbe und Durchsichtigkeit
betrifft:

 

![image]({static}water/wasser01.jpg)

 

textures/yavin/wasser01

{

   
qer_editorimage textures/yavin/wasser01

   
surfaceparm nonsolid

   
surfaceparm nonopaque

   
surfaceparm water

   
surfaceparm trans

   
qer_trans 0.9

   
surfaceparm fog

   
fogparms ( 0.462464 0.571832
0.967132 ) 1024.0

   
q3map_material Water

   
q3map_nolightmap

   
q3map_onlyvertexlighting

   
cull disable

       
{

       
map textures/yavin/wasser01

       
blendFunc GL_ONE GL_ONE_MINUS_SRC_ALPHA

       
rgbGen exactVertex

       
alphaGen const 0.5

       
tcMod turb 0 0.08 0.04 0.08

       
tcMod scroll -0.05 -0.001

       
tcMod scale 3 3

       
}

       
{

       
map textures/yavin/wasser01

       
blendFunc GL_DST_COLOR GL_ONE

       
alphaGen const 0.5

       
tcMod turb 0 0.08 0.04 0.08

       
tcMod scroll 0.05 0.001

       
tcMod scale 3 3

       
}

}

 

----

Hier
habe ich die Farbe des "Wasser-Nebels",  ein wenig an die Textur
angepasst und die Unterwasser-Sichtweite geändert:

 

![image]({static}water/wasser02.jpg)

 

textures/yavin/wasser02

{

   
qer_editorimage textures/yavin/wasser02

   
surfaceparm nonsolid

   
surfaceparm nonopaque

   
surfaceparm water

   
surfaceparm trans

   
qer_trans 0.9

   
surfaceparm fog

   
fogparms ( 0.294506 0.474182
0.990098 ) 512.0

   
q3map_material Water

   
q3map_nolightmap

   
q3map_onlyvertexlighting

   
cull disable

       
{

       
map textures/yavin/wasser02

       
blendFunc GL_ONE GL_ONE_MINUS_SRC_ALPHA

       
rgbGen exactVertex

       
alphaGen const 0.5

       
tcMod turb 0 0.08 0.04 0.08

       
tcMod scroll -0.05 -0.001

       
tcMod scale 3 3

       
}

       
{

       
map textures/yavin/wasser02

       
blendFunc GL_DST_COLOR GL_ONE

       
alphaGen const 0.5

       
tcMod turb 0 0.08 0.04 0.08

       
tcMod scroll 0.05 0.001

       
tcMod scale 3 3

       
}

}

 

----

Hier
habe ich auch die Farbe des "Wasser-Nebels" an die Textur angepasst
und die Unterwasser-Sichtweite geändert:

 

![image]({static}water/wasser03.jpg)

 

textures/yavin/wasser03

{

   
qer_editorimage textures/yavin/wasser03

   
surfaceparm nonsolid

   
surfaceparm nonopaque

   
surfaceparm water

   
surfaceparm trans

   
qer_trans 0.9

   
surfaceparm fog

   
fogparms ( 0.347634 0.773388
0.933534 ) 256.0

   
q3map_material Water

   
q3map_nolightmap

   
q3map_onlyvertexlighting

   
cull disable

       
{

       
map textures/yavin/wasser03

       
blendFunc GL_ONE GL_ONE_MINUS_SRC_ALPHA

       
rgbGen exactVertex

       
alphaGen const 0.5

       
tcMod turb 0 0.08 0.04 0.08

       
tcMod scroll -0.05 -0.001

       
tcMod scale 3 3

       
}

       
{

       
map textures/yavin/wasser03

       
blendFunc GL_DST_COLOR GL_ONE

       
alphaGen const 0.5

       
tcMod turb 0 0.08 0.04 0.08

       
tcMod scroll 0.05 0.001

       
tcMod scale 3 3

       
}

}

----

Und
hier noch mal ein paar kleine Änderungen an der Farbe und der Sichtweite

 

![image]({static}water/wasser04.jpg)

 

textures/yavin/wasser04

{

   
qer_editorimage textures/yavin/wasser04

   
surfaceparm nonsolid

   
surfaceparm nonopaque

   
surfaceparm water

   
surfaceparm trans

   
qer_trans 0.9

   
surfaceparm fog

   
fogparms ( 0.264814 0.366370
0.757764 ) 512.0

   
q3map_material Water

   
q3map_nolightmap

   
q3map_onlyvertexlighting

   
cull disable

       
{

       
map textures/yavin/wasser04

       
blendFunc GL_ONE GL_ONE_MINUS_SRC_ALPHA

       
rgbGen exactVertex

       
alphaGen const 0.5

       
tcMod turb 0 0.08 0.04 0.08

       
tcMod scroll -0.05 -0.001

       
tcMod scale 3 3

       
}

       
{

       
map textures/yavin/wasser04

       
blendFunc GL_DST_COLOR GL_ONE

       
alphaGen const 0.5

       
tcMod turb 0 0.08 0.04 0.08

       
tcMod scroll 0.05 0.001

       
tcMod scale 3 3

       
}

}

----

Den
Shader habe ich unter base/shaders
mit dem Namen "mywater.shader"
abgespeichert.

 

Damit,
die selbst erstellten Shader im Editor angezeigt werden, müssen diese in der
Shader-Liste eingetragen werden. 

Suche
in dem base/shaders
Ordner nach der Datei "shaderlist.txt".
Öffne sie mit dem Notepad und füge am Schluss den Namen unseres neuen Shaders mywater
ein.

 

(**WICHTIG!**:
ohne Datei-Erweiteung, nur den Namen eintragen!)

 

Speichere
dann die Shader-Liste. 

 

Jetzt
kannst du den Editor starten und die neuen Wasser-Shader ( "wasser01
- 04" ) unter Textures
> "yavin"
finden.

 

 

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

![image]({static}water/water_test.jpg)

 

Im
Anschluss an dieses Tutorial, findest du die neuen Shader zum Download. Folgende
Dateien sind in dem ZIP-Achiv "my_water.zip"
enthalten:

 

mywater.pk3
= pk3-Datei mit der Shader-Datei und den 4 neuen Texturen für MP - Modus (muss
in den base -
Ordner kopiert werden)

water_test.bsp
= Test-Map für unseren neuen Lava Shader (in den base/maps
Ordner kopieren)

water_test.map
= Test-Map Quellcode (in den base/maps
Ordner kopieren)

mywater.shader
= Shader-Datei, die in den base/shaders
- Ordner kopiert werden muss ( nicht vergessen, den Namen in die shaderlist.txt
einzutragen! )

 

----

[u][DOWNLOAD
DER TUTORIAL MAP](../downloads/my_water.zip)[/u]

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

