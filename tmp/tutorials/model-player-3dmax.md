title: Eigene Player-Modele erstellen
author: Charmin (Oliver J.) Deluxe
date: 2004-01-01
modified: 2015-04-14
category: models
type: tutorials/darth-arth
tags: Modelling, 3DS Max, auto-generated
slug: model-player-3dmax

**>>
Mapping Academy - Tutorials <<**

 

(c)
2003 [www.darth-arth.net](http://www.darth-arth.net)

----

**Player
Modelling-Tutorial für Jedi Knight 2 by Charmin Deluxe**

----

[color=windowtext]

[/color]
**Voraussetzungen für die Nutzung
dieses Tutorials:**

- Ihr habt das Tutorial auf **[Gargamel.de](http://www.gargamel.de)** schon gemacht!

- Ihr habt **Dateinamenerweiterung an** (falls du die Dateinamenendungen
nicht siehst, geh auf Systemsteuerung -> Ordneroptionen -> Ansicht ->
das Häckchen bei **"Dateinamenerweiterungen bei bekannten Dateitypen
ausblenden" entfernen -> OK** (s. **[Skinning-Tutorial](skinning_tut.htm)**)).[color=windowtext][/color]

**1. Material**[color=windowtext]

[/color]

- **[Milkshape](http://www.swissquake.ch/chumbalum-soft/ms3d/download.html)**[color=windowtext]

[/color]
- [**3D Studio Max 4.X**](http://www.discreet.com/products/3dsmax/)[color=windowtext][/color]

- **[JK2 Editing-Tools 1&2](http://plasmaskins.jediknightii.net/files/resources/programs.html)**

- **[Lith Unwrap](downloads/LithUnwrap.zip)**

- **[Paintshop Pro](http://www.jasc.com/download_4.asp?)** oder ein anderes
Bildbearbeitungsprogramm

- **[WinZIP](http://www.winzip.com/ddchomea.htm)** und **[WinRAR](http://www.winrar.de/)**

- **[Jedi Knight 2 Modelskelett](downloads/Jedi-Knight2-Modelskelett.zip)**

- **[MD3 Import Skript für 3D Studio
Max 4.X](downloads/MD3-Import-Skript_fuer_3D_Studio_Max_4.X.zip)**

-
Textbearbeitungsprogramm

 

**2.
Vorbereitung**

- Leg in
**C:** einen Ordner namens **base** an (**[color=red]Dieser Pfad wird später noch wichtig![/color]**).

-
Extrahier die **q3-md3.ms **in den **scripts **Ordner eures **3D Studio
Max **Hauptverzeichnisses.

-
Installier die **JK2 Editing-Tools 1 & 2** in **C:/base/**.

- Dann öffnest du im deinem **Gamedata/Base** Ordner die **assets0.pk3**
mit **WinRAR**.

- Dann entpackst (**[color=red]nicht rauslöschen![/color]**) du den Ordner **models/players** und
**shaders **nach **C:/base/**.

![image]({filename}./player_modelling_tut-Dateien/image001.jpg)

**3.**[color=windowtext] [/color] ** Das Model
modellen**

-
Startet **Milkshape**

- Geht
auf **File -> Import -> Ghoul2 Model GLM... **und importiert z.B. die **model.glm**
von **Kyle** (sie befindet sich in **C:/base/models/players/kyle/model.glm**)

![image]({filename}./player_modelling_tut-Dateien/image002.jpg)

- Dann
erscheint ein Fenster. Macht in diesem einfach überall ein Häckchen.

![image]({filename}./player_modelling_tut-Dateien/image003.jpg)

- Jetzt
seht ihr Kyle's Grundmodel.

![image]({filename}./player_modelling_tut-Dateien/image004.jpg)

- Ihr
macht jetzt folgendes: löscht alles was mit einem *** **beginnt und löscht **stupidtriangle_off**.
Danach könnt ihr beginnen euer Model um das von Kyle herumzubauen (um euer
Model besser zu sehen, könnt ihr die einzelnden Körperteile mit **Strg+h **verstecken.
Lasst die, die ein **cap** im Namen haben lieber sichtbar. da ihr Eure
Körperteile nach diesen **caps** richten müsst!)

![image]({filename}./player_modelling_tut-Dateien/image005.jpg)

- Wenn
euer Model dann soweit fertig ist könnt ihr die Körperteile des alten Models
löschen. Dann müsst ihr eure einzelnen **Boxen**, **Duplicates**, **Cylinder**,
etc. nur noch in die richtigen Körperteile umbenennen. Ich hab ein
Standardmodel gemacht. Die bestehen aus 9 Teilen. Ihr könnt natürlich auch noch
mehr Teile machen, nur reicht fürn Anfang das :P.

![image]({filename}./player_modelling_tut-Dateien/image006.jpg)

- Als
letzten wichtigen Schritt müsst ihr die **caps** noch eurem Model anpassen.
Dazu selektiert ihr einfach eins der Teile die ein **cap** im Namen haben. **Caps
**sind die Stellen an denen das Model mit dem Lichtschwert zertrennt wird.
Wie ihr dem Bild oben entnehmen könnt gibt es verschiedene Körperteile. Die **caps
**sitzen zwischen diesen Teilen (zwischen **torso **und **r_arm **sitzen
z.B. die beiden **caps torso_cap_r_arm_off **und **r_arm_cap_torso_off**).Also
ihr müsst eure Körperteile also **cappen**, dass wenn jemand euch z.B. die
linke Hand abhaut man von oben nicht in den Arm bzw. Hand reinguggen kann. **Die
Caps MÜSSEN an der selben Stelle sein wie sie beim alten Model waren! Sie
dürfen nur gaaanz wenig abweichen!**

-
Nachdem ihr euer Model soweit fertig habt, müsstet ihr jetzt in der **Groups**
Liste folgende Sachen finden:

**head**[color=windowtext][/color]

**torso**[color=windowtext][/color]

**r_arm**[color=windowtext][/color]

**l_arm**[color=windowtext][/color]

**r_hand**[color=windowtext][/color]

**l_hand**[color=windowtext][/color]

**hips**[color=windowtext][/color]

**r_legs**[color=windowtext][/color]

**l_legs**[color=windowtext][/color]

**head_cap_torso_off**[color=windowtext][/color]

**torso_cap_head_off**[color=windowtext][/color]

**r_arm_cap_torso_off**[color=windowtext][/color]

**torso_cap_r_arm_off**[color=windowtext][/color]

**l_arm_cap_torso_off**[color=windowtext][/color]

**torso_cap_l_arm_off**[color=windowtext][/color]

**r_hand_cap_r_arm_off**[color=windowtext][/color]

**r_arm_cap_r_hand_off**[color=windowtext][/color]

**l_hand_cap_l_arm_off**[color=windowtext][/color]

**l_arm_cap_l_hand_off**[color=windowtext][/color]

**hips_cap_torso_off**[color=windowtext][/color]

**torso_cap_hips_off**[color=windowtext][/color]

**hips_cap_r_leg_off**[color=windowtext][/color]

**r_leg_cap_hips_off**[color=windowtext][/color]

**hips_cap_l_leg_off**[color=windowtext][/color]

**l_leg_cap_hips_off**[color=windowtext][/color]

![image]({filename}./player_modelling_tut-Dateien/image007.jpg)

- Zum
Schluss verpasst ihr eurem Model noch die Texturen. Im Moment spielt es keine
Rolle was auf dieser Textur drauf is! Es ist nur wichtig das diese Texturen
sich in **C:/base/models/players/MeinErstesModel/** befindet und das es **tga**-Dateien
sind.

![image]({filename}./player_modelling_tut-Dateien/image008.jpg)

- Nun
legt ihr in euren **C:/base/models/players/ **Ordner einen Ordner mit dem
Namen **MeinErstesModel** an. Speichert in diesen Ordner euer Model als **model.ms3d**.

**4.
UV-Mapping**

- Wie
man Modelle texturiert ist auf **[Gargamel.de](http://www.gargamel.de)** schon
beschrieben. Doch bei komplexeren Saberhilts brauch man **Lith Unwrap**.
Leider gibt es jetzt nur noch **Ultimate Unwrap** und die Demo davon ist
nutzlos. Ich konnte aber glücklicherweise noch irgendwo ein altes **Lith
Unwrap** auftreiben, das auch das ms3d-Format unterstützt.

-
Startet **Lith Unwrap**

- Geht
auf **File -> Model -> Open** und öffnet eure gespeicherte **model.ms3d**

- Nun müsste es so oder so ähnlich aussehen:

![image]({filename}./player_modelling_tut-Dateien/image009.jpg)

- Wählt
jetzt rechts unter **Materials **oder **Groups **euer einzelnden Texturen
mit den zugewiesenen Körperteilen oder die Körperteile einzelnd aus. Drückt **Strg+a
**um alle **Faces **zu makieren. Wenn ihr Jetzt auf **Tools -> UV
mapping **klickt, seht ihr da verschieden Arten euer Model zu **UV-mappen**.
Probiert einfach rum was euch am Besten gefällt (z.B. **Tools -> UV mapping
-> Planar**).

![image]({filename}./player_modelling_tut-Dateien/image010.jpg)

- Wenn
ihr alles **UV-mappt **habt, siehst ungefähr so aus.

![image]({filename}./player_modelling_tut-Dateien/image011.jpg)

- Jetzt
müsst ihr nur die einzelnen Texturen neu speichern. Das tut ihr, indem ihr
rechts unter **Materials **immer auf eins der Texturen klickt und dann unter
**File -> UV Map **die Textur als **tga **abspeichert. **Achtet
darauf, dass die Auflösung immer aus diesen Zahlen besteht: 64, 128, 256, 512,
1024. Also eure Auflösung darf 256x256 oda 64x512 usw. sein, aber nich 83x145
oder so!** Orientiert euch bei der Auflösunge für die einzelnden Texturen der
Körperteile nach den Standard Modellen (z.B. is die Standardauflösung für die
Kopftextur 512x512 und für die Torsotextur 1024x512. Es ist natürlich euch
überlassen).

- Danach
müsst ihr euer Model auch nochmal abspeichern. Geht dafür auf **File ->
Model -> Save** und speichert es als eure **model.ms3d** ab.

- Danach könnt ihr **Lith Unwrap**  schließen.

-
Startet **Milkshape**

- Öffnet eure **model.ms3d**

- Wenn ihr jetzt im 3D-Fenster rechtsklickt und dann auf **Textured** geht,
seht ihr euer Model mit Textur.

![image]({filename}./player_modelling_tut-Dateien/image012.jpg)

**5.
Euer Model nach 3D Studio Max exportieren**

- Dazu
müsst ihr euer Model als md3 exportieren. Um das zu können müssen wir erstmal
eine **qc**-Datei schreiben. Klickt dafür auf **Tools -> Quake III Arena
-> Generate Control File ...**. Speichert diese Datei in eurem **models/players/meinerstesmodel
**Ordner als **model.qc **ab.

![image]({filename}./player_modelling_tut-Dateien/image013.jpg)

- Jetzt
öffnet sich ein Fenster.

![image]({filename}./player_modelling_tut-Dateien/image014.jpg)

-
Schreibt diese um, das sie ungefähr so aussieht (**achtet dabei auf die
Texturen-Pfade und das ihr oben bei frames die 30 durch 1 ersetzt**):

![image]({filename}./player_modelling_tut-Dateien/image015.jpg)

- Nach
dem Speichern könnt ihr euer Model nun als **md3 **exportieren. Dazu klickt
ihr auf **File -> Export -> Quake III Arena MD3** und speichert es als
**model.md3** in eure **models/players/meinerstesmodel/ **Ordner ab.

![image]({filename}./player_modelling_tut-Dateien/image016.jpg)

- Wenn
ihr wollt könnt ihr jetzt schon eure Texturen z.B. mit **Paintshop Pro **bearbeiten.
Ihr könnt es aber auch ganz zum Schluss machen.

![image]({filename}./player_modelling_tut-Dateien/image017.jpg)

- Wenn
ihr wollt könnt ihr euer Model** **mit **MD3View** (**MD3View** findet
ihr nach dem Installieren der **JK2 Editing-Tools** in eurem **Gamedata/Tools**
Ordner. Einfach starten und über **File -> Open** euer **model.md3**
öffnen) öffnen und betrachten wie die Texturen sitzen.

![image]({filename}./player_modelling_tut-Dateien/image018.jpg)

- Jetzt
startet **3D Studio Max** und öffnet mein **modelskelett.max**. Das
Besondere an diesem Skelett ist, das schon sämtliche **bolts **geweightet
sind (ihr werdet mit später dankbar sein :P ).

![image]({filename}./player_modelling_tut-Dateien/image019.jpg)

- Nun
müsst ihr dieses Skelett aber erstmal verstecken. Dazu rechtsklickt in eins der
Fenster und klickt auf **Hide unselected**.

- Als
Nächstes aktiviert ihr das **MD3 Import Skript**. Dazu klickt ihr auf den
Hammer und dann auf **MAXScript**. Dann klickt ihr auf **Run Script** und
öffnet die in eurem **scripts** Ordner befindliche **q3-md3.ms** Datei.
Jetzt klickt ihr unten nur unter Utilities auf** Quake3 MD3 Import**.

![image]({filename}./player_modelling_tut-Dateien/image020.jpg)

- Dann
könnt ihr da weiter runterscrollen. Da klickt ihr auf **Import MD3** und
öffnet unsere **model.md3**-Datei.

![image]({filename}./player_modelling_tut-Dateien/image021.jpg)

- Nach
dem Öffnen seht ihr da euer Model. Nachdem ihr es komplett makiert habt könnt
ihr jetzt das Skelett wieder sichtbar machen. Rechtsklickt und geht auf **Unhide
all**. Wie ihr feststellen werdet ist euer Model nicht in der richtigen
Postion. Dreht es und vergrößert es einfach bis es auf das Skelett passt (**Rechtsklick
-> Scale **und **Rotate**). Wenn alles passt, speichert euer Model in
eurem **models/players/meinerstesmodel/ **Ordner als **model.max **ab.

![image]({filename}./player_modelling_tut-Dateien/image022.jpg)

 

**6.
Das Weighten**

- Als
Nächstes müssen wir die einzelnden Körperteile und **caps** ans Skelett
binden (**weighten**). Das ist sehr wichtig, da das dem Game sagt, welches
Körperteil sich mit welchem **Bone **bewegt. Um eure Körperteile zu **weighten**,
macht ihr folgendes: Nehmen wir mal als Beispiel **head**. Um euren Kopf zu
selektieren drückt **h** und such ihn aus der Liste oder makiert ihn manuell
in einem der 3 Fenster. Wenn ihr ihn makiert habt klickt rechts auf das
Röhrensymbol. Eine Liste erscheint. Klickt dort auf **Skin**.

![image]({filename}./player_modelling_tut-Dateien/image023.jpg)

- Jetzt
klickt ihr auf **Envelope**. Dort klickt ihr unten auf **Add Bone**. Für
den Kopf brauchen wir den **cervical **und **cranium Bone**.

![image]({filename}./player_modelling_tut-Dateien/image024.jpg)

- Nun
wählt ihr rechts unten einen der **Bones **aus. Wenn ihr jetzt näher in
eines der Fenster reinzoomt könnt ihr an den Enden der **Bones **einen
kleinen braunen oder rosa Kasten sehen. Klickt diese an und zieht an denen bis
sich ein Halbkreis am Ende des **Bones** bildet und sämtliche **Vertics**
gelb bis rot makiert. Wenn ihr einem Körperteile mehrere **Bones **zuweist,
könnt ihr die **Vertics** natürlich auch aufteilen. Beim Kopf z.B. kann der
obere Teil des Kopfes der **Cervical Bone **übernehmen und den unteren Teil
der **Cranium Bone**.

![image]({filename}./player_modelling_tut-Dateien/image025.jpg)

- Das
Selbe müst ihr mit den restliche Körperteilen und **caps** auch tun. **Weightet**
sie einfach zu einem passenden **Bone **unten aus dem Bild.

![image]({filename}./player_modelling_tut-Dateien/image026.jpg)

- Wenn
ihr glaubt mit dem Weighting fertig zu sein, speichert euer Model ab.

 

**7.
Assimilieren**

**- **Ihr seid zwar
noch nicht ganz fertig, aber wir machen jetzt schon ein Assimilate-Test. Dazu
müsst ihr euer Model erstmal als **XSI**-Datei speichern. Klickt dafür auf **File
-> Export -> **und wählt als Dateityp **XSI 3.0 (*XSI) **aus und
speichert euer Model in **models/players/meinerstesmodel **als **root.xsi **ab.

![image]({filename}./player_modelling_tut-Dateien/image027.jpg)

- Es
erscheint ein Fenster. Stellt einfach folgendes ein:

![image]({filename}./player_modelling_tut-Dateien/image028.jpg)

- Für
den nächsten Schritt müsst ihr ein bisschen an den Ländereinstellungen
rumändern. Öffnet die **Ländereinstellungen **über **Systemsteuerung/Ländereinstellungen**
und stellt folgendes ein:

![image]({filename}./player_modelling_tut-Dateien/image029.jpg)

![image]({filename}./player_modelling_tut-Dateien/image030.jpg)

- Nach
dem Neustart müssen wir eine **model.car**-Datei schreiben. Dazu macht eine
neue **txt**-Datei und schreibt folgendes rein und benennt sie dann vom **model.txt
**in **model.car **um. Die **model.car **muss sich in eurem **models/players/meinerstesmodel/
**Ordner befinden.

![image]({filename}./player_modelling_tut-Dateien/image031.jpg)

- Jetzt
startet **Assimilate **(**Assimilate **befindet sich auch dort wo sich **MD3View**
befindet. Beim ersten mal müsst ihr noch die Pfade angeben. Stellt folgendes
ein:

![image]({filename}./player_modelling_tut-Dateien/image032.jpg)

- Wenn
ihr alles eingestellt habt, klickt auf **File -> Open **und öffnet eure **model.car-**Datei.
Dann drückt auf **B**. Jetzt öffnet sich ein Dos-Fenster. Wenn ihr beim **Weighten**
was übersehen habt, wird euch das gesagt und ihr müsst das korrigieren:

![image]({filename}./player_modelling_tut-Dateien/image033.jpg)

- Seit
ihr aber mit dem **Weighten **fertig, kommt das und ihr seid bereit für den
nächsten Schritt:

![image]({filename}./player_modelling_tut-Dateien/image034.jpg)

 

**8.
Das Verlinken**

- Nun
müssen wir die Körperteile nur noch richtig **verlinken**. Zuerst speichert
ihr aber eure **geweightete **Version eure Models als **model_nolink.max **ab
(warum erfahrt ihr später).

- Das **Verlinken
**ist nach dem **Weighten **das Wichtigste. Um eure Körperteile richtig
miteinander zu verlinken macht ihr folgendes: Wir nehmen als Beispiel **l_leg**.
Selektiert dafür zunächst folgende Teile per **h-Methode**:

**bolt_l_leg_calf
**

**bolt_l_leg_cap_hips
**

**bolt_l_leg_foot
**

**l_leg_cap_hips_off** 

![image]({filename}./player_modelling_tut-Dateien/image035.jpg)

- Nun
klickt ihr auf das 3. Symbol von links in der Menüleiste und drückt wieder **h**.
Nun makiert **l_leg** und klickt unten auf **Link**. Klickt danach wieder
in der Menüleiste auf den normalen Mauszeiger.

![image]({filename}./player_modelling_tut-Dateien/image036.jpg)

- So
fahrt ihr mit folgenden Körperteilen in der Reihenfolge wie ich sie aufliste
auch fort (wenn ihr mehr Körperteile verwendet als ich in diesem Tutorial
verwende, müsst ihr diese ebenfalls verlinken. Wenn ihr z.B. noch Augen und
Gesicht extra habt müsst ihr die zu **head**  linken):

**bolt_l_leg_calf
**

**bolt_l_leg_cap_hips
**

**bolt_l_leg_foot
**

**l_leg_cap_hips_off** 

werden zu **l_leg **gelinkt.

**bolt_r_leg_calf
**

**bolt_r_leg_cap_hips
**

**bolt_r_leg_foot
**

**r_leg_cap_hips_off** 

werden zu **r_leg **gelinkt.

**bolt_head_cap_torso
**

**bolt_head_eyes
**

**bolt_head_front
**

**bolt_head_left
**

**bolt_head_right
**

**bolt_head_top
**

**head_cap_torso_off**

 

werden zu **head** gelinkt.

 

**bolt_l_hand
**

**bolt_l_hand_cap_l_arm
**

**l_hand_cap_arm_off** 

werden zu **l_hand **gelinkt.

**bolt_r_hand
**

**bolt_r_hand_cap_r_arm
**

**r_hand_cap_r_arm_off** 

werden zu **r_hand **gelinkt.

**bolt_l_arm_cap_hand
**

**bolt_l_arm_cap_torso
**

**bolt_l_arm_elbow
**

**l_arm_cap_l_hand_off
**

**l_arm_cap_torso_off
**

**l_hand** 

werden zu **l_arm** 
gelinkt.

**bolt_r_arm_cap_r_hand
**

**bolt_r_arm_cap_torso
**

**bolt_r_arm_elbow
**

**r_arm_cap_r_hand_off
**

**r_arm_cap_torso_off
**

**r_hand** 

werden zu **r_arm **gelinkt.

**bolt_back
**

**bolt_chestg
**

**bolt_hip_bl
**

**bolt_hip_br
**

**bolt_hip_fl
**

**bolt_hip_fr
**

**bolt_hip_l
**

**bolt_hip_r
**

**bolt_lchest_l **

**bolt_lchest_r **

**bolt_shldr_l
**

**bolt_shldr_r
**

**bolt_torso_cap_head
**

**bolt_torso_cap_hips
**

**bolt_torso_cap_l_arm
**

**bolt_torso_cap_r_arm
**

**bolt_uchest_l
**

**bolt_uchest_r
**

**torso_cap_head_off
**

**torso_cap_hips_off
**

**torso_cap_l_arm_off
**

**torso_cap_r_arm_off
**

**head
**

**l_arm
**

**r_arm**

werden zu **torso** 
gelinkt.

**bolt_hips_cap_l_leg
**

**bolt_hips_cap_r_leg
**

**bolt_hips_cap_torso
**

**bolt_l_leg_knee
**

**bolt_r_leg_knee
**

**hips_cap_l_leg_off
**

**hips_cap_r_leg_off
**

**hips_cap_torso_off
**

**torso
**

**l_leg
**

**r_leg** 

werden zu **hips **gelinkt.

**hips**

wird zu **stupidtriangle_off **gelinkt.

**stupidtriangle_off**

wird zu **mesh_root** 
gelinkt.

**mesh_root**

wird zu **model_root** 
gelinkt.

- Wenn ihr fertig seid speichert es als **model.max
**ab.

- Jetzt könnt ihr wieder assimilieren. Wenn
folgendes erscheint, habt ihr was beim Verlinken vergessen. Er zählt sie euch
aber auf, so dass ihr wisst welche ihr diesmal mit verlinken müsst. Wenn ihr
welche vergessen habt öffnet eure **model_nolink.max **und verlinkt nochmal
alles neu.

![image]({filename}./player_modelling_tut-Dateien/image037.jpg)

- Wenn
diese Nachricht kommt, könnt ihr schonmal froh sein, da ihr jetzt das Größte
überstanden habt.

![image]({filename}./player_modelling_tut-Dateien/image038.jpg)

 

**9.
Das Model ins Spiel kriegen**

-
Zunächst müsst ihr jetzt ersmal eine **model_default.skin**-Datei schreiben.
Dazu erstellt eine **txt**-Datei. In einer **skin**-Datei stehen die
Pfade zu euren Texturen. Schreibt sie einfach wie unten im Bild sichtbar.
Speichert es als **model_default.txt** ab und benennt sie dann in **model_default.skin**
um. 

![image]({filename}./player_modelling_tut-Dateien/image039.jpg)

-
Außerdem erstellt ihr noch eine **icon_default.jpg**-Datei. Sie muss 256x256
Pixel groß sein. Das ist das Bild, welches ihr nachher in der Skin-Liste
anwählen könnt.

- Ihr
müsst noch von irgendeinem anderem Standardmodel aus eurem **model/players/ **Ordner
die **sounds.cfg **klauen. Z.b vom **Jedi**.

- Zum
Schluss wandelt ihr noch alle **tga**'s in **jpg**'s um, da **tga**'s
zu viel Speicher verbrauchen und wer will schon nen 10 MB Model runterladen o.O
(außer die DSL-User unter euch :D )

- Nun
habt ihr in eurem Ordner jede Menge Dateien:

![image]({filename}./player_modelling_tut-Dateien/image040.jpg)

- Ihr
könnt jetzt folgende Dateien löschen: **model.car**, **model.max**,**
model.md3**,** model.ms3d**,** model.qc** und** root.xsi**.

- Wenn
ihr wollt, könnt ihr euer Model nun mit **ModView** (**ModView **befindet
sich auch da, wo sich **MD3View **und **Assimilate** befinden) betrachten
( Einfach eure **model.glm **über **File -> Open **öffnen und auf das
Play-Zeichen drücken).

![image]({filename}./player_modelling_tut-Dateien/image041.jpg)

- Euer
Model muss jetzt nur noch als **pk3** verpackt werden. Kopiert dazu euren **meinerstesmodel**
Ordner. Jetzt erstellt ihr irgendwo einen Ordner namens **models**. In
diesem erstellt ihr einen Ordner namens **players**. In diesen Ordner
kopiert ihr euren **meinerstesmodel**  Ordner.

- Jetzt
erstelle mit **WinZip** eine **ZIP**-Datei. Wir nennen sie bei uns mal **MeinErstesModel.ZIP**.
Jetzt zippst du unseren **models** Ordner mit dem Model drin in diese Datei.

![image]({filename}./player_modelling_tut-Dateien/image042.jpg)

Danach
benenne sie von **MeinErstesModel.ZIP** in **MeinErstesModel.pk3** um (**[color=red]normalerweise kommt dann
eine Fehlermeldung. Einfach mit JA bestätigen[/color]**).

![image]({filename}./player_modelling_tut-Dateien/image043.jpg)

Diese
Datei musst du  nur
 noch in dein **Gamedata/Base **Ordner kopieren

- Dann starte das Spiel im Multiplayer. Wenn du alles richtig gemacht hast,
kannst du dort deinen Model auswählen.

**Gratulation! Du hast dein erstes Player-Model gemacht!**

![image]({filename}./player_modelling_tut-Dateien/image044.jpg)

Bei weiteren Fragen oder
Verbesserungstipps für dieses Saberhilt Modelling-Tutorial mailt bitte an **[oliver@mijun.de](mailto:oliver@mijun.de)**  oder
labert ihn über **ICQ**
 (**168661509**) an.[color=windowtext][/color]

