from crewai import Task

from agents import blog_researcher, blog_writer
from tools import yt_tool

research_task = Task(
    description=(
        "Identify the video about {topic}. "
        "Get detailed information about the video from the channel."
    ),
    expected_output="A comprehensive 3-paragraph report on the {topic} video content.",
    tools=[yt_tool],
    agent=blog_researcher,
)

write_task = Task(
    description="Using the research, write a blog post about the YouTube video on the topic {topic}.",
    expected_output="A well-structured blog post in Markdown summarising the video on the topic {topic}.",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    context=[research_task],
    output_file="new-blogpost.md",
)
