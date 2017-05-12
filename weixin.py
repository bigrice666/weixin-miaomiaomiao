# 导入模块
from wxpy import *
import random
import math
# 初始化机器人，扫码登陆

def miaomiaomiao(content):
    print(content)
    emoji_list = ['(゜-゜)','(=`ｪ´=；)ゞ','(;´༎ຶД༎ຶ`)','⁄(⁄⁄•⁄ω⁄•⁄⁄)⁄','(´･_･`)','(｀∀´)','(:3[▓▓▓]','（╯‵□′）╯︵┴─┴','₍•͈˽•͈₎','∠( ᐛ 」∠)＿','(*ﾉωﾉ)','ヾ(*>∀＜*) ','(ฅωฅ*)','<(￣︶￣)/ ','(´⊙ω⊙`)','(๑•̀ω•́๑)','(≧∀≦)♪','(*/∇＼*)','(｡･ω･｡)ﾉ♡','( • ̀ω•́ )✧','(☆ω☆)','╮(￣⊿￣")╭','(′へ`、)','(ﾟﾛ ﾟﾉ)ﾉ','(*｀▽´*)','Ծ‸Ծ','(ฅ´ω`ฅ)','(。-`ω´-)','(ㅍ_ㅍ)','((((;°Д°))))','｢(ﾟﾍﾟ)','(〃ﾉωﾉ)','(*/ω＼*)','∑(O_O；)','(●′ω`●)','(｀Д´*)','(-ι_-)','٩(๑´3‘๑)۶','(≡Д≡；)']
    if '汪汪' in content or '狗子' in content or '狗狗' in content or '蘑菇' in content:
        sig_choices = ['？','！','~','~~~','？？？','？！','！！！']
        miao_count = random.randrange(1,15)
        reply_list = ['汪'] * miao_count
        sig_count = random.randrange(0,math.ceil(miao_count/2))
        emoji_count = random.randrange(0,2)
        if emoji_count == 0:
            emoji = ''
        else:
            emoji = random.choice(emoji_list)
        reply_list += [emoji]
        for i in range(sig_count+1):
            reply_list += [random.choice(sig_choices)]
        random.shuffle(reply_list)
        return ''.join(reply_list)
    if '你的主人' in content:
        return '屁股味！'
    if '笨狗' in content:
        return '汪( －з)'
    if '菇菇菇' in content:
        return '咕咕咕(*ﾉ▽ﾉ)'
    if '喂食' in content:
        return '汪汪ψ(*｀ω´)ψ'
    if '屁屁' in content:
        return '(｀Д´*)汪汪'
    if '博士' in content:
        return '博士(☆ω☆)屁股味！'
    if '不要你了' in content:
        return '✄╰ひ╯汪！'

if __name__ == '__main__':
    bot = Bot(console_qr=-2)
    bot.file_helper.send('微信机器人已成功登录')
    test_group = ensure_one(bot.groups().search('test_group'))
    fans_group = ensure_one(bot.groups().search('同好会'))
    zhuoyou_group = ensure_one(bot.groups().search('桌游'))
    listening_group = [test_group] + [fans_group] + [zhuoyou_group] + bot.friends()
    my_self = ensure_one(bot.friends().search('蘑菇萌萌的'))
    @bot.register(chats=[listening_group] + [fans_group] + [zhuoyou_group] + bot.friends(),except_self=False,msg_types=TEXT)
    def test_group_auto(msg):
        return miaomiaomiao(msg.text)
    @bot.register(chats=my_self,except_self=False,msg_types=TEXT)
    def turn_it_on_and_off(msg):
        if msg.text == 'off':
            bot.registered.disable()
            bot.registered.enable(turn_it_on_and_off)
            return '狗子走了汪'
        if msg.text == 'on':
            bot.registered.enable()
            return '狗子来了汪'
    bot.join()
    
