@ECHO OFF

SETLOCAL

SET _IMAGE=temp\02-February-2022.png

IF EXIST %_IMAGE% (del %_IMAGE%)
del .\temp\*.png

python calendizer.py testImages\png  .\temp

explorer .\temp
explorer %_IMAGE%
