import streamlit as st
import openai
import os




# Define Streamlit app
def app():
    
    def summeryizer( user_input,max_tokens,temperature=1,engine="gpt3"):
            response = openai.Completion.create(
              engine=engine,
              prompt=f"Summary:{user_input}",
              temperature=temperature,
              max_tokens=max_tokens,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0,
              stop=None)

            return  response['choices'][0]['text']
        

    
    
    st.set_page_config(page_title="OpenAI Simple Summerizer By Katya", page_icon=":robot:")
    st.title("OpenAI Simple Summerizer By Katya")
    
    with st.expander("Settings"):
            max_tokens = st.number_input("Max tokens", value=2000, key="max_tokens")
            temperature = st.number_input("Temperature", value=1, key="temperature")
            engine = st.text_input("Engine", "gpt3", key="gpt3")
            
            

            # Set up OpenAI API key
            openai.api_type = "azure"
            openai.api_base = st.text_input("API base", value="https://aks-production.openai.azure.com/", key="api_base")
            openai.api_version = st.text_input("api version",value="2023-03-15-preview")
            openai.api_key = st.text_input('azure openai key', key="KEY_AZURE_AI", value=os.getenv("KEY_AZURE_AI"), type="password") 
            if st.checkbox("Submit", key="submit"):
                st.success("Submitted!")

        
        

    user_input = st.text_area("Context", height=200, key="you are a bot very nice of a israeli startup",value="simple text summerizer should be here")
    st.write(summeryizer(user_input=user_input,max_tokens=max_tokens,temperature=temperature,engine=engine))

def main():
    app()


if __name__ == '__main__':
    main()
