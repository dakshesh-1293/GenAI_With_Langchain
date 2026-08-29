import os
from llama_cpp import Llama
import streamlit as st
from langchain_core.prompts import PromptTemplate

# Load the local GGUF model
llm = Llama(
    model_path=r"D:\AI_Models\qwen2.5-1.5b-instruct-q4_k_m.gguf",
    n_ctx=2048,
    verbose=False
)

st.header("Research Assistant")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


#Templete for the prompt
template = PromptTemplate(
    template="""Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.""",
input_variables=["paper_input", "style_input", "length_input"]
)


#fill the placeholders in the prompt template with the user inputs
prompt = template.invoke({
    'paper_input' : paper_input,
    'style_input' : style_input,
    'length_input' : length_input
})



if st.button("Summarize"):

    # Convert prompt to text
    prompt_text = prompt.text

    # Generate response using local model
    result = llm(
        prompt_text,
        max_tokens=100,
        temperature=0.7
    )

    # Display the response
    st.write(result["choices"][0]["text"])