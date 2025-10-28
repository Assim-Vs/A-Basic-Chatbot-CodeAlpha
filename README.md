# 🤖 Anu - Basic Chatbot with UI

**CodeAlpha Internship - Task 4: Basic Chatbot**

## About
This is a simple rule-based chatbot with a graphical user interface (GUI) built using Python and Tkinter. The chatbot, named **Anu**, can have basic conversations and perform mathematical calculations.

## Features

### ✅ Conversation Features
- Greetings: "hello", "hi", "hey"
- Status inquiries: "how are you"
- Farewells: "bye", "goodbye"
- Help commands: "help", "what can you do"
- General conversation responses

### ✅ Mathematical Calculations
The chatbot can perform basic arithmetic operations:

#### Addition
- `5 + 10` → Returns: "The sum of 5 and 10 is 15"
- `add 5 and 10` → Returns: "Addition: 5 + 10 = 15"

#### Subtraction
- `50 - 20` → Returns: "50 minus 20 equals 30"
- `subtract 20 from 50` → Returns: "Subtraction: 50 - 20 = 30"

#### Multiplication
- `6 * 7` → Returns: "6 multiplied by 7 equals 42"
- `multiply 6 by 7` → Returns: "Multiplication: 6 × 7 = 42"

#### Division
- `100 / 5` → Returns: "100 divided by 5 equals 20"
- `divide 100 by 5` → Returns: "Division: 100 ÷ 5 = 20"
- Handles division by zero with error message

## How to Run

1. **Prerequisites**: Make sure Python is installed on your system (Python 3.6 or higher)

2. **Run the chatbot**:
   ```bash
   python chatbot_anu.py
   ```

3. **Interact with Anu**:
   - Type your message in the input field at the bottom
   - Press **Enter** or click the **Send** button
   - Chat with Anu and try mathematical calculations!

## Key Concepts Used

### ✅ if-elif statements
Used in `get_response()` method to handle different user inputs and route to appropriate responses.

Example from code:
```python
if user_input in ['hello', 'hi', 'hey']:
    return "Hi there! How can I help you today?"
elif user_input in ['how are you', 'how are you?']:
    return "I'm doing great, thank you for asking!"
```

### ✅ Functions
- `get_response()`: Processes user input and returns appropriate response
- `process_math()`: Handles mathematical calculations
- `add_message()`: Adds messages to the chat display
- `send_message()`: Handles the send button click event
- `chatbot()` / `main()`: Main function to initialize and run the application

### ✅ Loops
- **while loop**: Used in the main program structure for continuous conversation (handled by Tkinter's `mainloop()`)
- The chat continues until the user says "bye" or closes the window

### ✅ Input/Output
- **Input**: Text input field and Entry widget for user messages
- **Output**: ScrolledText widget for displaying the conversation

## UI Components

- **Header**: Blue header bar with bot name
- **Chat Display**: Scrollable text area showing conversation history
- **Input Field**: Text input for user messages
- **Send Button**: Button to send messages

## Example Conversation

```
🤖 Anu: Hi! I'm Anu, your assistant chatbot. 👋

You: hello
🤖 Anu: Hi there! How can I help you today? 🙂

You: 10 + 15
🤖 Anu: The sum of 10 and 15 is 25. ✨

You: multiply 7 by 8
🤖 Anu: Multiplication: 7 × 8 = 56. ✨

You: how are you
🤖 Anu: I'm doing great, thank you for asking! How about you? 😊

You: bye
🤖 Anu: Goodbye! It was nice chatting with you! Have a wonderful day! 👋
```

## Requirements Met

✅ **Task Requirements:**
- Built a simple rule-based chatbot
- Input from user like: "hello", "how are you", "bye"
- Predefined replies like: "Hi!", "I'm fine, thanks!", "Goodbye!"
- Added **bonus feature**: Graphical User Interface (UI) using Tkinter
- Added **bonus feature**: Mathematical calculation capabilities
- Added **bonus feature**: Bot named "Anu"

✅ **Key Concepts:**
- ✅ `if-elif` statements
- ✅ Functions
- ✅ Loops
- ✅ Input/output

## File Structure

```
.
├── chatbot_anu.py    # Main chatbot application with GUI
└── README.md         # This file
```

## Notes

- The chatbot uses simple pattern matching for understanding user input
- Mathematical operations support both direct expressions (e.g., `5 + 10`) and text-based commands (e.g., `add 5 and 10`)
- The GUI provides a user-friendly interface for interacting with the chatbot
- All error handling is implemented for edge cases (like division by zero)

---

**Created for:** CodeAlpha Internship Program  
**Task:** 4 - Basic Chatbot  
**Bot Name:** Anu 🤖

