import random
import time

class printColors:
    CYAN = "\033[1;36m"      # 青蓝色
    END = '\033[0m'
print(printColors.CYAN + "V1nny日语五十音" + printColors.END)
print(printColors.CYAN + "欢迎使用V1nny日语五十音，版权©归v1nny所有，请勿用于商用" + printColors.END)
def choose():
    global num
    num = input('请输入你要检测的假名数量，最大50: ')
    num = int(num)
choose()
if num >= 51:
    choose()

def main():
    yin = random.randint(0, num)
    jm_type = random.randint(0, 2)
    jm_type = int(jm_type)
    yin = int(yin)
    jm = ['a','i','u','e','o','ka','ki','ku','ke','ko','sa','si','su','se','so','ta','ti','tu','te','to','na','ni','nu','ne','no','ha','hi','hu','he','ho','ma','mi','mu','me','mo','ya','i','yu','e','yo','ra','ri','ru','re','ro','wa','i','u','e','wo','n']
    jmping = ['あ','い','う','え','お','か','き','く','け','こ','さ','し','す','せ','そ','た','ち','つ','て','と','な','に','ぬ','な','の','は','ひ','ふ','へ','ほ','ま','み','む','め','も','や','い','ゆ','え','よ','ら','り','る','れ','ろ','わ','い','う','え','を','ん']
    jmpian = ['ア','イ','ウ','エ','オ','カ','キ','ク','ケ','コ','サ','シ','ス','セ','ソ','タ','チ','ツ','テ','ト','ナ','ニ','ヌ','ネ','ノ','ハ','ヒ','フ','ヘ','ホ','マ','ミ','ム','メ','モ','ヤ','イ','ユ','エ','ヨ','ラ','リ','ル','レ','ロ','ワ','イ','ウ','エ','ヲ','ン']
    jm_type2 = ['平假名','片假名','片假名和平假名']
    print('你要检测的假名是:' + jm[yin])
    print('请写出它的:'+ jm_type2[jm_type])
    print('你有3秒时间思考')
    time.sleep(5)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    print('时间到')
    print('正确答案是:  ' + jmping[yin] + jmpian[yin])
    print('你答对了嘛')
    global c
    c = input("你还要玩吗？ （Y/N）: ")
    c = str(c)

while True:
    main()
    if c == 'N' or c == 'n':
        print('游戏结束，下次再见！')
        exit()