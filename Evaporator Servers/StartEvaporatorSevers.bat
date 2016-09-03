start /min labrad
ping 127.0.0.1 -n 3 > nul 
start /min python data_vault.py & start /min python serial_server.py
ping 127.0.0.1 -n 3 > nul 
start /min python rvc_300.py & start /min python FTM_2400.py & start /min python ValveRelayBoxEvaporator.py & start /min python TDK_GEN10-240.py & start /min python StepperBoxEvaporator.py