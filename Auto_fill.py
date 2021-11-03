import pyautogui as pg
import time

def auto_fill_ggfrom():
    pg.click(x=374,y=312)
    pg.sleep(1)
    pg.click(x=374,y=429)
    pg.sleep(1)
    pg.click(x=374,y=490)
    pg.sleep(1)
    pg.click(x=374,y=616)
    pg.sleep(1)
    pg.click(x=374,y=743)
    pg.sleep(1)
    pg.click(x=374,y=796)
    pg.sleep(1)
    pg.click(x=374,y=874)
    pg.sleep(3)
    pg.click(x=374,y=260)
    pg.sleep(3)

def position_check():
    position = pg.position()
    print(position)

def main():
    time.sleep(5)
    loop = 0
    while loop < 30:
        auto_fill_ggfrom()
        loop += 1

main()