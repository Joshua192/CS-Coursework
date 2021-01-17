<?php
// print_r($_POST);
include_once ("connection.php");
array_map("htmlspecialchars", $_POST);

$stmt = $conn->prepare("SELECT * FROM staff WHERE forename =:forename " );
$stmt->bindParam(':forename', $_POST['forename']);
$stmt->execute();

while ($row = $stmt->fetch(PDO::FETCH_ASSOC))
{ 
    if($row['Password']== $_POST['passwd']){
        switch($row["Role"]){
            case 1:
                print_r($_POST);
                echo $_POST["forename"];
                // header('Location: database.php');
            default:
            print_r($_POST);
                // header("Location: driver.php");
        }
    }
    else{
        echo "You're name and/or password are incorrect";
    }
    
}
$conn=null;
?>
