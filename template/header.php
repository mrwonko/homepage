<?php
//Name -> link
require_once("../config.php");
if(!isset($title2))
{
	$title2 = $title;
}
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" 
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
	<title>
	<?php
	echo $title2;
	?>
	</title>
	<link rel="stylesheet" type="text/css" href="../css/common.css"/>
<?php
	foreach($additional_stylesheets as $stylesheet)
	{
echo '	<link rel="stylesheet" type="text/css" href="'.$stylesheet.'"/>
';
	}
	
	if(isset($header_stuff)) echo $header_stuff;
?>
</head>

<body>
	<div id="mrw_topcontainer">
		<span id="mrw_logo">
			W
		</span>
		<span id="mrw_nav">
			<?php
			$first = true;
			foreach($pages as $name=>$url)
			{
				echo ($first ? "" : " - ").($name == $pagename ? '<span id="mrw_nav_current">'.$name.'</span>' : '<a href="../'.$url.'">'.$name.'</a>');
				$first = false;
			}
			?>
		</span>
	</div>
	<hr class="mrw_vertical_line"/>
	<div id="mrw_main">
		<div id="mrw_title">
			<?php echo $title; ?>
		</div>
	