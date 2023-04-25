import random
import sys

import pygame as pg

delta = {
         pg.K_UP: (0, -1) ,
         pg.K_DOWN: (0, 1),
         pg.K_LEFT: (-1, 0),
         pg.K_RIGHT: (1, 0)
         }


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02-20230422/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02-20230422/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bb_img = pg.Surface((20, 20))
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # 練習1
    bb_img.set_colorkey((0, 0, 0))  # 練習1
    x, y = random.randint(0, 1600), random.randint(0, 900)
    vx, vy = +1, +1
    bb_rect = bb_img.get_rect()  # 練習3
    bb_rect.center = x, y  # 練習3
    kk_rect = kk_img.get_rect()
    kk_rect.center = 900, 400
    
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0
            
        tmr += 1

        key_lst = pg.key.get_pressed()
        for k, mv in delta.items():
            if key_lst[k]:
                kk_rect.move_ip(mv)

        if check_bound(screen.get_rect(), kk_rect) != (True, True):
            for k, mv in delta.items():
                if key_lst[k]:
                    kk_rect.move_ip(-mv[0], -mv[1])

        yoko, tate = check_bound(screen.get_rect(), bb_rect)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1

        bb_rect.move_ip(vx, vy)
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rect)
        screen.blit(bb_img, bb_rect)

        if kk_rect.colliderect(bb_rect):
            return

        pg.display.update()
        clock.tick(1000)

def check_bound(scr_rct: pg.Rect, obj_rct: pg.Rect) -> tuple[bool, bool]: 
    """
    オブジェクトが画面外or画面内を判定し,　真理値タプルを返す関数
    引数1 :
    """
    yoko, tate = True, True
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = False
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
    