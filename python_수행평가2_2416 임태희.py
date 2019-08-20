#2416 임태희
#18개의 질문을 통해 자가진단을 진행합니다
#예를 들어, Q1의 답이 0이라면 Q4의 질문으로 답이 1이라면 Q2의 질문으로 넘어가는 방식입니다.
#함수 하나씩 질문을 넣어서 해당 질문의 답에 따라서 다음 함수를 호출해주는 방식으로 진행합니다.
print("FIND YOUR COLOR!")
print("♡쉽고 빠른 자가진단으로 나만의 컬러를 찾아보세요♡\n")
#함수 q1() ~ q18()과 spring(), summer(), autumn(), winter()를 생성해 줍니다.
#자가진단 결과를 spring(), summer(), autumn(), winter() 함수를 호출해서 알려준다.
#봄웜톤
def spring():
    print("당신은 ☆봄웜톤☆ 입니다!")
    print("이 타입의 사람들은 생기발랄하고 젊은 느낌을 줍니다.")
    print("피부색 >> 복숭아빛의 밝고 노란빛의 투명한 피부를 가지고 있습니다.")
    print("머리색 >> 대체로 눈동자색과 비슷한 밝은 갈색으로 윤기나고 찰랑찰랑한 머릿결을 가지고 있습니다.")
    print("눈동자색 >> 밝은갈색으로 빛이 나고 맑아 보입니다.")
    print("대표연예인 >> 수지, 설리, 아이유가 있습니다.\n")

#여름쿨톤
def summer():
    print("당신은 ☆여름쿨톤☆ 입니다!")
    print("이 타입의 사람들은 우아하고 여성스러운 느낌을 줍니다.")
    print("피부색 >> 핑크빛이 도는 혈색이 좋은 피부를 가지고 있습니다.")
    print("머리색 >> 약간 부시시한 회갈색 머리카락을 가지고 있습니다.")
    print("눈동자색 >> 차분하고 부드러운 갈색의 눈동자를 가지고 있습니다.")
    print("대표연예인 >> 손예진, 김하늘이 있습니다.\n")

#가을웜톤
def autumn():
    print("당신은 ☆가을웜톤☆ 입니다!")
    print("이 타입의 사람들은 어른스럽고 차분한 이미지를 가지고 있습니다.")
    print("피부색 >> 노르스름하며 윤기가 없고, 얼굴의 혈색이 없는 편입니다.")
    print("머리색 >> 윤기가 없는 짙은갈색입니다.")
    print("눈동자색 >> 짙고 깊이감있는 짙은 황갈색 계열입니다.")
    print("대표연예인 >> 이효리, 박정아, 탕웨이가 있습니다.\n")

#겨울쿨톤
def winter():
    print("당신은 ☆겨울쿨톤☆ 입니다!")
    print("이 타입의 사람들은 심플하면서 모던한 스타일로 도회적입니다.")
    print("피부색 >> 희고 푸른빛을 지니고 있어 차갑고 창백해 보입니다.")
    print("머리색 >> 푸른빛이 도는 짙은갈색이나 검은색입니다.")
    print("눈동자색 >> 검은색이나 짙은회갈색입니다.")
    print("대표연예인 >> 김혜수, 선우선이 있습니다.\n")

#질문 1
def q1():
    answer = input(">>당신의 피부톤은 어떻습니까? (0:하얀색이다, 1:검은색이다) : ")
    if(answer == "0"):
        q4()
    elif(answer == "1"):
        q2()
    else:
        q1()

#질문 2
def q2():
    answer = input(">>당신의 눈동자색은 무엇입니까? (0:검은색, 1:짙은갈색, 2:밝은갈색) : ")
    if(answer == "0"):
        q5()
    elif(answer == "1"):
        q5()
    elif(answer == "2"):
        q3()
    else:
        q2()

#질문 3
def q3():
    answer = input(">>당신과 잘 어울리는 아이섀도우 계열은 무엇입니까? (0:회색계열, 1:갈색계열) : ")
    if(answer == "0"):
        q5()
    elif(answer == "1"):
        q11()
    else:
        q3()

#질문 4
def q4():
    answer = input(">>당신의 눈 인상은 어떻습니까? (0:강한편, 1:부드러운편) : ")
    if(answer == "0"):
        q5()
    elif(answer == "1"):
        q7()
    else:
        q4()

#질문 5
def q5():
    answer = input(">>당신에게 어울리는 분홍색은 무엇입니까? (0:핫핑크, 1:코랄핑크) : ")
    if(answer == "0"):
        q10()
    elif(answer == "1"):
        q8()
    else:
        q5()

#질문 6
def q6():
    answer = input(">>연분홍색이나 연노란색처럼 포근하고 사랑스러운 색이 잘 어울리나요? (0:어울립니다, 1:어울리지 않습니다) : ")
    if(answer == "0"):
        q17()
    elif(answer == "1"):
        q14()
    else:
        q6()

#질문 7
def q7():
    answer = input(">>화장하지 않은 얼굴에 검은색 옷을 입으면 어떻습니까? (0:이목구비가 뚜렷하게 보입니다 1:얼굴색이 안 좋아보입니다) : ")
    if(answer == "0"):
        q10()
    elif(answer == "1"):
        q5()
    else:
        q7()

#질문 8
def q8():
    answer = input(">>당신에게 잘 어울리는 액세서리는 무엇입니까? (0:골드제품, 1:실버제품) : ")
    if(answer == "0"):
        q6()
    elif(answer == "1"):
        q9()
    else:
        q8()

#질문 9
def q9():
    answer = input(">>황토색, 겨자색, 이끼색, 적갈색처럼 차분하고 고상한 색이 잘 어울리나요? (0:어울립니다, 1:어울리지 않습니다) : ")
    if(answer == "0"):
        q15()
    elif(answer == "1"):
        q6()
    else:
        q9()

#질문 10
def q10():
    answer = input(">>당신의 첫인상은 어떻습니까? (0:강한인상, 1:부드러운인상, 2:평범한인상) : ")
    if(answer == "0"):
        q13()
    elif(answer == "1"):
        q11()
    elif(answer == "2"):
        q8()
    else:
        q10()

#질문 11
def q11():
    answer = input(">>햇볕에 노출되면 피부가 어떻게 되나요? (0:잘 탑니다, 1:잘 타지 않습니다, 2:보기에 해당하지 않습니다) : ")
    if(answer == "0"):
        q9()
    elif(answer == "1"):
        q8()
    elif(answer == "2"):
        q12()
    else:
        q11()

#질문 12
def q12():
    answer = input(">>상대방이 보는 당신의 이미지는 어떻습니까? (0:친근감 있고 부드러운 이미지, 1:강하고 차가운 이미지) : ")
    if(answer == "0"):
        q17()
    elif(answer == "1"):
        q14()
    else:
        q12()

#질문 13
def q13():
    answer = input(">>당신과 잘 어울리는 색은 무엇입니까? (0:선명한 원색, 1:부드러운 파스텔색) : ")
    if(answer == "0"):
        q14()
    elif(answer == "1"):
        q8()
    else:
        q13()

#질문 14
def q14():
    answer = input(">>당신의 얼굴 가까이에 대보았을 때 가장 잘 어울리는 꽃은 무엇입니까? (0:붉은빛의 장미, 1:핑크빛의 튤립) : ")
    if(answer == "0"):
        q18()
    elif(answer == "1"):
        q17()
    else:
        q14()

#질문 15
def q15():
    answer = input(">>당신의 머리색은 무엇입니까? (0:진한갈색, 1:진한검은색, 2:밝은갈색, 3:부드러운검은색) : ")
    if(answer == "0"):
        q18()
    elif(answer == "1"):
        q18()
    elif(answer == "2"):
        q14()
    elif(answer == "3"):
        q14()
    else:
        q15()

#질문 16
def q16():
    answer = input(">>당신의 얼굴은 어려보이는 편입니까? (0:그렇습니다, 1:그렇지 않습니다) : ")
    if(answer == "0"):
        print("\n")
        spring()
    elif(answer == "1"):
        print("\n")
        autumn()
    else:
        q16()

#질문 17
def q17():
    answer = input(">>당신에게 잘 어울리는 니트색상은 무엇입니까? (0:노란기가 있는 따뜻한색, 1:푸른기가 있는 차가운색) : ")
    if(answer == "0"):
        q16()
    elif(answer == "1"):
        print("\n")
        summer()
    else:
        q17()

#질문 18
def q18():
    answer = input(">>당신이 어두운색 정장을 입는다면 어울리는 색상은 무엇입니까? (0:검은색계열, 1:회색계열, 2:어두운갈색계열) : ")
    if(answer == "0"):
        print("\n")
        winter()
    elif(answer == "1"):
        print("\n")
        winter()
    elif(answer == "2"):
        print("\n")
        autumn()
    else:
        q18()

#q1()함수 호출로 인해서 프로그램이 실행됩니다.
q1()