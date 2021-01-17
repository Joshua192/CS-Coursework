<!-- !!!!DONT FORGET TO COPY THE FILES INTO THE PATH C:\xaamp\htdocs\phpcoursework{DONE}-->
<!--CTRL+FN+F5->
<!DOCTYPE html-->
<html>
  <div class="all">
    <head>
    <link href="style.css" rel="stylesheet">
    <!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"> -->
    <!--SIGN UP PAGE HERE-->
        <title>Sign Up</title>
    </head>
<body>
<div class="header">
<h1>Sign Up</h1>
</div>

<form action="post.php" class="form" method = "post"><!--Form takes in the values for singup and redirects to "Post"-->
  First name:<input type="text" name="forename"><br>
  Last name:<input type="text" name="surname"><br>
  Email:<input type="text" name="mail"><br>
  Department:<input type="text" name="dept"><br>
  Create Password:<input type="password" name="passwd"><br>
  Phone Number:<input type="int" name="number"><br>
  <!--A radio button which users can use to select their role-->
    User Type:<br>
    <input class="form" type="radio" name="role" value="driver" checked> Driver<br>
    <input class="form" type="radio" name="role" value="admin"> Admin<br>
    <button class="button">Add User</button>
</form>

</body>

</div>
</html>
<?php
    include_once('connection.php');
    array_map("htmlspecialchars", $_POST);

?>