import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load .env file FIRST
load_dotenv()

# Now create client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

class SupportAgent:
    def __init__(self):
        self.conversation_history = []
    
    def chat(self, user_message):
        """Send message and get response from Claude"""
        
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=500,
            system="You are a helpful customer support agent. Answer questions briefly and clearly.",
            messages=self.conversation_history
        )
        
        assistant_message = response.content[0].text
        
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message


if __name__ == "__main__":
    agent = SupportAgent()
    
    response1 = agent.chat("Hello, I need help with my order")
    print(f"Agent: {response1}\n")
    
    response2 = agent.chat("Can you track it for me?")
    print(f"Agent: {response2}\n")