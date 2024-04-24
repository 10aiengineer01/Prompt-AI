from crewai_tools import BaseTool

class PromptDetailsSaverInstance:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PromptDetailsSaverInstance, cls).__new__(cls)
            cls._instance.data = {}
        return cls._instance

    def add_data(self, value, tac):
        #self.data.append(value)
        self.data.update({tac: value})

    def get_data(self) -> dict:
        return self.data

class saverTool(BaseTool):

    name: str = "SaveContentTool"
    description: str = "Saves your generated content"

    def _run(self, step_by_step_thinking: str, value: str = "The input you want to save", tac: str = "Use one of this words: PROMPT, PROMPT_INSTRUCTION, PROMPT_TEST") -> str:
        data_instance = PromptDetailsSaverInstance()
        if tac=="PROMPT" or tac=="PROMPT_INSTRUCTION" or tac=="PROMPT_TEST" or tac=="IDEA":
            if tac=="PROMPT":
                data_instance.add_data(value=value, tac=tac)
            elif tac=="IDEA":
                data_instance.add_data(value=value, tac=tac)
            elif tac=="PROMPT_INSTRUCTION":
                data_instance.add_data(value=value, tac=tac)
            elif tac=="PROMPT_TEST":
                data_instance.add_data(value=value, tac=tac)
            else:
                pass
            return "Your input was saved"
        else:
            return "Use one of these tacs: PROMPT, PROMPT_INSTRUCTION, PROMPT_TEST"
    
class saverToolExtended(BaseTool):

    name: str = "SaveContentTool"
    description: str = "Saves your generated content"

    def _run(self, step_by_step_thinking: str = "Think Step by Step about, what you want to save in this tool", name: str = "The promptname", description: str = "The promptdescription") -> str:
        data_instance = PromptDetailsSaverInstance()
        data_instance.add_data(name, tac="NAME")
        data_instance.add_data(description, tac="DESCRIPTION")
        return "Your input was saved"

class get_previous_promptnames(BaseTool):

    name: str = "GetInformationToll"
    description: str = "Gives you all previous prompt names"

    def get_prompt_ideas(self) -> str:
        """ Lese alle Zeilen aus der Datei promptideas.md und gib sie als String zurück """
        try:
            with open('IO/promptideas.md', 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return "Datei nicht gefunden"
        except Exception as e:
            return f"Ein Fehler ist aufgetreten: {str(e)}"

    def _run(self, value: str="") -> str:
        """
        Gets all previous prompt ideas 
        """
        return self.get_prompt_ideas()
    
class get_prompt_idea(BaseTool):

    name: str = "GetPromptInformation"
    description: str = "Gives you the prompt and all already created information"

    def _run(self, value: str="") -> str:
        data = PromptDetailsSaverInstance()
        return str(data.get_data())
