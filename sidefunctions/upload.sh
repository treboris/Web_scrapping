#!/bin/bash -f

clear


printf "Commit messege: "
read message


git add .
git commit -m "$message"
git push -u origin master | treboris

expect "username: " # write the keyword you get as prompt for entering username
send "treboris\r"
# remove the below 2 lines if you do not want script to interact for password.
expect "password: " # write the keyword you get as prompt for entering password
send "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\r"
interact
