import lib.bot_main_logic as bot
import lib.clock as clock

if clock.check_time():
    bot.sender_call()