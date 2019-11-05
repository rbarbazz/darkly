On: ```/?page=feedback```

### Flaw
The Name field is not sanitized.

You can test by removing the maxlength attribute and submitting: ```<h1 style="color: red;">Hello</h1>```

If you can submit HTML you can potentially submit Javascript which could then be executed next time another user displays the comment.

### Flag
You then get the flag by writting ```script``` (or only the first letters) in the Name or Message fields.
