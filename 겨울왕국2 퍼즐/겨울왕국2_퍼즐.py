from bangtal import *
import random
import time

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene0=Scene("겨울왕국2 퍼즐", "images/배경.png")

bgm0=Sound("Images/Into The Unknown(piano.ver).mp3")
def scene0_onEnter():
    bgm0.play(True)
scene0.onEnter=scene0_onEnter

location=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
location_x=[300, 470, 640, 810, 300, 470, 640, 810, 300, 470, 640, 810, 300, 470, 640, 810]
location_y=[530, 530, 530, 530, 361, 361, 361, 361, 191, 191, 191, 191, 21, 21, 21, 21]
chk=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

p1=Object("images/조각1.jpg")
p1.flag=0
p1.locate(scene0, location_x[p1.flag], location_y[p1.flag])
p1.show()

p2=Object("images/조각2.jpg")
p2.flag=1
p2.locate(scene0, location_x[p2.flag], location_y[p2.flag])
p2.show()

p3=Object("images/조각3.jpg")
p3.flag=2
p3.locate(scene0, location_x[p3.flag], location_y[p3.flag])
p3.show()

p4=Object("images/조각4.jpg")
p4.flag=3
p4.locate(scene0, location_x[p4.flag], location_y[p3.flag])
p4.show()

p5=Object("images/조각5.jpg")
p5.flag=4
p5.locate(scene0, location_x[p5.flag], location_y[p5.flag])
p5.show()

p6=Object("images/조각6.jpg")
p6.flag=5
p6.locate(scene0, location_x[p6.flag], location_y[p6.flag])
p6.show()

p7=Object("images/조각7.jpg")
p7.flag=6
p7.locate(scene0, location_x[p7.flag], location_y[p7.flag])
p7.show()

p8=Object("images/조각8.jpg")
p8.flag=7
p8.locate(scene0, location_x[p8.flag], location_y[p8.flag])
p8.show()

p9=Object("images/조각9.jpg")
p9.flag=8
p9.locate(scene0, location_x[p9.flag], location_y[p9.flag])
p9.show()

p10=Object("images/조각10.jpg")
p10.flag=9
p10.locate(scene0, location_x[p10.flag], location_y[p10.flag])
p10.show()

p11=Object("images/조각11.jpg")
p11.flag=10
p11.locate(scene0, location_x[p11.flag], location_y[p11.flag])
p11.show()

p12=Object("images/조각12.jpg")
p12.flag=11
p12.locate(scene0, location_x[p12.flag], location_y[p12.flag])
p12.show()

p13=Object("images/조각13.jpg")
p13.flag=12
p13.locate(scene0, location_x[p13.flag], location_y[p13.flag])
p13.show()

p14=Object("images/조각14.jpg")
p14.flag=13
p14.locate(scene0, location_x[p14.flag], location_y[p14.flag])
p14.show()

p15=Object("images/조각15.jpg")
p15.flag=14
p15.locate(scene0, location_x[p15.flag], location_y[p15.flag])
p15.show()

play=Object("images/play.png")
play.locate(scene0, location_x[15], location_y[15])
play.show()

quit=Object("images/종료.png")
quit.locate(scene0, location_x[12], location_y[12])

trial=0
record_time=time.time()
record_try=0
play_now=False
def play_onMouseAction(x, y, action):
    play.hide()
    quit.hide()
    global play_now

    for i in range(101):
        idx=random.randrange(4)
        if idx==0 and location_y[location[15]]!=530:
            empty=location[15]
            target=location.index(location[15]-4)
            location[15]=location[target]
            location[target]=empty
        elif idx==1 and location_y[location[15]]!=21:
            empty=location[15]
            target=location.index(location[15]+4)
            location[15]=location[target]
            location[target]=empty
        elif idx==2 and location_x[location[15]]!=810:
            empty=location[15]
            target=location.index(location[15]+1)
            location[15]=location[target]
            location[target]=empty
        elif idx==3 and location_x[location[15]]!=300:
            empty=location[15]
            target=location.index(location[15]-1)
            location[15]=location[target]
            location[target]=empty

    p1.locate(scene0, location_x[location[0]], location_y[location[0]])
    p2.locate(scene0, location_x[location[1]], location_y[location[1]])
    p3.locate(scene0, location_x[location[2]], location_y[location[2]])
    p4.locate(scene0, location_x[location[3]], location_y[location[3]])
    p5.locate(scene0, location_x[location[4]], location_y[location[4]])
    p6.locate(scene0, location_x[location[5]], location_y[location[5]])
    p7.locate(scene0, location_x[location[6]], location_y[location[6]])
    p8.locate(scene0, location_x[location[7]], location_y[location[7]])
    p9.locate(scene0, location_x[location[8]], location_y[location[8]])
    p10.locate(scene0, location_x[location[9]], location_y[location[9]])
    p11.locate(scene0, location_x[location[10]], location_y[location[10]])
    p12.locate(scene0, location_x[location[11]], location_y[location[11]])
    p13.locate(scene0, location_x[location[12]], location_y[location[12]])
    p14.locate(scene0, location_x[location[13]], location_y[location[13]])
    p15.locate(scene0, location_x[location[14]], location_y[location[14]])

    p1.show()
    p2.show()
    p3.show()
    p4.show()
    p5.show()
    p6.show()
    p7.show()
    p8.show()
    p9.show()
    p10.show()
    p11.show()
    p12.show()
    p13.show()
    p14.show()
    p15.show()

    global chk
    chk[location[15]]=False

    global trial
    trial+=1

    global start_time
    start_time=time.time()
    play_now=True
play.onMouseAction=play_onMouseAction

def move(object, x, y, action):
    global play_now
    global location
    if play_now:
        if action==MouseAction.DRAG_RIGHT and not chk[location[object.flag]+1] and not location[object.flag]%4==3:
            chk[location[object.flag]]=0
            location[object.flag]+=1
            object.locate(scene0, location_x[location[object.flag]], location_y[location[object.flag]])
            object.show()
            chk[location[object.flag]]=1

        elif action==MouseAction.DRAG_LEFT and not chk[location[object.flag]-1] and not location[object.flag]%4==0:
            chk[location[object.flag]]=0
            location[object.flag]-=1
            object.locate(scene0, location_x[location[object.flag]], location_y[location[object.flag]])
            object.show()
            chk[location[object.flag]]=1

        elif action==MouseAction.DRAG_UP and not chk[location[object.flag]-4] and not location[object.flag]/4==0:
            chk[location[object.flag]]=0
            location[object.flag]-=4
            object.locate(scene0, location_x[location[object.flag]], location_y[location[object.flag]])
            object.show()
            chk[location[object.flag]]=1

        elif action==MouseAction.DRAG_DOWN and not chk[location[object.flag]+4] and not location[object.flag]/4==3:
            chk[location[object.flag]]=0
            location[object.flag]+=4
            object.locate(scene0, location_x[location[object.flag]], location_y[location[object.flag]])
            object.show()
            chk[location[object.flag]]=1

        if location[p2.flag]==1 and location[p3.flag]==2 and location[p4.flag]==3 and location[p5.flag]==4 and location[p6.flag]==5 and location[p7.flag]==6 and location[p8.flag]==7 and location[p9.flag]==8 and location[p10.flag]==9 and location[p11.flag]==10 and location[p12.flag]==11 and location[p13.flag]==12 and location[p14.flag]==13 and location[p15.flag]==14 and location[p1.flag]==0:
            end_time=time.time()
            total_time=end_time-start_time
            global record_time
            global record_try
            if total_time<record_time:
                record_time=total_time
                record_try=trial
            showMessage("<{:}번째 시도>\n{:.4}초 만에 성공!\n최단 기록: {:}차 시도 {:.4}초".format(trial, total_time, record_try, record_time))
            location[15]=15
            play.show()
            quit.show()
            play_now=False       
Object.onMouseActionDefault=move

def quit_onMouseAction(x, y, action):
    endGame()
quit.onMouseAction=quit_onMouseAction

startGame(scene0)
