#!/bin/bash
if [ -z $3 ]
then 
  sphinx-build -a $1 $2
else
  if [ $3 == conf.py ]
  then
    sphinx-build -a $1 $2
  else
    mv conf.py conf.py_2
    mv $3 conf.py 
    sphinx-build -a $1 $2
    mv conf.py $3
    mv conf.py_2 conf.py
  fi
fi
