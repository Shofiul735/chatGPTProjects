import openai
from dotenv import load_dotenv
import os
import argparse


PROMPT = """
Yout will receive a file's contents as text
Generate a code review for the file. Indicate what changes should be made to improve its
style, performance, readbility, and maintainability. If there are any reputable libraries that
could be introduced to improve the code, suggest them.
For each suggested change, include the line number to which you are referring
"""


def get_code_review(filecontent,model):
    messages = [
        {"role":"system", "content":PROMPT},
        {"role":"user","content":f"Code review the following code: {filecontent}"}
    ]

    result = openai.ChatCompletion.creat(
        model = model,
        messages = messages
    )

    return result["choices"][0]["message"]["content"]

def make_code_review_request(file_path,model):
    with open(file_path,"r") as file:
        file_content = file.read()
    
    code_review_content = get_code_review(file_content,model)
    return code_review_content

def main():
    parser = argparse.ArgumentParser(description="Code reviwer arguments")
    parser.add_argument('file')
    parser.add_argument('--model',default="gpt-4")
    args = parser.parse_args()
    result = make_code_review_request(args.file,args.model)
    print(result)

# Intruction
# python reviwer.py YOUR_FILE_NAME.WHATEVER --model=gpt-3.5-turbo(default=gpt-4)

if __name__ == '__main__':
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    main()