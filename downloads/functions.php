<?php
require_once("../config.php");
//prints the given download, or an error if the ID doesn't exist.
function PrintDownloadById($id)
{
	global $db;
	
	$result = $db->query("SELECT name, description, date, thumbnail, downloadcount FROM downloads WHERE id=".$id);
	if(!$result)
	{
		echo $db->error;
		return;
	}
	$row = $result->fetch_assoc();
	if(!$row)
	{
		echo "Error: Download with id $id does not exist!";
		return;
	}
	global $mrw_dateformat;
	echo '<div class="mrw_boxed mrw_download_infobox">
		<img src="'.$row['thumbnail'].'" alt="thumbnail"/><br/>
		'.$row['downloadcount'].' Downloads<br/>
		<a href="../downloads/download.php?id='.$id.'">Download</a>
	</div>
	<div class="mrw_boxed mrw_download_box">
		<b>'.$row['name'].'</b><span class="mrw_floatright">'.date($mrw_dateformat, strtotime($row['date'])).'</span>
		<hr/>
		'.nl2br($row['description']).'
	</div>
';
}

function PrintDownloadNav()
{
	echo '<a href="index.php">back</a>';
}
?>