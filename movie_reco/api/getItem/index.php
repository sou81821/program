<?php
//echo json_encode({'q' : htmlspecialchars($_SERVER['QUERY_STRING'])});
// echo "test";
$cmd = '/usr/bin/python test.py "' . htmlspecialchars($_SERVER['QUERY_STRING']) . '"';
$output = shell_exec($cmd);
echo $output;
// echo json_encode(array("1" => $_SERVER['QUERY_STRING']));