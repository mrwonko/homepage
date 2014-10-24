<?php
$additional_stylesheets = array("../css/home.css");
$title="Mr. Wonko's Website";
//name of the current page, so it can be highlighted on navigation
$pagename = "Home";

require_once("../config.php");
require("../downloads/functions.php");
require("../template/header.php");
?>

<!-- additional navigation on homepage -->

	<h2>Welcome!</h2>
	I am Willi "Mr. Wonko" Schinmeyer and this is my website.
	
	<!-- Latest Blog Entry. Dynamic. -->
	<h2>Latest blog entry:</h2>
	<div class="mrw_boxed_centered">
		<?php
		$result = $db->query('SELECT ID, post_date, post_excerpt, post_title FROM wp_posts WHERE post_status = "publish" AND post_type = "post" ORDER BY post_date DESC LIMIT 0,1');
		if(!$result)
		{
			echo $db->error;
		}
		else
		{
			$row = $result->fetch_assoc();
			if(!$row)
			{
				echo "No blog entries yet.";
			}
			else
			{
				echo '<a href="../blog/?p='.$row['ID'].'">'.$row['post_title'].'</a><span class="mrw_floatright">'.date($mrw_datetimeformat, strtotime($row['post_date'])).'</span>
		<hr/>
		'.nl2br($row['post_excerpt']).'<br/><a href="../blog/?p='.$row['ID'].'">read more</a>';
			}
		}
		?>
	</div>
	
	<!-- Latest download. Dynamic. -->
	<h2>Latest download:</h2>
	<?php
	global $db;
	$result = $db->query("SELECT id FROM downloads ORDER BY id DESC LIMIT 0, 1");
	if(!$result)
	{
		echo $db->error;
	}
	else
	{
		$row = $result->fetch_assoc();
		if($row)
		{
			PrintDownloadById($row['id']);
		}
		else
		{
			echo "No downloads yet.<br/>";
		}
	}
	?>

<?php
require("../template/footer.php");
?>