#!/usr/bin/env bash

clear

printf "Commit messege: "
read asd

git add .
git commit -m "$asd"
git status
