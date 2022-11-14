# PythonFileManipulationDemo
This program was made for one of my class's labs. I chose to upload it to provide an example of how basic file manipulation can be used in Python.

## ```add_user```
This function takes a string as its argument and appends it to the end of the file (which is created if it does not already exist). I use the 'a' argument as I only need to append the string to the end of the file; I do not want to overwrite the entire file. "\n" is used to make sure each user is on its own line.

## ```update_user```
Takes two strings as arguments: old and new. The function uses   ```f.readlines()```   to create a list, with each element being one line of our file. It iterates through the list replacing all line that match the old argument with the new argument. "\n" is added to the new argument and is accounted for while matching the old ones. ```writelines()```   is used to overwrite the file with the new set of users from the list.

## ```remove_user```
Same process as   ```update_user```   but instead of replacing the given user, it simply removes it. Takes one argument: user to remove. Puts the lines in a list with   ```readlines()```   , iterates through them removing all strings that match the given argument, and rewrites the file with the new set of users per our list.

## ```with open('users.txt', 'a') as f:```   VS   ```f = open('users.txt', 'a')```
```with open('users.txt', 'a') as f:```   removes the requirement of explicitly closing the file. Aside from that, the two are functionally the same. ```f = open('users.txt', 'a')```   must be closed manually and the file can be used repeatedly until closed. Using "with", the file can be used repeatedly while indented within the statement, after which the file closes automatically.
