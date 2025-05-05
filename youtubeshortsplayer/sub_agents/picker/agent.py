from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from youtubeshortsplayer.sub_agents.picker import prompt
from youtubeshortsplayer.sub_agents.picker.tools import video_picker

picker_agent = Agent(
    model="gemini-2.0-flash-001",
    name="picker_agent",
    instruction=prompt.PICKER_AGENT_INSTR,
    description="This agent creates youtube shorts videos based on text inputs",
    tools=[video_picker],
)