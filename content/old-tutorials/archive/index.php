<?
	//Konfiguration laden
	include("config.php");

	include("bbcode.php");
	include('functions.php');

	mysql_connect($dbhost, $dbuser, $dbpasswd) OR die(mysql_error());
	mysql_select_db($dbname) OR die(mysql_error());
	
	$find = array ('ä', 'ö', 'ü', 'ß', 'Ö', 'Ä', 'Ü');
	$replace = array ('&auml;', '&ouml;', '&uuml;', '&szlig;', '&Ouml', '&Auml', '&Uuml;');
?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html xmlns="http://www.w3.org/1999/xhtml" lang="de" xml:lang="de">
<head>
<title>Mapping Academy - Tutorials Mainmenu</title>
<LINK href="style.css" rel="stylesheet" type="text/css"/>
</head>

<body lang=DE>
<div style="float: left; background-color:black;"><a href="../../home/">Back to mrwonko.de</a></div>
<center>
<img border=0 src="images/JediKnights2_logo.jpg" alt="" />
</center>
<br/>
<table width="95%"  border="0" cellpadding="0" cellspacing="0" align="center" summary="">
	<colgroup>
		<col width="66"/>
		<col/>
		<col width="116"/>
		<col width="66"/>
	</colgroup>
	
	<!-- Oberer Teil: Übersicht -->
	
	<tr style="height:23" id="oben">
		<td width="66">
			<img src="images/t_head_left.gif" width="66" height="23" alt=""/>
		</td>
		<td class="top" colspan="2">
			Tutorials
		</td>
		<td width="66">
			<img src="images/t_head_right.gif" width="66" height="23" alt=""/>
		</td>
	</tr>
	
	<tr style="height:23" id="oben">
		<td width="66">
			<img src="images/t_head2_left.gif" width="66" height="23" alt=""/>
		</td>
		<td class="top" colspan="2">
			Mit freundlicher Erlaubnis von Darth-Arth a.k.a. MetalBeast - <a href="http://www.3d-get.de/metalbeast" target="_BLANK">Website</a>
		</td>
		<td width="66">
			<img src="images/t_head2_right.gif" width="66" height="23" alt=""/>
		</td>
	</tr>
	
	<tr class="title">
		<td colspan="4">
			Mapping Academy Tutorials: Kategorien - &Uuml;bersicht / Categories
		</td>
	</tr>
	<tr class="blackbg">
		<td colspan="4"><img src="images/black_dot.gif" alt=""/></td>
	</tr>
	<?
	
	foreach($kategorien as $shortname => $longname)
	{
		echo '
	<tr class="middle2">
		<td align="center" valign="middle"></td>
		<td colspan="3"><a href="#'.$shortname.'">'.str_replace($find, $replace, $longname).'</a></td>
	</tr>
	<tr class="blackbg">
		<td colspan="4"><img src="images/black_dot.gif" alt=""/></td>
	</tr>';
	}
	
	?>
	<tr class="middle2">
		<td colspan="4">&nbsp;</td>
	</tr>
	<tr class="blackbg">
		<td colspan="4"><img src="images/black_dot.gif" alt=""/></td>
	</tr>
	<tr class="middle2">
		<td colspan="4">&nbsp;</td>
	</tr>
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
	
	<tr class="spacer">
		<td colspan="4"></td>
	</tr>
	
	<!-- Unterer Teil: Tutorials -->
	
	<tr style="height:23">
		<td width="66">
			<img src="images/t_head_left.gif" width="66" height="23" alt=""/>
		</td>
		<td class="top" colspan="2">
			Tutorials
		</td>
		<td width="66">
			<img src="images/t_head_right.gif" width="66" height="23" alt=""/>
		</td>
	</tr>
	
	<tr class="title_left">
		<td></td>
		<td>
			Kategorie bzw. Name / category or name
		</td>
		<td colspan="2" width="182">
			Verfasser / author
		</td>
	</tr>
	<tr class="middle2">
		<td colspan="4">&nbsp;</td>
	</tr>
	<?
	
	foreach($kategorien as $shortname => $longname)
	{
		echo '
	<tr class="title_left" id="'.$shortname.'">
		<td></td>
		<td colspan="1">
			'.str_replace($find, $replace, $longname).'
		</td>
		<td colspan="2"><a href="#oben">hoch / top</a></td>
	</tr>
	<tr class="middle2">
		<td colspan="4">&nbsp;</td>
	</tr>
	<tr class="blackbg">
		<td colspan="4"><img src="images/black_dot.gif" alt=""/></td>
	</tr>';
		//Die Vordefinierten Tutorials laden
		foreach($alte_tutorials[$shortname] as $key => $tutorial)
		{
			$tutorial->make_html_code();
		}
	
		//Die Tutorials aus der Datenbank laden
		$sql="	SELECT
					ID, Titel, Autor, Datum, Autor_ID
				FROM
					mrw_tutorials
				WHERE
					Kategorie='".$shortname."'
					AND
					Freigeschaltet=1;";
		$result = mysql_query($sql) or die(mysql_error());
		if(mysql_num_rows($result))
		{
			while($row = mysql_fetch_assoc($result))
			{	
				$image="images/tut.gif";
				
				echo '
			<tr class="middle2">
				<td align="center" valign="middle">
					<img src="'.$image.'" alt=""/>';
				echo '
				</td>
				<td>
					<a href="viewtut.php?id='.$row['ID'].'" target="_BLANK">'.mrw_reuse($row['Titel']).'</a></td>
				<td colspan="2">'.mrw_reuse($row['Autor']).'</td>
			</tr>
			<tr class="blackbg">
				<td colspan="4"><img src="images/black_dot.gif" alt=""/></td>
			</tr>';
			}
		}
		
		echo'
	<tr class="middle2">
		<td colspan="4">&nbsp;</td>
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
<? echo str_replace($find, $replace, COPYRIGHT);?>
<a href="admin.php">Administration</a>
</center>
</body>

</html>