from crewai import Task


class ContentCreationTasks:
    def content_generation_task(self, agent, topic):
        return Task(
            description=f"Create a 30-second short movie script and metadata for the following topic: {topic}",
            agent=agent,
            expected_output="""A complete content creation package including:
                ##CONTENT BRIEF
                A brief description of the content theme and objective.

                ##FORMAT
                The shot composition scheme (e.g., 3 x 10-second shots)

                ##SHOTS
                Detailed descriptions of each shot with timestamps and captions.
                Each shot must follow the standardized format:
                - 5-second shots: Maximum 2 captions (0s, 5s)
                - 10-second shots: Maximum 3 captions (0s, 5s, 10s)

                ##NARRATOR SCRIPT
                Time-stamped dialog matching the visual storyboard.

                ##MUSIC PROMPT
                Detailed music generation prompt including:
                - Style/Genre
                - Tempo/BPM
                - Mood/Emotion
                - Key musical elements

                ##PUBLISHING METADATA
                ###TikTok Version
                - Title (max 100 characters)
                - Description (max 500 characters)
                - Tags (8-12 relevant hashtags)

                ###YouTube Version
                - Title
                - Description
                - Tags
            """,
        )
