# Multichar
## Basic usage:
```
from multichar import multichar
multichar("Hello world")
```
## Using the waiting arguments:
Using a different wait function:
```
from multichar import multichar
def waiting:
  #the code that waits
multichar("Hello World", function_that_waits = waiting)
```
Writing text at a different speed:
```
from multichar import multichar
multichar("Hello World", amount_to_wait = 0.12)
multichar("Typing ever faster...", amount_to_wait = 0.08)
multichar("SLOW...", amount_to_wait = 0.2)
```
## Ending with a different character:
Printing the last part instantly:
```
from multichar import multichar
multichar("Loading... ", end="DONE\n")
```
Printing at different speeds (reference Using the waiting arguments section):
```
from multichar import multichar
multichar("Loading", end='')
multichar("...", amount_to_wait = 0.4)
```
# Char
Multichar secretly calls char() TO WORK ON