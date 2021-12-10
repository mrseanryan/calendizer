@ECHO OFF

SETLOCAL

SET _IMAGE=temp\02-February-2022.png

IF EXIST %_IMAGE% (del %_IMAGE%)
del .\temp\*.png

python render_calendar_tables.py 2022 .\temp

explorer .\temp
explorer %_IMAGE%
