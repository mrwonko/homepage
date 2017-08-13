<?

include("../../config.php");

$dbhost = $db_url;
$dbname = $db_name;
$dbuser = $db_user;
$dbpasswd = $db_password;

    // config.php
    error_reporting(E_ALL);
    
	//Einstellungen für die Copyrights unten
    define('COPYRIGHT', 'Alle Bilder, Texte, Grafiken, wenn nicht anders gekennzeichnet:<br/>
© 2000 - 2010 (Artur L.) <a href="http://www.darth-arth.de" target="_blank">www.darth-arth.de</a><br/>
Tutorialsystem : © 2007 - '.date('Y').' Mr. Wonko (Willi S.)<br/>
Nur zur privaten Nutzung. Kopieren ohne Erlaubnis nicht gestattet.<br/>mrwonko.de ist ausdr&uuml;cklich nicht f&uuml;r den Inhalt externer Seiten verantwortlich.<br/>Es gelten die angegebenen Nutzungsbedingungen.<br/><br/>
All images, texts and graphics if not marked differently:<br/>
© 2000 - 2010 (Artur L.) <a href="http://www.darth-arth.de" target="_blank">www.darth-arth.de</a><br/>
Tutorialsystem : © 2007 - '.date('Y').' Mr. Wonko (Willi S.)<br/>
Just for private use. Copying without permission forbidden.<br/>
Darth-arth.de is explicitly not responsible for the content of extern pages.<br/>
The specified terms of use apply.<br/>');

	include("altes_tutorial.php");
    
    //Kurzform (Database) - Langform (Anzeige)
	//Neue  Kategorien werden hier eingetragen.
	global $kategorien;
	$kategorien = array();
	
    $kategorien['german'] = "<b>Deutscher Teil</b>";
	
    $kategorien['editor'] = "Deutsch - Editor und Editing-Tools";
    $kategorien['jk_allgemein'] = "Deutsch - Kompilieren und Allgemeines zu Jedi Knight";
    $kategorien['texturen'] = "Deutsch - Texturen und Shader";
    $kategorien['mapping'] = "Deutsch - Mapping / World Editing";
    $kategorien['advanced'] = "Deutsch - Mapping f&uuml;r Fortgeschrittene";
    $kategorien['scripts'] = "Deutsch - Single Player Modus, Cutscenes, Scripting, NPCs, Men&uuml;-Coding";
    $kategorien['multiplayer'] = "Deutsch - Multiplayer Modus";
    $kategorien['models'] = "Deutsch - Player- und Objekt Modeling, Model-Skins, Effekte";
	$kategorien['gfx'] = "Deutsch - Grafik Gestaltung";
	
	$kategorien['english'] = "<b>English Part</b>";
	
	$kategorien['editor_en'] = "English - editor and editing tools";
	$kategorien['mapping_en'] = "English - mapping / world editing";
	$kategorien['other_en'] = "For more please visit www.map-craft.com";
	
	//Wo sind die alten Tutorials?
	$tutorial_link = "../";
	
	
	$alte_tutorials = array();
	foreach ($kategorien as $shortname => $longname)
	{
		$alte_tutorials[$shortname] = array();
	}
	
	//				Kategorie-Kurzname							Link, Name, Autor
	//EDITOR
	//$alte_tutorials['editor'][]		=	new altes_tutorial($tutorial_link."radiant/jk2_etools1.htm", "Installation - JK2 Editing Tools", "Darth Arth (Artur L.)");
	//$alte_tutorials['editor'][]		=	new altes_tutorial($tutorial_link."radiant/jk2_etools2.htm", "Installation - JK2 Editing Tools 2", "Darth Arth (Artur L.)");
	$alte_tutorials['editor'][]		=	new altes_tutorial($tutorial_link."radiant/gtk_radiant.htm", "Installation - GTK Radiant", "Darth Arth (Artur L.)");
	//$alte_tutorials['editor'][]		=	new altes_tutorial($tutorial_link."gtk14/install/gtk14.html", "Installation - GTK Radiant 1.4 (Raven)", "Killermic (Michael S.)");
	$alte_tutorials['editor'][]		=	new altes_tutorial($tutorial_link."radiant/hotkeys/hotkeys.htm", "GTK Radiant Hotkeys und Eigenschaften", "Darth Norman (Norman P.)");
	
	//Kompilieren & JK Allgemein
	$alte_tutorials['jk_allgemein'][]	=	new altes_tutorial($tutorial_link."q3map2.htm", "Kompilieren mit Q3map2", "Darth Arth (Artur L.)");
	$alte_tutorials['jk_allgemein'][]	=	new altes_tutorial($tutorial_link."suche/suche/suche.html", "Probleme lösen und Suche benutzen", "Killermic (Michael S.)");
	
	//TEXTUREN
	$alte_tutorials['texturen'][]	=	new altes_tutorial($tutorial_link."shader/shader1.htm", "Was sind Shader ?, Lava - Shader", "Darth Arth (Artur L.)");
	$alte_tutorials['texturen'][]	=	new altes_tutorial($tutorial_link."shader/shader_water.htm", "Wasser - Shader", "Darth Arth (Artur L.)");
	
	//MAPPING
	$alte_tutorials['mapping'][]	=	new altes_tutorial($tutorial_link."mapping/firstroom/firstroom.htm", "Mein erster Raum", "Darth Arth (Artur L.)");
	$alte_tutorials['mapping'][]	=	new altes_tutorial($tutorial_link."mapping/tworooms/tworooms.htm", "Zwei Räume verbinden, erste Tür", "Darth Arth (Artur L.)");
	$alte_tutorials['mapping'][]	=	new altes_tutorial($tutorial_link."door.htm", "Tür mit Schalter", "TheDark-Jedi (Johannes B.)");
	$alte_tutorials['mapping'][]	=	new altes_tutorial($tutorial_link."mapping/curves1/curves1.htm", "Curves & Patches - Torbogen / archway", "Darth Arth (Artur L.)");
	$alte_tutorials['mapping'][]	=	new altes_tutorial($tutorial_link."cylinder.htm", "Curves - Cylinder", "Jack");
	$alte_tutorials['mapping'][]	=	new altes_tutorial($tutorial_link."lift.htm", "Aufzug mit Schalter", "Sentinel (Paul S.)");
	$alte_tutorials['mapping'][]	=	new altes_tutorial($tutorial_link."doors2.htm", "Verschiedene Türarten", "Guard (Christophe B.)");
	$alte_tutorials['mapping'][]	=	new altes_tutorial($tutorial_link."mapping/light/light.html", "Licht", "Killermic (Michael S.)");
	$alte_tutorials['mapping'][]	=	new altes_tutorial($tutorial_link."mapping/teleporter/teleporter.htm", "Teleporter", "SithMaster ( Andreas K.)");
	$alte_tutorials['mapping'][]	=	new altes_tutorial($tutorial_link."minituts/minituts.htm", "Minitutorials: Firstroom, Caulk, Arena- & pk3-Datei, func_* Brushes, Triggers, Tips und Tricks", "Ice Dyn4stY™ ( Marc E.)");
	$alte_tutorials['mapping'][]	=	new altes_tutorial($tutorial_link."mapping/runderaeume/runderaeume.htm", "Runde Räume + Fenster und Durchgänge", "Bastardo (Sebastian M.)");
	$alte_tutorials['mapping'][]	=	new altes_tutorial($tutorial_link."regen-schnee/regen-schnee.htm", "Regen und Schnee", "SithMaster ( Andreas K.)");
	$alte_tutorials['mapping'][]	=	new altes_tutorial($tutorial_link."mapping/rotate/rotate.html", "Aufschwingende Türen", "Blue Wonder (Andreas P.)");
	$alte_tutorials['mapping'][]	=	new altes_tutorial($tutorial_link."mapping/flares/flares.htm", "Light - Flares", "Destroyer (Stephan K.)");
	$alte_tutorials['mapping'][]	=	new altes_tutorial($tutorial_link."mapping/curves2/curves2.htm", "Der effiziente Umgang mit Curves und Patches", "Chux (Mike H.S.)");
	$alte_tutorials['mapping'][]	=	new altes_tutorial($tutorial_link."_neu/target_speaker/speaker_tutorial.htm", "Target Speaker (Geräusche machen)", "FexXo (Andreas N.)");
	
	//ADVANCED
	$alte_tutorials['advanced'][]	=	new altes_tutorial($tutorial_link."mapping/aportals/aportals.htm", "Performance & FPS Optimierung: Area - Portale", "Darth Arth (Artur L.)");
	$alte_tutorials['advanced'][]	=	new altes_tutorial($tutorial_link."hintportals.htm", "Performance & FPS Optimierung: Hint - Portale", "Darth Arth (Artur L.)");
	//$alte_tutorials['advanced'][]	=	new altes_tutorial($tutorial_link."mapping/easygen/easygen.htm", "Terrain Erstellung mit EasyGen", "Darth Arth (Artur L.)");
	$alte_tutorials['advanced'][]	=	new altes_tutorial($tutorial_link."gensurf.html", "Terrain Erstellung mit Gensurf", "Zero (Dave H.)");
	$alte_tutorials['advanced'][]	=	new altes_tutorial($tutorial_link."outdoor_light.htm", "Richtiges Licht in Outdoor-Maps", "Shooter ( Oliver M.)");
	
	//SCRIPTS
	$alte_tutorials['scripts'][]	=	new altes_tutorial($tutorial_link."_neu/icarus_manual_de_mrw/index.html", "ICARUS-Manual Deutsch", "Mr. Wonko (Willi S.)");
	$alte_tutorials['scripts'][]	=	new altes_tutorial($tutorial_link."_neu/scripting_move/index.html", "Brushes per Script bewegen", "Mr. Wonko (Willi S.)");
	$alte_tutorials['scripts'][]	=	new altes_tutorial($tutorial_link."_neu/scripting_npc1/index.html", "NPC's per Script steuern", "Mr. Wonko (Willi S.)");
	$alte_tutorials['scripts'][]	=	new altes_tutorial($tutorial_link."_neu/scripting_password/index.php", "Passworteingabefeld via Script", "Mr. Wonko (Willi S.)");
	$alte_tutorials['scripts'][]	=	new altes_tutorial($tutorial_link."_neu/menucoding1/index.html", "Menü - Coding Teil1", "BiKi (Benjamin K.)");
	$alte_tutorials['scripts'][]	=	new altes_tutorial($tutorial_link."_neu/menucoding2/index.html", "Menü - Coding Teil2", "BiKi (Benjamin K.)");
	$alte_tutorials['scripts'][]	=	new altes_tutorial($tutorial_link."npcs.htm", "NPC Tutorial", "Darth Arth (Artur L.)");
	$alte_tutorials['scripts'][]	=	new altes_tutorial($tutorial_link."behaved/behaved.htm", "Scripting - Installation: BehavEd (Script-Editor)", "Darth Arth (Artur L.)");
	$alte_tutorials['scripts'][]	=	new altes_tutorial($tutorial_link."cutscenes/cam1/camera1.htm", "Cutscenes - Kamera Modus (camera modus)", "Darth Arth (Artur L.)");
	$alte_tutorials['scripts'][]	=	new altes_tutorial($tutorial_link."cutscenes/cam2/camera2.htm", "Cutscenes - die erste Kamera-Fahrt (Camera moving)", "Darth Arth (Artur L.)");
	$alte_tutorials['scripts'][]	=	new altes_tutorial($tutorial_link."npc_waves.htm", "NPC's - Angriffswellen", "Darth Arth (Artur L.)");
	$alte_tutorials['scripts'][]	=	new altes_tutorial($tutorial_link."npc_actors.htm", "NPC's als Schauspielen in Cutscenes", "Darth Arth (Artur L.)");
	
	//MODELS
	$alte_tutorials['models'][]		=	new altes_tutorial($tutorial_link."jk2models.htm", "Komplete Liste aller MD3 Models aus JKII", "Darth Arth (Artur L.)");
	$alte_tutorials['models'][]		=	new altes_tutorial($tutorial_link."sebcrea.htm", "Animierte Modele erstellen", "Seb (Crea)");
	$alte_tutorials['models'][]		=	new altes_tutorial($tutorial_link."effectsed_tut.htm", "Editieren von Effekten", "Charmin (Oliver J.) Deluxe");
	$alte_tutorials['models'][]		=	new altes_tutorial($tutorial_link."skinning_tut.htm", "Skins selber machen", "Charmin (Oliver J.) Deluxe");
	$alte_tutorials['models'][]		=	new altes_tutorial($tutorial_link."saberhilt_modeling_tut.htm", "Eigene Schwertgriffe erstellen", "Charmin (Oliver J.) Deluxe");
	$alte_tutorials['models'][]		=	new altes_tutorial($tutorial_link."player_modelling_tut.htm", "Eigene Player-Modele erstellen", "Charmin (Oliver J.) Deluxe");
	
	//MULTIPLAYER
	$alte_tutorials['multiplayer'][]=	new altes_tutorial($tutorial_link."botsupport.htm", "Bot Support", "Darth Arth (Artur L.)");
	$alte_tutorials['multiplayer'][]=	new altes_tutorial($tutorial_link."force_mp.htm", "Macht Tricks (Force Activate)", "Luke rg ( René G.)");
?>