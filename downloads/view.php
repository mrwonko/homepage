<?php
//we use the same h2 style as home
$additional_stylesheets = array("../css/downloads.css");

require_once("../config.php");

$title="Mr. Wonko's Downloads";

$id = intval($_GET['id']);

$result = $db->query("SELECT name FROM downloads WHERE id=".$id);
if($result)
{
	$row = $result->fetch_assoc();
	if($row)
	{
		$title2 = $row['name']." by Mr. Wonko";
	}
}
//name of the current page, so it can be highlighted on navigation
$pagename = "Downloads";

require_once("functions.php");
require("../template/header.php");

if(!$result)
{
	echo $db->error;
}
PrintDownloadNav();
echo '<br/><br/>';
PrintDownloadById($id);

require("../template/footer.php");
?>