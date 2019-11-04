On: /

There is a cookie called "I_am_admin", its value is the md5 for "false"

Modify it from the console with the md5 for "true" -> ```document.cookie="I_am_admin=b326b5062b2f0e69046810717534cb09"```

Finally refresh

This flaw is called Insecure Deserialization by OWASP
