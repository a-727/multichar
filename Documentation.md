# Multichar
## Basic usage:
```python
from multichar import multichar
multichar("Hello world")
```
## Using the waiting arguments:
Using a different wait function:
```python
from multichar import multichar
def waiting():
    pass#the code that waits
multichar("Hello World", function_that_waits = waiting)
```
Writing text at a different speed:
```python
from multichar import multichar
multichar("Hello World", amount_to_wait = 0.12)
multichar("Typing ever faster...", amount_to_wait = 0.08)
multichar("SLOW...", amount_to_wait = 0.2)
```
## Ending with a different character:
Printing the last part instantly:
```python
from multichar import multichar
multichar("Loading... ", end="DONE\n")
```
Printing at different speeds (reference Using the waiting arguments section):
```python
from multichar import multichar
multichar("Loading", end='')
multichar("...", amount_to_wait = 0.4)
```
# Char
Multichar secretly calls char().
## Basic use:
Printing text and then waiting a little bit:
```python
from multichar import char
char("After this text you will need to wait 0.15 seconds, ")
char("as that's the default.")
```
Printing text and then waiting a while:
```python
from multichar import char
char("Now waiting 1 second...", wait_amount=1)
char("now longer...\n", wait_amount=2.5)
char("DONE!")
```
Notice how you have to specify the \n for it to appear... unlike multichar, it does not automatically generate it for you.
## Use in modules:
Rotatechar module (rotates a list of speeds)
```python
from multichar import char #This module needs the multichar module
def rotatechar(text: str, wait_list = [0.1, 0.2, 0.1, 0,15], end = '\n', pos = 0):
    for i in text:
        char(i, wait_amount = wait_list[pos])
        pos+=1
        if pos >= len(wait_list):
            pos = 0
    print(end=end)
```
Char isn't that powerful all on its own, but it can create cool modules (like multichar)!
# Filechar and Filemultichar:
Filechar and filemultichar are exactly the same as char and multichar, except they print out to a file-like object (other than `sys.stdout`). Pass the arguments the same way you would do for print. Note: these functions are in testing, they may not work.