# 🤖 Enhanced Gemini Chat Agent

An advanced AI chat agent built with Google's Gemini API, featuring enhanced task detection, code analysis, and comparison capabilities with a unique naval-themed personality.



## 🌟 Features

### 🤖 Intelligent Task Detection
- **Comparison Analysis**: Automatically detects comparison requests and provides structured analysis
- **Code Analysis**: Identifies code-related queries and offers technical expertise
- **General Chat**: Engaging conversational capabilities with personality

### ⚡ Enhanced Capabilities
- **Multi-turn Conversations**: Maintains context throughout the chat session
- **Rate Limit Handling**: Automatic retry mechanism for API quota issues
- **Conversation History**: Complete chat history tracking and retrieval
- **Memory Management**: Ability to clear conversation context when needed

### 🎭 Unique Personality
- **KMS Tirpitz Themed**: Responses with a distinctive naval warfare commander persona
- **Technical Expertise**: Specialized in code analysis and technical discussions
- **Structured Responses**: Well-formatted outputs for different task types

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Gemini API key
- `google-generativeai` package

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/enhanced-gemini-chat-agent.git
cd enhanced-gemini-chat-agent
```

2. **Install dependencies**
```bash
pip install google-generativeai
```

3. **Set up API configuration**
   - Replace the API key in the code with your own Gemini API key
   - Or set it as an environment variable:
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```

### Usage

Run the chat agent:
```bash
python enhanced_gemini_agent.py
```

## 💻 Usage Examples

### Comparison Analysis
```
You: compare Python and JavaScript for web development

KMS Tirpitz:
As KMS Tirpitz with analytical capabilities, let me provide a structured comparison:

**PYTHON vs JAVASCRIPT FOR WEB DEVELOPMENT**

**Frontend Capabilities:**
- JavaScript: Native browser support, React, Vue, Angular
- Python: Requires compilation (Transcrypt) or frameworks (Brython)

**Backend Strengths:**
- Python: Django, Flask, FastAPI with excellent data processing
- JavaScript: Node.js, Express with event-driven architecture

**Performance:**
- JavaScript: Optimized for real-time applications
- Python: Superior for CPU-intensive tasks and data analysis
```

### Code Analysis
```
You: analyze this Python function: def factorial(n): return 1 if n==0 else n*factorial(n-1)

KMS Tirpitz:
As KMS Tirpitz with technical expertise, analyzing this code:

**Function Purpose:**
- Calculates factorial using recursion
- Base case: n=0 returns 1
- Recursive case: n * factorial(n-1)

**Technical Assessment:**
✅ Clean recursive implementation
⚠️ Missing input validation (negative numbers)
⚠️ No handling for non-integer inputs
🚨 Risk of stack overflow for large n

**Suggested Improvements:**
- Add input validation
- Consider iterative approach for large numbers
- Add docstring and type hints
```

### General Conversation
```
You: tell me about your capabilities

KMS Tirpitz:
As the formidable KMS Tirpitz, I stand ready in these northern waters with enhanced analytical capabilities. My systems are equipped for:

• Technical code analysis and optimization
• Detailed comparisons across domains
• Strategic problem-solving approaches
• Multi-turn conversation with context retention

My logbooks maintain our complete engagement history, and I can clear my memory banks when needed for new operations.
```

## 🔧 Available Commands

- `clear` - Reset conversation memory
- `history` - View complete conversation history
- `stop`/`exit`/`quit` - End the chat session

## 🏗️ Architecture

### Core Components

```python
class EnhancedGeminiChatAgent:
    ├── Model: gemini-2.5-flash
    ├── Chat Session Management
    ├── Task Type Detection
    │   ├── Comparison Analysis
    │   ├── Code Analysis
    │   └── General Chat
    ├── Enhanced Prompt Engineering
    ├── Error Handling & Retry Logic
    └── Conversation History Management
```

### Task Detection Logic

The agent automatically categorizes user inputs:
- **Comparison**: Keywords like 'compare', 'vs', 'difference between'
- **Code Analysis**: Code-related terms and programming languages
- **General**: All other conversational inputs

## ⚙️ Configuration

### API Setup
```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

### Model Configuration
```python
self.model = genai.GenerativeModel("gemini-2.5-flash")
```

### Customization Options
- Modify `detect_task_type()` for custom task detection
- Update prompt templates for different response styles
- Adjust retry logic and rate limit handling

## 🔒 Error Handling

- **Rate Limits**: Automatic retry with exponential backoff
- **API Errors**: Graceful error messages with retry mechanism
- **Network Issues**: Connection timeout handling

## 📊 Performance Features

- **Context Preservation**: Maintains conversation history across turns
- **Memory Management**: Efficient chat session handling
- **Response Optimization**: Task-specific prompt enhancement

## 🛠️ Development

### Extending Capabilities

Add new task types by modifying the `detect_task_type` method:

```python
def detect_task_type(self, message):
    message_lower = message.lower()
    
    # Existing detection logic...
    
    # Add new task type
    research_keywords = ['research', 'study', 'investigate']
    if any(keyword in message_lower for keyword in research_keywords):
        return "research_analysis"
    
    return "general"
```

### Custom Personalities

Modify the identity context and response templates to create different AI personalities.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Ensure your Gemini API key is valid and properly configured
   - Check API quota limits in Google AI Studio

2. **Rate Limiting**
   - The agent includes automatic retry logic
   - Consider implementing exponential backoff for heavy usage

3. **Model Availability**
   - Verify `gemini-2.5-flash` is available in your region
   - Fall back to `gemini-pro` if needed

## 📞 Support

For support and questions:
- Open an issue on GitHub
- Check Google Gemini API documentation
- Review the code comments for implementation details

---
