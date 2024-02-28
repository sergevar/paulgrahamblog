<?php

$lines = [];

foreach (glob("./cleaned/*.txt") as $filename) {
    echo "$filename size " . filesize($filename) . "\n";

    $file = file_get_contents($filename);

    $lines[] = json_encode(["line" => $file]);
}

file_put_contents("ALL_PAUL_GRAHAM.jsonl", implode("\n", $lines));