<?
	//Die alten Tutorials: Titel, Autor & Link
	class altes_tutorial
	{
		//die Eigenschaften
		var $mTitel;
		var $mAutor;
		var $mLink;
		
		//die Methoden
		//erstmal der Konstruktor
		function altes_tutorial($derlink="Link", $dertitel="Titel", $derautor="Autor")
		{
			$find 		= array("&", 	);
			$replace	= array("&amp;"	);
			$this->mTitel = str_replace($find, $replace, $dertitel);
			$this->mAutor = str_replace($find, $replace, $derautor);
			$this->mLink  = $derlink;
		}
		
		function make_html_code()
		{
			$find = array ('ä', 'ö', 'ü', 'ß', 'Ö', 'Ä', 'Ü');
			$replace = array ('&auml;', '&ouml;', '&uuml;', '&szlig;', '&Ouml', '&Auml', '&Uuml;');
			echo '
			<tr class="middle2">
				<td align="center" valign="middle">
					<img src="images/tut.gif" alt=""/>
				</td>
				<td>
					<a href="'.$this->mLink.'" target="_BLANK">'.str_replace($find, $replace, $this->mTitel).'</a></td>
				<td colspan="2">'.str_replace($find, $replace, $this->mAutor).'</td>
			</tr>
			<tr class="blackbg">
				<td colspan="4"><img src="images/black_dot.gif" alt=""/></td>
			</tr>';
		}
	}
?>