<!DOCTYPE html>
<html>
    <head>
    <link href="style.css" rel=stylesheet>
        <title>TempName</title>
    </head>

<body>
<p>LOREM IPSUM DOLOR SIT AMET</p>
<form action="TempName2.php">
  First name:<input type="text" name="forename"><br>
  Last name:<input type="text" name="surname"><br>
  Email:<input type="text" name="mail"><br>
  Department:<input type="text" name="dept"><br>
  Create Password:<input type="password" name="passwd"><br>
  Phone Number:<input type="int" name="number"><br>
  <!--Creates a drop down list-->
  Gender:<select name="gender">
        <option value="M">Male</option>
        <option value="F">Female</option>
    </select>
  <br>
  <!--Next 3 lines create a radio button which we can use to select the user role-->
  <input type="radio" name="role" value="Pupil" checked> Pupil<br>
  <input type="radio" name="role" value="Teacher"> Teacher<br>
  <input type="radio" name="role" value="Admin"> Admin<br>
  <input type="submit" value="Add User">
</form>

</body>

</html>
<?php
    include_once('connection.php');

?>