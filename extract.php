<?php

$lines = [];

foreach (glob("./cleaned/*.md") as $filename) {
    echo "$filename size " . filesize($filename) . "\n";

    $file = file($filename);

    $firstLine = $file[0];

    $theRest = implode("\n", array_slice($file, 1));

    // make sure first line starts with #
    if (!preg_match('/^#/', $firstLine)) {
        throw new \Exception("First line does not start with #");
    }

    $lines[] = json_encode(["input" => trim($firstLine), "output" => trim($theRest)]);
}

file_put_contents("ALL_PAUL_GRAHAM.jsonl", implode("\n", $lines));