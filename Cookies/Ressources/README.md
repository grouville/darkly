Link of the video demonstration of the exploit :
https://www.loom.com/share/24b75a384bf544719eadd83e8d2eefae

Fix : 

Don't store cookies privilege on a bool, check server side if that cookie is still up-to-date and if it has privileges. Generate cookies upon connection, with a timeout
