@ECHO OFF

del .\temp\*.png

python calendize.py 2022 testImages\png  .\temp -a 0.7 --dpi 250 -c purple -t cyan -b 100 -r 60

explorer .\temp
