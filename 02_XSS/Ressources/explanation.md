On: /?page=feedback

The Name field is not sanitized

You can test by removing the maxlength attribute and submitting: <h1 style="color: red;">Hello</h1>

You then get the flag by writting "script" (or only the first letters) in Name or Message