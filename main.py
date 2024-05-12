import google.generativeai as genai
import random
import time

API_KEY = 'YOUR_API_KEY'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def generate_idea():
    response = model.generate_content("Write any idea for python code. Give response as only this idea")
    response.resolve()
    idea = response.text
    return idea

def generate_code(idea):
    response = model.generate_content(f"Write code for {idea}. As response give only code")
    response.resolve()
    code = response.text
    return code

def main():
    for i in range(10):
        idea = generate_idea()
        code = generate_code(idea)
        print(f"Idea {i+1}: {idea}\n\nCode:\n")
        lines = code.split('\n')
        for line in lines:
            print(line)
            time.sleep(random.uniform(0.1, 0.5))
        print("\n\n")
        print("This is the end of coden\n\n")
        print(("-" * 100), '\n\n')
        c = input("Press 'C' key to continue\nPress any other key to stop\nPress anything...  ")
        if c == 'C' or c == 'c':
            continue
        else:
            break

if __name__ == '__main__':
    main()
