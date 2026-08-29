# GenAI_With_Langchain
# GenAI With LangChain

A practical collection of Generative AI and LangChain examples covering LLMs, Chat Models, Prompt Templates, Output Parsers, and Structured Output.

This repository contains my hands-on learning and implementation of core LangChain concepts using Python and different LLM providers.

---

## 📚 Topics Covered

- Large Language Models (LLMs)
- Chat Models
- OpenAI Chat Models
- Anthropic Chat Models
- Google Gemini Chat Models
- Hugging Face Models
- Local Hugging Face Models
- Prompt Templates
- Chat Prompt Templates
- Message Placeholders
- Output Parsers
- String Output Parser
- JSON Output Parser
- Pydantic Output Parser
- Structured Output
- JSON Schema
- Pydantic
- TypedDict
- LangChain Expression Language (LCEL)

---

## 📂 Repository Structure

```text
GenAI_With_Langchain/
│
├── Langchain_models/
│   ├── 1. LLMs/
│   ├── 2.ChatModels/
│   ├── 3.EmbeddedModels/
│   ├── requirements.txt
│   └── test.py
│
├── Langchain_Output_Parsers/
│   ├── jsonoutputparser.py
│   ├── pydanticoutputparser.py
│   ├── stroutputparser.py
│   ├── stroutputparser1.py
│   └── structuredoutputparser.py
│
├── Langchain_Prompts/
│   ├── chat_prompt_template.py
│   ├── chatbot.py
│   ├── message_placeholder.py
│   ├── messages.py
│   ├── prompt_generator.py
│   ├── prompt_ui.py
│   ├── prompt_ui_local.py
│   ├── template.json
│   └── test_streamlit.py
│
├── Langchain_Structured_Output/
│   ├── json_schema.json
│   ├── pydantic_demo.py
│   ├── typeddict_demo.py
│   ├── with_structured_output_json.py
│   ├── with_structured_output_pydantic.py
│   └── with_structured_output_typeddict.py
│
├── .gitignore
└── README.md
