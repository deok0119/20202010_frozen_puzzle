# 20202010_frozen_puzzle

## 라이브러리
게임을 만들기 위한 "bangtal", 퍼즐을 임의로 섞기 위한 "random", 시간을 측정하기 위한 "time"을 import 해주었습니다.
```python
from bangtal import *
import random
import time
```

## 초기 설정 및 장면 설정
setGameOption() 함수를 이용해 인벤토리 창과 메시지 박스를 비활성화 시켰습니다.

미리 제작해 둔 퍼즐도안을 배경으로하여 장면을 설정해줍니다.

게임을 실행하는 동안 재생될 배경음악을 선언해줍니다.
```python
setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene0=Scene("겨울왕국2 퍼즐", "images/배경.png")

bgm0=Sound("Images/Into The Unknown(piano.ver).mp3")
def scene0_onEnter():
    bgm0.play(True)
scene0.onEnter=scene0_onEnter
```

## 퍼즐조각의 위치를 기록 할 리스트 선언
본 퍼즐은 4*4규격으로 이루어졌습니다. 추후 위치를 바꿀 때, 보다 명료하고 간단한 코딩을 위하여 사전에 각각 퍼즐 자리의 x, y좌표를 나타낸 
리스트를 선언 해주었습니다. 가장 왼쪽 위 조각부터 1번(리스트의 인덱스는 0번부터 시작! [1번 조각=인덱스 0])이고 오른쪽으로 갈수록 순서가 증가합니다.

location[] 리스트는 퍼즐조각이 현재 어디에 위치하는지 알려줍니다.(ex. location[0]=12 :1번 조각(인덱스 0)의 현재위치는 13번 자리(인덱스 12)이다.)

chk[] 리스트는 현재 각 위치의 조각 존재 유무를 기록합니다. 빈 곳은 0, 채워진 곳은 1로 기록됩니다. 초기에는 모두 1로 선언한 후 조각을 섞고
 난 후 0을 할당하게 됩니다.
```python
location=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
location_x=[300, 470, 640, 810, 300, 470, 640, 810, 300, 470, 640, 810, 300, 470, 640, 810]
location_y=[530, 530, 530, 530, 361, 361, 361, 361, 191, 191, 191, 191, 21, 21, 21, 21]
chk=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```

## 오브젝트
퍼즐의 조각들을 오브젝트로 생성합니다. 이때 각 오브젝트 변수에 선언된 .flag 변수는 위 location[] 등에서 다양한 요소들을 호출하기 위한 인덱스 입니다.
```python
p1=Object("images/조각1.jpg")
p1.flag=0
p1.locate(scene0, location_x[p1.flag], location_y[p1.flag])
p1.show()

p2=Object("images/조각2.jpg")
p2.flag=1
p2.locate(scene0, location_x[p2.flag], location_y[p2.flag])
p2.show()
`
`
`
p15=Object("images/조각15.jpg")
p15.flag=14
p15.locate(scene0, location_x[p15.flag], location_y[p15.flag])
p15.show()
```
게임을 시작하기 위한 'play'버튼, 종료하기 위한 'quit'버튼도 선언했습니다.
```python
play=Object("images/play.png")
play.locate(scene0, location_x[15], location_y[15])
play.show()

quit=Object("images/종료.png")
quit.locate(scene0, location_x[12], location_y[12])
```

## play(게임 시작), 퍼즐 섞기
우선 프로그램을 실행시키면 최초 1번에 trial변수(시도횟수)가 0으로 선언되고, 최고기록을 나타내는 record_time에 일단 기준시부터 지금까지의 시간,
 record_try(최고기록을 갱신한 차수)에 0이 선언됩니다. play_now는 현재 게임진행중인지 나타내는 변수입니다.
```python
trial=0
record_time=time.time()
record_try=0
play_now=False
```
play버튼을 누르면 먼저 play버튼과 quit버튼을 숨깁니다. 다음으로 퍼즐을 섞게 되는데 원리는 다음과 같습니다.

* 셔플원리
  1. 0~3(4개, 각각 상하좌우 이동 의미) 중 임의의 난수를 random.randrange() 함수로 생성합니다.
  2. 발생한 난수을 idx변수(인덱스)에 저장하고 이는 빈공간(빈공간 위치: location[15])을 옮기는 인자가 됩니다.
  3. 이제 if문을 이용하여 각각 인덱스에 따른 상하좌우 이동이 가능한지 파악 후 이동을 시작합니다. (이동이 불가능한 경우: 빈공간이 위로
  이동해야하는데 빈공간의 y좌표가 맨 위에 도달한 상태일때->다음 난수 생성)
  4. 이동이 가능한 상태라면 이동해야 할 위치에 존재하는 조각과 위치를 바꿉니다.
  5. 수차례 반복해 퍼즐을 섞습니다.

위의 과정에서 특별한 점은 4번에서 이동해야 할 위치에 어떤 조각이 존재하는지 파악하는 과정입니다. 이에 해당하는 코드는 다음과 같습니다.
```python
target=location.index(location[15]+1)
```
이는 오른쪽으로 이동할 때 오른쪽에 있는 퍼즐 조각의 인덱스를 target변수로 저장하는 코드입니다. 우선 빈공간 오른쪽의 위치는 location[15]+1 임을 쉽게
 알 수 있습니다. 이 위치에 존재하는 퍼즐의 인덱스를 파악하기 위해서 .index()함수를 사용했습니다. location.index()를 사용하면 location 리스트에
내가 찾고자 하는 요소의 인덱스를 출력해줍니다.

전체 play함수는 다음과 같습니다.
```python
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
    `
    `
    p15.locate(scene0, location_x[location[14]], location_y[location[14]])

    p1.show()
    p2.show()
    `
    `
    p15.show()

    global chk
    chk[location[15]]=False

    global trial
    trial+=1

    global start_time
    start_time=time.time()
    play_now=True
play.onMouseAction=play_onMouseAction
```
마지막으로 셔플이 끝나고 빈공간의 위치를 chk리스트에 기록합니다.

trial변수를 1 증가시킴으로써 시도횟수를 증가시키고 추후 소요시간 측정하기 위해 종료시간과 연산할 시작시간을 기록합니다.

play_now를 활성화시켜 게임중임을 나타냅니다.

## move(조각 이동)
play_now가 활성화되어 있을시만 move함수를 사용가능합니다.

드래그 방향에 따라 이동하려는 위치에 chk[]가 0임을 확인해 빈곳임을 파악했을 때만 이동을 가능하게 합니다. 
또한 조각의 현재위치가 가장 끝 줄에 위치한지도 파악해 이동가능성을 파악합니다.
만약 조건을 충족하여 이동이 가능하다면 chk[현재위치]=0을 실행해 원래 위치한 곳이 빈 곳이 됐음을 명시하고, 이동 "후" 다시 chk[현재위치]=1을 
통해 이동한 위치가 채워졌음을 명시합니다.

```python
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
```
move 함수를 실행 할 때 마지막마다 퍼즐의 완성을 체크합니다.

만약 퍼즐이 완성되었다면 종료시간을 체크하고 시작시간과 비교하여 소요시간을 계산해 출력합니다.
그리고 소요시간이 record_time에 기록된 최단시간 보다 작다면 기록을 갱신하게 됩니다.
"시도횟수, 소요시간, 최단기록 해당차수, 최단기록"을 출력함으로써 해당 시도는 종료됩니다.
마지막으로 play_now를 비활성화하고 play버튼과 quit버튼을 show()해 재시작을 하려면 play버튼을, 그대로 게임을 종료하려면 quit버튼을 누르면 됩니다.
