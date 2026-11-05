import os

from crewai_tools import YoutubeChannelSearchTool
from crewai_tools.tools.rag.rag_tool import RagTool
from crewai_tools.rag.data_types import DataType

# Channel to search; override with the YOUTUBE_CHANNEL_HANDLE environment variable (with or without the "@").
YOUTUBE_CHANNEL_HANDLE = os.getenv("YOUTUBE_CHANNEL_HANDLE", "@krishnaik06").lstrip("@")
YOUTUBE_CHANNEL_URL = f"https://www.youtube.com/@{YOUTUBE_CHANNEL_HANDLE}"


def build_youtube_tool() -> YoutubeChannelSearchTool:
    """Create the channel search tool and index the channel (needs network access).

    crewai-tools' own constructor shortcut hands the loader a bare "@handle", which its loader rejects
    (it requires a full youtube.com URL), so the channel URL is registered through the base RagTool.add().
    """
    tool = YoutubeChannelSearchTool()
    RagTool.add(tool, YOUTUBE_CHANNEL_URL, data_type=DataType.YOUTUBE_CHANNEL)
    tool.description = f"Semantic search over the content of the YouTube channel @{YOUTUBE_CHANNEL_HANDLE}."
    return tool


yt_tool = build_youtube_tool()
