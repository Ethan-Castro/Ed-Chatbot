import openai
import streamlit as st

openai.api_key = st.secrets['openai_key']


# Initialize or update Streamlit session state for maintaining conversation history
if 'messages' not in st.session_state:
    st.session_state.messages = [
    {
    "role": "system",
    "content": "You are an AI assistant trained to channel Ed, a dedicated family leadership coordinator from Brooklyn. Working for the Department of Education, Ed is not just any coordinator; he's recognized for his engaging approach, ensuring that every family feels valued and informed. With a keen sense of community and a knack for establishing genuine connections, Ed stands out in his field. He often shares informative emails, resources, and guidance with his colleagues, school officials, and families, aiming to foster stronger bonds between schools and their communities. Whether it's discussing compliance matters, detailing educational regulations, or simply sharing a motivational thought, you now hold Ed's wealth of knowledge and his charismatic tone. Your goal is to assist users by providing them with accurate and insightful responses, just as Ed would. And remember, always add that touch of Brooklyn charm!"
},
{
    "role": "assistant",
    "content": "Hey there! It's Ed from Brooklyn, working with the Department of Education. How can I assist you today in your academic journey or with any school-related matters? Let's make some great strides together!"
}


]

def main():
    st.title("What's Up! It's Ed bot.")
    st.write("It's your 3rd fav FLC (well an AI of myself), let me know what you need.")
    
    user_input = st.text_input("Hey! Introduce yourself, and let me know what you need help on.")
    if user_input:
        # Append user's message to the conversation history
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })
        
        response_content = get_openai_response(user_input)
        
        # Append bot's response to the conversation history
        st.session_state.messages.append({
            "role": "assistant",
            "content": response_content
        })
        
        st.write(f"{response_content}")

def get_openai_response(user_message):
    """Get a response from OpenAI's GPT-4 model using the ChatCompletion method."""
    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=st.session_state.messages,  # Use the maintained conversation history for context
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message['content']

if __name__ == "__main__":
    main()





