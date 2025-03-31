import os
from aiohttp import web
from botbuilder.core import BotFrameworkAdapterSettings, BotFrameworkAdapter, TurnContext
from botbuilder.schema import Activity
from logic import BotLogic

from dotenv import load_dotenv

load_dotenv()

APP_ID = os.environ.get("MicrosoftAppId", "") # Replace here the AppID
APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "") # Replace here the microsoft app password

bot = BotLogic()
adapter_settings = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
adapter = BotFrameworkAdapter(adapter_settings)

async def messages(req: web.Request) -> web.Response:
    body = await req.json()
    activity = Activity().deserialize(body)
    auth_header = req.headers.get("Authorization", "")
    async def call_bot(turn_context: TurnContext):
        await bot.on_turn(turn_context)
    await adapter.process_activity(activity, auth_header, call_bot)
    return web.Response(status=200)

app = web.Application()
app.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    web.run_app(app, host="localhost", port=3978)
