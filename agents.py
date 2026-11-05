from crewai import Agent

from tools import yt_tool

blog_researcher = Agent(
    role="Blog Researcher from YouTube videos",
    goal="Get the relevant video content for the topic {topic} from the YouTube channel",
    backstory=(
        "Expert in understanding videos in AI, Data Science, Machine Learning and Gen AI, "
        "and in providing well-grounded suggestions."
    ),
    tools=[yt_tool],
    verbose=True,
    memory=True,
    allow_delegation=True,
)

blog_writer = Agent(
    role="Blog Writer",
    goal="Narrate compelling stories about the video {topic} from the YouTube channel",
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging narratives that "
        "captivate and educate, bringing new discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    verbose=True,
    memory=True,
    allow_delegation=False,
)
