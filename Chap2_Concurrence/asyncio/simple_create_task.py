import asyncio 

async def worker(name, sleep_time):
    print(f" {name} : Je commence à travailler")
    await asyncio.sleep(sleep_time)
    print( f"{name} Finis de travailer")
    return name

async def main():
    await asyncio.create_task(worker("Numero 1", 10))
    await asyncio.create_task(worker("Numero Bis", 5))

asyncio.run(main())
