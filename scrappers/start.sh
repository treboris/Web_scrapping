#!/usr/bin/env bash




if python3 cv_online.py ;then
  echo "Cvonline scrap executed."
else
  echo "An error has occurred(cvonline)!"
fi


if python3 jobline_scrap.py ;then
  echo "Jobline scrap executed."
else
  echo "An error has occurred(jobline)!"
fi

if python3 cv_online.py ;then
  echo "Profession scrap executed."
else
  echo "An error has occurred(profession)!"
fi
