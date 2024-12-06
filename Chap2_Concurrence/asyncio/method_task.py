import asyncio 

async def worker(name, sleep_time):
    print(f" {name} : Je commence à travailler")
    await asyncio.sleep(sleep_time)
    print( f"{name} Finis de travailer")
    raise ValueError("ERROR")
    return name

async def main():
    task1 = asyncio.create_task(worker("Numero 1", 5))
    print(f" cancelled ? {task1.cancelled()}")
    print(f" done 1 ? {task1.done()}")
    #print(f" result is {task1.result()}")
    try:
        await task1
    except Exception as e:
        print(f"{e}")
    print(f" exception ? {task1.exception()}")
    print(f" done 2 ? {task1.done()}")
    print(f" result is {task1.result()}")
    


asyncio.run(main())
