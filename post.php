<!DOCTYPE html>
<!--Enter the data into database from here then redirect to 'Login'. connection form Temp1 redirects here-->
<html>
<head>
<link href="style.css" rel="stylesheet">
    
    <title>Post</title>
    
</head>
<body>
       
</body>
</html>
<?php
include_once('connection.php');
print_r($_POST);
switch($_POST["role"]){
    case "driver":
        $role=0;
        break;
        case "admin":
            $role=1;
            break;
        }
        $stmt = $conn->prepare("INSERT INTO staff (PeopleID,Forename,Surname,DEPT,MAIL,PHONE,PASSWORD,Role)VALUES (null,:forename,:surname,:department,:mail,:phone,:password,:role)");
        
        $stmt->bindParam(':forename', $_POST["forename"]);
        $stmt->bindParam(':surname', $_POST["surname"]);
        $stmt->bindParam(':department', $_POST["dept"]);
        $stmt->bindParam(':mail', $_POST["mail"]);
        $stmt->bindParam(':phone', $_POST["number"]);
        $stmt->bindParam(':password', $_POST["passwd"]);
        $stmt->bindParam(':role', $role);
        $stmt->execute();
        $conn=null;
        
header('Location: login.php');

?>
