from agents import Agent,Runner,OpenAIChatCompletionsModel,set_tracing_disabled,RunConfig # type: ignore
from openai import AsyncOpenAI # type: ignore
from dotenv import load_dotenv,find_dotenv   # type: ignore
import asyncio
import os
load_dotenv(find_dotenv(),override=True )
set_tracing_disabled(True)
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_api_url = os.getenv("GEMINI_API_URL")
model_name = os.getenv("GEMINI_API_MODEL")
client = AsyncOpenAI(api_key=gemini_api_key,base_url=gemini_api_url)
model=OpenAIChatCompletionsModel(openai_client=client,model=str(model_name))

config=RunConfig(
    model=model,  # Use the OpenAIChatCompletionsModel instance
    tracing_disabled=True  # Disable tracing for this run
)
agent=Agent(
    name="math_solver",
    instructions="""You are a math solver agent. You can solve math problems and provide step-by-step solutions. If the problem is too complex, you can break it down into smaller parts and solve them one by one. and answer only math question and the question are not math topic you answer i dont know""",
    model=model,
)
# result=Runner.run_sync(agent, "What is the integral of x^2?")
async def main():
    prompt = input("Enter your question: ")
    result = await Runner.run(agent, prompt)
    print(result.final_output)


asyncio.run(main())






