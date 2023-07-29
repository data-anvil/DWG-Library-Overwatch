<!DOCTYPE html>
<html>
<head>
    <title>DWG Overwatch</title>
</head>
<body>
    <h1>Python Results:</h1>
    <ul>
        <?php
        // Very much untested and in progress - requires php compiler & python to be running on host and communicating with eachother
        // Execute the Python script and collect its output
        $pythonScript = 'overwatch.py';
        $command = 'python3 ' . escapeshellarg($pythonScript);
        $output = shell_exec($command);

        // Process the output and display it as a list
        $results = explode("\n", trim($output));
        foreach ($results as $result) {
            echo "<li>{$result}</li>";
        }
        ?>
    </ul>
</body>
</html>