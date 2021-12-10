@ECHO OFF

del .\temp\*.png

python calendize.py 2022 testImages\jpg  .\temp

explorer .\temp
