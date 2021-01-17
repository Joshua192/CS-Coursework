<!DOCTYPE html>
<html class="all">
<head>
    <title>Login</title>
    <link href="style.css" rel="stylesheet">

</head>   

<body>
    <div class="header">
    Login
    </div>

<form class= "form" action="loginprocess.php" method= "POST">
First name:<input type="text" name="forename"><br>
Password:<input type="password" name="passwd"><br>
<input type="submit" value="Login"> </form>


</body>
</html>
<?php
include_once('connection.php');
?>