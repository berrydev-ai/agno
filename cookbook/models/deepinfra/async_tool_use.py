"""Run `pip install duckduckgo-search` to install dependencies."""

import asyncio

from agno.agent import Agent
from agno.models.deepinfra import DeepInfra
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=DeepInfra(id="meta-llama/Llama-2-70b-chat-hf"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

asyncio.run(agent.aprint_response("What's the latest news about AI?", stream=True))
