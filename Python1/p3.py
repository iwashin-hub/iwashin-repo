# coding:UTF-8
'''
Created on 2020/02/21

@author: iwaki-local
'''

import random

result_list=['あいこです。','あなたの勝ちです。','あなたの負けです。']
hand_list=['グー','チョキ','パー']

usr_str=input('1:グー　2:チョキ　3:パー　9:終わり　＞')

while usr_str != '9':
    if usr_str !='1' and usr_str!='2' and usr_str!='3':
        print('1～3の数字か9を入力してください。')
        print('')
    else:
        cpu_hand=random.randint(0,2)
        usr_hand=int(usr_str)-1
        print('')
        print('私は'+ hand_list[cpu_hand])
        print('あなたは'+ hand_list[usr_hand])
        print(result_list[cpu_hand-usr_hand])
        print('')

    usr_str=input('1:グー　2:チョキ　3:パー　9:終わり　＞')

else:
    print('')
    print('終わります。')
