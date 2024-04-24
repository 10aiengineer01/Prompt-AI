
class Memory:
    
    @staticmethod
    def get_prompt_ideas() -> str:
        """ Lese alle Zeilen aus der Datei promptideas.md und gib sie als String zurück """
        try:
            with open('promptideas.md', 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return "Datei nicht gefunden"
        except Exception as e:
            return f"Ein Fehler ist aufgetreten: {str(e)}"
    
    @staticmethod
    def add_prompt_idea(prompt_idea: str) -> None:
        """ Füge eine neue Idee zur Datei promptideas.md hinzu """
        try:
            with open('promptideas.md', 'a', encoding='utf-8') as file:
                file.write(prompt_idea + '\n')
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten beim Schreiben in die Datei: {str(e)}")
