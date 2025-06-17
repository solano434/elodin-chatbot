
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.llms import HuggingFacePipeline
from transformers import pipeline
import torch
# change one added imports gr & st
import gradio as gr
import streamlit as st
import sys

# Load a local Hugging Face model for text generation
generator = pipeline("text-generation", model="distilgpt2", torch_dtype=torch.float32)

# Wrap it with LangChain
llm = HuggingFacePipeline(pipeline=generator)

# Define a basic prompt template
prompt = PromptTemplate.from_template("You are Elodin, an AI assistant. Reply to: {question}")

# Build a simple LangChain chain
chain = prompt | llm | StrOutputParser()

# Main chat loop
print("Elodin is ready! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Elodin: Until next time.")
        break
    response = chain.invoke({"question": user_input})
    print("Elodin:", response)

# change 2
import sys

def chatbot_interface(input_text):
    return chain.run(input_text)

def run_cli():
    print("Welcome to Elodin (CLI mode). Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Elodin: Farewell, dreamer.")
            break
        response = chain.run(user_input)
        print("Elodin:", response)

def run_gradio():
    gr.Interface(fn=chatbot_interface,
                 inputs="text",
                 outputs="text",
                 title="Elodin - LangChain Chatbot",
                 description="Chat with your LangChain-powered assistant."
                 ).launch()

def run_streamlit():
    st.title("Elodin - LangChain Chatbot")
    user_input = st.text_input("You:", "")
    if user_input:
        response = chain.run(user_input)
        st.write("Elodin:", response)

if __name__ == "__main__":
    mode = "cli"  # default
    if len(sys.argv) > 1:
        mode = sys.argv[1]

    if mode == "cli":
        run_cli()
    elif mode == "gradio":
        run_gradio()
    elif mode == "streamlit":
        run_streamlit()
    else:
        print("Invalid mode. Use 'cli', 'gradio', or 'streamlit'.")
