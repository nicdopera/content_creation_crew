from crewai import Task


class ContentCreationTasks:
    def marketing_analysis_task(self, agent, topic):
        return Task(
            description=f"""Improve the idea:{topic}. Make it more engaging, audience-focused, and optimized for maximum watch time and viewer retention.""",
            agent=agent,
            input=topic,
            expected_output="""
            MARKETING OUTPUT
            [one-sentence viral content description]
            """,
        )

    def visual_description_task(self, agent):
        return Task(
            description="""Describe the video structure for a 30-second duration, consisting of 5 or 10-second clips. Specify each clip's purpose, style, and transitions.""",
            agent=agent,
            input=lambda: agent.previous_output(),
            expected_output="""
            VISUAL PLAN
            - Clip Descriptions:
              Clip 1: [description]
              Clip 2: [description]
              ...
            - Total Duration: 30 seconds
            """,
        )

    def photo_reference_task(self, agent):
        return Task(
            description="""Generate specific image prompts for each clip based on the visual descriptions. Ensure these prompts align with Runway's capabilities.""",
            agent=agent,
            input=lambda: agent.previous_output(),
            expected_output="""
            IMAGE PROMPTS
            - Clip 1 Prompt: [detailed image prompt]
            - Clip 2 Prompt: [detailed image prompt]
            ...
            """,
        )

    def narration_task(self, agent):
        return Task(
            description="""Write a narration script that complements the visual structure while adhering to the 30-second duration limit.""",
            agent=agent,
            input=lambda: agent.previous_output(),
            expected_output="""
            NARRATION SCRIPT
            - Full Script: [narration text synchronized with clips]
            """,
        )

    def music_task(self, agent):
        return Task(
            description="""Generate a brief music prompt that matches the mood and pace of the video.""",
            agent=agent,
            input=lambda: agent.previous_output(),
            expected_output="""
            MUSIC PROMPT
            - Style: [music style]
            - Mood: [music mood]
            """,
        )

    def metadata_task(self, agent):
        return Task(
            description="""Create optimized metadata, including titles, descriptions, and tags for YouTube and Instagram.""",
            agent=agent,
            input=lambda: {
                "marketing": agent.previous_output(step=-5),
                "visual": agent.previous_output(step=-4),
                "narration": agent.previous_output(step=-2),
                "music": agent.previous_output(step=-1),
            },
            expected_output="""
            METADATA
            - YouTube:
              Title: [title]
              Description: [description]
              Tags: [tags]
            - Instagram:
              Title: [title]
              Description: [description]
              Hashtags: [hashtags]
            """,
        )
