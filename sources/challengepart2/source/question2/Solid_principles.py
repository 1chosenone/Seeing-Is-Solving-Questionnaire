
from sources.challengepart1.commontools.Answer_choices import AnswerChoices


class SolidPrinciples:
    def __init__(self):
        self.__name = "SOLID Principles"
        self.__description = """SOLID Principles are the five design principles of object-oriented programming and design.
         They are a mnemonic acronym, giving acronyms to each of the principles: Single responsibility,  
         Open–closed, Liskov substitution, Interface segregation, and Dependency inversion. The principles are a subset
         of many principles promoted by American software engineer and instructor Robert C. Martin. They are intended to 
         make software designs more understandable, flexible and maintainable."""
        self.tipsToAnswer = """Read the description in the following file : Question2.pynb and choose the correct 
        answer from AnswerChoices enum. Then implement each method of this class."""

    def get_answer_for_problem_A(self) -> AnswerChoices:
        return "LSP"
    
    def get_answer_for_problem_B(self) -> AnswerChoices:
        return "OCP"
    
    def get_answer_for_problem_C(self) -> AnswerChoices:
        return "ISP"

    def get_answer_for_problem_D(self) -> AnswerChoices:
        return "SRP"

    def get_answer_for_problem_E(self) -> AnswerChoices:
        return "DIP"
