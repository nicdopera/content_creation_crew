import os

from agents import ContentCreationAgents
from crewai import Crew, Process
from dotenv import load_dotenv
from knowledge import ContentCreationKnowledge
from langchain_openai import ChatOpenAI
from openai import OpenAI
from tasks import ContentCreationTasks

# Load environment variables
load_dotenv()
print(f"Loaded API Key: {os.getenv('OPENAI_API_KEY')}")
OpenAIGPT4 = ChatOpenAI(model="chatgpt-4o-latest", api_key=os.getenv("OPENAI_API_KEY"))
print("All environment variables:")
for key, value in os.environ.items():
    if "OPENAI" in key:
        print(f"{key}: {value}")


def run_content_creation_crew(topic):
    # Get content creation guidelines
    knowledge = ContentCreationKnowledge()
    # Initialize agents and tasks
    agents = ContentCreationAgents()
    tasks = ContentCreationTasks()

    # Initialize agents
    marketing_director = agents.marketing_director_agent()
    photography_director = agents.photography_director_agent()
    sora_advisor = agents.sora_advisor_agent()
    music_expert = agents.music_expert_agent()
    session_manager = agents.session_manager_agent()

    # Initialize tasks
    content_generation = tasks.content_generation_task(marketing_director, topic)

    # Form the crew
    crew = Crew(
        agents=[
            marketing_director,
            photography_director,
            sora_advisor,
            music_expert,
            session_manager,
        ],
        tasks=[content_generation],
        process=Process.hierarchical,
        knowledge_sources=[
            knowledge.get_content_guidelines(),
            knowledge.get_output_template(),
            knowledge.get_example_output(),
        ],
        manager_llm=OpenAIGPT4,
        manager_agent=session_manager,
        verbose=True,
    )

    # Kick off the crew's work
    results = crew.kickoff()
    return results


if __name__ == "__main__":
    topic = "A super engaging video on how to let people go even if you still love them"
    results = run_content_creation_crew(topic)
    print("Content Creation Results:")
    print(results)
