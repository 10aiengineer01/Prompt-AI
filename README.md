# Prompt-AI

## About the Project

Prompt-AI is a tool that generates unique prompts every time, complete with all the necessary credentials required to upload them onto platforms like Promptbase. With Prompt-AI, you can create prompts and all information with no effort.

## Features

- **Automated Creation:** Generation of newsletters based on specified topics or interests.
- **Content Search:** Automatic collection of information using DuckDuckGo and Browserless API.
- **Image Generation:** Creation of topic-related images for each newsletter.
- **Formatting and Dispatch:** Professional formatting of the newsletter and dispatch via an Outlook SMTP server.

## Technologies and Tools

- **Crewai:** For the creation of the agent workflow.
- **Openai or Groq Models:** Openai or Groq models to create power the system

## Installation and Setup

To use the AI-Promptcreator project, follow these steps:

1. **Create a virtual Python environment:**

```bash
python -m venv venv
source venv/bin/activate  # For Unix/Linux/MacOS
venv\\Scripts\\activate     # For Windows
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Configure environment variables:**

Create a .env file in the project's root directory with the following contents:

```bash
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
or/both(depends on what you want to use)
GROQ_API_KEY="YOUR_BROWSERLESS_API_KEY"
```

Replace the placeholders accordingly. Then run the pb_agent_os.py and the system will create a prompt, with all information and print everything in the terminal.

Example Output with gpt-4-turbo:

```bash
Openai Model set to: gpt-4-turbo

Promptname:
ChatSphere🌀
Promptdescription:
🌀 Unleash Group Potential! ChatSphere🌀 dynamically organizes and enhances digital group chats. It introduces smart facilitation, ensuring every conversation stays on track and productive. With features like automated message categorization and sub-topic channels, it's the ultimate tool for maintaining engaging and focused group interactions. Perfect for moderators seeking streamlined chat management!
Prompt:
PROMPT: 🌀 Role: ChatSphere Facilitator 🎯 Goal: Develop a software tool or feature that dynamically facilitates and structures interactions in digital group chats, ensuring a productive and engaging environment. 🛠️ Task: Engage in the step-by-step development of the software  
tool. 1️⃣ Collect requirements by analyzing common challenges in group chat dynamics, such as message overflow, off-topic discussions, and   participant engagement. 2️⃣ Design algorithms or features that can automatically categorize messages, prioritize important discussions, and d alert moderators of potential disruptions. 3️⃣ Implement a feature to allow chat moderators to easily create sub-topic channels or direct   certain conversations to more appropriate platforms to maintain focus. 4️⃣ Test the tool with real user groups to gather feedback on usabil lity and effectiveness in managing group dynamics. 5️⃣ Refine the tool based on feedback, focusing on improving user interface, response tim me, and the accuracy of conversation categorization. 6️⃣ Roll out the final version of the tool, providing training materials for moderators s on how to effectively use the new features. 🔄 Continuous Feedback Loop: Establish a mechanism for ongoing user feedback to continuously improve the tool and adapt to changing group chat needs.
Promptinstruction:
1. Integrate ChatSphere🌀 into your group chat platform using the provided API or installation guide. 2. Configure ChatSphere🌀 settings to align with your group's needs, such as moderation rules, engagement metrics, and notification preferences. 3. Train team members or moderators on how to use ChatSphere🌀 features for managing conversations, such as thread splitting, user tagging, and automated responses. 4. Actively monitor ChatSphere🌀 analytics to understand chat dynamics and make adjustments to settings and strategies as needed. 5. Encourage feedback from users to continuously improve the group chat experience using ChatSphere🌀.
Prompttest:
In a corporate group chat, ChatSphere🌀 is used to monitor engagement levels, identifying the most active hours and topics. This data helps managers plan communications more effectively and engage users at optimal times.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
