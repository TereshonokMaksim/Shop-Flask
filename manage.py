import project
import threading
from bot.tele_bot import bot

if __name__ == "__main__":
    # project.project.run(debug = True)

    # Thread part (shop website - debug off due to error that occures if using threads)

    thread_website = threading.Thread(target = project.project.run)
    thread_bot = threading.Thread(target = bot.infinity_polling)
    thread_website.start()
    thread_bot.start()

    # Hello :D