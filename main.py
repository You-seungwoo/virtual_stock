
import random
import time

stocklist= {
    '삼성전자':[84000,1],
    '삼성물산':[155000,1],
    'SK하이닉스':[185700,1],
    '현대차':[225500, 1],
    '기아차':[210000, 1],
    '알리익스프레스':[125000,3],
    'LG전자':[250000,1],
    '하이버프':[220000,5],
    '넥슨':[80000,4],
    'NC':[20000,3],
    '한화':[500000, 2],
    '대성전자':[460000,5],
    '한성컴퓨터':[25000,4]
    }

bought_stock = []
stock_class = []
money = 10000000 # 기본 자본금
day = 1

def gamestart():
    input('가상 주식 투자\n주식 투자를 통해 1억(100,000,000원)을 벌어 게임을 클리어하세요.\n\nEnter 키를 눌러 시작하세요\n')

class stock:
    def __init__(self, name, initial, risk):
        self.name = name
        self.value = initial
        self.risk = risk

    def change_price(self):
        if self.value == -404:
            return

        self.value += random.randint(-(self.risk * 50000), self.risk * 40000)

        if self.value <= 5000:
            self.value = -404

    def sell_price(self):
        for i in range(len(bought_stock)):
            if bought_stock[i] == self.value:
                del bought_stock[i]

        return self.value

    def revalue(self):
        return self.value

    def rename(self):
        return self.name

for key, val in stocklist.items():
    locals()[key] = stock(key, val[0], val[1])
    stock_class.append(locals()[key])

gamestart()
while True:
    if money >= 100000000:
        print('끝! 소유금이 1억을 돌파했습니다.')
        print(f'걸린 기간 : {day}')
        break

    print(f'\n{"="*50}\n자본금 : {money}', end = '')

    print(f'\n보유주식 :', end='')
    for k in bought_stock:
         for i in stock_class:
            try:
                if i.rename() == k[0]:
                    if i.revalue() == -404:
                        del k
                        continue
                    print(f' {k[0]} ({k[1]}주)', end='')
            except:
                break

    print(f'\n{"="*18} {day}일차 : 주가 {"="*18}')

    print('='*50)
    for i in stock_class:
        if i.revalue() == -404:
            print(f'{i.rename()} 주가 : 상장폐지')
        else:
            print(f'{i.rename()} 주가 : {i.revalue()}')
    print('='*50)

    input_stock= str(input('(1) : 주식을 매수하기, (2) : 주식을 매도하기, (3) : 다음날로 넘어가기 >>> '))

    if input_stock == '1':
        qaz = False
        stock_name = input('매수할 주식의 이름을 입력하세요. >>> ')

        for i in stock_class:
            if i.rename() == stock_name:
                if i.revalue() == -404:
                    print('경고 : 폐지된 주식입니다.')
                    time.sleep(2)
                    break

                amonut = int(input(f'{i.rename()} 주식을 몇 주 구매하실건가요? >>> '))

                if money - amonut * i.revalue() >= 0:
                    money -= amonut * i.revalue()
                    bought_stock.append([i.rename(), amonut])
                    print(f'\n성공 : {i.rename()} 주식 {amonut}주를 성공적으로 구매했습니다.\n')

                else:
                    print('주식을 구매하기에 자본금이 부족합니다.')
                    time.sleep(2)
            qaz = True

        if qaz == False:
            print('\n경고 : 올바른 주식이름을 입력해주세요.\n')
            time.sleep(2)
            continue

    if input_stock == '2':
        paz2 = False
        stock_name = input('매도할 주식의 이름을 입력하세요. >>> ')

        for i in range(len(bought_stock)):
            if bought_stock[i][0] == stock_name:
                paz2 = True
                break

        if paz2 == False:
            print(f'{"="*50}\n경고 : 소유중이지 않거나 폐지 된 주식명입니다.\n{"="*50}')
            time.sleep(2)
            break

        for i in stock_class:
            if i.rename() == stock_name:
                amonut = int(input(f'{i.rename()} 주식을 몇 주 매도하실건가요? >>> '))

                for a in range(len(bought_stock)):

                    if bought_stock[a][0] == stock_name:
                        if bought_stock[a][1] - amonut <= 0:
                            money += amonut * i.revalue()
                            del bought_stock[a]

                        else:
                            money += amonut * i.revalue()
                            bought_stock[a][1] -= amonut

    if input_stock == '3':
        day += 1
        for i in stock_class:
            i.change_price()
        continue
