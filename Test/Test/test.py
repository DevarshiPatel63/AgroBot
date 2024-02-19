import os
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import boto3

#connect to claude model
def test_chatbot():
    demo_llm = Bedrock(
        credentials_profile_name='default',
        model_id='anthropic.claude-v2',
        model_kwargs={
            "temperature": 0.5,
            "top_p": 0.8,
            "top_k": 250,
            "max_tokens_to_sample": 200,
            "stop_sequences": []
        }
    )    
    return demo_llm

# response = test_chatboat("How India is Growing?")
# print(response)

def testing_memory():
    llm_data = test_chatbot()
    memory = ConversationBufferMemory(llm=llm_data,max_token_limit=512)
    return memory

def test_conversation(input_text,memory):
    llm_chain_data = test_chatbot()
    llm_conversation =  ConversationChain(llm=llm_chain_data,memory=memory,verbose=True)
    chat_reply = llm_conversation.predict(input=input_text)
    return chat_reply

    

