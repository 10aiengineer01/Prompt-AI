from crewai import Agent, Task, Crew

from mem.memory import Memory
from tool.tools import saverTool, saverToolExtended, PromptDetailsSaverInstance, get_previous_promptnames, get_prompt_idea
from LPU.models import setup_models
from LPU.prompts import prompt_initiator

class run_promptbase_agent:

    def __init__(self) -> None:

        model_setup = setup_models("openai")

        self.memory_editor = Memory()
        
        self.promptideas_memory = self.memory_editor.get_prompt_ideas()

        self.llm = model_setup.get_llm()

        self.prompts = prompt_initiator()

        saver = saverTool()
        promptnamegetter = get_previous_promptnames()
        promptIdea = get_prompt_idea()
        savernd = saverToolExtended()

        self.manager = Agent(
                role="Manager Agent",
                goal=self.prompts.manager_prompt,
                llm=self.llm, 
                verbose=True,
                allow_delegation=True,
                backstory=(" "),
                tools=[]
            )

        task = Task(
            description="Create a new prompt with all information", agent=self.manager, expected_output='A confirmation that every promptpart has been created', tools= []
        )

        agents = [
            self.manager,
            Agent(
                role="Promptidea Creator",
                goal=self.prompts.PromptIdeaAgent,
                llm=self.llm, 
                verbose=True,
                allow_delegation=False,
                backstory=(" "),
                tools=[saver, promptnamegetter],
            ),
            Agent(
                role="Prompt Creator",
                goal=self.prompts.promptGenerator,
                llm=self.llm, 
                verbose=True,
                allow_delegation=False,
                tools=[saver, promptIdea],
                backstory=(" ")
            ),
            Agent(
                role="Promptdescriber Agent",
                goal=self.prompts.promptdescriber,
                llm=self.llm, 
                verbose=True,
                allow_delegation=False,
                tools=[savernd, promptIdea],
                backstory=(" ")
            ),
            Agent(
                role="Promptinstructor Agent",
                goal=self.prompts.promptinstructor,
                llm=self.llm, 
                verbose=True,
                allow_delegation=False,
                tools=[saver, promptIdea],
                backstory=(" ")
            ),
            Agent(
                role="Prompttester Agent",
                goal=self.prompts.prompttester,
                llm=self.llm, 
                verbose=True,
                allow_delegation=False,
                tools=[saver, promptIdea],
                backstory=(" ")
            ),
        ]

        self.crew = Crew(
            agents=agents,
            tasks=[task],
            verbose=2
        )

    def run(self) -> str:

        self.crew.kickoff()

        instance = PromptDetailsSaverInstance()
        result = instance.get_data()

        self.memory_editor.add_prompt_idea(result["IDEA"])
        
        return result

if __name__=="__main__":
    agent = run_promptbase_agent()
    result = agent.run()
    print("Promptname: ")
    print(result["NAME"])
    print("Promptdescription: ")
    print(result["DESCRIPTION"])
    print("Prompt: ")
    print(result["PROMPT"])
    print("Promptinstruction: ")
    print(result["PROMPT_INSTRUCTION"])
    print("Prompttest: ")
    print(result["PROMPT_TEST"])
