import random
import asyncio
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount, Activity, ActivityTypes

class BotLogic(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        # Send typing indicator
        typing_activity = Activity(type=ActivityTypes.typing)
        await turn_context.send_activity(typing_activity)

        text = turn_context.activity.text.strip()

        # Simulate a fake request with random delay
        response = await self.fake_request(text)

        # Send the final response
        await turn_context.send_activity(f"Response: {response}")

    async def fake_request(self, message: str) -> str:
        delay = random.uniform(1.0, 10.0)  # Random delay between 1 and 10 seconds
        await asyncio.sleep(delay)
        return message  # Replace here the response of the LLM

    async def on_members_added_activity(self, members_added, turn_context: TurnContext):
        await turn_context.send_activity("Hello and welcome to the Echo Bot!")
