import google.generativeai as genai
import time

# ==============================================
# 🔑 Gemini API Key 
# ==============================================
genai.configure(api_key="AIzaSyDPuwNY1IaBn7PMliZFbIZoQ3HM7tiWDJI")

# ==============================================
# 🤖 Enhanced Gemini Chat Agent
# ==============================================
class EnhancedGeminiChatAgent:
    def _init_(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")
        self.chat = None
        
        self.reset_chat()
    
    def reset_chat(self):
        """Start a new chat session with identity"""
        self.chat = self.model.start_chat(history=[])
        # Set the identity context
        self.chat.send_message(self.identity_context)
    
    def detect_task_type(self, message):
        """Detect what kind of task the user is requesting"""
        message_lower = message.lower()
        
        # Comparison detection
        comparison_keywords = ['compare', 'vs', 'versus', 'difference between', 'which is better', 'pros and cons']
        if any(keyword in message_lower for keyword in comparison_keywords):
            return "comparison"
        
        # Code analysis detection
        code_keywords = ['code', 'program', 'function', 'script', 'python', 'java', 'javascript', 'c++', 'analyze this code']
        if any(keyword in message_lower for keyword in code_keywords):
            return "code_analysis"
        
        return "general"
    
    def send_message(self, message, retries=3):
        """Send message to chat with enhanced task handling"""
        task_type = self.detect_task_type(message)
        
        # Enhance the prompt based on task type
        if task_type == "comparison":
            enhanced_prompt = f"As KMS Tirpitz with analytical capabilities, compare and contrast the following in detail: {message}. Provide a structured analysis with key differences and similarities."
        elif task_type == "code_analysis":
            enhanced_prompt = f"As KMS Tirpitz with technical expertise, analyze this code: {message}. Explain what it does, identify any issues, and suggest improvements if needed."
        else:
            enhanced_prompt = f"As KMS Tirpitz, respond to: {message}"
        
        for attempt in range(retries):
            try:
                response = self.chat.send_message(enhanced_prompt)
                return response.text
                
            except Exception as e:
                error_msg = str(e)
                
                # Handle rate limit
                if "429" in error_msg or "quota" in error_msg:
                    print("⚠ Rate limit hit, retrying...")
                    time.sleep(2)
                    continue
                
                return f"Error: {e}"
        
        return "Error: Please try again later."
    
    def get_history(self):
        """Get the conversation history in readable format"""
        readable_history = []
        for message in self.chat.history:
            # Skip the system prompt for cleaner history
            if message.parts and message.parts[0].text != self.identity_context:
                role = "You" if message.role == "user" else "AI"
                text = message.parts[0].text if message.parts else "[No text]"
                readable_history.append(f"{role}: {text}")
        
        return readable_history
    
    def clear_memory(self):
        """Clear the conversation memory"""
        self.reset_chat()

# ==============================================
# 🚀 Enhanced Main Program
# ==============================================
def main():
    # Initialize the enhanced chat agent
    chat_agent = EnhancedGeminiChatAgent()
    
    print("I now have enhanced capabilities:")
    print("- I can compare and analyze different topics")
    print("- I can read and understand code")
    print("- I provide detailed technical analysis")
    print("\nCommands:")
    print("Type 'clear' to reset my memory")
    print("Type 'history' to see our conversation")
    print("Type 'stop' or 'exit' to quit the program.\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ["stop", "exit", "quit", "bye"]:
            print("AI: Until we meet again in these northern waters. Farewell!")
            break
        
        elif user_input.lower() == "clear":
            chat_agent.clear_memory()
            print("AI: My memory has been cleared. The fog lifts, and we begin anew.")
            continue
        
        elif user_input.lower() == "history":
            history = chat_agent.get_history()
            if not history:
                print("AI: No conversation history yet. My logbooks are empty.")
                continue
                
            print("\n" + "="*50)
            print("CONVERSATION HISTORY")
            print("="*50)
            for i, message in enumerate(history, 1):
                print(f"{i}. {message}")
            print("="*50 + "\n")
            continue
        
        # Send message with enhanced processing
        ai_reply = chat_agent.send_message(user_input)
        print("\n KMS Tirpitz: \n", ai_reply)

if __name__ == "_main_":
    main()
