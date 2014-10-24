<?php
//we use the same h2 style as home
$additional_stylesheets = array("../css/about.css");
$title="About Mr. Wonko";
//name of the current page, so it can be highlighted on navigation
$pagename = "About Me";

require("../template/header.php");
?>

	<div id="mrw_about_text">
		<h2>Who am I?</h2>
		My Name is Willi "Mr. Wonko" Schinmeyer, I'm <?php
		$day = date("j");
		$month = date("n");
		$year = date("Y");
		if($month < 7 || ( $month == 7 && $day < 14))
		{
			echo $year-1993;
		}
		else
		{
			echo $year-1992;
		}
		?> years old and from Germany.
		<h2>What do I do?</h2>
		I'm a Computer Science student at the FH Wedel University of Applied Sciences and in my spare time I like to play videogames, program and create mods/maps for games. I also play the Cello, listen to Rock/Metal and read Fantasy/Sci-Fi books.
		<h2>What are my modding skills?</h2>
		I like programming best, but I also have some experience in creating maps with the GTK Radiant, the Hammer Editor and UnrealEd. I can also create models in Blender and make some basic textures. I'm better at thinking then at imagining, i.e. I can't come up with a cool weapon design but I know how to make one into a model. Obviously I can also create websites, at least the technical part. I leave clever desigs to someone else.<br/>
		Have a look at the <a href="../downloads">Downloads</a> to see some things I've made.
		<h2>How can you contact me?</h2>
		Send me a PM on the Forum or write me a mail: <a href="contact.php">Contact form</a>
	</div>
<?php
require("../template/footer.php");
?>