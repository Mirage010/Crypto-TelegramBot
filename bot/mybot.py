import datetime
import random
import telebot
import sqlite3
from telebot import types
from pycoingecko import CoinGeckoAPI
from py_currency_converter import convert

cg = CoinGeckoAPI()

bot = telebot.TeleBot('5777543369:AAG63ElcUQ2L2pFi1MIPguK0ZYgRa4uZYvs')









# მთავარი გვერდი

@bot.message_handler(commands=['start'])
def view(message):
    if message.text == '/start':
        b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1.add(types.KeyboardButton('ყიდვა'), types.KeyboardButton('გაყიდვა'))
        b1.row(types.KeyboardButton('ავტორიზაცია/რეგისტრაცია'))
        msg = bot.send_message(message.chat.id, f'მოგესალმებით! \n\n'
                                                f'ამ ბოტის მეშვეობით შეძლებთ დააკონვერტიროთ კრიპტოვალუტები სტანდარტულ ვალუტაში (ლარი/აშშ დოლარი)\n\n'
                                                f'Crypto_Orcinus-ზე შეგიძლიათ დააკონვერტიროთ მხოლოდ მხარდაჭერილი სტაბილური კრიპტოვალუტები შესაბამისი ქსელის მეშვეობით \n \n'
                                                f'- USDT - ქსელები: Tron (TRC20), Solana, Polygon. BSC (BER20)\n'
                                                f'- USDC - ქსელები: Tron(TRC20) Solana, Polygon, BSC(BER20) \n'
                                                f'- BUSD - ქსელები: BSC (BER20)\n\n'
                                                f'Crypto_Orcinus-დან თქვენს საბანკო ანგარიშზე სტანდარტული ვალუტის (ლარი/აშშ დოლარი) გადარიცხვა მომხმარებლის ბანკის ანგარიშზე ხორციელდება კოინის ასახვიდან 20 წუთის განმავლობაში\n\n'
                                                f'', reply_markup=b1)
        bot.register_next_step_handler(msg, step)

################################################################################################
def main(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('ყიდვა'), types.KeyboardButton('გაყიდვა'))
    b1.row(types.KeyboardButton('ავტორიზაცია/რეგისტრაცია'))
    cr = bot.send_message(message.chat.id, 'ჩვენ ვართ მთავარ გვერდზე', reply_markup=b1)
    bot.register_next_step_handler(cr, step)

def step(message):
    if message.text == 'ყიდვა':
        repeat_all_message2(message)
    elif message.text == 'გაყიდვა':
        repeat_all_message(message)
    elif message.text == 'ავტორიზაცია/რეგისტრაცია':
        repeat_all_message100(message)
    else:
        main(message)
#################################################################################################






#####################################################################################################
def sign(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.row(types.KeyboardButton('ყიდვა'))
    b1.row(types.KeyboardButton('გაყიდვა'))
    cr = bot.send_message(message.chat.id, 'ჩვენ ვართ მთავარ გვერდზე', reply_markup=b1)
    bot.register_next_step_handler(cr, signstep)


def signstep(message):
    if message.text == 'ყიდვა':
        step4(message)
    elif message.text == 'გაყიდვა':
        usdtbtc(message)
    else:
        main(message)
#########################################################################################









##############################3
#########################3#####
###############################
################################ #######3 ავტორიზაცია რეგისტრაცია

def getAccess100(user_id):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT user_id FROM users WHERE user_id=?',(user_id,))
        result = cursor.fetchone()
        return result


def repeat_all_message100(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='რეგისტრაცია', url='https://t.me/Crypto_Orcinus_verificationBot')
    markup.add(btn_my_site)
    print(message.chat.id)
    bot.send_message(message.chat.id, message.text)
    access = getAccess(message.chat.id)
    if access:
        if access[0] == '1':
            bot.send_message(message.chat.id,'გამარჯობა ადმინო')
            sign(message)
        else:
            bot.send_message(message.chat.id,'სისტემაში შესვლა წარმატებით შესრულდა')
            sign(message)

    else:
        bot.send_message(message.chat.id,'თქვენი ტელეგრამ-ექაუნთი არ არის რეგისტრირებული სისტემაში, გაგრძელებისთვის გაიარეთ რეგისტრაცია', reply_markup=markup)
        main(message)


##############################
###########################
############################
#########################
###########################
#########################























####გაყიდვა- შესვლა-რეგისტრაცია
#######################################################




def getAccess(user_id):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT user_id FROM users WHERE user_id=?',(user_id,))
        result = cursor.fetchone()
        return result


def repeat_all_message(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='რეგისტრაცია', url='https://t.me/Crypto_Orcinus_verificationBot')
    markup.add(btn_my_site)
    print(message.chat.id)
    bot.send_message(message.chat.id, message.text)
    access = getAccess(message.chat.id)
    if access:
        if access[0] == '1':
            bot.send_message(message.chat.id,'გამარჯობა ადმინო')
            usdtbtc(message)
        else:
            bot.send_message(message.chat.id,'სისტემაში შესვლა წარმატებით შესრულდა')
            usdtbtc(message)

    else:
        bot.send_message(message.chat.id,'თქვენი ტელეგრამ-ექაუნთი არ არის რეგისტრირებული სისტემაში, გაგრძელებისთვის გაიარეთ რეგისტრაცია', reply_markup=markup)
        main(message)


# def captcha(message):
 #   button = types.ReplyKeyboardMarkup(resize_keyboard=True)
  #  button.add(types.KeyboardButton('დაბრუნება მთავარ გვერდზე'))
 #   global a, b
  #  a, b = random.randint(1, 10), random.randint(1, 10)
  #  msg = bot.send_message(message.chat.id, f'გაგრძელებისთვის გაიარეთ შემოწმება: {a} + {b} = ?', reply_markup=button)
 #   bot.register_next_step_handler(msg, captcha2)



#def captcha2(message):
  #  i = a + b
 #   if message.text == str(i):
  #      bot.send_message(message.chat.id, 'თქვენ წარმატებით გაიარეთ შემოწმება')
  #      usdtbtc(message)
  #  elif message.text == 'დაბრუნება მთავარ გვერდზე':
  #      main(message)

  #  else:
   #     bot.send_message(message.chat.id, 'თქვენ ვერ გაიარეთ შემოწმება, გთხოვთ გაიმეოროთ')
    #    captcha(message)

#################################### გაყიდვასშესვლა რეგისტრაციის დამთავრება
####################################
######################################
#######################################



##ყიდვასშესვლა რეგისტრაციის დაწყება
################################
##################################
##################################
def auto2(message):
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button.add(types.KeyboardButton('ავტორიზაცია ტელეგრამით'), types.KeyboardButton('რეგისტრაცია'))
    msg = bot.send_message(message.chat.id, 'შესასვლელად გაიარეთ ავტორიზაცია', reply_markup=button)
    bot.register_next_step_handler(msg, autoregister2)




def autoregister2(message):
    if message.text == 'ავტორიზაცია ტელეგრამით':
        repeat_all_message2(message)
    elif message.text == 'რეგისტრაცია':
        verification2(message)
    else:
        main(message)



def verification2(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(text='რეგისტრაცია', url='https://t.me/Crypto_Orcinus_verificationBot')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, 'გაიარეთ რეგისტრაცია ტელეგრამით', reply_markup=markup)
    if message.text:
        main(message)




def getAccess2(user_id):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT user_id FROM users WHERE user_id=?',(user_id,))
        result = cursor.fetchone()
        return result


def repeat_all_message2(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='რეგისტრაცია', url='https://t.me/Crypto_Orcinus_verificationBot')
    markup.add(btn_my_site)
    print(message.chat.id)
    bot.send_message(message.chat.id, message.text)
    access = getAccess(message.chat.id)
    if access:
        if access[0] == '1':
            bot.send_message(message.chat.id,'გამარჯობა ადმინო')
            step4(message)
        else:
            bot.send_message(message.chat.id,'სისტემაში წარმატებით შესრულდა')
            step4(message)

    else:
        bot.send_message(message.chat.id,'თქვენი ტელეგრამ-ექაუნთი არ არის რეგისტრირებული სისტემაში, გაგრძელებისთვის გაიარეთ რეგისტრაცია', reply_markup=markup)
        main(message)


#def captcha2_2(message):
 #   button = types.ReplyKeyboardMarkup(resize_keyboard=True)
 #   button.add(types.KeyboardButton('დაბრუნება მთავარ გვერდზე'))
  #  global a, b
  #  a, b = random.randint(1, 10), random.randint(1, 10)
  ##  msg = bot.send_message(message.chat.id, f'გაგრძელებისთვის გაიარეთ შემოწმება: {a} + {b} = ?', reply_markup=button)
   # bot.register_next_step_handler(msg, captcha22)



#def captcha22(message):
  #  i = a + b
   # if message.text == str(i):
  #      bot.send_message(message.chat.id, 'თქვენ წარმატებით გაიარეთ შემოწმება')
  #      step4(message)
  #  elif message.text == 'დაბრუნება მთავარ გვერდზე':
  #      main(message)

   # else:
   #     bot.send_message(message.chat.id, 'თქვენ ვერ გაიარეთ შემოწმება, გთხოვთ გაიმეოროთ')
  #      captcha2_2(message)



###############################
###############################
###############################
############################### ყიდვასშესვლა რეგეგისტრაცია დამთავრება
###############################
###############################


def usdtbtc(message):
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button.add(types.KeyboardButton('USDT'), types.KeyboardButton('USDC'), types.KeyboardButton('BUSD'), types.KeyboardButton('დაბრუნება'))

    msg = bot.send_message(message.chat.id, 'აირჩიეთ რომელი კრიპტოვალუტის გაყიდვა გსურთ გსურთ', reply_markup=button)
    bot.register_next_step_handler(msg, sellstep1)


def sellstep1(message):
    if message.text == 'USDT':
        usdtsell1(message)
    elif message.text == 'USDC':
        usdcsell1(message)
    elif message.text == 'BUSD':
        busd_sell(message)
    elif message.text == 'დაბრუნება':
        sign(message)
    else:
        sign(message)


############################USDC ##################################################################
def usdcsell1(message):                                                                           #
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button.row(types.KeyboardButton('USDC (Solana) - Solana Network'))
    button.row(types.KeyboardButton('USDC (BER20) - Binance Smart Chain'))
    button.row(types.KeyboardButton('USDC (TRC20) - Tron Network'))
    button.row(types.KeyboardButton('USDC (Polygon) - Polygon Newtork'))
    button.row(types.KeyboardButton('დაბრუნება'))
    msg = bot.send_message(message.chat.id, 'აირჩიეთ ქსელი', reply_markup=button)
    bot.register_next_step_handler(msg, usdcsell2)


################## USDC-s გაყიდვები
def usdcsell2(message):
    if message.text == 'USDC (Solana) - Solana Network':
        usdtsell1(message)
    elif message.text == 'USDC (BER20) - Binance Smart Chain':
        usdcsell1(message)
    elif message.text == 'USDC (TRC20) - Tron Network':
        main(message)
    elif message.text == 'USDC (Polygon) - Polygon Newtork':
        main(message)
    elif message.text == 'დაბრუნება':
        usdtbtc(message)
    else:                                                                                    #
        main(message)                                                                        #
##############################################################################################




#########################################################USDT##############################
def usdtsell1(message):                                                                    #
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)                                #
    button.row(types.KeyboardButton('USDT (TRC20) - TRON Network'))                         #
    button.row(types.KeyboardButton('USDT (Solana) - Solana Network'))
    button.row(types.KeyboardButton('USDT (Polygon) - Polygon Network'))
    button.row(types.KeyboardButton('USDT (BER20) - Binance Smart Chain'))
    button.row(types.KeyboardButton('დაბრუნება'))
    msg = bot.send_message(message.chat.id, 'აირჩიეთ ქსელი', reply_markup=button)
    bot.register_next_step_handler(msg, choise0usdtbatc)




def choise0usdtbatc(message):
    if message.text == 'USDT (TRC20) - TRON Network':
        usdtsell(message)
    elif message.text == 'USDT (Solana) - Solana Network':
        btcsell(message)
    elif message.text == 'USDT (Polygon) - Polygon Network':
        btcsell(message)
    elif message.text == 'USDT (BER20) - Binance Smart Chain':
        buy1(message)
    elif message.text == 'USDT (BER20) - Binance Smart Chain':
        buy1(message)
    elif message.text == 'დაბრუნება':
        usdtbtc(message)

    else:                                                                                                #
        buy1(message)                                                                                    #
##########################################################################################################
############################################################################################################
def busd_sell(message):                                                                           #
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button.row(types.KeyboardButton('BUSD (BER20) - Binance Smart Chain'))
    button.row(types.KeyboardButton('დაბრუნება'))
    msg = bot.send_message(message.chat.id, 'აირჩიეთ ქსელი', reply_markup=button)
    bot.register_next_step_handler(msg, choise_busd_sell)



def choise_busd_sell(message):
    if message.text == 'BUSD (BER20) - Binance Smart Chain':
        usdtsell(message)
    elif message.text == 'დაბრუნება':
        usdtbtc(message)
    else:
        usdtbtc(message)

















    ###############################################################
############################################################################# USDTS გაყიდვა
#####################################################              ########
#####################################################
def usdtsell(message):
    button = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id, 'გთხოვთ შეიყვანოთ თქვენი სახელი და გვარი', reply_markup=button)
    bot.send_message(message.chat.id,
                     'გაითვალისწინეთ, საბანკო ანგარიშის მფლობელის სახელი და გვარი უნდა ემთხვეოდეს შეკვეთის განმთავსებლის ინფორმაციას. წინააღმდეგ შემთხვევაში არ განხორციელდება ტრანზაქცია')
    bot.register_next_step_handler(msg, nameusdtcash)

#სახელის ველი

def nameusdtcash(message):
    try:
        global nickcash
        nickcash = {}
        msg = nickcash = message.text
        bot.register_next_step_handler(msg, usdtbankcash)
    except:
        usdtbankcash(message)



def usdtbankcash(message):
        button = types.ReplyKeyboardRemove()
    #    price = cg.get_price(ids='tether', vs_currencies='usd')
    #    msg = bot.send_message(message.chat.id, f'1 USDT = {float("{0:.3f}". format(price["tether"]["usd"] * 0.99))} USD\nმინიმალური თანხა გაცვლისთვის არის'
    #                                      f' 5 $')
        msg = bot.send_message(message.chat.id, 'მინიმალური თანხა გაცვლისთვის არის 5$')

        bot.send_message(message.chat.id,  'დაწერეთ რამდენი USDT-ს გაყიდვა გსურთ', reply_markup=button)
        bot.register_next_step_handler(msg, shemocusdtcash)







def shemocusdtcash(message):
    try:
        global courseusdtcash
        courseusdtcash = {}
        shemocusdt1cash = {}
        shemocusdt1cash["usdtbankcash"] = message.text
        courseusdtcash = float(shemocusdt1cash["usdtbankcash"])

        button = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button.add(types.KeyboardButton('საქართველოს ბანკი'), types.KeyboardButton('თბს ბანკი'),
                   types.KeyboardButton('თანხის შეცვლა'))
#        price = cg.get_price(ids='tether', vs_currencies='usd')

        if courseusdtcash >= 102:
            msg = bot.send_message(message.chat.id, f'თქვენ მიიღებთ {float("{0:.3f}". format(courseusdtcash * 0.99))}USD-ს  საბანკო ანგარიშზე ')
            bot.send_message(message.chat.id, f' აირჩიეთ ბანკი თანხის მისაღებად', reply_markup=button)
            bot.register_next_step_handler(msg, other_money_usdc)
        elif courseusdtcash >= 5:
            msg = bot.send_message(message.chat.id, f'თქვენ მიიღებთ {float("{0:.3f}". format(courseusdtcash - 1))}USD-ს  საბანკო ანგარიშზე ')
            bot.send_message(message.chat.id, f' აირჩიეთ ბანკი თანხის მისაღებად', reply_markup=button)

            bot.register_next_step_handler(msg, other_money_usdc)
        elif courseusdtcash == 'თანხის შეცვლა':
            usdtbankcash(message)





        else:
            bot.send_message(message.chat.id, 'თქვენი თანხა ნაკლებია მინიმალურზე, გთხოვთ შეცვალოთ')
            usdtbankcash(message)
    except ValueError:
        bot.send_message(message.chat.id, 'გთხოვთ შეიყვანოთ კორექტული მონაცემები')
        usdtbankcash(message)


def other_money_usdc(message):
    if message.text == 'თანხის შეცვლა':
        usdtbankcash(message)
    elif message.text == 'საქართველოს ბანკი':
        walletanswer(message)
    elif message.text == 'თბს ბანკი':
        walletanswer(message)











def walletanswer(message):
    global bankwalletname
    bankwalletname = {}
    bankwalletname["bankwalletaddres"] = message.text
    button = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id, ' გთხოვთ მიუთითოთ თქვენი საბანკო ანგარიშის ნომერი(IBAN)', reply_markup=button)
    bot.send_message(message.chat.id, 'ლარის- ანგარიშის შეყვანის შემთხვევაში თანხა ავტომატურად დაკონვერტირდება ლარზე')
    bot.register_next_step_handler(msg, usdtshemoc2cash)


def walletaddreserror(message):
    msg = bot.send_message(message.chat.id, ' გთხოვთ მიუთითოთ თქვენი საბანკო ანგარიშის ნომერი(IBAN)')
    bot.register_next_step_handler(msg, usdtshemoc2cash)





def usdtshemoc2cash(message):
    try:
        global walletusdtcash
        walletusdtcash = {}
        walletusdtcash["walletanswer"] = message.text
        if message.text.startswith('GE'):
            if courseusdtcash >= 102:
                bot.send_message(message.chat.id,f'თქვენ ცვლით {float("{0:.8f}".format(courseusdtcash))} USDT-ს {float("{0:.3f}".format(courseusdtcash * 0.99))} $-ში. \n'
                         f'თქვენი საბანკო ანგარიში: {walletusdtcash["walletanswer"]}')
            elif courseusdtcash >= 5:
                bot.send_message(message.chat.id,
                         f'თქვენ ცვლით {float("{0:.8f}".format(courseusdtcash))} USDT-ს {float("{0:.3f}".format(courseusdtcash - 1))} $-ში. \n'
                         f'თქვენი საბანკო ანგარიში: {walletusdtcash["walletanswer"]}')

                bot.send_message(message.chat.id, f'ჩვენ ველოდებით თქვენგან {float("{0:.8f}". format(courseusdtcash))} USDT-ს ჩარიცხვას  USDT(TRC20) კრიპტო მისამართზე ')
                bot.send_message(message.chat.id, '1231423რ23რფ2342323რ2342325234')
                button = types.ReplyKeyboardMarkup(resize_keyboard=True)
                button.add(types.KeyboardButton('ვადასტურებ გადახდას'))
                button.row(types.KeyboardButton('ოპერაციის გაუქმება'))
                msg = bot.send_message(message.chat.id, 'ჩარიცხვის შემდეგ გთხოვთ აუცილებლად  დაადასტურეთ გადახდა', reply_markup=button )
                bot.register_next_step_handler(msg, usdtfinishcash)
        else:
            bot.send_message(message.chat.id, 'მონაცემები არასწორია !')
            walletaddreserror(message)



    except ValueError:
        bot.send_message(message.chat.id, 'გთხოვთ მიუთითოთ თქვენი საბანკო ანგარიშის ნომერი!')
        walletanswer(message)








def usdtfinishcash(message):
    try:
        if message.text == 'ვადასტურებ გადახდას':
            ################################################# თუ 100$ზე მეტია
            if courseusdtcash >= 102:
                bot.send_message(message.chat.id, f'თქვენი მოთხოვნა მიღებულია \n'
                                          f'დრო: {datetime.datetime.now()}.\n'
                                          f'ბანკი: " {bankwalletname["bankwalletaddres"]}."\n'
                                          f'თქვენი საბანკო ანგარიში: " {walletusdtcash["walletanswer"]}."\n'
                                          f'{float("{0:.8f}". format(courseusdtcash * 0.99))} USD-ს ჩაირიცხება თქვენს საბანკო ანგარიშზე  30 წუთის განმავლობაში.\n'
                                          f'მადლობა ჩვენი რომ ჩვენი ბოტით სარგებლობთ')

                main(message)




                bot.send_message(789435088,  f"გადახდის თანხა: {float('{0:.7f}'.format(courseusdtcash))} USDC\n"
                             f" გადასარიცხი თანხა: {float('{0:.8f}'. format(courseusdtcash * 0.99))} USD\n"
                             f"საბანკო ანგარიში: \n\n"
                             f"{walletusdtcash['walletanswer']}\n\n"
                             f"ბანკი: {bankwalletname['bankwalletaddres']}\n"
                             f"სახელი გვარი: {nickcash}\n"
                             f"მოთხოვნის დრო: {datetime.datetime.now()}")

        if message.text == 'ვადასტურებ გადახდას':
            ################################################# თუ 100$ზე ნაკლებია
            if courseusdtcash <= 100:
                bot.send_message(message.chat.id, f'თქვენი მოთხოვნა მიღებულია \n'
                                                  f'დრო: {datetime.datetime.now()}.\n'
                                                  f'ბანკი: " {bankwalletname["bankwalletaddres"]}."\n'
                                                  f'თქვენი საბანკო ანგარიში: " {walletusdtcash["walletanswer"]}."\n'
                                                  f'{float("{0:.8f}".format(courseusdtcash - 1))} USD-ს ჩაირიცხება თქვენს საბანკო ანგარიშზე  20 წუთის განმავლობაში.\n'
                                                  'მადლობა ჩვენი რომ ჩვენი ბოტით სარგებლობთ')
                main(message)

                bot.send_message(789435088, f"გადახდის თანხა: {float('{0:.7f}'.format(courseusdtcash))} USDT (TRC20)\n"
                                            f" გადასარიცხი თანხა: {float('{0:.8f}'.format(courseusdtcash - 1))} USD\n"
                                            f"საბანკო ანგარიში: \n\n"
                                            f"{walletusdtcash['walletanswer']}\n\n"
                                            f"ბანკი: {bankwalletname['bankwalletaddres']}\n"
                                            f"სახელი გვარი: {nickcash}\n"
                                            f"მოთხოვნის დრო: {datetime.datetime.now()}")












     ##### შეგვიძლია სხვა ადამიანების დამატება

        elif message.text == 'ოპერაციის გაუქმება':
            sign(message)
        else:
            usdtshemoc2cash(message)

    except:
        usdtshemoc2cash(message)











############################################
############################################  ბტკს განაღდება
############################################
############################################
def btcsell(message):
    button = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id, 'გთხოვთ შეიყვანოთ თქვენი სახელი', reply_markup=button)
    bot.send_message(message.chat.id,
                     'გაითვალისწინეთ, საბანკო ანგარიშის თანხის მიმღების სახელი და გვარი უნდა ემთხვეოდეს თქვენს მიერ მითითებულ სახელსა და გვარს ')
    bot.register_next_step_handler(msg, namebtccash)

#სახელის ველი

def namebtccash(message):
    try:
        global nickbtccash
        nickbtccash = {}
        msg = nickbtccash = message.text
        bot.register_next_step_handler(msg, btcbankcash)
    except:
        btcbankcash(message)



def btcbankcash(message):
        button = types.ReplyKeyboardRemove()
        price = cg.get_price(ids='bitcoin', vs_currencies='usd')
        msg = bot.send_message(message.chat.id, f'1 BTC == {float("{0:.3f}". format(price["bitcoin"]["usd"] * 0.98))} USD\nმინიმალური თანხა გაცვლისთვის არის'
                                          f' 0.00523 BTC')
        bot.send_message(message.chat.id,  'დაწერეთ რამდენი BTC-ს გადაცვლა გინდათ USD-ში:', reply_markup=button)
        bot.register_next_step_handler(msg, shemocbtccash)







def shemocbtccash(message):
    try:
        global coursebtccash
        coursebtccash = {}
        shemocbtc1cash = {}
        shemocbtc1cash["btcbankcash"] = message.text
        coursebtccash = float(shemocbtc1cash["btcbankcash"])

        button = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button.add(types.KeyboardButton('საქართველოს ბანკი'), types.KeyboardButton('თბს ბანკი'),
                   types.KeyboardButton('ლიბერთი ბანკი'))
        price = cg.get_price(ids='bitcoin', vs_currencies='usd')
        if coursebtccash >= 0.00523:
            msg = bot.send_message(message.chat.id, f'თქვენ მიიღებთ {float("{0:.2f}". format(coursebtccash * price["bitcoin"]["usd"] * 0.98))}USD-ს  საბანკო ანგარიშზე ')
            bot.send_message(message.chat.id, f' აირჩიეთ ბანკი თანხის მისაღებად', reply_markup=button)



            bot.register_next_step_handler(msg, walletanswerbtc)
        else:
            bot.send_message(message.chat.id, 'თქვენი თანხა ნაკლებია მინიმალურზე, გთხოვთ შეცვალოთ')
            btcbankcash(message)
    except ValueError:
        bot.send_message(message.chat.id, 'გთხოვთ შეიყვანოთ კორექტული მონაცემები')
        btcbankcash(message)

def walletanswerbtc(message):
    global bankwalletnamebtc
    bankwalletnamebtc = {}
    bankwalletnamebtc["bankwalletaddresbtc"] = message.text
    button = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id, ' შეიყვანეთ თქვენი საბანკო ანგარიში', reply_markup=button)
    bot.register_next_step_handler(msg, btcshemoc2cash)




def btcshemoc2cash(message):
    global walletbtccash
    walletbtccash = {}
    walletbtccash["walletanswerbtc"] = message.text
    price = cg.get_price(ids='bitcoin', vs_currencies='usd')
    msg = bot.send_message(message.chat.id, f'თქვენ ცვლით {float("{0:.8f}". format(coursebtccash ))} BTC-ს {float("{0:.2f}". format(coursebtccash * price["bitcoin"]["usd"] * 0.98))} $-ში. \n'
                                      f'თქვენი საბანკო ანგარიში: {walletbtccash["walletanswerbtc"]}')
    bot.send_message(message.chat.id, f'ჩვენ ველოდებით თქვენგან {float("{0:.8f}". format(coursebtccash))} BTC-ს ჩარიცხვას  Bitcoin კრიპტო მისამართზე ')
    bot.send_message(message.chat.id, '1231423რ23რფ2342323რ2342325234')
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button.add(types.KeyboardButton('ვადასტურებ გადახდას'))
    button.row(types.KeyboardButton('ოპერაციის გაუქმება'))

    msg = bot.send_message(message.chat.id, 'ჩარიცხვის შემდეგ გთხოვთ აუცილებლად  დაადასტურეთ გადახდა', reply_markup=button )
    bot.register_next_step_handler(msg, btcfinishcash)







def btcfinishcash(message):
    try:
        price = cg.get_price(ids='bitcoin', vs_currencies='usd')
        if message.text == 'ვადასტურებ გადახდას':
            bot.send_message(message.chat.id, f'თქვენი მოთხოვნა მიღებულია \n'
                                          f'დრო: {datetime.datetime.now()}.\n'
                                          f'ბანკი: " {bankwalletnamebtc["bankwalletaddresbtc"]}."\n'
                                          f'{float("{0:.8f}". format(coursebtccash * price["bitcoin"]["usd"] * 0.98))} USD-ს ჩაირიცხება თქვენს საბანკო ანგარიშზე  20 წუთის განმავლობაში.\n'
                                           'მადლობა რომ ჩვენი ბოტით სარგებლობთ')
            main(message)

            bot.send_message(789435088, f"გადახდის თანხა: {float('{0:.7f}'.format(coursebtccash))} BTC\n"
                             f" გადასარიცხი თანხა: {float('{0:.8f}'. format(coursebtccash  * price['bitcoin']['usd'] * 0.98))} USD\n"
                             f"საბანკო ანგარიში: \n\n"
                             f"{walletbtccash['walletanswerbtc']}\n\n"
                             f"ბანკი: {bankwalletnamebtc['bankwalletaddresbtc']}\n"
                             f"სახელი გვარი: {nickbtccash}\n"
                             f"მოთხოვნის დრო: {datetime.datetime.now()}")
        elif message.text == 'ოპერაციის გაუქმება':
            buy1(message)
        else:
            btcshemoc2cash(message)
    except:
        btcshemoc2cash(message)





















######################################################
####################################################
######################################################    ყიდვის ველი
####################################################


def step4(message):
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button.add(types.KeyboardButton('USDT'), types.KeyboardButton('USDC'), types.KeyboardButton('დაბრუნება'))
    msg = bot.send_message(message.chat.id, 'აირჩიეთ რომელი კრიპტოვალუტის ყიდვა გსურთ', reply_markup=button)
    bot.register_next_step_handler(msg, choise0)



def choise0(message):
    if message.text == 'USDT':
        usdt_buy(message)
    elif message.text == 'USDC':
        usdc_buy(message)
    elif message.text == 'დაბრუნება':
        sign(message)
    else:
        sign(message)



def usdt_buy(message):
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button.row(types.KeyboardButton('USDT (TRC20) Solana Network'))
    button.row(types.KeyboardButton('დაბრუნება'))
    msg = bot.send_message(message.chat.id, 'აირჩიეთ ქსელი', reply_markup=button)
    bot.register_next_step_handler(msg, usdt_buyif)

def usdt_buyif(message):
    if message.text == 'USDT (TRC20) Solana Network':
        usdt_buy(message)
    elif message.text == 'USDC':
        usdc_buy(message)
    elif message.text == 'დაბრუნება':
        step4(message)
    else:
        main(message)





def usdc_buy(message):
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button.row(types.KeyboardButton('USDC (Solana) Solana Network'))
    button.row(types.KeyboardButton('დაბრუნება'))
    msg = bot.send_message(message.chat.id, 'აირჩიეთ ქსელი', reply_markup=button)
    bot.register_next_step_handler(msg, usdc_buyif)


def usdc_buyif(message):
    if message.text == 'USDC (Solana) Solana Network':
        usdt_buy(message)
    elif message.text == 'დაბრუნება':
        step4(message)
    else:
        step4(message)












#### #################################       USDT-ს ყიდვა
######################################
######################################
def usdtbuy(message):
    button = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id, 'გთხოვთ შეიყვანოთ თქვენი სახელი და გვარი', reply_markup=button)
    bot.send_message(message.chat.id, 'გაითვალისწინეთ, საბანკო ანგარიშიდან თანხის გამომგზავნის სახელი და გვარი უნდა ემთხვეოდეს თქვენს მიერ მითითებულ სახელსა და გვარს ')
    bot.register_next_step_handler(msg, nameusdt)

#სახელის ველი

def nameusdt(message):
    try:
        global nick
        nick = {}
        msg = nick = message.text
        bot.register_next_step_handler(msg, usdtbank)
    except:
        usdtbank(message)




def usdtbank(message):
        button = types.ReplyKeyboardRemove()
        price = cg.get_price(ids='tether', vs_currencies='usd')
        msg = bot.send_message(message.chat.id, f'1 Tether == {float("{0:.3f}". format(price["tether"]["usd"] * 0.98))} USD\nმინიმალური თანხა გაცვლისთვის არის'
                                          f' 100 $')
        bot.send_message(message.chat.id,  'დაწერეთ რამდენი USD-ს გადაცვლა გინდათ USDT-ში:', reply_markup=button)
        bot.register_next_step_handler(msg, shemocusdt)

### თანხა გაცვლისთვის
###
def shemocusdt(message):
    try:
        global courseusdt
        courseusdt = {}
        shemocusdt1 = {}
        shemocusdt1["usdtbank"] = message.text
        courseusdt = float(shemocusdt1["usdtbank"])
#        price = cg.get_price(ids='tether', vs_currencies='usd')
        if courseusdt >= 100:
            msg = bot.send_message(message.chat.id, f'თქვენ მიიღებთ {float("{0:.3f}". format(courseusdt * 0.98))}USDT-ს  კრიპტოსაფულეზე ')
            bot.send_message(message.chat.id, f' გთხოვთ შეიყვანოთ თქვენი Tether \n'
                                              f'(TRC 20) კრიპტომისამართი')


            bot.register_next_step_handler(msg, usdtshemoc2)
        else:
            bot.send_message(message.chat.id, 'თქვენი თანხა ნაკლებია მინიმალურზე, გთხოვთ შეცვალოთ')
            usdtbank(message)
    except ValueError:
        bot.send_message(message.chat.id, 'გთხოვთ შეიყვანოთ კორექტული მონაცემები')
        usdtbank(message)




def usdtshemoc2(message):
    global walletusdt
    walletusdt = {}
    walletusdt["shemocusdt1"] = message.text
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button.add(types.KeyboardButton('საქართველოს ბანკი'), types.KeyboardButton('თბს ბანკი'), types.KeyboardButton('ლიბერთი ბანკი'))
#    price = cg.get_price(ids='tether', vs_currencies='usd')
    msg = bot.send_message(message.chat.id, f'თქვენ ცვლით {float("{0:.8f}". format(courseusdt))} $-ს {float("{0:.3f}". format(courseusdt * 0.98))} USDT-ში. \n'
                                      f'თქვენი საფულე: {walletusdt["shemocusdt1"]}', reply_markup=button)
    bot.send_message(message.chat.id, f'ჩვენ ველოდებით თქვენგან {float("{0:.8f}". format(courseusdt))} USD-ს ჩარიცხვას საბანკო ანგარიშზე \n'
                                      f'აირჩიეთ ბანკი')
    bot.register_next_step_handler(msg, bankname)



def bankname(message):
    global bankwalletusdt
    bankwalletusdt = {}
    bankwalletusdt["walletusdt1"] = message.text
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button.add(types.KeyboardButton('ვადასტურებ გადახდას'))
    button.row(types.KeyboardButton('ოპერაციის გაუქმება'))

    if message.text == 'საქართველოს ბანკი':
        msg = bot.send_message(message.chat.id, 'GE0101010101010101010', reply_markup=button )
 #       price = cg.get_price(ids='tether', vs_currencies='usd')
        bot.send_message(message.chat.id,
                               f'ოპერაციის დასრულებისთვის ჩარიცხეთ {float("{0:.2f}".format(courseusdt))} $ და დაადასტურეთ გადახდა \n')
        bot.register_next_step_handler(msg, usdtfinish)
    if message.text == 'თბს ბანკი':
 #       price = cg.get_price(ids='tether', vs_currencies='usd')
        msg = bot.send_message(message.chat.id, 'GE0101010101010101010', reply_markup=button)
        bot.send_message(message.chat.id,
                         f'ოპერაციის დასრულებისთვის ჩარიცხეთ {float("{0:.2f}".format(courseusdt))} $ და დაადასტურეთ გადახდა \n')
        bot.register_next_step_handler(msg, usdtfinish)
    if message.text == 'ლიბერთი ბანკი':
        msg = bot.send_message(message.chat.id, 'GE0101010101010101010', reply_markup=button)
 #       price = cg.get_price(ids='tether', vs_currencies='usd')
        bot.send_message(message.chat.id,
                         f'ოპერაციის დასრულებისთვის ჩარიცხეთ {float("{0:.2f}".format(courseusdt))} $ და დაადასტურეთ გადახდა \n')
        bot.register_next_step_handler(msg, usdtfinish)





 #   price = cg.get_price(ids='tether', vs_currencies='usd') ქვემოთ ჩასადები
def usdtfinish(message):
    try:
        if message.text == 'ვადასტურებ გადახდას':
            bot.send_message(message.chat.id, f'თქვენი მოთხოვნა მიღებულია \n'
                                          f'დრო: {datetime.datetime.now()}.\n'
                                          f'{float("{0:.8f}". format(courseusdt * 0.98))} USDT-ს ჩაირიცხება თქვენს საფულეზე  20 წუთის განმავლობაში.\n'
                                           'მადლობა  რომ ჩვენი ბოტით სარგებლობთ')
            main(message)

            bot.send_message(789435088, f"გადახდის თანხა: {float('{0:.7f}'.format(courseusdt))}\n"
                             f" მიღების თანხა: {float('{0:.8f}'. format(courseusdt * 0.98))} USDT\n"
                             f"საფულეზე: \n\n"
                             f"{walletusdt['shemocusdt1']}\n\n"
                             f"სახელი გვარი: {nick}\n"
                             f"ბანკი: {bankwalletusdt['walletusdt1']}\n"
                             f"მოთხოვნის დრო: {datetime.datetime.now()}")
        elif message.text == 'ოპერაციის გაუქმება':
            buy1(message)
        else:
            usdtshemoc2(message)
    except:
        usdtshemoc2(message)






##########################################################
############################################################
#################################################################### ბიტკოინის ყიდვა
############################################################
def btcbuy(message):
    button = types.ReplyKeyboardRemove()
    msg = bot.send_message(message.chat.id, 'გთხოვთ შეიყვანოთ თქვენი სახელი', reply_markup=button)
    bot.send_message(message.chat.id,
                     'გაითვალისწინეთ, საბანკო ანგარიშიდან თანხის გამომგზავნის სახელი და გვარი უნდა ემთხვეოდეს თქვენს მიერ მითითებულ სახელსა და გვარს ')
    bot.register_next_step_handler(msg, name2)

#სახელის ველი

def name2(message):
    try:
        global nick
        nick = {}
        msg = nick = message.text
        bot.register_next_step_handler(msg, geobank)
    except:
        geobank(message)



def geobank(message):
        button = types.ReplyKeyboardRemove()
        price = cg.get_price(ids='bitcoin', vs_currencies='usd')
        msg = bot.send_message(message.chat.id, f'1 Bitcoin == {price["bitcoin"]["usd"] * 0.98} USD\nმინიმალური თანხა გაცვლისთვის არის'
                                          f' 100 $')
        bot.send_message(message.chat.id,  'დაწერეთ რამდენი USD-ს გადაცვლა გინდათ BTC-ში:', reply_markup=button)
        bot.register_next_step_handler(msg, shemoc)

### თანხა გაცვლისთვის
###
def shemoc(message):
    try:
        global course
        course = {}
        shemoc = {}
        shemoc["geobank"] = message.text
        course = float(shemoc["geobank"])
        price = cg.get_price(ids='bitcoin', vs_currencies='usd')
        if course >= 100:
            msg = bot.send_message(message.chat.id, f'თქვენ მიიღებთ {float("{0:.8f}". format(course / (price["bitcoin"]["usd"] * 1.02)))} BTC-ს კრიპტოსაფულეზე')
            bot.send_message(message.chat.id, f' გთხოვთ შეიყვანოთ თქვენი Bitcoin ანგარიში')

            bot.register_next_step_handler(msg, shemoc2)
        else:
            bot.send_message(message.chat.id, 'თქვენი თანხა ნაკლებია მინიმალურზე, გთხოვთ შეცვალოთ')
            geobank(message)
    except ValueError:
        bot.send_message(message.chat.id, 'გთხოვთ შეიყვანოთ კორექტული მონაცემები')
        geobank(message)

def shemoc2(message):
    global wallet
    wallet = {}
    wallet["shemoc"] = message.text
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button.add(types.KeyboardButton('საქართველოს ბანკი'), types.KeyboardButton('თბს ბანკი'), types.KeyboardButton('ლიბერთი ბანკი'))

    price = cg.get_price(ids='bitcoin', vs_currencies='usd')
    msg = bot.send_message(message.chat.id, f'თქვენ ცვლით  {float("{0:.8f}". format(course))} USD-ს {float("{0:.8f}". format(course / (price["bitcoin"]["usd"] * 1.02)))} BTC-ში. \n'
                                      f'თქვენი საფულე: {wallet["shemoc"]}', reply_markup=button)
    bot.send_message(message.chat.id, f'ჩვენ ველოდებით თქვენგან {float("{0:.8f}". format(course))} USD-ს ჩარიცხვას საბანკო ანგარიშზე ')

    bot.register_next_step_handler(msg, btcbankname)


def btcbankname(message):
    global bankwalletbtc
    bankwalletbtc = {}
    bankwalletbtc["walletbtc1"] = message.text
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button.add(types.KeyboardButton('ვადასტურებ გადახდას'))
    button.add(types.KeyboardButton('ოპერაციის გაუქმება'))

    if message.text == 'საქართველოს ბანკი':
        price = cg.get_price(ids='bitcoin', vs_currencies='usd')
        msg = bot.send_message(message.chat.id, 'GE0101010101010101010', reply_markup=button )
        bot.send_message(message.chat.id,
                               f'ოპერაციის დასრულებისთვის ჩარიცხეთ {float("{0:.8f}".format(course))} $ და დაადასტურეთ გადახდა \n')
        bot.register_next_step_handler(msg, finish)
    if message.text == 'თბს ბანკი':
        price = cg.get_price(ids='bitcoin', vs_currencies='usd')
        msg = bot.send_message(message.chat.id, 'GE0101010101010101010', reply_markup=button)
        bot.send_message(message.chat.id,
                         f'ოპერაციის დასრულებისთვის ჩარიცხეთ {float("{0:.8f}".format(course))} $ და დაადასტურეთ გადახდა \n')
        bot.register_next_step_handler(msg, finish)
    if message.text == 'ლიბერთი ბანკი':
        msg = bot.send_message(message.chat.id, 'GE0101010101010101010', reply_markup=button)
        price = cg.get_price(ids='bitcoin', vs_currencies='usd')
        bot.send_message(message.chat.id,
                         f'ოპერაციის დასრულებისთვის ჩარიცხეთ {float("{0:.8f}".format(course ))} $ და დაადასტურეთ გადახდა \n')
        bot.register_next_step_handler(msg, finish)








def finish(message):
    try:
        price = cg.get_price(ids='bitcoin', vs_currencies='usd')
        if message.text == 'ვადასტურებ გადახდას':
            bot.send_message(message.chat.id, f'თქვენი მოთხოვნა მიღებულია \n'
                                           f'დრო: {datetime.datetime.now()}\n'
                                           f'{float("{0:.8f}". format(course / (price["bitcoin"]["usd"] * 1.02)))} BTC ჩაირიცხება თქვენს საფულეზე 20 წუთის განმავლობაში.'
                                           'მადლობა, რომ ჩვენი ბოტით სარგებლობთ')
            main(message)

            bot.send_message(789435088, f"გადახდის თანხა: {float('{0:.8f}'.format(course))}\n"
                             f" მიღების თანხა: {float('{0:.8f}'. format(course / (price['bitcoin']['usd'] * 1.02)))} BTC\n"
                             f"საფულეზე: \n\n"
                             f"{wallet['shemoc']}\n\n"
                             f"სახელი გვარი: {nick}\n"
                             f"ბანკი: {bankwalletbtc['walletbtc1']}\n"
                             f"მოთხოვნის დრო: {datetime.datetime.now()}")

        elif message.text == 'ოპერაციის გაუქმება':
            buy1(message)
        else:
            shemoc2(message)
    except:
        shemoc2(message)





##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################




################################################# კონვერტერი
#################################################



bot.polling()