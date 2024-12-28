import os

from agents import ContentCreationAgents
from crewai import Crew, Process
from dotenv import load_dotenv
from knowledge import ContentCreationKnowledge
from langchain_openai import ChatOpenAI
from tasks import ContentCreationTasks

load_dotenv()

OpenAIGPT4 = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL_NAME"), api_key=os.getenv("OPENAI_API_KEY")
)


def run_content_creation_crew(topic):
    # Initialize components
    knowledge = ContentCreationKnowledge()
    agents = ContentCreationAgents()
    tasks = ContentCreationTasks()

    # Create agents
    marketing_director = agents.marketing_director_agent(topic)
    photography_director = agents.photography_director_agent()
    photo_asset_manager = agents.photo_asset_agent()
    narrator = agents.narrator_agent()
    music_expert = agents.music_expert_agent()
    metadata_specialist = agents.metadata_agent()

    # Form the crew with sequential task execution
    crew = Crew(
        agents=[
            marketing_director,
            photography_director,
            photo_asset_manager,
            narrator,
            music_expert,
            metadata_specialist,
        ],
        tasks=[
            tasks.marketing_analysis_task(marketing_director, topic),
            tasks.visual_description_task(photography_director),
            tasks.photo_reference_task(photo_asset_manager),
            tasks.narration_task(narrator),
            tasks.music_task(music_expert),
            tasks.metadata_task(metadata_specialist),
        ],
        process=Process.sequential,
        knowledge_sources=[
            knowledge.get_content_guidelines(),
            knowledge.get_output_template(),
        ],
        verbose=True,
    )

    # Execute the workflow
    crew.kickoff()

    # Fetch outputs from all agents
    final_output = {
        "Visual Plan": crew.get_task_output(
            tasks.visual_description_task(photography_director)
        ),
        "Image Prompts": crew.get_task_output(
            tasks.photo_reference_task(photo_asset_manager)
        ),
        "Narration Script": crew.get_task_output(tasks.narration_task(narrator)),
        "Music Prompt": crew.get_task_output(tasks.music_task(music_expert)),
        "Metadata": crew.get_task_output(tasks.metadata_task(metadata_specialist)),
    }

    return final_output


if __name__ == "__main__":
    topic = input("Provide the initial content topic: ")
    final_result = run_content_creation_crew(topic)

    print("\nFinal Outputs:")
    for section, output in final_result.items():
        print(f"{section}:\n{output}\n")
