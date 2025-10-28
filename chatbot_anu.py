"""
Task 4: Basic Chatbot with UI
CodeAlpha Internship Program

A simple rule-based chatbot with graphical user interface.
Bot Name: Anu
Features: Conversation + Mathematical calculations
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
import re

class AnuChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Anu - Basic Chatbot")
        self.root.geometry("600x700")
        self.root.configure(bg="#f0f0f0")
        
        # Bot name
        self.bot_name = "Anu"
        
        # Create GUI components
        self.create_widgets()
        
        # Welcome message
        self.add_message(self.bot_name, f"Hi! I'm {self.bot_name}, your assistant chatbot. 👋\n"
                            "I can help you with:\n"
                            "- Basic conversations\n"
                            "- Math calculations (addition, subtraction, multiplication, division)\n"
                            "Try saying 'hello' or ask me to calculate something!")
    
    def create_widgets(self):
        """Create the chat interface widgets"""
        
        # Header
        header = tk.Frame(self.root, bg="#4a90e2", height=60)
        header.pack(fill=tk.X)
        
        title_label = tk.Label(header, text=f"🤖 {self.bot_name} Chatbot", 
                               font=("Arial", 18, "bold"), 
                               bg="#4a90e2", fg="white")
        title_label.pack(pady=15)
        
        # Chat display area
        self.chat_display = scrolledtext.ScrolledText(
            self.root,
            width=60,
            height=25,
            font=("Arial", 11),
            bg="#ffffff",
            wrap=tk.WORD,
            state=tk.DISABLED,
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.chat_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Configure text tags for styling
        self.chat_display.tag_config("bot", foreground="#4a90e2", font=("Arial", 11, "bold"))
        self.chat_display.tag_config("user", foreground="#2c3e50", font=("Arial", 11))
        self.chat_display.tag_config("system", foreground="#7f8c8d", font=("Arial", 10, "italic"))
        
        # Input frame
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        # Input field
        self.user_input = tk.Entry(input_frame, font=("Arial", 12), relief=tk.FLAT, bd=2)
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)
        self.user_input.bind("<Return>", lambda e: self.send_message())
        
        # Send button
        send_button = tk.Button(
            input_frame,
            text="Send",
            command=self.send_message,
            font=("Arial", 11, "bold"),
            bg="#4a90e2",
            fg="white",
            relief=tk.FLAT,
            padx=20,
            cursor="hand2"
        )
        send_button.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Focus on input field
        self.user_input.focus()
    
    def add_message(self, sender, message, tag="user"):
        """Add a message to the chat display"""
        self.chat_display.config(state=tk.NORMAL)
        
        if sender == self.bot_name:
            self.chat_display.insert(tk.END, f"{sender}: ", "bot")
            self.chat_display.insert(tk.END, f"{message}\n\n", "user")
        else:
            self.chat_display.insert(tk.END, f"{sender}: ", "bot")
            self.chat_display.insert(tk.END, f"{message}\n\n", "user")
        
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def get_response(self, user_input):
        """
        Function to process user input and return appropriate response.
        Handles conversations and mathematical calculations.
        """
        user_input_lower = user_input.lower().strip()
        
        # Handle mathematical calculations
        math_result = self.process_math(user_input)
        if math_result:
            return math_result
        
        # Handle greetings
        if user_input_lower in ['hello', 'hi', 'hey', 'hi there', 'good morning', 'good evening']:
            return f"Hi there! How can I help you today? 🙂"
        
        # Handle status inquiries
        elif user_input_lower in ['how are you', 'how are you?', 'how r u', 'hru']:
            return "I'm doing great, thank you for asking! How about you? 😊"
        
        # Handle farewells
        elif user_input_lower in ['bye', 'goodbye', 'see you', 'see ya', 'exit', 'quit']:
            return "Goodbye! It was nice chatting with you! Have a wonderful day! 👋"
        
        # Handle questions about the chatbot
        elif user_input_lower in ['what are you', 'who are you', 'what is your name', 'who r u', 'introduce yourself']:
            return f"I'm {self.bot_name}, a simple rule-based chatbot created for CodeAlpha Internship Task 4! I love helping with conversations and math. 🤖"
        
        # Handle help requests
        elif user_input_lower in ['help', 'what can you do', 'commands', 'features']:
            return ("I can help you with:\n"
                   "• Basic conversations and greetings\n"
                   "• Math calculations:\n"
                   "  - Addition: 'add 5 and 10' or '5 + 10'\n"
                   "  - Subtraction: 'subtract 20 from 50' or '50 - 20'\n"
                   "  - Multiplication: 'multiply 6 by 7' or '6 * 7'\n"
                   "  - Division: 'divide 100 by 5' or '100 / 5'\n"
                   "• General chit-chat\n\n"
                   "Try asking me to calculate something! 🧮")
        
        # Handle thank you
        elif user_input_lower in ['thanks', 'thank you', 'thx', 'thankyou']:
            return "You're welcome! I'm always here to help! 😊"
        
        # Handle calculator requests
        elif 'calculate' in user_input_lower or 'solve' in user_input_lower:
            return "I'd be happy to help! Try entering a math expression like '10 + 5' or '100 / 4'. 🧮"
        
        # Default response for unrecognized input
        else:
            return "I didn't quite understand that. Try saying 'hello', 'help', or ask me to do a math calculation! 💭"
    
    def process_math(self, user_input):
        """Process mathematical operations from user input"""
        try:
            # Try to extract and evaluate math expressions
            
            # Pattern 1: Direct operations like "5 + 3", "10 - 4", etc.
            math_pattern = r'(-?\d+\.?\d*)\s*([+\-*/])\s*(-?\d+\.?\d*)'
            match = re.search(math_pattern, user_input)
            
            if match:
                num1 = float(match.group(1))
                operator = match.group(2)
                num2 = float(match.group(3))
                
                if operator == '+':
                    result = num1 + num2
                    return f"The sum of {num1} and {num2} is {result}. ✨"
                elif operator == '-':
                    result = num1 - num2
                    return f"{num1} minus {num2} equals {result}. ✨"
                elif operator == '*':
                    result = num1 * num2
                    return f"{num1} multiplied by {num2} equals {result}. ✨"
                elif operator == '/':
                    if num2 == 0:
                        return "Oops! Division by zero is not possible. 🤔"
                    result = num1 / num2
                    return f"{num1} divided by {num2} equals {result}. ✨"
            
            # Pattern 2: Text-based operations
            if 'add' in user_input.lower() or '+' in user_input and 'plus' in user_input.lower():
                nums = re.findall(r'\d+\.?\d*', user_input)
                if len(nums) >= 2:
                    result = sum(float(n) for n in nums[:2])
                    return f"Addition: {nums[0]} + {nums[1]} = {result} ✨"
            
            elif 'subtract' in user_input.lower() or 'minus' in user_input.lower():
                nums = re.findall(r'\d+\.?\d*', user_input)
                if len(nums) >= 2:
                    result = float(nums[0]) - float(nums[1])
                    return f"Subtraction: {nums[0]} - {nums[1]} = {result} ✨"
            
            elif 'multiply' in user_input.lower() or 'product' in user_input.lower():
                nums = re.findall(r'\d+\.?\d*', user_input)
                if len(nums) >= 2:
                    result = float(nums[0]) * float(nums[1])
                    return f"Multiplication: {nums[0]} × {nums[1]} = {result} ✨"
            
            elif 'divide' in user_input.lower():
                nums = re.findall(r'\d+\.?\d*', user_input)
                if len(nums) >= 2:
                    if float(nums[1]) == 0:
                        return "Division by zero is not possible! 🙅"
                    result = float(nums[0]) / float(nums[1])
                    return f"Division: {nums[0]} ÷ {nums[1]} = {result} ✨"
            
        except Exception as e:
            return f"Sorry, I couldn't calculate that. Try a simpler expression! 😅"
        
        return None
    
    def send_message(self):
        """Handle sending a message"""
        user_message = self.user_input.get().strip()
        
        if not user_message:
            messagebox.showinfo("Empty Message", "Please enter a message!")
            return
        
        # Display user message
        self.add_message("You", user_message)
        
        # Clear input field
        self.user_input.delete(0, tk.END)
        
        # Get and display bot response
        response = self.get_response(user_message)
        self.add_message(self.bot_name, response)
        
        # Check if user wants to exit
        if user_message.lower() in ['bye', 'goodbye', 'exit', 'quit']:
            self.root.after(2000, self.root.quit)


def main():
    """Main function to run the chatbot GUI"""
    root = tk.Tk()
    app = AnuChatbot(root)
    root.mainloop()


if __name__ == "__main__":
    main()

