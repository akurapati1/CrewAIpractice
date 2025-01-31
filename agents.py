from crewai import Agent
from tools import yt_tool

blog_researcher = Agent(
    role = 'Blog Researcher from Youtube videos',
    goal = 'get the relevent video content for the topic{topic} from youtube channel',
    verbose = True,
    memory = True,
    backstory= (
        "Expert in understanding videos in AI Data Science, Machine Learning and Gen AI and providing suggestions"
        ),
    tools = [],
    allow_deligation = True
)


blog_writer = Agent(
        role = 'Blog Writer',
        goal = 'Narrate Compelling teh stories about the video{topic} from youtube channel',
        verbose = True,
        memory = True,
        backstory= (
            "With a flair for simplifying complex topics, you craft"
            "engaging narratives that captivate and aducate, bringing new"
            "discoverables to light in as accessible manner"
        ),
        tools = [yt_tool],
        allow_deligation = False

)