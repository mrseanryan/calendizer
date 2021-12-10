SETLOCAL

SET _IMAGE=temp\pyplot-table-demo.png

IF EXIST %_IMAGE% (del %_IMAGE%)

python calendizer.py testImages\png  .\temp

explorer %_IMAGE%
