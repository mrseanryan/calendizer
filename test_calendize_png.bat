@ECHO OFF

del .\temp\*.png

python calendize.py 2022 testImages\png  .\temp

explorer .\temp
