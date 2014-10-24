<?php
$additional_stylesheets = array("../css/about.css");
$title="Contact Mr. Wonko";
//name of the current page, so it can be highlighted on navigation
$pagename = "";

require("../template/header.php");
?>

	<div id="mrw_about_text">
		<form action="sent.php" method="post">
			<table border="0" style="margin-left: auto; margin-right: auto">
				<tr>
					<td>Your E-Mail:</td><td style="text-align: right"><input type="text" maxlength="128" size="32" name="mail"/></td>
				</tr>
				<tr>
					<td>Subject:</td><td style="text-align: right"><input type="text" maxlength="64" size="32" name="subject"/></td>
				</tr>
				<tr>
					<td colspan="2">Message:<br/><textarea cols="50" rows="10" name="message"></textarea><br/><input type="submit"/></td>
				</tr>
			</table>
		</form>
	</div>
<?php
require("../template/footer.php");
?>