import asyncio
from bot.handlers import start_bot
from services.monitor import run_monitor

async def main():
    bot_task = start_bot()
    monitor_task = run_monitor()
    await asyncio.gather(bot_task, monitor_task)

if __name__ == "__main__":
    asyncio.run(main())