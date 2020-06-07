weight, tall = input("몸무게(kg)와 키(cm) 입력 : ").split()

BMI = float(weight)/(float(tall)*float(tall))

if (20 <= BMI < 25):
    print("표준입니다")
else:
    print("체중관리가 필요합니다")