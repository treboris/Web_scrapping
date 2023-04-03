#!/usr/bin/env bash




if python3 cvonline.py ;then
  true
else
  echo "An error has occurred(cvonline)!"
fi


if python3 kariera.py ;then
  true
else
  echo "An error has occurred(jobline)!"
fi


if python3 profession.py ;then
  true
else
  echo "An error has occurred(profession)!"
fi



if python3 it_people.py ;then
  true
else
  echo "An error has occurred(itpeople)!"
fi
