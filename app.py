import streamlit as st

# Fashion Stylist Chatbot using basic Python

def start_chat():
    st.write("Hi! I am Maggie!")
    st.write("Your Personal Fashion Stylist Chat Assistant for today!")
    st.write("--------------------------------------------")
    st.write("👉 To start a new chat, type: hi")
    st.write("👉 To end the chat, type: bye")
    st.write("--------------------------------------------")

def fashion_bot(user):
    if user == "hi":
        st.write("MAGGIE: Hello! 😊 How can I help you today?")
        st.write("You can ask about:")
        st.write("- casual wear")
        st.write("- party wear")
        st.write("- ethnic wear")
        st.write("- office wear")
        st.write("- footwear")
        st.write("- accessories")
        st.write("- winter wear")
        st.write("- summer wear")

    elif user == "casual wear":
        st.write("MAGGIE: Casual wear ideas include:")
        st.write("- jeans and t-shirt")
        st.write("- shorts and tops")
        st.write("- kurtis with leggings")
        st.write("- oversized shirts")

    elif user == "party wear":
        st.write("MAGGIE: Party wear options are:")
        st.write("- dresses")
        st.write("- gowns")
        st.write("- crop tops with skirts")
        st.write("- blazers with trousers")

    elif user == "ethnic wear":
        st.write("MAGGIE: Ethnic wear includes:")
        st.write("- sarees")
        st.write("- lehengas")
        st.write("- anarkali suits")
        st.write("- kurta sets")

    elif user == "office wear":
        st.write("MAGGIE: Office wear suggestions:")
        st.write("- formal shirts and trousers")
        st.write("- blazers")
        st.write("- pencil skirts")
        st.write("- formal kurtis")

    elif user == "footwear":
        st.write("MAGGIE: Footwear choices:")
        st.write("- sneakers")
        st.write("- heels")
        st.write("- sandals")
        st.write("- loafers")
        st.write("- traditional juttis")

    elif user == "accessories":
        st.write("MAGGIE: Accessories to complete your look:")
        st.write("- watches")
        st.write("- handbags")
        st.write("- earrings")
        st.write("- belts")
        st.write("- sunglasses")

    elif user == "winter wear":
        st.write("MAGGIE: Winter wear collection:")
        st.write("- jackets")
        st.write("- hoodies")
        st.write("- sweaters")
        st.write("- coats")
        st.write("- scarves")

    elif user == "summer wear":
        st.write("MAGGIE: Summer wear ideas:")
        st.write("- cotton dresses")
        st.write("- skirts")
        st.write("- shorts")
        st.write("- tank tops")
        st.write("- light kurtis")

    elif user == "bye":
        st.write("MAGGIE: Thank you for chatting with me! Stay stylish ✨")

    else:
        st.write("MAGGIE: Sorry, I didn't understand that.")
        st.write("Please type one of the fashion categories mentioned.")


st.title("MAGGIE – Fashion Stylist Chatbot 🤖")
start_chat()

user_input = st.text_input("You:")

if user_input:
    fashion_bot(user_input.lower())
