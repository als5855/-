import threading 
import time

number = 0 

def t1():
    global number #전역변수
    while True:
        number += 1
        print("쓰레드 1 실행")
        print(f"thread1 -> {number}")
        time.sleep(1)

def t2():
    global number
    while True:
        number += 1
        print("쓰레드 2 실행")
        print(f"theade2 -> {number}")
        time.sleep(1)

if __name__ == "__main__":
    thread1 = threading.Thread(target=t1, daemon=True) #하나의 프로세서를 실행하는 사용하는 단위
    thread2 = threading.Thread(target=t2, daemon=True)

    thread1.start()
    thread2.start()

    while True:
        print("main 실행중!!")
        print("main 실행중!!")
        time.sleep(3)
