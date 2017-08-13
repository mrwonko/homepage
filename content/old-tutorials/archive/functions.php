<?php
	function mrw_strip_tags($string)
	{
		$string = str_replace("<", "&lt;", $string);
		$string = str_replace(">", "&gt;", $string);
		return $string;
	}
	
    //Parses BBCode, nl2br etc.
    function makenice ($string, $smileys=true)
    {
      //first strip any html tags
	  $string = mrw_strip_tags($string);
	  
	  //then do the linebrakes - not before! ouch
	  $string = nl2br($string);      
      $string = preg_replace('/\[quote=\\\"(.*?)\\\"\](.*?)\[\/quote\]/', "[quote:=\"$1\"]$2[/quote:]", $string);
	  $string = preg_replace('/\[quote=\"(.*?)\"\](.*?)\[\/quote\]/', "[quote:=\"$1\"]$2[/quote:]", $string);	 
	  
	  $string = preg_replace('/\[code\]([^\[]*)\[\/code\]/', "[code:]$1[/code:]", $string);	 
	  
      $string = preg_replace('/\[img](.*?)\[\/img\]/', "[img:]$1[/img:]", $string);
	  //there must not be any <br />s inside of [code]
	  $match_count = preg_match_all("/\[code\][^\[]*\[\/code\]/", $string, $matches);
		for ($i = 0; $i < $match_count; $i++)
		{
			$before_replace = $matches[0][$i];
			$after_replace = $matches[0][$i];
			$after_replace = str_replace("<br />", "\n", $after_replace);
			//echo $after_replace;
			$string = str_replace($before_replace, $after_replace, $string);
		}
      
      //Now do the bbcode stuff
	  // TODO: bb code!
      $string = bbencode_first_pass($string, "" );
      $string = bbencode_second_pass($string, "" );
	  
	  //no auto link creation or smiley support.
	  
      //some of the img tags are lacking an alt=""
      $string = preg_replace('/<img src\=\"([^\"]*)\" border\=\"0\" \/>/', '<img src="$1" border="0" alt=""/>', $string);
		
      //My own "Trennlinien"-Code:
      $string = preg_replace('/\[trenn\]([^\[]*)\[\/trenn\]/', "
            </span>
            <br/>
        		</td>
        		<td></td>
        	</tr>
          <tr class=\"title\">
        		<td></td>
        		<td>
            $1
        		</td>
        		<td></td>
        	</tr>
      	
        	<tr class=\"middle\">
        		<td></td>
        		<td>
            <span class=\"postbody\">", $string);
	
		//" und ' werden automatisch escaped - das wollen wir doch nicht, oder?
		$string = str_replace('\\"', '"', $string);
		$string = str_replace("\\'", "'", $string);
	
	//habt ihr schon bemerkt, was für ein Sprachgewirr die Kommentare hier sind?
	
	//ö, ü, ä und ß zu entsprechendem html code machen
	$find = array ('ä', 'ö', 'ü', 'ß', 'Ö', 'Ä', 'Ü');
	$replace = array ('&auml;', '&ouml;', '&uuml;', '&szlig;', '&Ouml;', '&Auml;', '&Uuml;');
	$string = str_replace($find, $replace, $string);
      
      //now return the string, now it's all nice and shiny!
      return $string;
    }
	
	function mrw_create_tutorial($titel, $inhalt, $active, $noetig="")
    {
      //Creates a Tutorial out of the code
      $string = '
          <table width="95%"  border="0" cellpadding="0" cellspacing="0" align="center"  summary="">
          	<tr style="height:23">
          		<td width="66">
          			<img src="images/t_head_left.gif" width="66" height="23" alt=""/>
          		</td>
          		<td class="top">
                '.makenice($titel).'
          		</td>
          		<td width="66">
          			<img src="images/t_head_right.gif" width="66" height="23" alt=""/>
          		</td>
          	</tr>';
      if($noetig!='')
      {
          //Voraussetzungen
      	  $string .= '
          <tr class="title">
        		<td></td>
        		<td>
        			Voraussetzungen
        		</td>
        		<td></td>
        	</tr>
      	
        	<tr class="';
			$string.= ($active) ? 'middle' : 'middle_red';
			$string .= '">
        		<td></td>
        		<td>
            <span class="postbody">
            '.makenice($noetig).'
            </span>
            <br/><br/>
        		</td>
        		<td></td>
        	</tr>
          <tr class="title">
        		<td></td>
        		<td>
            '.makenice($titel).'
            </td>
        		<td></td>
        	</tr>';
      }
      else
      {
        $string .= '<tr class="title">
        		<td></td>
        		<td>
            '.makenice($titel).'
            </td>
        		<td></td>
        	</tr>';
      }
      $string .= '        	
        	<tr class="';
			$string.= ($active) ? 'middle' : 'middle_red';
			$string .= '">
        		<td></td>
        		<td>
            <span class="postbody">
            '.makenice($inhalt).'
            </span>
            </td>
        		<td></td>
        	</tr>
        	
        	<tr style="height:23">
        		<td width="66">
        			<img src="images/t_bottom_left.gif" width="66" height="23" alt=""/>
        		</td>
        		<td class="bottom">
        		</td>
        		<td width="66">
        			<img src="images/t_bottom_right.gif" width="66" height="23" alt=""/>
        		</td>
        	</tr>
        </table><br/><br/>';
      //By using multiple [trenn]s next to each other you may produce empty <span>s resulting in html errors. We don't want that.
      $string = preg_replace('/<span class=\"postbody\">(\s*)<\/span>/','$1',$string);
      return $string;
    }
	
	function mrw_show_entries($neue, $kategorie="alle")
	{
		global $kategorien;
		$sql="SELECT
				ID, Autor, Titel, Kategorie, Freigeschaltet
			FROM
				mrw_tutorials
			WHERE
			1";
		if ($kategorie!="alle")
		{
			$sql.="
			AND
				Kategorie = '".$kategorie."'";
		}
		if($neue=="neue")
		{
			$sql.="
			AND
				Freigeschaltet = '0'";
		}
		else if($neue=="alte")	
		{
			$sql.="
			AND
				Freigeschaltet = '1'";
		}
		$sql .="	
			ORDER BY
				Kategorie ASC;";
		$result = mysql_query($sql) or die(mysql_error());
		$blub;
		$string = '<table border="0" cellpadding="0" cellspacing="0" align="center" style="text-align: center">
						<tr>
							<td>Kategorie</td>
							<td class="blackbg" width="1"> </td>
							<td>Name</td>
							<td class="blackbg" width="1"> </td>
							<td>Autor</td>
							<td class="blackbg" width="1"> </td>
							<td>Funktionen</td>
						</tr>';
		if(mysql_num_rows($result))
		{
			while($row=mysql_fetch_assoc($result))
			{
				$string .='
				<tr><td colspan="7" class="blackbg"></td></tr>
				<tr';
				if($row['Freigeschaltet']==false)
				{
					$string .= ' class="redbg"';
				}
				else
				{
					$string .= ' class="greenbg"';
				}
				$string .='><td>'.$kategorien[$row['Kategorie']].'</td>
				<td class="blackbg" width="1"> </td>
				<td><a href="viewtut.php?id='.$row['ID'].'" target="_BLANK">'.makenice($row['Titel']).'</a></td>
				<td class="blackbg" width="1"></td>
				<td>'.makenice($row['Autor']).'</td>
				<td class="blackbg" width="1"> </td>
				<td><a href="admin.php?section=';
				$string .= ($row['Freigeschaltet']=='0') ? 'activate' : 'deactivate';
				$string .= '&amp;id='.$row['ID'].'">';
				$string .= ($row['Freigeschaltet']=='0') ? 'freigeben' : 'deaktivieren';
				$string .='</a> - <a href="admin.php?section=edit&amp;id='.$row['ID'].'">bearbeiten</a> - <a href="admin.php?section=delete&amp;id='.$row['ID'].'">l&ouml;schen</a></td></tr>
				';
			}
		}
		mysql_free_result($result);
		$string .= '</table>';
		return $string;
	}
	
    function mrw_reuse($string)
    {
		$string = mrw_strip_tags($string);
		//Removes the \ in front of the " at quotes
		//$string = preg_replace('/\[quote=\\\"(.*?)\\\"\](.*?)\[\/quote\]/', "[quote=\"$1\"]$2[/quote]", $string);
		$string = str_replace('\\"', '"', $string);
		$string = str_replace("\\'", "'", $string);
		$find = array ('ä', 'ö', 'ü', 'ß', 'Ö', 'Ä', 'Ü');
		$replace = array ('&auml;', '&ouml;', '&uuml;', '&szlig;', '&Ouml;', '&Auml;', '&Uuml;');
		$string = str_replace($find, $replace, $string);
		return $string;
    }
?>