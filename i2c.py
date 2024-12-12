import smbus
from time import sleep

bus = smbus.SMBus(1)

address = 0X48
ain0 = 0x40 #채널번호
ain1 = 0x41

def read(channel):
    bus.write_byte(address, channel)
    bus.read_byte(address)
    return bus.read_byte(address)


if __name__== "__main__":
    try:
        while True:
            data1 = read(ain0)
            data2 = read(ain1)
            print(f"조도센서 값: {data1}")
            print(f"온도센서 값: {data2}")
            sleep(0.5)

    except KeyboardInterrupt:
        pass
