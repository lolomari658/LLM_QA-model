# LLM_QA_CLI.py

import openai
import re

# Set your OpenAI API key
openai.api_key = "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"

def preprocess_question(question):
    """Basic preprocessing: lowercase, remove punctuation"""
    question = question.lower()
    question = re.sub(r'[^\w\s]', '', question)
    return question

def get_answer(question):
    """Send the question to the LLM API and get the response"""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Answer the following question:\n{question}",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def main():
    print("=== LLM Q&A CLI ===")
    while True:
        question = input("\nEnter your question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            print("Exiting...")
            break
        processed = preprocess_question(question)
        print(f"Processed Question: {processed}")
        answer = get_answer(processed)
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
