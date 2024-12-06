import asyncio 

async def worker(name, sleep_time):
    print(f" {name} : Je commence à travailler")
    await asyncio.sleep(sleep_time)
    print( f"{name} Finis de travailer")
    return name

async def main():
    for task in asyncio.as_completed((worker("Numero 1", 10), worker("Numero Bis", 2), worker("Numero TRois", 3), worker("Numero 6", 8))):
        result = await task
        print(result)
   

asyncio.run(main())
