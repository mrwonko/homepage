<?php
//we use the same h2 style as home
$additional_stylesheets = array("../css/downloads.css");
$title="Mr. Wonko's Downloads";
//name of the current page, so it can be highlighted on navigation
$pagename = "Downloads";

$valid_order = array("date", "name", "downloadcount");

require_once("functions.php");
require("../template/header.php");

//let the user choose the ordering
$order = (isset($_GET['order']) ? $_GET['order'] : "date");
$asc = ($_GET['asc'] == 1 ? 1 : 0);
$ascstr = ($asc == 1 ? "ASC" : "DESC");
if(!in_array($order, $valid_order))
{
	echo "invalid ordering";
	$order="date";
}

$heading = "Downloads";
if($order == "date")
{
	if($asc == 1) $heading = "Oldest downloads";
	else $heading = "Newest downloads";
}
elseif($order == "downloadcount")
{
	if($asc == 1) $heading = "Least downloaded";
	else $heading = "Most downloaded";
}

echo '
	<h2>'.$heading.'</h2>
	<br/>
	';

$count = 0;
$result = $db->query("SELECT COUNT(id) AS count FROM downloads");
if(!$result)
{
	echo $db->error;
}
$row = $result->fetch_assoc();
if($row)
{
	$count = $row['count'];
}

$start = 0;
if(isset($_GET['start']) && is_numeric($_GET['start']) && $_GET['start'] >= 0)
{
	$start = $_GET['start'];
}

$result = $db->query("SELECT id, name, date, downloadcount FROM downloads ORDER BY ".$order." ".$ascstr." LIMIT ".$start.", 10");
if(!$result)
{
	echo $db->error;
}
else
{
	echo '
	<table id="downloadtable">
		<tr id="downloadtable_title">
			<td style="width: 80%"><a href="index.php?order=name&amp;asc='.($order != "name" || $asc == 0 ? 1 : 0).'">Name</a></td>
			<td><a href="index.php?order=downloadcount&amp;asc='.($order != "downloadcount" || $asc == 1 ? 0 : 1).'">Downloads</a></td>
			<td><a href="index.php?order=date&amp;asc='.($order != "date" || $asc == 1 ? 0 : 1).'">Date</a></td>
		</tr>';
	while($row = $result->fetch_assoc())
	{
		echo '
		<tr>
			<td><a href="view.php?id='.$row['id'].'">'.$row['name'].'</a></td>
			<td>'.$row['downloadcount'].'</td>
			<td>'.date($mrw_dateformat, strtotime($row['date'])).'</td>
		</tr>';
	}
	if($start > 0 || $start + 10 < $count)
	{
		echo '
		<tr>
			<td colspan="3">';
		if($start > 0)
		{
			echo '<a href="index.php?start='.max($start - 10, 0).'&amp;asc='.($asc==1 ? 1 : 0).'&amp;order='.$order.'">previous page</a>';
		}
		echo '<div style="text-align: right;">';
		if($start + 10 < $count)
		{
			echo '<a href="index.php?start='.($start+10).'&amp;asc='.($asc==1 ? 1 : 0).'&amp;order='.$order.'">next page</a>';
		}
		echo '</div></td>
		</tr>';
	}
	echo '
	</table>';
}

require("../template/footer.php");
?>