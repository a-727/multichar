def char(text, wait_function = None, wait_amount = 0.15):
  if wait_function is None:
    from time import sleep
    wait_function = sleep
  print(text, end="", flush=True)
  wait_function(wait_amount)
def multichar(text, function_that_waits = None, amount_to_wait = 0.15, end="\n"):
  if function_that_waits is None:
    from time import sleep
    function_that_waits = sleep
  for i in text:
    char(i, function_that_waits, amount_to_wait)
  print(end=end)
def filechar(text, fileObject, wait_function = None, wait_amount = 0.15):
  if wait_function is None:
    from time import sleep
    wait_function = sleep
  print(text, end="", flush=True, file=fileObject)
def filemultichar(text, fileObject, function_that_waits = None, amount_to_wait = 0.15, end="\n"):
  if function_that_waits is None:
    from time import sleep
    function_that_waits = sleep
  for i in text:
    filechar(i, fileObject, function_that_waits, amount_to_wait)
  print(end=end, file=fileObject)