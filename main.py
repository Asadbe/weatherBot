import config
import telebot
import requests
from bs4 import BeautifulSoup as BS
from telebot import types

bot  = telebot.TeleBot(config.token)



@bot.message_handler(commands=[ 'start'])
def main(message):
  
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Toshkent')
    itembtn2 = types.KeyboardButton('Andijon')
    itembtn3 = types.KeyboardButton('Buxoro')
    itembtn4 = types.KeyboardButton('Guliston')
    itembtn5 = types.KeyboardButton('Jizzax')
    itembtn6 = types.KeyboardButton('Zarafshon')
    itembtn7 = types.KeyboardButton('Qarshi')
    itembtn8 = types.KeyboardButton('Navoiy')
    itembtn9 = types.KeyboardButton('Namangan')
    itembtn10 = types.KeyboardButton('Nukus')
    itembtn11 = types.KeyboardButton('Samarqand')
    itembtn12 = types.KeyboardButton('Termiz')
    itembtn13 = types.KeyboardButton('Urganch')
    itembtn14 = types.KeyboardButton("Farg'ona")
    itembtn15 = types.KeyboardButton('Xiva')
    markup.row(itembtn1, itembtn2, itembtn3)
    markup.row(itembtn4, itembtn5, itembtn6)
    markup.row(itembtn7, itembtn8, itembtn9)
    markup.row(itembtn10, itembtn11, itembtn12)
    markup.row(itembtn13, itembtn14, itembtn15)

    bot.send_message(message.chat.id, "Salom "+message.from_user.first_name +" bu bot orqali siz havo harorati haqidagi malumotga ega bo'lasiz kerakli joyni tanlang"    
 ,reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):

    if message.text == "Toshkent":
        tashkent  = requests.get('https://obhavo.uz/tashkent')
        html = BS(tashkent.content , 'html.parser')
        el = html.select('.current-forecast')
        cal = el[0]
        pic = cal.span.img["src"]
        min_temp = el[0].contents[5].text
        max_temp = el[0].contents[3].text
        description = html.select('.current-forecast-desc')
        desc = description[0].text
        info = html.select('.current-forecast-details')
        information = info[0].text
        photo = open('clear.png', 'rb')
        bot.send_photo(message.chat.id, photo , "Bugun toshkentdagi \nminimal temperatura : " +min_temp +" \nmaximal temperatura :"+max_temp + "\n"+
"va havo " + desc + " bo'lishi kutilmoqda " +"\n " + information)
    elif message.text == "Andijon":
        andijan  = requests.get('https://obhavo.uz/andijan')
        html = BS(andijan.content , 'html.parser')
        el = html.select('.current-forecast')
        cal = el[0]
        pic = cal.span.img["src"]
        min_temp = el[0].contents[5].text
        max_temp = el[0].contents[3].text
        description = html.select('.current-forecast-desc')
        desc = description[0].text
        info = html.select('.current-forecast-details')
        information = info[0].text
        photo = open('clear.png', 'rb')
        bot.send_photo(message.chat.id, photo , "Bugun andijondagi \nminimal temperatura : " +min_temp +" \nmaximal temperatura :"+max_temp + "\n"+
    "va havo " + desc + " bo'lishi kutilmoqda " +"\n " + information)
    elif message.text == "Buxoro":
        buxoro  = requests.get('https://obhavo.uz/bukhara')
        html = BS(buxoro.content , 'html.parser')
        el = html.select('.current-forecast')
        cal = el[0]
        pic = cal.span.img["src"]
        min_temp = el[0].contents[5].text
        max_temp = el[0].contents[3].text
        description = html.select('.current-forecast-desc')
        desc = description[0].text
        info = html.select('.current-forecast-details')
        information = info[0].text
        photo = open('clear.png', 'rb')
        bot.send_photo(message.chat.id, photo , "Bugun buxorodagi \nminimal temperatura : " +min_temp +" \nmaximal temperatura :"+max_temp + "\n"+
    "va havo " + desc + " bo'lishi kutilmoqda " +"\n " + information)
    elif message.text == "Jizzax":
        jizzax  = requests.get('https://obhavo.uz/jizzakh')
        html = BS(jizzax.content , 'html.parser')
        el = html.select('.current-forecast')
        cal = el[0]
        pic = cal.span.img["src"]
        min_temp = el[0].contents[5].text
        max_temp = el[0].contents[3].text
        description = html.select('.current-forecast-desc')
        desc = description[0].text
        info = html.select('.current-forecast-details')
        information = info[0].text
        photo = open('clear.png', 'rb')
        bot.send_photo(message.chat.id, photo , "Bugun jizzaxdagi \nminimal temperatura : " +min_temp +" \nmaximal temperatura :"+max_temp + "\n"+
    "va havo " + desc + " bo'lishi kutilmoqda " +"\n " + information)
    elif message.text == "Guliston":
        guliston  = requests.get('https://obhavo.uz/gulistan')
        html = BS(guliston.content , 'html.parser')
        el = html.select('.current-forecast')
        cal = el[0]
        pic = cal.span.img["src"]
        min_temp = el[0].contents[5].text
        max_temp = el[0].contents[3].text
        description = html.select('.current-forecast-desc')
        desc = description[0].text
        info = html.select('.current-forecast-details')
        information = info[0].text
        photo = open('clear.png', 'rb')
        bot.send_photo(message.chat.id, photo , "Bugun gulistondagi \nminimal temperatura : " +min_temp +" \nmaximal temperatura :"+max_temp + "\n"+
    "va havo " + desc + " bo'lishi kutilmoqda " +"\n " + information)
    elif message.text == "Zarafshon":
        zarafshon  = requests.get('https://obhavo.uz/zarafshan')
        html = BS(zarafshon.content , 'html.parser')
        el = html.select('.current-forecast')
        cal = el[0]
        pic = cal.span.img["src"]
        min_temp = el[0].contents[5].text
        max_temp = el[0].contents[3].text
        description = html.select('.current-forecast-desc')
        desc = description[0].text
        info = html.select('.current-forecast-details')
        information = info[0].text
        photo = open('clear.png', 'rb')
        bot.send_photo(message.chat.id, photo , "Bugun zarafshondagi \nminimal temperatura : " +min_temp +" \nmaximal temperatura :"+max_temp + "\n"+
    "va havo " + desc + " bo'lishi kutilmoqda " +"\n " + information)
    elif message.text == "Qarshi":
        qarshi  = requests.get('https://obhavo.uz/karshi')
        html = BS(qarshi.content , 'html.parser')
        el = html.select('.current-forecast')
        cal = el[0]
        pic = cal.span.img["src"]
        min_temp = el[0].contents[5].text
        max_temp = el[0].contents[3].text
        description = html.select('.current-forecast-desc')
        desc = description[0].text
        info = html.select('.current-forecast-details')
        information = info[0].text
        photo = open('clear.png', 'rb')
        bot.send_photo(message.chat.id, photo , "Bugun qarshidagi \nminimal temperatura : " +min_temp +" \nmaximal temperatura :"+max_temp + "\n"+
    "va havo " + desc + " bo'lishi kutilmoqda " +"\n " + information)
    elif message.text == "Navoiy":
        navoiy  = requests.get('https://obhavo.uz/navoi')
        html = BS(navoiy.content , 'html.parser')
        el = html.select('.current-forecast')
        cal = el[0]
        pic = cal.span.img["src"]
        min_temp = el[0].contents[5].text
        max_temp = el[0].contents[3].text
        description = html.select('.current-forecast-desc')
        desc = description[0].text
        info = html.select('.current-forecast-details')
        information = info[0].text
        photo = open('clear.png', 'rb')
        bot.send_photo(message.chat.id, photo , "Bugun navoiydagi \nminimal temperatura : " +min_temp +" \nmaximal temperatura :"+max_temp + "\n"+
    "va havo " + desc + " bo'lishi kutilmoqda " +"\n " + information)
    elif message.text == "Namangan":
        namangan  = requests.get('https://obhavo.uz/namangan')
        html = BS(namangan.content , 'html.parser')
        el = html.select('.current-forecast')
        cal = el[0]
        pic = cal.span.img["src"]
        min_temp = el[0].contents[5].text
        max_temp = el[0].contents[3].text
        description = html.select('.current-forecast-desc')
        desc = description[0].text
        info = html.select('.current-forecast-details')
        information = info[0].text
        photo = open('clear.png', 'rb')
        bot.send_photo(message.chat.id, photo , "Bugun namangandagi \nminimal temperatura : " +min_temp +" \nmaximal temperatura :"+max_temp + "\n"+
    "va havo " + desc + " bo'lishi kutilmoqda " +"\n " + information)
    elif message.text == "Nukus":
        nukus  = requests.get('https://obhavo.uz/nukus')
        html = BS(nukus.content , 'html.parser')
        el = html.select('.current-forecast')
        cal = el[0]
        pic = cal.span.img["src"]
        min_temp = el[0].contents[5].text
        max_temp = el[0].contents[3].text
        description = html.select('.current-forecast-desc')
        desc = description[0].text
        info = html.select('.current-forecast-details')
        information = info[0].text
        photo = open('clear.png', 'rb')
        bot.send_photo(message.chat.id, photo , "Bugun nukusdagi \nminimal temperatura : " +min_temp +" \nmaximal temperatura :"+max_temp + "\n"+
    "va havo " + desc + " bo'lishi kutilmoqda " +"\n " + information)
    elif message.text == "Samarqand":
        samarqand  = requests.get('https://obhavo.uz/samarkand')
        html = BS(samarqand.content , 'html.parser')
        el = html.select('.current-forecast')
        cal = el[0]
        pic = cal.span.img["src"]
        min_temp = el[0].contents[5].text
        max_temp = el[0].contents[3].text
        description = html.select('.current-forecast-desc')
        desc = description[0].text
        info = html.select('.current-forecast-details')
        information = info[0].text
        photo = open('clear.png', 'rb')
        bot.send_photo(message.chat.id, photo , "Bugun samarqanddagi \nminimal temperatura : " +min_temp +" \nmaximal temperatura :"+max_temp + "\n"+
    "va havo " + desc + " bo'lishi kutilmoqda " +"\n " + information)
    elif message.text == "Termiz":
        termiz  = requests.get('https://obhavo.uz/termez')
        html = BS(termiz.content , 'html.parser')
        el = html.select('.current-forecast')
        cal = el[0]
        pic = cal.span.img["src"]
        min_temp = el[0].contents[5].text
        max_temp = el[0].contents[3].text
        description = html.select('.current-forecast-desc')
        desc = description[0].text
        info = html.select('.current-forecast-details')
        information = info[0].text
        photo = open('clear.png', 'rb')
        bot.send_photo(message.chat.id, photo , "Bugun termizdagi \nminimal temperatura : " +min_temp +" \nmaximal temperatura :"+max_temp + "\n"+
    "va havo " + desc + " bo'lishi kutilmoqda " +"\n " + information)
    elif message.text == "Urganch":
        urganch  = requests.get('https://obhavo.uz/urgench')
        html = BS(urganch.content , 'html.parser')
        el = html.select('.current-forecast')
        cal = el[0]
        pic = cal.span.img["src"]
        min_temp = el[0].contents[5].text
        max_temp = el[0].contents[3].text
        description = html.select('.current-forecast-desc')
        desc = description[0].text
        info = html.select('.current-forecast-details')
        information = info[0].text
        photo = open('clear.png', 'rb')
        bot.send_photo(message.chat.id, photo , "Bugun urganchdagi \nminimal temperatura : " +min_temp +" \nmaximal temperatura :"+max_temp + "\n"+
    "va havo " + desc + " bo'lishi kutilmoqda " +"\n " + information)
    elif message.text == "Farg'ona":
        fargona  = requests.get('https://obhavo.uz/fergana')
        html = BS(fargona.content , 'html.parser')
        el = html.select('.current-forecast')
        cal = el[0]
        pic = cal.span.img["src"]
        min_temp = el[0].contents[5].text
        max_temp = el[0].contents[3].text
        description = html.select('.current-forecast-desc')
        desc = description[0].text
        info = html.select('.current-forecast-details')
        information = info[0].text
        photo = open('clear.png', 'rb')
        bot.send_photo(message.chat.id, photo , "Bugun farg'onadagi \nminimal temperatura : " +min_temp +" \nmaximal temperatura :"+max_temp + "\n"+
    "va havo " + desc + " bo'lishi kutilmoqda " +"\n " + information)
    elif message.text == "Xiva":
        xiva  = requests.get('https://obhavo.uz/khiva')
        html = BS(xiva.content , 'html.parser')
        el = html.select('.current-forecast')
        cal = el[0]
        pic = cal.span.img["src"]
        min_temp = el[0].contents[5].text
        max_temp = el[0].contents[3].text
        description = html.select('.current-forecast-desc')
        desc = description[0].text
        info = html.select('.current-forecast-details')
        information = info[0].text
        photo = open('clear.png', 'rb')
        bot.send_photo(message.chat.id, photo , "Bugun xivadagi \nminimal temperatura : " +min_temp +" \nmaximal temperatura :"+max_temp + "\n"+
    "va havo " + desc + " bo'lishi kutilmoqda " +"\n " + information)



if __name__ == '__main__':
    bot.polling(none_stop=True)