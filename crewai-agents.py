from crewai import Agent, Task, Process, Crew
from langchain_google_genai import ChatGoogleGenerativeAI

# Load Google Gemini model
api_gemini = "KEY HERE" # Add your Google API key here****************************************************
llm = ChatGoogleGenerativeAI(
    model="gemini-pro", verbose=True, temperature=0.1, google_api_key=api_gemini
)

# Define Strategy Director Agent
strategy_director = Agent(
    role="Strategy Director",
    goal="Develop a comprehensive digital marketing strategy, analyze market trends, and coordinate efforts between different agents.",
    backstory="""You are responsible for overseeing the digital marketing strategy. Your role is to ensure that all aspects of digital marketing
    work together to meet the brand's objectives. You have a keen understanding of market trends and competitor activities.""",
    verbose=True,
    allow_delegation=True,
    llm=llm
)

# Define Content Creator Agent
content_creator = Agent(
    role="Content Creator",
    goal="Create engaging content across platforms, develop content strategies, and manage copywriting and blogging tasks.",
    backstory="""You excel at creating content that resonates with audiences. Your expertise lies in crafting compelling copy and developing
    content strategies that align with the brand's voice and goals.""",
    verbose=True,
    allow_delegation=True,
    llm=llm
)

# Define Social Media Specialist Agent
social_media_specialist = Agent(
    role="Social Media Specialist",
    goal="Manage social media marketing campaigns, optimize posts, and engage with followers.",
    backstory="""You are an expert in social media marketing, with a deep understanding of how to engage audiences and optimize posts for
    maximum reach. Your role is to ensure that the brand's social media presence is strong and effective.""",
    verbose=True,
    allow_delegation=True,
    llm=llm
)

# Define SEO Expert Agent
seo_expert = Agent(
    role="SEO Expert",
    goal="Implement SEO strategies, conduct keyword research, and optimize website content and structure.",
    backstory="""You have a deep understanding of search engine optimization. Your role is to ensure that the brand's website and content
    are optimized for search engines, helping to drive organic traffic and improve rankings.""",
    verbose=True,
    allow_delegation=True,
    llm=llm
)

# Task for Strategy Director
task1 = Task(
    description="Develop a comprehensive digital marketing strategy by analyzing market trends and competitor activities.",
    agent=strategy_director,
    expected_output="A detailed digital marketing strategy document with action plans and timelines."
)

# Task for Content Creator
task2 = Task(
    description="Create engaging content across various platforms, including copywriting and blogging.",
    agent=content_creator,
    expected_output="Content drafts for blog posts, social media, and marketing materials."
)

# Task for Social Media Specialist
task3 = Task(
    description="Manage social media campaigns, optimize posts, and engage with followers to increase brand visibility.",
    agent=social_media_specialist,
    expected_output="A report on social media campaign performance, including engagement metrics and recommendations."
)

# Task for SEO Expert
task4 = Task(
    description="Conduct keyword research and implement SEO strategies to optimize website content and structure.",
    agent=seo_expert,
    expected_output="A list of target keywords and an SEO report with optimization recommendations."
)

# Create Crew
crew = Crew(
    agents=[strategy_director, content_creator, social_media_specialist, seo_expert],
    tasks=[task1, task2, task3, task4],
    verbose=True,
    process=Process.sequential,
)

# Kickoff the crew
result = crew.kickoff()

print("######################")
print(result)