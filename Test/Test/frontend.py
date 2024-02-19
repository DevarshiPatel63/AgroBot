# import streamlit as st
# import boto3 
# import test as test

# s3 = boto3.client('s3')

# st.title("AgroBot: A chatBot for farmers")

# if 'memory' not in st.session_state:
#     st.session_state.memory = test.testing_memory() 
        
# if 'chat_history' not in st.session_state:
#     st.session_state.chat_history = []
        
# for message in st.session_state.chat_history:
#     with st.chat_message(message["role"]):
#         st.markdown(message["text"])
            
# input_text = st.chat_input("Ask your Problem")
# uploaded_file = st.sidebar.file_uploader("Choose an image")


# if input_text:
#     with st.chat_message("user"):
#         st.markdown(input_text)
            
#     st.session_state.chat_history.append({"role":"user","text":input_text})
        
#     chat_response = test.test_conversation(input_text=input_text , memory=st.session_state.memory)
        
#     with st.chat_message("Assistant"):
#          st.markdown(chat_response)
            
#     st.session_state.chat_history.append({"role":"assistant","text":chat_response})

# elif uploaded_file is not None:
#     file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type}
#     st.write(file_details) 
    
#     # Display the image
#     chat_image = st.image(uploaded_file, width=300)  

#     # Upload original file to S3  
#     # s3.upload_fileobj(
#     #     Fileobj=uploaded_file,    
#     #     Bucket="agro-boat",
#     #     Key=uploaded_file.name
#     # )

#     st.session_state.chat_history.append({
#         "role": "user",
#         "text": chat_image
#     })
    
import streamlit as st
import boto3 
import test as test

s3 = boto3.client('s3')

st.title("AgroBot: A chatBot for farmers :seedling: ")

if 'memory' not in st.session_state:
    st.session_state.memory = test.testing_memory() 
        
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
        
for message in st.session_state.chat_history:
    if message["role"] == "user":
        if "text" in message:
            with st.chat_message("user"):
                st.markdown(message["text"])
        elif "image" in message:
            with st.chat_message("user"):
                st.image(message["image"], width=300)
    else:
        with st.chat_message("assistant"):
            st.markdown(message["text"])
            
input_text = st.chat_input("Ask your Problem")
uploaded_file = st.sidebar.file_uploader("Choose an image")

if input_text:
    with st.chat_message("user"):
        st.markdown(input_text)
            
    st.session_state.chat_history.append({"role": "user", "text": input_text})
        
    chat_response = test.test_conversation(input_text=input_text, memory=st.session_state.memory)
        
    with st.chat_message("assistant"):
         st.markdown(chat_response)
            
    st.session_state.chat_history.append({"role": "assistant", "text": chat_response})

elif uploaded_file is not None:    
    # Display the image
    chat_image = st.image(uploaded_file, width=300)      

    # Upload original file to S3  
    # s3.upload_fileobj(
    #     Fileobj=uploaded_file,    
    #     Bucket="agro-boat",
    #     Key=uploaded_file.name
    # )
    if st.button('Send'):
        st.session_state.chat_history.append({
            "role": "user",
            "image": uploaded_file
        })
