
from bleak import BleakClient, discover, BleakError
import asyncio

#temperatureUUID = "45366e80-cf3a-11e1-9ab4-0002a5d5c51b"
#ecgUUID = "46366e80-cf3a-11e1-9ab4-0002a5d5c51b"

notify_uuid = "0000{0:x}-0000-1000-8000-00805f9b34fb".format(0xFFE1)


def callback(sender, data):
    #print(data)
    a=data[:5]


    b=data[7:12]

    c=data[13:18]

    bytes_to_int(a)

    print("xaxis",a,"yaxis",b,"zaxis",c)
    e=data
    abc=bytes_to_int(a)
    print(abc)
    cbd=bytes_to_int(b)
    print(cbd)
    ebd=bytes_to_int(c)
    print(ebd)
   # f= len(data)

   # print("values",e)
def bytes_to_int(bytes):
    result = 0

    for b in bytes:
        result = result * 256 + int(b)

    return result
def run(addresses):
    loop = asyncio.get_event_loop()

    tasks = asyncio.gather(*(connect_to_device(address, loop) for address in addresses))

    loop.run_until_complete(tasks)


async def connect_to_device(address, loop):
    print("starting", address, "loop")
    async with BleakClient(address, loop=loop, timeout=5.0) as client:

        print("connect to", address)
        try:
            await client.start_notify(notify_uuid, callback)
            await asyncio.sleep(20, loop=loop)
            await client.stop_notify(notify_uuid)
        except Exception as e:
            print(e,"exception")

    print("disconnect from", address)


if __name__ == "__main__":
    run(
        ["90:E2:02:91:5E:5C"]
    )
