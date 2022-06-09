import pyautogui
import schedule
import time
import telegram

bot = telegram.Bot(token='TELEGRAM_BOT_TOKEN')
bot.send_message(chat_id='TELEGRAM_CHAT_ID', text="💻 Bot aktif...")
print("💻 Bot aktif...")

def amogus():
    print("💵 Son sayfa yenileme: " + time.ctime())
    bot.send_message(chat_id='TELEGRAM_CHAT_ID', text="💵 Son sayfa yenileme: " + time.ctime())
    pyautogui.hold(keys='shift')
    pyautogui.press(keys='f5' , interval=1, presses=10)

schedule.every(15).minutes.do(amogus)

while True:
    schedule.run_pending()
    time.sleep(1)