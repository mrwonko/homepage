<?
	//Konfiguration laden
	include("config.php");
	include("functions.php");

	//anderes zeugs laden
	$phpbb_root_path = PHPBB_PATH;
	include($phpbb_root_path . 'extension.inc');
	include($phpbb_root_path . 'common.'.$phpEx);
	$forum_id = intval($forum_topic_data['forum_id']);
	$userdata = session_pagestart($user_ip, $forum_id);
	init_userprefs($userdata);
	include($phpbb_root_path."config.$phpEx");
	include($phpbb_root_path."includes/bbcode.$phpEx");

	mysql_connect($dbhost, $dbuser, $dbpasswd) OR die(mysql_error());
	mysql_select_db($dbname) OR die(mysql_error());
	
	$good = false;
	$error = "";
	$page_title = " - Login";
	if($userdata['session_logged_in'])
	{
		if($userdata['user_level']>0)
		{
			$page_title = "";
			if(isset($_POST['section']))
				$page_title = " - " . $_POST['section'];
			$good = true;
		}
		else //user_level > 1
		{
			$error = '<span class="red">Unzureichende Rechte</span> <a href="index.php">zur&uuml;ck</a>';
		}
	}
	else
	{
		$error = '<span class="red">Nicht eingeloggt</span> <a href="'. PHPBB_PATH.'login.php?redirect='.THIS_RELATIVE_TO_FORUM.'/admin.php">login</a>';
	}
?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html xmlns="http://www.w3.org/1999/xhtml" lang="de" xml:lang="de">
<head>
<title>Administration<? echo $page_title; ?></title>
<LINK href="style.css" rel="stylesheet" type="text/css"/>
</head>

<body lang=DE>
<center>
	<a href="http://darth-arth.de/forum/portal.php"><img border="0" src="images/JediKnights2_logo.jpg" alt="" /></a>
</center>
<br/>
<table width="95%"  border="0" cellpadding="0" cellspacing="0" align="center">

	<!-- Oberer Teil: Übersicht -->
	
	<tr style="height:23">
		<td width="66">
			<img src="images/t_head_left.gif" width="66" height="23" alt=""/>
		</td>
		<td class="top" colspan="2">
			Administration
		</td>
		<td width="66">
			<img src="images/t_head_right.gif" width="66" height="23" alt=""/>
		</td>
	</tr>
<?
	if(!$good)
	{
		?>
	<tr class="title">
		<td colspan="4">
			<? echo $error; ?>
		</td>
	</tr>
		<?
	}
	//  (!$good)
	else
	{
		?>
	<tr class="title">
		<td colspan="4">
			Willkommen, <?echo $userdata['username'];?>!
		</td>
	</tr>
		<?
		echo '
		<tr class="middle">
			<td></td>
			<td colspan="2">';
		switch($_GET['section'])
		{
			//Tutorials anzeigen
			case 'show':
				echo mrw_kategorie_wahl();
				
				echo '<br/><br/>'.mrw_show_entries($_POST['neue'], $_POST['kategorie']).'<br/><br/>';
				//Alle Einträge (einer bestimmten Kategorie) anzeigen
				echo '<a href="admin.php">Hauptmen&uuml;</a> - ';
				break;
			
			//Alles, was mit Usern zu tun hat - also suchen, Tutorials erlauben & verbieten
			case 'user':
				echo mrw_user($table_prefix);
				echo '<a href="admin.php">Hauptmen&uuml;</a> - ';
				break;
			
			//Tutorial freischalten
			case 'activate':
				$sql = "UPDATE mrw_tutorials SET Freigeschaltet = 1 WHERE ID = ".$_GET['id']." LIMIT 1 ;";
				mysql_query($sql) or die (mysql_error());
				echo 'Tutorial freigeschaltet!<br/><br/>';
				echo '<a href="admin.php">Hauptmen&uuml;</a> - ';
				break;
			
			//Tutorial deaktivieren
			case 'deactivate':
				$sql = "UPDATE mrw_tutorials SET Freigeschaltet = 0 WHERE ID = ".$_GET['id']." LIMIT 1 ;";
				mysql_query($sql) or die (mysql_error());
				echo 'Tutorial deaktiviert!<br/><br/>';
				echo '<a href="admin.php">Hauptmen&uuml;</a> - ';
				break;
				
			//Tutorial löschen
			case 'delete':
				if(empty($_GET['sure']))
				{
					echo '<center>Tutorial l&ouml;schen - Sicher?<br/>
					<a href="admin.php?section=delete&amp;id='.$_GET['id'].'&amp;sure=1">Ja</a> - <a href="admin.php">nein</a></center><br/>';
				}
				else
				{
					$sql = "DELETE FROM mrw_tutorials WHERE ID = '".$_GET['id']."' LIMIT 1 ;";
					mysql_query($sql) or die (mysql_error());
					echo "Tutorial wurde gelöscht.<br/><br/>";
				}
				echo '<a href="admin.php">Hauptmen&uuml;</a> - ';
				break;
			
			//Tutorial bearbeiten
			case 'edit':
				$edit_ok=true;
				$edit_id=$_GET['id'];
				include('edit.php');
				echo '<a href="admin.php">Hauptmen&uuml;</a> - ';
				break;
			
			case 'deaktivieren':
				$sql = "UPDATE mrw_tutorials SET Freigeschaltet = 0 WHERE ID = ".$_GET['id']." LIMIT 1 ;";
				mysql_query($sql) or die (mysql_error());
				echo 'Tutorial deaktiviert!<br/><br/>';
			
			case 'aktivieren':
				$sql = "UPDATE mrw_tutorials SET Freigeschaltet = 1 WHERE ID = ".$_GET['id']." LIMIT 1 ;";
				mysql_query($sql) or die (mysql_error());
				echo 'Tutorial freigeschaltet!<br/><br/>';				
			
			default:
				echo mrw_kategorie_wahl();
				echo '<h3 align="center">Noch nicht freigeschaltete Tutorials:</h3>';
				//Main-Menü: alle nicht-freigeschalteten Tutorials auf einen Blick anzeigen mit View, Edit & Freischalt-Knopf
				echo mrw_show_entries('neue').'<br/><br/>';
				//Main Menü Ende
				break;
		}
		echo '<a href="index.php">zur&uuml;ck zu den Eintr&auml;gen</a> - <a href="admin.php?section=user">Benutzerberechtigungen</a>
			</td>
			<td></td>
		</tr>';
	}
?>
	<tr style="height:23">
		<td width="66">
			<img src="images/t_bottom_left.gif" width="66" height="23" alt=""/>
		</td>
		<td class="bottom" colspan="2">
		</td>
		<td width="66">
			<img src="images/t_bottom_right.gif" width="66" height="23" alt=""/>
		</td>
	</tr>
</table>
<br/>
<center class="copyright">
<? echo COPYRIGHT;?>
<? echo ($userdata['user_level']>0) ? '<a href="admin.php">Administration</a>' : ''; ?>
</center>
</body>

</html>