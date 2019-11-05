On: ```/?page=survey```

### Flaw
Change the value attribute to a high number and select that option.

This is an Input Validation flaw, the input should be checked on the backend to prevent from data manipulation.

Here we are dealing with a ```select``` input but this can be an issue with any input type.
