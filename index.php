<?php

$base = 'https://www.paulgraham.com/articles.html';

$html = file_get_contents($base);

// get all <a href="_____.html"> using regex

$pattern = '/<a href="(.*?)">/';

preg_match_all($pattern, $html, $matches);

// $matches[1] will contain all the links
$links = $matches[1];

// take only those that end with .html and don't start with http
$links = array_filter($links, function($link) {
    return preg_match('/\.html$/', $link) && !preg_match('/^http/', $link);
});

foreach ($links as &$link) {
    $link = 'https://www.paulgraham.com/' . $link;

    // get the html of each link
    $html = file_get_contents($link);

    // save
    file_put_contents('articles/' . basename($link), $html);
}

var_dump($links);