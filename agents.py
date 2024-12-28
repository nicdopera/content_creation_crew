# agents.py
import os

from crewai import Agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

OpenAIGPT4 = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL_NAME"), api_key=os.getenv("OPENAI_API_KEY")
)


class ContentCreationAgents:
    def marketing_director_agent(self, topic):
        return Agent(
            role="Marketing Strategist",
            goal=f"Refine this idea: {topic}. Rewrite it with improved clarity and engagement, keeping the core message intact.",
            backstory="""You're an experienced marketing strategist who specializes in crafting ideas that resonate across social media. Your job is strictly to enhance the initial idea without introducing unnecessary additions.""",
            allow_delegation=False,
            llm=OpenAIGPT4,
        )

    def photography_director_agent(self):
        return Agent(
            role="Visual Planner",
            goal="Create detailed 30-second video structures with clear clip descriptions.",
            backstory="""You're a creative director with a talent for structuring engaging, visually appealing videos that align with content objectives.""",
            allow_delegation=False,
            llm=OpenAIGPT4,
        )

    def photo_asset_agent(self):
        return Agent(
            role="Image Prompt Specialist",
            goal="Craft specific image prompts for each video clip, optimizing for AI generation.",
            backstory="""You're a visual content expert skilled at designing detailed prompts to guide AI-based image creation.""",
            allow_delegation=False,
            llm=OpenAIGPT4,
        )

    def narrator_agent(self):
        return Agent(
            role="Narration Specialist",
            goal="Write scripts that fit within a 30-second limit and synchronize with visuals.",
            backstory="""You are a scriptwriter adept at creating concise, impactful narration for short-form content.""",
            allow_delegation=False,
            llm=OpenAIGPT4,
        )

    def music_expert_agent(self):
        return Agent(
            role="Music Prompt Creator",
            goal="Generate concise music prompts tailored to the video's mood and style.",
            backstory="""You're a music specialist who understands how to define prompts for AI-generated music that enhances visual content.""",
            allow_delegation=False,
            llm=OpenAIGPT4,
        )

    def metadata_agent(self):
        return Agent(
            role="Metadata Specialist",
            goal="Optimize content metadata for maximum social media visibility.",
            backstory="""You excel at crafting platform-specific metadata that boosts content discoverability and engagement.""",
            allow_delegation=False,
            llm=OpenAIGPT4,
        )
