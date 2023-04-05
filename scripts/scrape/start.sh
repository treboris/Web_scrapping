#!/usr/bin/env bash


if python3 cvonline.py ;then
  true
else
  echo "An error has occurred(cvonline)!"
fi


if python3 it_people.py ;then
  true
else
  echo "An error has occurred(itpeople)!"
fi


if python3 jobline.py ;then
  true
else
  echo "An error has occurred(jobline)!"
fi


if python3 kariera_new.py ;then
  true
else
  echo "An error has occurred(kariera)!"
fi


if python3 professia.py ;then
  true
else
  echo "An error has occurred(professia)!"
fi


if python3 profession.py ;then
  true
else
  echo "An error has occurred(profession)!"
fi

if python3 stepstone.py ;then
  true
else
  echo "An error has occurred(stepstone)!"
fi
