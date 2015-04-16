title: Vehikel mit eigenem Skin
date: 2008-07-01
type: tutorials/darth-arth
author: mrwonko
category: models
modified: 2015-04-12
slug: skins-vehicles
tags: Skin, Vehicle, PK3

# Voraussetzungen

*   [Gimp](http://www.gimp.org) oder anderes Bildbearbeitungsprogramm
*   [Winrar](http://www.winrar.de), [7-Zip](http://7-zip.org) oder anderes Programm zum zips öffnen & erstellen
*   Jedi Academy

# Tutorial

In diesem Tutorial möchte ich euch erklären, wie man in Jedi Academy ein neues Fahrzeug auf Basis eines bestehenden erstellen kann.

Zuerst braucht ihr das entsprechende Model sowie die zugehörigen .npc und .veh Dateien. Öffnet in <code><em>JKA-Verzeichnis</em>/GameData/Base</code> die Datei `assets1.pk3` mit Winrar - es ist eine einfache .zip Datei mit anderer Endung.

In dieser Datei befinden sich u.a. die Ordner `models` und `ext_data`. (Wenn ihr WinZip nutzt, müsst ihr glaube ich erst das Anzeigen von Unterordnern aktivieren - wo das geht, weiß ich allerdings nicht.)

![image]({filename}skins-vehicle/_shot1_c9wf.jpg)



Nun entpackt ihr den Unterordner <code>models/players/<em>Name des Fahrzeugs</em>/</code> sowie die Dateien <code>ext_data/npcs/<em>Name des Fahrzeugs</em>.npc</code> und <code>ext_data/vehicles/<em>Name des Fahrzeugs</em>.veh</code>. Ihr könnt auch gleich die ganzen Ordner `ext_data` und `models` entpacken, vor allem `models` ist allerdings recht groß.

Im Beispiel will ich das Swoop verändern:

![image]({filename}skins-vehicle/_shot2_yiht.jpg)

(Außerdem entpacke ich noch `ext_data/vehicles/swoop.veh` und `models/players/swoop/`.)

Damit die am Ende entstehende PK3 Datei nicht zu groß wird, nehme ich nun nur die Dateien, die ich verändern möchte, und kopiere diese mit gleicher Ordnerstruktur in einen neuen Ordner, z.B. `swoop_wonko`.

Die benötigten Dateien sind:

*   <code>models/players/<em>Name des Fahrzeugs</em>/model_default.skin</code>
*   <code>ext_data/npcs/<em>Name des Fahrzeugs</em>.npc</code>
*   <code>ext_data/vehicles/<em>Name des Fahrzeugs</em>.veh</code>
*   sämtliche Bilder im <codeYmodels/players/<em>Name des Fahrzeugs</em>/</code>-Ordner, die man verändern möchte

Es ist dabei ratsam, einen Blick in die vorhin erwähnte `model_default.skin` Datei zu werfen, dort stehen sämtliche benutzte Bilder vom normalen Model drin.

In meinem Beispiel kopiere ich

*   `models/players/swoop/model_default.skin`
*   `ext_data/npcs/swoop.npc`
*   `ext_data/vehicles/swoop.veh`
*   `models/players/swoop/swoop.jpg`

Jetzt benennen wir die Dateien um, da wir ja einen neuen Skin machen wollen, bei mir:

*   `models/players/swoop/model_wonko.skin`
*   `ext_data/npcs/swoop_wonko.npc`
*   `ext_data/vehicles/swoop_wonko.veh`
*   `models/players/swoop/swoop_wonko.jpg`

Jetzt malen wir, z.B. mit Gimp, in den Bildern herum. Hier mein Kunstwerk (verkleinerte Version):

![image]({filename}skins-vehicle/_shot3_j9i1.jpg)

Als nächstes öffnen wir `ext_data/npcs/swoop_wonko.npc` (oder wie auch immer es bei euch heißt) mit einem Texteditor unserer Wahl. Die Datei ist möglicherweise schreibgeschützt, macht also vorher einen Rechtsklick auf sie, geht in die Eigenschaften und entfernt das Häkchen bei "schreibgeschützt".

Was uns interessiert, ist nun alles vom ersten Namen bis zum Ende der geschweiften Klammer, den Rest löschen wir. Dies passen wir nun an:

<pre><em>Swoop_wonko</em>
{
    weapon      WP_BLASTER
    playerTeam  TEAM_NEUTRAL
    enemyTeam   TEAM_NEUTRAL
    class       CLASS_VEHICLE
    width       24
    height      32
}</pre>

Das gleiche machen wir mit `ext_data/vehicles/swoop_wonko.veh` - dort passen wir den Namen vor dem `{` an, dann den Namen, der rechts von `name` steht. Außerdem setzen wir `skin` auf den Namen unser `model_***.skin` Datei, ohne `model_` und `.skin`, also z.B. `wonko` bei `model_wonko.skin`. Wenn ihr wollt, könnt ihr noch an den Werten herumspielen.

<pre><em>Swoop_wonko</em>
{
    <em>name                    Swoop_wonko</em>
    type                    VH_SPEEDER
    numHands                2
    lookYaw                 45
    lookPitch               20
    length                  128
    width                   32
    height                  32
    centerOfGravity         "-0.222 0 0"
    speedMax                900
    speedMin                -150
    turboSpeed              1900
    turboDuration           2000
    turboRecharge           8000
    acceleration            20
    decelIdle               10
    strafePerc              0.5
    bankingSpeed            0.5
    rollLimit               45
    pitchLimit              30
    braking                 10
    mouseYaw                0.0038
    turningSpeed            5
    turnWhenStopped         0
    traction                12
    friction                1.5
    maxSlope                0.75
    mass                    200
    armor                   2000
    toughness               80.0
    malfunctionArmorLevel   1000
    model                   swoop
    <em>skin                    wonko</em>
    riderAnim               BOTH_VS_IDLE
    radarIcon               "gfx/menus/radar/swoop"
    
    soundOn                 "sound/vehicles/swoop/on.mp3"
    soundOff                "sound/vehicles/swoop/off.mp3"
    soundLoop               "sound/vehicles/swoop/loop.wav"
    soundTakeOff            "sound/vehicles/swoop/on.mp3"
    soundEngineStart        "sound/vehicles/swoop/on.mp3"
    soundSpin               "sound/vehicles/swoop/loop.wav"
    soundTurbo              "sound/vehicles/swoop/sb_revup.mp3"
    soundFlyBy              "sound/vehicles/swoop/flyby1.mp3"
    soundFlyBy2             "sound/vehicles/swoop/flyby2.mp3"
    soundShift              "sound/vehicles/swoop/sb_shift1.mp3"
    soundShift2             "sound/vehicles/swoop/sb_shift2.mp3"
    soundShift3             "sound/vehicles/swoop/sb_shift3.mp3"
    soundShift4             "sound/vehicles/swoop/sb_shift4.mp3"
    
    exhaustFX               "ships/burner"
    impactFX                "ships/scrape_sparks"
    turboStartFX            "ships/swoop_turbo_start"
    armorLowFX              "volumetric/black_smoke"
    armorGoneFX             "ships/fire"
    flammable               1
    explosionRadius         100
    explosionDamage         250
    explodeFX               "ships/swoop_explosion"
    explosionDelay          4500
    wakeFX                  "ships/vehicle_wake"
    gravity                 800
    waterProof              1
    bouyancy                1
    hoverHeight             30
    hoverStrength           35
    
    cameraOverride          1
    cameraRange             125
    cameraVertOffset        0
    cameraPitchOffset       0
    cameraFOV               100
    cameraAlpha             0
    
    weap1                   swoop_laser
    weap1Aim                1
    
    weap1Delay              100
    
    weap1AmmoMax            2000
    weap1AmmoRechargeMS     200
    
    weapMuzzle1             swoop_laser
}</pre>

Nun müssen wir nur noch in der `models/players/swoop/model_wonko.skin` Datei die Pfade der Bilder anpassen, die wir verändert haben, also bei mir alle:

<pre>lbody,models/players/swoop/swoop.tga
rbody,models/players/swoop/swoop_wonko.tga
lfront,models/players/swoop/swoop_wonko.tga
rfront,models/players/swoop/swoop_wonko.tga
rfin,models/players/swoop/swoop_wonko.tga
lfin,models/players/swoop/swoop_wonko.tga
front_cap,models/players/swoop/swoop_wonko.tga
body_cap,models/players/swoop/swoop_wonko.tga</pre>

Dann nehmen wir die beiden Ordner `models` und `ext_data` (die jetzt nur unsere neuen Dateien enthalten) und fügen sie zu einem **zip**-Archiv hinzu. Markiert dazu beide und klickt auf (bei Winrar) `zu einem Archiv hinzufügen`.

<div class="alert alert-warning">Im Dialogfeld müssen wir <strong>unbedingt ein Häkchen bei Zip setzen</strong>, denn Jedi Academy kann mit rar Archiven nichts anfangen, und ändern die Endung zu <code>.pk3</code>.</div>

![image]({filename}skins-vehicle/_shot4_ceml.jpg)

Dadurch bekommt ihr eine PK3 Datei. Wenn ihr alles richtig gemacht habt, könnt ihr diese nun in <code><em>JKA-Verzeichnis</em>/GameData/Base</code> verschieben und das Fahrzeug im Spiel mit `/npc spawn vehicle swoop_wonko` reincheaten. (Dazu die Karte mit <code>devmap <em>mapname</em></code> starten, also z.B. `devmap mp/ffa1`, und im Einzelspielermodus auch ohne das `/` am Anfang.)

![image]({filename}skins-vehicle/_shot5_mk9x.jpg)

Der Glanz-Effekt des Swoops ist übrigens weg, denn das war ein Shader; Den müssten wir auch kopieren und anpassen, darauf will ich jetzt hier aber nicht weiter eingehen, das würde den Rahmen des Tutorials sprengen.

[Download des Swoops]({filename}examples/swoop_wonko.pk3)

Euer Mr. Wonko