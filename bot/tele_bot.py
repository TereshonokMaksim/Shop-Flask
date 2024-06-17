import telebot
import sqlite3
import os

def change_database(command:str):
    with sqlite3.connect(os.path.abspath(__file__+"/../../project/data.db")) as database:
        cursor = database.cursor()
        cursor.execute(command)
        data = cursor.fetchall()
        database.commit()
    return data    

# DELETE THIS TOKEN BEFORE COMMITING!
token = "blank, i guess"
bot = telebot.TeleBot(token = token)
states = {}
''' Keyboard Part '''
# Start keyboads
keyboard_start_products = telebot.types.InlineKeyboardMarkup(keyboard = [[telebot.types.InlineKeyboardButton(text = "GET PRODUCTS", callback_data = "get_products")]])
keyboard_start_users = telebot.types.InlineKeyboardMarkup(keyboard = [[telebot.types.InlineKeyboardButton(text = "GET USERS", callback_data = "get_user")]])
keyboard_start_basket = telebot.types.InlineKeyboardMarkup(keyboard = [[telebot.types.InlineKeyboardButton(text = "SHOW BASKET", callback_data = "show_basket")]])
# User topic keyboards
button_remove_user = telebot.types.InlineKeyboardButton(text = "DELETE USER", callback_data = "delete_user")
user_keyboard = telebot.types.InlineKeyboardMarkup(keyboard = [[button_remove_user, telebot.types.InlineKeyboardButton(text = "ADD ADMIN", callback_data = "add_admin")]])
admin_keyboard = telebot.types.InlineKeyboardMarkup(keyboard = [[button_remove_user, telebot.types.InlineKeyboardButton(text = "REMOVE ADMIN", callback_data = "remove_admin")]])
# Product topic keyboards
product_keyboard = telebot.types.InlineKeyboardMarkup(keyboard = [[telebot.types.InlineKeyboardButton(text = "EDIT PRODUCT", callback_data = "edit_product")],
                                                                  [telebot.types.InlineKeyboardButton(text = "DELETE PRODUCT", callback_data = "delete_product")]])
edit_product_keyboard = telebot.types.InlineKeyboardMarkup(keyboard = [[telebot.types.InlineKeyboardButton(text = "EDIT IMAGE", callback_data = "edit_image"), telebot.types.InlineKeyboardButton(text = "EDIT NAME", callback_data = "edit_name")],
                                                                       [telebot.types.InlineKeyboardButton(text = "EDIT PRICE", callback_data = "edit_price"), telebot.types.InlineKeyboardButton(text = "EDIT DESCRIPTION", callback_data = "edit_description")],
                                                                       [telebot.types.InlineKeyboardButton(text = "EDIT DISCOUNT", callback_data = "edit_discount"), telebot.types.InlineKeyboardButton(text = "EDIT COUNT", callback_data = "edit_count")],
                                                                       [telebot.types.InlineKeyboardButton(text = "CLOSE EDIT", callback_data = "close_edit")]]) # емае
# Basket topic keyboard

''' Keyboard Part End '''

@bot.message_handler(commands = ['start'])
def start_command(message: telebot.types.Message):
    print(message.message_thread_id)
    states[message.from_user.id] = {"users": "", "products": "", "basket": ""}
    if message.message_thread_id == None:
        bot.send_message(chat_id = message.chat.id, text = "Привіт, користувач.\nЩоб почати щоось робити увійдіть у потрібну вам гілку.")
    elif message.message_thread_id == 3:
        bot.send_message(chat_id = message.chat.id, text = "Привіт, Адмін", reply_markup = keyboard_start_users, message_thread_id = 3)
    elif message.message_thread_id == 6:
        bot.send_message(chat_id = message.chat.id, text = "Привіт, Адмін", reply_markup = keyboard_start_products, message_thread_id = 6)
    elif message.message_thread_id == 8:
        bot.send_message(chat_id = message.chat.id, text = "Привіт, користувач", reply_markup = keyboard_start_basket, message_thread_id = 8)
        
@bot.callback_query_handler(func = lambda call: True)
def callback_handler(callback: telebot.types.CallbackQuery):
    if callback.data == "get_user":
        information = change_database(command= 'SELECT * FROM user')
        for info_user in information:
            if info_user[4] == 1:
                bot.send_message(chat_id = callback.message.chat.id, text = f'ID: {info_user[0]} \n Name: {info_user[1]} \n Password: {info_user[3]} \n ➡️Is_admin: 1⚠️', reply_markup = admin_keyboard, message_thread_id = callback.message.message_thread_id)
            else:
                bot.send_message(chat_id = callback.message.chat.id, text = f'ID: {info_user[0]} \n Name: {info_user[1]} \n Password: {info_user[3]} \n ➡️Is_admin: 0', reply_markup = user_keyboard, message_thread_id = callback.message.message_thread_id) 
    
    elif callback.data == "delete_user":
        user_id = callback.message.text.split(" ")[1]
        change_database(command = f"DELETE FROM user WHERE id = '{user_id}'")
        bot.delete_message(chat_id = callback.message.chat.id, message_id = callback.message.id)
        
    elif callback.data == "add_admin":
        user_id = callback.message.text.split(" ")[1]
        change_database(command = f"UPDATE user SET admin = '1' WHERE id = '{user_id}'")
        bot.edit_message_text(chat_id = callback.message.chat.id, message_id = callback.message.id, text = " ".join([" ".join(callback.message.text.split(" ")[:-2]), "➡️Is_admin: 1⚠️"]), reply_markup = admin_keyboard)
        
    elif callback.data == "remove_admin":
        user_id = callback.message.text.split(" ")[1]
        change_database(command = f"UPDATE user SET admin = '0' WHERE id = '{user_id}'") 
        bot.edit_message_text(chat_id = callback.message.chat.id, message_id = callback.message.id, text = " ".join([" ".join(callback.message.text.split(" ")[:-2]), "➡️Is_admin: 0"]), reply_markup = user_keyboard)   

    elif callback.data == "get_products":
        information = change_database(command = 'SELECT * FROM product')
        for info_product in information:
            bot.send_photo(chat_id = callback.message.chat.id, 
                           caption = f'''ID: {info_product[0]} \n Name: {info_product[1]} \n Price: {info_product[2]} \n Description: {info_product[3]} \n In stock: {info_product[4]}\n Discount: {info_product[5]}%\n Count: {info_product[6]}''', 
                           photo = telebot.types.InputFile(os.path.abspath(__file__ + f"/../../static/shop_page/images/{info_product[1]}.png")),
                           reply_markup = product_keyboard,
                           message_thread_id = callback.message.message_thread_id)
            
    elif callback.data == "delete_product":
        product_id = callback.message.caption.split(" ")[1]
        change_database(command = f"DELETE FROM product WHERE id = '{product_id}'")
        bot.delete_message(chat_id = callback.message.chat.id, message_id = callback.message.id)
    
    elif callback.data == "edit_product":
        # print(callback.message, callback.message.text)
        product_id = callback.message.caption.split(" ")[1]
        bot.edit_message_reply_markup(chat_id = callback.message.chat.id, message_id = callback.message.id, reply_markup = edit_product_keyboard)

    # Edit Product Part

    elif "edit" in callback.data and "edit" not in states[callback.from_user.id]["products"]:
        product_id = callback.message.caption.split(" ")[1]
        chat_id = callback.message.chat.id
        thread_id = callback.message.message_thread_id
        base_text = f"з {product_id} ID, {callback.from_user.first_name}"
        
        if "image" in callback.data:
            message = bot.send_message(chat_id = chat_id, text = f"Пришліть нове фото товару {base_text}:",  message_thread_id = thread_id)

        elif "name" in callback.data:
            message = bot.send_message(chat_id = chat_id, text = f"Уведіть нове ім'я товару {base_text}: ",  message_thread_id = thread_id)

        elif "price" in callback.data:
            message = bot.send_message(chat_id = chat_id, text = f"Уведіть нову ціну товару (повинна бути числом та більше 0) {base_text}: ",  message_thread_id = thread_id)
            
        elif "description" in callback.data:
            message = bot.send_message(chat_id = chat_id, text = f"Уведіть новий опис товару (по такий самій схеми як і на сайті) {base_text}: ",  message_thread_id = thread_id)

        elif "discount" in callback.data:
            message = bot.send_message(chat_id = chat_id, text = f"Уведіть нову скидку (повинна бути числом та більше або дорівнювати 0) товару {base_text}: ", message_thread_id = thread_id)  

        elif "count" in callback.data:
            message = bot.send_message(chat_id = chat_id, text = f"Уведіть нову кількість товару (вона повинна бути числом і більше або дорівнювати 0) {base_text}: ",  message_thread_id = thread_id)

        elif "close" in callback.data:
            bot.edit_message_reply_markup(chat_id = chat_id, message_id = callback.message.id, reply_markup = product_keyboard)
            return None
            
        states[callback.from_user.id]["products"] = f"{callback.data}-{message.id}-{callback.message.id}-{product_id}"


@bot.message_handler(content_types = ["text", "photo"])
def message_manager(message: telebot.types.Message):
    print(states[message.from_user.id])
    if "edit" in states[message.from_user.id]["products"]:
        state = states[message.from_user.id]["products"].split("-")
        product = change_database(command = f"SELECT * FROM product WHERE id = '{state[-1]}'")[0]
        if "image" in states[message.from_user.id]["products"]:
            print("hello", message.photo)
            if message.photo != None:
                print("im a photo now")
                photo_id = message.photo[-1].file_id
                photo_path = bot.get_file(photo_id)
                photo = bot.download_file(photo_path.file_path)
                with open(file = os.path.abspath(__file__ + f"/../../static/shop_page/images/{product[1]}.png"), mode = "wb") as file:
                    file.write(photo)
                bot.delete_message(chat_id = message.chat.id, message_id = state[1])
                states[message.from_user.id]["products"] = ""
            bot.edit_message_media(chat_id = message.chat.id, 
                                   media = telebot.types.InputMediaPhoto(photo), 
                                   message_id = state[2])
            bot.delete_message(chat_id = message.chat.id, message_id = message.id)
                
        elif "name" in states[message.from_user.id]["products"]:
            if message.text != None:
                change_database(f"UPDATE product SET name = '{message.text}' WHERE id = '{state[-1]}'")
                image_path = os.path.abspath(__file__ + "/../../static/shop_page/images")
                os.rename(src = os.path.join(image_path, product[1]) + ".png", dst = os.path.join(image_path, message.text) + ".png")
                bot.delete_message(chat_id = message.chat.id, message_id = state[1])
                states[message.from_user.id]["products"] = ""
            bot.delete_message(chat_id = message.chat.id, message_id = message.id)

        elif "price" in states[message.from_user.id]["products"]:
            # try:
            new_price = int(message.text)
            if new_price > 0:
                change_database(command = f"UPDATE product SET price = {new_price} WHERE id = '{state[-1]}'")
                bot.delete_message(chat_id = message.chat.id, message_id = state[1])
                states[message.from_user.id]["products"] = ""
            # except:
            #     print("none")
            bot.delete_message(chat_id = message.chat.id, message_id = message.id)
            
        elif "description" in states[message.from_user.id]["products"]:
            if message.text != None:
                change_database(command = f"UPDATE product SET description = '{message.text}' WHERE id = '{state[-1]}'")
                bot.delete_message(chat_id = message.chat.id, message_id = state[1])
                states[message.from_user.id]["products"] = ""
            bot.delete_message(chat_id = message.chat.id, message_id = message.id)

        elif "discount" in states[message.from_user.id]["products"]:
            try:
                new_discount = int(message.text)
                if 0 <= new_discount <= 100:
                    change_database(command = f"UPDATE product SET discount = {round(new_discount)} WHERE id = '{state[-1]}'") 
                    bot.delete_message(chat_id = message.chat.id, message_id = state[1])
                    states[message.from_user.id]["products"] = ""
            except:
                pass
            bot.delete_message(chat_id = message.chat.id, message_id = message.id)

        elif "count" in states[message.from_user.id]["products"]:
            try:
                new_count = int(message.text)
                if new_count >= 0:
                    if new_count == 0:
                        in_stock_new = 0
                    else:
                        in_stock_new = 1
                    change_database(command = f"UPDATE product SET in_stock = {in_stock_new} WHERE id = '{state[-1]}'")
                    change_database(command = f"UPDATE product SET count = {new_count} WHERE id = '{state[-1]}'")
                    bot.delete_message(chat_id = message.chat.id, message_id = state[1])
                    states[message.from_user.id]["products"] = ""
            except:
                pass
            bot.delete_message(chat_id = message.chat.id, message_id = message.id)

        info_product = change_database(command = f"SELECT * FROM product WHERE id = '{state[-1]}'")[0]
        print(info_product, os.path.abspath(__file__ + f"/../../static/shop_page/images/{info_product[1]}.png"))
        try:
            bot.edit_message_caption(chat_id = message.chat.id, 
                            caption = f'''ID: {info_product[0]} \n Name: {info_product[1]} \n Price: {info_product[2]} \n Description: {info_product[3]} \n In stock: {info_product[4]}\n Discount: {info_product[5]}%\n Count: {info_product[6]}''', 
                            reply_markup = product_keyboard,
                            message_id = state[2])
        except Exception as error:
            print(error)
