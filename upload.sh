#!/usr/bin/env bash

clear


token = "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"
user = "treboris"

printf "Commit messege: "
read asd

git add .
git commit -m "$asd"
git push -u origin master
$user
$token
