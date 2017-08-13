<?

	//Konfiguration laden
	include("config.php");
	include("functions.php");

	include('bbcode.php');
	
	@mysql_connect($dbhost, $dbuser, $dbpasswd) OR die("Fehler beim Connecten: ".mysql_error());
	mysql_select_db($dbname) OR die("Fehler beim Wählen der Datenbank: ".mysql_error());

	$printme="Tutorial existiert nicht / Tutorial does not exist";
	if(isset($_GET['id']))
	{
		$sql="SELECT
				Titel, Noetig, Inhalt, Autor_ID, ID, Freigeschaltet
			FROM
				mrw_tutorials
			WHERE
				ID='".$_GET['id']."'
			LIMIT 1;";
		$result = mysql_query($sql) or die(mysql_error());
		$tut_active = true;
		if(mysql_num_rows($result))
		{
			$row=mysql_fetch_assoc($result);
			$tut_active = ($row['Freigeschaltet']) ? true : false;
			if($row['Noetig']=="")
			{
				$printme=mrw_create_tutorial($row['Titel'], $row['Inhalt'], $row['Freigeschaltet']);
			}
			else
			{
				$printme=mrw_create_tutorial($row['Titel'], $row['Inhalt'], $row['Freigeschaltet'], $row['Noetig']);
			}
		}
	}
  
?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html xmlns="http://www.w3.org/1999/xhtml" lang="de" xml:lang="de">
<head>
<title><? echo makenice($row['Titel']); ?></title>
<LINK href="style.css" rel="stylesheet" type="text/css"/>
</head>

<body lang=DE>
<center>
<a href="index.php"><img border=0 src="images/JediKnights2_logo.jpg" alt="" /></a>
</center>
<br/>
<?
	echo $printme;
?>
<br/>
<center class="copyright">
<?
echo "<br/>";
echo COPYRIGHT; ?>
</center>
</body>

</html>