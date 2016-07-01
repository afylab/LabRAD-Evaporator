@ECHO OFF
call activate Python27

pyuic4 EvaporatorUI.ui -o EvaporatorUI.py & pyuic4 dataCollectorUI.ui -o dataCollectorUI.py
