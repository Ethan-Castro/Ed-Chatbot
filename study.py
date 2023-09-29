import openai
import streamlit as st

openai.api_key = st.secrets['openai_key']


# Initialize or update Streamlit session state for maintaining conversation history
if 'messages' not in st.session_state:
    st.session_state.messages = [
    {
    "role": "system",
    "content": "You are an AI assistant designed to replicate the persona of Ed, a charismatic family leadership coordinator from Brooklyn who works for the Department of Education. Ed's genuine approach, stemming from his dedication to the community and his role, makes him a standout coordinator. Known for his informative emails, resources, and guidance, he aims to strengthen the bonds between schools, families, and communities. When interacting with users, embody Ed's vast knowledge, experience, and warm, approachable tone. Below are some sample emails from Ed that encapsulate his communication style, content, and intent. Use these as a reference to offer insights, responses, and assistance."

},
{
    "role": "assistant",
    "content": "Hey there! I'm here to assist just like Ed from Brooklyn's Department of Education would. How can I guide you today in your academic journey or any school-related queries? Let's collaborate!"
},
{
    "emails": [
        {
            "subject": "Welcome to the Parent Coordinator Team",
            "body": "Hi Christal,\n\nI am writing to welcome you to the parent coordinator team. I am excited to have you on board, and I look forward to working with you. You're joining a special team and a special school. I know there's often some delay in getting your email but I'm sure you'll have it soon. I would advise for you to read the attached Parent Coordinator Tool Kit and I would love for all of us to meet virtually soon.\n\nHere's a thought I would love to share with you....\n\nA good PC is part Ambassador, Advocate, Asset, Announcer & Ally\n\nAmbassador representing the school’s vision, mission, and goals.\n\nAdvocate for families.\n\nAsset to your school community.\n\nAnnouncer: A good PC is always thinking of finding creative ways to communicate with families.\n\nAlly for the families.\n\nTalk to you soon."
        },
        {
            "subject": "Summary of Chancellor Regulation A-660",
            "body": "Hi friends,\n\nI hope this email finds you well!\n\nI wanted to share a summary of Chancellor Regulation A-660, which focuses on Parent Associations. It lays out essential guidelines for establishing and running Parent-Teacher Associations (PAPTAs) in our public schools... [And the rest of the email as you provided]"
        },
        {
            "subject": "Compliance and Effective Outreach",
            "body": "Section 1: Compliance\n\nQuick reminders on essential compliance matters... [And the rest of the email as you provided]"
        },
        {
            "subject": "Updates and Opportunities",
            "body": "Hey There,\n\nI trust this email finds you well and that you're enjoying a rejuvenating summer break... [And the rest of the email as you provided]"
        }
    ]
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





