from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field

class Reflection(BaseModel):
    missing: str = Field(description="Critique of what is missing in the answer.")
    superfluous: str = Field(description="Critique of what is superfluous in the answer.")

class AnswerQuestion(BaseModel):
    answer: str = Field(description="Around 250 word answer to the question.")
    reflection: Reflection = Field(description="Reflection on the initial answer.")
    search_queries: List[str] = Field(description="1 to 3 search queries to address the critique of your current answer.")
    