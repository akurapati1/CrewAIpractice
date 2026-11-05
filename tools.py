import os

from crewai_tools import YoutubeChannelSearchTool

# Channel to search; override with the YOUTUBE_CHANNEL_HANDLE environment variable.
YOUTUBE_CHANNEL_HANDLE = os.getenv("YOUTUBE_CHANNEL_HANDLE", "@krishnaik06")

yt_tool = YoutubeChannelSearchTool(youtube_channel_handle=YOUTUBE_CHANNEL_HANDLE)
