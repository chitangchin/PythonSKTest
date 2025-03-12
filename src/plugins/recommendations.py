from semantic_kernel.functions import kernel_function
from agents import FinancialAIAgent;
from agents import PsychiatristAIAgent;

class RecommendationsPlugin:

    @kernel_function(
        name="get_recommendations",
        description="Sending Psychological data to Psychiatrist AI Agent, then sending the full json to Financial Data to Financial AI Agent",
    )
    def get_recommendation(
        self,
        message: str,
    ) -> str:
    
        PsychiatristAIAgent(message)
        json = {
            "psychology": PsychiatristAIAgent(message),
            "income": "$2000 per month",
            "expenses": "$1500 per month",
            "savings": "$500 per month",
        }
        FinancialAIAgent(json)
        return message