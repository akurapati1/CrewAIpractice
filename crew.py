"""Run a two-agent CrewAI pipeline: research a YouTube video, then write a blog post about it.

Usage:  python crew.py "AI vs ML vs DL vs Data Science"
"""
import sys

from crewai import Crew, Process
from dotenv import load_dotenv

from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

DEFAULT_TOPIC = "AI vs ML vs DL vs Data Science"


def build_crew() -> Crew:
    return Crew(
        agents=[blog_researcher, blog_writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        memory=True,
        cache=True,
        max_rpm=100,
        share_crew=False,
    )


def main(topic: str) -> None:
    load_dotenv()
    result = build_crew().kickoff(inputs={"topic": topic})
    print(result)


if __name__ == "__main__":
    main(" ".join(sys.argv[1:]) or DEFAULT_TOPIC)
