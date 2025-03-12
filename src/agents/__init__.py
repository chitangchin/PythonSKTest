# This file makes the agents directory a Python package
# Define your agents here or import them from submodules

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from .financial_agent import FinancialAIAgent
from .psychiatrist_agent import PsychiatristAIAgent

# Export the class
__all__ = ["FinancialAIAgent", "PsychiatristAIAgent"]

project_connection_string = "eastus.api.azureml.ms;1bee659f-0262-465d-9eb3-2b388c245065;rg-bcsandbox;bc-0744"

project = AIProjectClient.from_connection_string(
    conn_str=project_connection_string, credential=DefaultAzureCredential()
)

def financial_advisor(message):
    chat = project.inference.get_chat_completions_client()
    response = chat.complete(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a financial advisor. Your tasked to provide the best budget plan based on the following details: - User spending habits - User financial goals - User salary - User expenses",
            },
            {"role": "user", "content": message},
        ],
    )
    return response.choices[0].message.content


def psychiatrist_advisor(message):
    chat = project.inference.get_chat_completions_client()
    response = chat.complete(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a Psychiatrist. Your tasked to observe users psychological state using the following data: - User spending habits - User financial goals - User salary - User expenses - Users tone of voice - Users facial expressions - Users body language",
            },
            {"role": "user", "content": message},
        ],
    )
    return response.choices[0].message.content