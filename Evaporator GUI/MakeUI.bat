@ECHO OFF
call activate Python27

pyuic4 EvaporatorUIv3.ui -o EvaporatorUI.py & pyuic4 dataCollectorUIv3.ui -o dataCollectorUI.py
