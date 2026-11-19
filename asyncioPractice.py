import asyncio


async def waits(param):
    await asyncio.sleep(param)
    return param


async def main():
    task1 = asyncio.create_task(waits(1))
    task2 = asyncio.create_task(waits(2))
    task3 = asyncio.create_task(waits(3))
    task4 = asyncio.create_task(waits(4))
    task5 = asyncio.create_task(waits(5))

    result1 = await task1
    print("Task 1 is finished!")
    result2 = await task2
    print("Task 2 is finished!")
    result3 = await task3
    print("Task 3 is finished!")
    result4 = await task4
    print("Task 4 is finished!")
    result5 = await task5
    print("Task 5 is finished!")

    print("The End!")


if __name__ == "__main__":
    asyncio.run(main())
