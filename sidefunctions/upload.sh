#!/bin/bash

clear


printf "Commit messege: "
read message


git add .
git commit -m "$message"
git push -u origin master | treboris
treboris
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
