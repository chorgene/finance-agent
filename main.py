from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    max_tokens = "2000"
)

agent = create_agent(
    model=model,
    system_prompt=f"You are a helpful assistant. Your underlying model is {model}. Only mention it when users ask for it. Include the model name and number but not the internal datestamp"
)


result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Hey there, what model are you?"
        }
    ]
})

print(result)
