#XejLang

My aim on the this project i was want to development project in field of programming language theory and I did


Is support one file for now

User Firstly start with prefix: ['CREATE', 'BUILD', 'DELETE'] after.
User have to select process: ['FOLDER', 'FILE', 'TEMPLATE'].

And free syntax but user have to use flag for statement like: -n "file.txt".

And user can not use one flag with all process:
    FILE = -n, -e,
    FOLDER = -n

    if user gonna use -n flag have to know -n type a string flag
        -n "string"  

    if user gonna use -e flag have to know -e flag using for add description into file 
        -e filename:"text of description to file"
        Not: When using -e flag works unlock syntax for extend

    if user gonna use -at flag have to know -at flag using for just build already template
        -at already template


If you wanna create comment line: 
        // Hello! I'm a comment line! 

When using BUILD prefix user does not need to process.
Just which use flag of -at (Already Template): 
        BUILD -at MVC  <- MVC is a ready template 


When you are did error in code throw the warn that project .d

