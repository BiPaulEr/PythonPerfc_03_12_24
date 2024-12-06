import asyncio 

async def worker(name, sleep_time):
    print(f" {name} : Je commence à travailler")
    await asyncio.sleep(sleep_time)
    print( f"{name} Finis de travailer")
    return name

def print_task(task):
    print(f"RESULT is {task.result()}")
    
async def main():
    task1 = asyncio.create_task(worker("Numero 1", 5))
    task1.add_done_callback(print_task) 
    task1.add_done_callback(print_task) 
    task1.add_done_callback(print_task) 
    task1.add_done_callback(print_task) 
    await task1

asyncio.run(main())
