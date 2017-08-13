<html>
<head></head>
<body>
<?
$myDirectory = opendir(".");

// get each entry
while($entryName = readdir($myDirectory))
{
	echo '<img src="'.$entryName.'" alt=""><br/>
';
}
?>
</body>
</html>