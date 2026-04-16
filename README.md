
This is my personal logging system, for now its just a small change in the Structlog changing the names of the errors.

# TODO: 
- Add parameter to append the name of the file where the logger is being called at.
- Change the .exception to only return the errors of your code, not the imported libraries.
- Add a wrapper that disable this specific type of loggers when the wrapper is set to false
