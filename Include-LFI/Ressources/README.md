Link of the video demonstration of the exploit :
https://www.loom.com/share/0b7e1a7e77c449fe952a8421fdf39dff

Fix : Configure properly your Apache or Nginx
==> 

Local File Inclusion can be devastating. There is a reason it was listed in the OWASP top 10 list. This brings us to some suggestions that can help you with your LFI issues:
– ID assignation (save your file paths in a secure database and give an ID for every single one, this way users only get to see their ID without viewing or altering the path)
– Whitelisting (Use the verified and secured whitelist files and ignore everything else)
– Use databases (Don’t include files on a web server that can be compromised, use a database)
– Better server instructions (Make the server send download headers automatically instead of executing files in a specified directory)
