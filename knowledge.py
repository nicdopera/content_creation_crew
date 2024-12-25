class ContentCreationKnowledge:
    @staticmethod
    def get_content_guidelines():
        return """
# AI Content Creation Knowledge Base
## Overview
This document outlines the standardized structure and rules for generating optimal content output using AI agents. Each piece of content must follow specific formatting guidelines and include all required components to ensure consistency and quality.

## Required Output Components
### 1. Content Brief
Short overview of the content theme and objective
Target audience and platform considerations
Key messages or takeaways
Estimated engagement metrics

### 2. Sora Storyboard Script
Technical Requirements
Total Duration - Exactly 30 seconds
Shot Combinations - Use only 5-second and 10-second shots
Valid combinations:
  6 x 5-second shots
  3 x 10-second shots
  2 x 10-second shots + 2 x 5-second shots
  4 x 5-second shots + 1 x 10-second shot
Caption Rules
5-second shots:
  Maximum 2 captions
  Placement - Second 0, Second 5
  Example:
    Shot 1 (0-5s)
    (0s) A serene beach at sunrise, gentle waves rolling in
    (5s) A flock of seabirds glides across the golden sky
10-second shots:
  Maximum 3 captions
  Placement - Second 0, Second 5, Second 10
  Example:
    Shot 1 (0-10s)
    (0s) A bustling city street during rush hour
    (5s) Traffic begins to slow as people notice something in the sky
    (10s) A brilliant aurora appears above the skyscrapers
    
### 3. Narrator Script
Time-stamped dialog matching the visual storyboard
Voice tone and style specifications
Pacing guidelines
Example:
  (0:00-0:05) "In the heart of nature's canvas..."
  (0:05-0:10) "Where dreams take flight..."
  
### 4. Music Prompt
Components:
  Genre/Style
  Tempo/BPM
  Mood/Emotion
  Key musical elements
  Reference tracks (if applicable)
Example:
  Style - Ambient Electronic
  Tempo - 80-85 BPM
  Mood - Contemplative, Uplifting
  Elements - Soft synthesizer pads, gentle percussion, atmospheric textures
  
### 5. Content Publishing Metadata
Required fields:
  Title (max 100 characters)
  Description (max 500 characters)
  Tags (8-12 relevant hashtags)
  Platform-specific requirements
  TikTok format
  YouTube format

## Quality Guidelines
1. Visual Continuity:
  Ensure smooth transitions between shots
  Maintain consistent visual style
  Consider color palette and composition
2. Narrative Flow:
  Clear beginning, middle, and end
  Engaging story arc
  Coherent message delivery
3. Audio Integration:
  Synchronize narration with visuals
  Balance music with voice-over
  Strategic use of silence
4. Platform Optimization:
  Adhere to platform-specific best practices
  Consider aspect ratios and formatting
  Optimize for mobile viewing

## Review Checklist
- All required components included
- Storyboard follows shot duration rules
- Captions properly spaced and timed
- Narration matches visual elements
- Music specifications complete
- Metadata optimized for platform
- Total duration exactly 30 seconds
- Transitions and flow verified
"""

    @staticmethod
    def get_output_template():
        return """
##CONTENT BRIEF
(brief content description)

##FORMAT
(the scheme for the shots composition e.g. 3 x 10-second shots)

##SHOT1
(first shot divided by captions)

##SHOT(N)
(n shot divided by captions)

##NARRATOR SCRIPT
(narrator script)

##MUSIC PROMPT
(music prompt)

##PUBLISHING METADATA
##TikTok Version
Title:
Description:
Tags:

##YouTube Version
Title:
Description:
Tags:
"""

    @staticmethod
    def get_example_output():
        return """
##CONTENT BRIEF
A reflective and empowering piece targeting young adults struggling with the pressures of their twenties. The narrative takes a warm, mentor-like approach, using metaphorical imagery of nature and growth to convey the message that personal development is not a race. The content aims to provide comfort and perspective to viewers aged 18-29 who feel overwhelmed by societal expectations.

##FORMAT
3 x 10-second shots

##SHOT1
0s
A young person sits alone on a rooftop at golden hour, overlooking a bustling city, the expression thoughtful and slightly worried
5s
The camera slowly circles around him as time-lapse clouds race overhead
10s
The scene transitions to show multiple versions of the same person walking different paths in a beautiful garden maze

##SHOT2
0s
Split screen showing the same person in different scenarios - studying in a library, laughing with friends at a cafe, working late at a startup
5s
The splits begin to merge as the person walks forward, leaving the different versions behind
10s
They approach a mirror in a sunlit room, their reflection showing them smiling confidently

##SHOT3
0s
The person stands at the edge of a forest clearing, surrounded by seedlings and fully grown trees
5s
As they walk through the forest, each tree they pass represents a different life milestone, some trees tall, others still growing
10s
The final frame shows them sitting peacefully under a young but healthy tree, writing in a journal, surrounded by soft natural light

##NARRATOR SCRIPT
"Dear twenty-something me, I see you there, carrying the weight of a thousand expectations...
Trying to sprint through chapters that were meant to be savored...
Here's what I wish I knew: There's no single path to success...
No universal timeline for finding yourself...
Like these trees in the forest, we all grow at our own pace...
Your journey is uniquely yours, and that's what makes it beautiful."

##MUSIC PROMPT
Style - Ambient Electronic
Tempo - 80-85 BPM
Mood - Contemplative, Uplifting
Elements - Soft synthesizer pads, gentle percussion, atmospheric textures

##PUBLISHING METADATA
##TikTok Version
Title: "POV: Reading a Letter to My Anxious 20-Year-Old Self 📝✨"
Description: "Friendly reminder: Your 20s aren't a race to be won, they're chapters to be lived. 🌱 Each of us blooms in our own time. Save this for when you need to hear it. #TwentySomething"
Tags: #GrowthMindset #QuarterLifeCrisis #TwentySomething #PersonalGrowth #SelfLove #LifeAdvice #MentalHealth #Mindfulness #Healing #LifeLessons #Motivation #SelfDiscovery

##YouTube Version
Title: "A Gentle Reminder: Your 20s Don't Need to Be Perfect | Letter to My Younger Self"
Description: "Feel like everyone has it figured out except you? This letter is for every twenty-something feeling overwhelmed by the pressure to have it all figured out. Remember: your journey is uniquely yours, and that's what makes it beautiful. 🌱
Take a breath. You're exactly where you need to be.
Share this with someone who needs to hear it today. 💌"
Tags: mindfulness, personal growth, life advice, twenty something, quarter life crisis, mental health, self development, life lessons, motivation, healing journey, self discovery, growth mindset
"""
