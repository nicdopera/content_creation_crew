# knowledge.py


class ContentCreationKnowledge:
    @staticmethod
    def get_content_guidelines():
        return """
# AI Content Creation Guidelines

## Workflow Overview
The content creation process is divided into six key stages, each handled by a specialized agent. These stages ensure structured, high-quality outputs optimized for short-form video content.

### 1. Marketing Brief
- Refine the topic to maximize viral potential.
- Provide a concise, actionable idea for content creation.

### 2. Visual Plan
- Structure a 30-second video using 5- or 10-second clips.
- Include clear descriptions of each clip's purpose, style, and transitions.

### 3. Image Prompts
- Create detailed, scene-specific prompts for image generation.
- Ensure compatibility with Runway's AI video generation capabilities.

### 4. Narration Script
- Write a script synchronized with the visual plan.
- Maintain a 30-second limit, matching the tone and style of the visuals.

### 5. Music Prompt
- Generate a concise music prompt aligned with the video's mood and pacing.
- Specify style, mood, and rhythm for AI music generation.

### 6. Metadata
- Optimize titles, descriptions, and tags for platforms like Instagram and YouTube.
- Ensure metadata enhances discoverability and engagement.

## Quality Guidelines

### General Principles
- **Consistency:** Maintain a unified style across visuals, narration, and music.
- **Conciseness:** Outputs should be succinct and focused on the core idea.
- **Clarity:** Ensure all descriptions, prompts, and scripts are easy to interpret by AI systems.

### Visual Storytelling
- Define a clear narrative progression.
- Use engaging visual elements and transitions.

### Synchronization
- Align narration and music with the visual structure.
- Ensure smooth transitions between video clips.

### Platform Optimization
- Tailor content for platform-specific requirements (e.g., aspect ratio, duration).
- Use relevant hashtags and tags for better reach.

"""

    @staticmethod
    def get_output_template():
        return """
## Final Output Schema

### Marketing Output
- Refined Content Idea: [concise viral refinement]

### Visual Plan
- Clip Descriptions:
  Clip 1: [description]
  Clip 2: [description]
  ...
- Total Duration: 30 seconds

### Image Prompts
- Clip 1 Prompt: [detailed prompt]
- Clip 2 Prompt: [detailed prompt]
  ...

### Narration Script
- Full Script: [narration text synchronized with visuals]

### Music Prompt
- Style: [music style]
- Mood: [music mood]

### Metadata
#### YouTube
- Title: [title]
- Description: [description]
- Tags: [tags]

#### Instagram
- Title: [title]
- Description: [description]
- Hashtags: [hashtags]

"""
