start /min labrad
ping 127.0.0.1 -n 3 > nul 
call activate python27 
start /min python data_vault.py & start /min python serial_server.py
ping 127.0.0.1 -n 3 > nul 
start /min python rvc_300.py & start /min python FTM_2400.py & start /min python valve_relay_server.py