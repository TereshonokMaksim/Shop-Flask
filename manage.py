import project
import threading
from bot.tele_bot import bot

# Если правда, то будет запущено с помощью потоков
bot_on = False

if __name__ == "__main__":
    if not bot_on:
        project.project.run(debug = True)

    else:
        # Thread part (shop website - debug off due to error that occures if using threads)
        # PLEASE, DO NOT USE ON HOST

        thread_website = threading.Thread(target = project.project.run)
        thread_bot = threading.Thread(target = bot.infinity_polling)
        thread_website.start()
        thread_bot.start()

    # Hello :D