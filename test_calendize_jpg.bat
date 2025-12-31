@ECHO OFF

del .\temp\*.png

uv run python calendize.py 2022 testImages\jpg  .\temp

explorer .\temp
