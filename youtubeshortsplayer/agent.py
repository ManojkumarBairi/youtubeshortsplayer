# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Demonstration of Youtube Shorts Player using Agent Development Kit"""

from google.adk.agents import SequentialAgent
from youtubeshortsplayer.sub_agents.picker.agent import picker_agent
from youtubeshortsplayer.sub_agents.player.agent import player_agent

root_agent = SequentialAgent(
    name="root_agent",
    description="A Root Agent to orchestrate the flow",
    sub_agents=[
        picker_agent,
        player_agent,
    ],
)
