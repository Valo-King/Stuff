del C:\Windows\softwaredistribution2
del C:\Windows\system32\catroot2v2
net stop cryptsvc
net stop wuauserv
net stop bits
net stop msiserver
ren C:\Windows\SoftwareDistribution softwaredistribution2
ren C:\Windows\system32\catroot2 catroot2v2
net start bits
net start cryptsvc
net start msiserver
net start wuauserv
