import random

# 음식 데이터 ------------------------------------------------------------------------------------------------------------

file = 'fooddata.txt'

wholeFood = []
foodC = {}
foodK = {}
foodS = {}
foodCDict = {}

with open(file,mode='r',encoding='utf-8') as f:
    datas = f.readlines()
    for data in datas:
        if data =='endw\n':break
        wholeFood.append(data[:-1])
    flag = 0
    k = 1
    for data in datas:
        if data == 'endw\n':
            flag = 1
        elif flag:
            if data == 'endc\n': break
            if data[0] == 'c':
                key = data[1:-1]
                foodC[key] = []
                foodCDict[k] = key
                k +=1
            else:
                foodC[key].append(data[:-1])

    flag = 0
    for data in datas:
        if data == 'endc\n':
            flag = 1
        elif flag:
            if data == 'endk\n': break
            if data[0] == 'k':
                key = data[1:-1]
                foodK[key] = []
            else:
                foodK[key].append(data[:-1])
    flag = 0
    for data in datas:
        if data == 'endk\n':
            flag = 1
        elif flag:
            if data == 'ends\n': break
            if data[0] == 's':
                key = data[1:-1]
                foodS[key] = []
            else:
                foodS[key].append(data[:-1])


# -------------------------------------------
# 함수 기능 : 점심 메뉴 랜덤 돌리기 함수
#           1. 메뉴 추천 - 랜덤으로
#           2. 없는 메뉴 추가
#           3. 존재하는 메뉴 확인 - 추가된 메뉴도 확인 가능
#           4. 추가된 메뉴도 랜덤 메뉴판에 포함
#           5. 종료
# 함수 이름 : Whatismylunch()
# 매개 변수 : 없음
# 함수 결과 : 없음
# --------------------------------------------
def Whatismylunch():
    print('    ===========점심 메뉴 골라드려요============')
    mychoice = ''
    mychoice = input('    아무거나 드실래요? Y/N')
    # 빈 런치리스트
    lunchList = []
    # 아무거나 먹는다고 하면 전체 음식에서 랜덤으로 아무거나 추천
    if mychoice in ('Y', 'y'):
        return print(f'''    {wholeFood[random.randint(0, len(wholeFood) - 1)]} 드세요^^;;
    ======================================='''), checkPan()

    # 아무거나 안먹는다고 하면 취향 물어서 교집합 찾아 추천
    elif mychoice in ('N', 'n'):
        lunchSetC = foodCountry()
        lunchSetK = foodYNkuk()
        lunchSetS = foodYNspicy()
        # 교집합이 없다면 NoneMenu()와 menuPlus()함수 반환/ 있다면 lunchList에 교집합을 추가
        if lunchSetS.intersection(lunchSetK).intersection(lunchSetC) == set():
            return NoneMenu(), checkPan()
        else:
            lunchList.extend(lunchSetS.intersection(lunchSetK).intersection(lunchSetC))

    # y/n 말고 다른거 누르면 반환
    else:
        return print('    그냥 굶으세요.')

    # lunchList에 추가된 메뉴를 랜덤으로 돌려서 myLunch에 저장
    myLunch = lunchList[random.randint(0, len(lunchList) - 1)]
    print('\n    =================추천 결과=================')
    print(f'    오늘 점심으로 {myLunch} 추천드려용~!')
    print('    =========================================')

    checkPan()






# 땡기는 거 고르기 -----------------------------------------------------------------------------------------------------

# 빈 세트 생성 -> 교집합하기 위해

lunchSetC = set()
lunchSetK = set()
lunchSetS = set()


# -------------------------------------------
# 함수 기능 : 한식/중식/일식/양식 중에서 고르는 함수
#           + 메뉴 추가하면 추가된 음식의 나라도 나옴
# 함수 이름 : foodCountry()
# 매개 변수 : 없음
# 함수 결과 : lunchSetC
# --------------------------------------------
def foodCountry():
    print('    ==================메뉴판===================')
    cnt = 0
    for f in foodC.keys():
        cnt += 1
        print(f'     {cnt}. {f}')
    print('    =========================================')

    while True:
        foodCnumber = int(input("    땡기시는 음식의 번호를 입력해주세용!"))
        if foodCnumber in foodCDict.keys():
            lunchSetC.update(foodC[foodCDict[foodCnumber]])
            print(f'    {foodCDict[foodCnumber]}이 땡기시는군요!')
            break
        else:
            print('    메뉴판의 번호 중에서 골라주세요.')
    return lunchSetC


# -------------------------------------------
# 함수 기능 : 국물 있/없 중에서 고르는 함수
# 함수 이름 : foodYNkuk()
# 매개 변수 : 없음
# 함수 결과 : lunchSetK
# --------------------------------------------
def foodYNkuk():
    print('''
    ================취향고르기=================
    1. 국물 있는 음식            2. 국물 없는 음식
    =========================================
    ''')
    while True:
        foodKnumber = input("    땡기시는 음식의 번호를 입력해주세용!")
        if foodKnumber == '1':
            lunchSetK.update(foodK['국물 있는 음식'])
            print('    국물 있는게 땡기시는군요!')
            print('    =========================================')
            break
        elif foodKnumber == '2':
            lunchSetK.update(foodK['국물 없는 음식'])
            print('    국물 없는게 땡기시는군요!')
            print('    =========================================')
            break
        else:
            print('    메뉴판의 번호 중에서 골라주세요.')
    return lunchSetK


# -------------------------------------------
# 함수 기능 : 맵/안맵 중에서 고르는 함수
# 함수 이름 : foodYNspicy()
# 매개 변수 : 없음
# 함수 결과 : lunchSetS
# --------------------------------------------
def foodYNspicy():
    print('''
    ================취향고르기=================
    1. 매운 음식                  2. 안매운 음식
    =========================================
    ''')
    while True:
        foodSnumber = input('    땡기시는 음식의 번호를 입력해주세용!')
        if foodSnumber == '1':
            lunchSetS.update(foodS['매운 음식'])
            print('    매운 음식이 땡기시는군요!')
            print('    =========================================')
            break
        elif foodSnumber == '2':
            lunchSetS.update(foodS['안매운 음식'])
            print('    안매운 음식이 땡기시는군요!')
            print('    =========================================')
            break
        else:
            print('    메뉴판의 번호 중에서 골라주세요.')
    return lunchSetS




# -------------------------------------------
# 함수 기능 : 찾고자 하는 메뉴가 없을 때, 없다고 말해주고 랜덤으로 아무 음식 추천해주는 함수
# 함수 이름 : NoneMenu()
# 매개 변수 : 없음
# 함수 결과 : 없음
# --------------------------------------------
def NoneMenu():
    myLunch = wholeFood[random.randint(0, len(wholeFood) - 1)]


    print(f'''\n    =================== 엥 ===================
    죄송하지만 그런 메뉴는 없어용 ~ 아무거나 드세용! 
    =================랜덤 추천=================
    오늘 점심으로 {myLunch} 추천드려용~!
    =========================================
    혹시 그런 메뉴 알고 계시면 추천해주세용!

               ''')



# -------------------------------------------
# 함수 기능 : 찾고자 하는 메뉴가 없을 때, 메뉴 추가 하는 함수
# 함수 이름 : menuPlus()
# 매개 변수 : 없음
# 함수 결과 : 없음
# --------------------------------------------
def menuPlus():
    while True:
        print('    =================메뉴 추가=================')
        menuP = input('    메뉴를 추가하시겠어요?    Y/N ')
        if menuP in ('n', 'N'):
            print("    메뉴 추가가 종료되었습니다.")
            print('    =========================================')
            break
        elif menuP in ('y', 'Y'):
            while True:

                foodEx = input('    추가하려는 음식이 메뉴판에 없는 나라 음식인가요?    Y/N')

                if foodEx in ('y', 'Y'):
                    while True:
                        data = input('    음식의 특징을 입력해주세용!!  예)*식(ex 베트남식)/국물 있(없)는 음식/(안)매운 음식')
                        if list(data).count('/') == 2:
                            newfoodCon, newfoodK, newfoodS = data.split('/')
                            if newfoodCon.endswith('식') and newfoodK in ('국물 있는 음식', '국물 없는 음식') and newfoodS in (
                                    '매운 음식', '안매운 음식'):
                                newfoodname = input('    음식의 이름을 입력해주세용!')
                                if newfoodname in wholeFood:
                                    print('이미 메뉴에 있는 음식이에용')
                                    print('    =========================================')

                                    break
                                # dict 추가
                                foodCDict[str(len(foodCDict)+1)] = newfoodCon
                                foodC[newfoodCon] = [newfoodname]
                                foodK[newfoodK].append(newfoodname)
                                foodS[newfoodS].append(newfoodname)
                                # 전체 음식 리스트에 음식명 추가
                                wholeFood.append(newfoodname)
                                print(f'    {newfoodCon}/{newfoodK}/{newfoodS}인 {newfoodname}이(가) 메뉴판에 추가 되었어요!')

                                break
                            else:
                                print('    형식이 잘못 입력되었어요! 다시 입력해주세요.')
                        else:
                            print('    형식이 잘못 입력되었어요! 다시 입력해주세요.')
                    break
                elif foodEx in ('n', 'N'):
                    while True:
                        data = input('    음식의 특징을 입력해주세용!!  예)*식(ex 베트남식)/국물 있(없)는 음식/(안)매운 음식')
                        if list(data).count('/') == 2:
                            newfoodC, newfoodK, newfoodS = data.split('/')
                            if newfoodC in ('한식', '양식', '일식', '중식') and newfoodK in (
                            '국물 있는 음식', '국물 없는 음식') and newfoodS in ('매운 음식', '안매운 음식'):
                                newfoodname = input('    음식의 이름을 입력해주세용!')
                                if newfoodname in wholeFood:
                                    print('    이미 메뉴에 있는 음식이에용')
                                    print('    =========================================')
                                    break
                                # dict 추가
                                foodC[newfoodC].append(newfoodname)
                                foodK[newfoodK].append(newfoodname)
                                foodS[newfoodS].append(newfoodname)
                                # 전체 음식 리스트에 음식명 추가
                                wholeFood.append(newfoodname)
                                print(f'    {newfoodC}/{newfoodK}/{newfoodS}인 {newfoodname}이(가) 메뉴판에 추가 되었어요!')

                                break
                            else:
                                print('    형식이 잘못 입력되었어요! 다시 입력해주세요.')
                        else:
                            print('    형식이 잘못 입력되었어요! 다시 입력해주세요.')
                    break
                else:
                    print('    엥! Y 아니면 N을 입력해주세요!!')
        else:
            print('    엥! Y 아니면 N을 입력해주세요!!')

    return




# -------------------------------------------
# 함수 기능 : 선택지 판 제공하는 함수
# 함수 이름 : checkPan()
# 매개 변수 : 없음
# 함수 결과 : 없음
# --------------------------------------------
def checkPan():
    while True:
        print('''    1. 메뉴 돌리기          2. 메뉴 추가하기      
    3. 메뉴 확인하기        4. 프로그램 종료''')
        print('    =========================================')
        checkNum = input('    원하시는 번호를 선택해주세용!')
        if checkNum == '1':
            Whatismylunch()
        elif checkNum =='2':
            menuPlus()
        elif checkNum =='3':
            print('    =================전체 메뉴=================')
            print('\n'.join(f'    {c} : {f}' for c, f in foodC.items()))
            print('    =========================================')
        elif checkNum =='4':
            break
        else:
            print('    존재하는 번호만 입력하셔야죠!!!!')

# 함수 호출 -------------------------------------------------------------

Whatismylunch()
# noodleChoice()

# 추가 된 메뉴를 파일에 저장

with open(file,mode ='w',encoding='utf-8') as file:

    for i in wholeFood:
        file.write(i+ '\n')
    file.write('endw\n')

    for k in foodC:
        file.write('c'+k+'\n')
        for v in foodC[k]:
            file.write(v+'\n')
    file.write('endc\n')

    for k in foodK:
        file.write('k'+k+'\n')
        for v in foodK[k]:
            file.write(v+'\n')
    file.write('endk\n')

    for k in foodS:
        file.write('s'+k+'\n')
        for v in foodS[k]:
            file.write(v+'\n')
    file.write('ends\n')