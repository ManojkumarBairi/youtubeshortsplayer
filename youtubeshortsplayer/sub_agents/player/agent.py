from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from youtubeshortsplayer.sub_agents.player import prompt
from youtubeshortsplayer.sub_agents.picker.agent import picker_agent
from youtubeshortsplayer.sub_agents.player.tools import video_player

player_agent = Agent(
    model="gemini-2.0-flash-001",
    name="player_agent",
    instruction=prompt.PLAYER_AGENT_INSTR,
    description="This agent plays youtube shorts videos based on text inputs",
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
    tools=[video_player]
)