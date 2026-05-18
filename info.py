print("Concurrency and Parallelism")

""""
Concurrency:
Switching between the tasks and 
Only one cpu core is engaged but 
there are multiple threads which are switching and performing the task 
threading.Thread
asyncio 
I/O bound tasks 
such as disk read and write, Web request


Parallelism:
Doing multiple tasks together, python uses multiple cores
multiprocessing.Process
concurrent.futures.ProcessPoolExecutor


Single threaded process and multi threaded process


######################################################
Asyncio: 
######################################################
async def
declare a coroutine: special function that can be paused
Async gives you coroutines: pause the execution until you are ready

await: to use this function must be async 
pause until the result is ready


asyncio : library which provides async and await feature 

event loop: engin that runs and schedule co-routines in 
time.sleep(3)
await asyncio.sleep(3)
in await you will wait but in non blocking fashion


######################################################
Pydantic: 
######################################################

Tries to convert data 

"""