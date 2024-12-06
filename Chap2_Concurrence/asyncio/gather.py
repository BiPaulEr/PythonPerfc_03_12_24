import asyncio 

async def worker(name, sleep_time):
    print(f" {name} : Je commence à travailler")
    await asyncio.sleep(sleep_time)
    print( f"{name} Finis de travailer")
    return name

async def main():
    list = await asyncio.gather(worker("Numero 1", 10), worker("Numero Bis", 5), worker("Numero TRois", 5))

    print(list)
   

asyncio.run(main())
