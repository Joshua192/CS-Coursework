<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "coursework_db";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    //echo "Connected" ; 
    }
catch(PDOException $e)
    {
    echo "Connection failed, check your code!: " . $e->getMessage();
    }
?>