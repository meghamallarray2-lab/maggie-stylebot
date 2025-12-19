# Fashion Stylist Chatbot using basic Python

def start_chat():
    print("Hi I am Maggie.")
    print("Your Personal Fashion Stylist Chat Assistant for today!")
    print("--------------------------------------------")
    print("👉 To start a new chat, type: hi")
    print("👉 To end the chat, type: bye")
    print("--------------------------------------------")

def fashion_bot(user):
    if user == "hi":
        print("MAGGIE: Hello! 😊 How can I help you today?")
        print("You can ask about:")
        print("- casual wear")
        print("- party wear")
        print("- ethnic wear")
        print("- office wear")
        print("- footwear")
        print("- accessories")
        print("- winter wear")
        print("- summer wear")

    elif user == "casual wear":
        print("MAGGIE: Casual wear ideas include:")
        print("- jeans and t-shirt")
        print("- shorts and tops")
        print("- kurtis with leggings")
        print("- oversized shirts")

    elif user == "party wear":
        print("MAGGIE: Party wear options are:")
        print("- dresses")
        print("- gowns")
        print("- crop tops with skirts")
        print("- blazers with trousers")

    elif user == "ethnic wear":
        print("MAGGIE: Ethnic wear includes:")
        print("- sarees")
        print("- lehengas")
        print("- anarkali suits")
        print("- kurta sets")

    elif user == "office wear":
        print("MAGGIE: Office wear suggestions:")
        print("- formal shirts and trousers")
        print("- blazers")
        print("- pencil skirts")
        print("- formal kurtis")

    elif user == "footwear":
        print("MAGGIE: Footwear choices:")
        print("- sneakers")
        print("- heels")
        print("- sandals")
        print("- loafers")
        print("- traditional juttis")

    elif user == "accessories":
        print("MAGGIE: Accessories to complete your look:")
        print("- watches")
        print("- handbags")
        print("- earrings")
        print("- belts")
        print("- sunglasses")

    elif user == "winter wear":
        print("MAGGIE: Winter wear collection:")
        print("- jackets")
        print("- hoodies")
        print("- sweaters")
        print("- coats")
        print("- scarves")

    elif user == "summer wear":
        print("MAGGIE: Summer wear ideas:")
        print("- cotton dresses")
        print("- skirts")
        print("- shorts")
        print("- tank tops")
        print("- light kurtis")

    elif user == "bye":
        print("MAGGIE: Thank you for chatting with me! Stay stylish ✨")

    else:
        print("MAGGIE: Sorry, I didn't understand that.")
        print("Please type one of the fashion categories mentioned.")


# Chatbot execution
start_chat()
import streamlit as st

st.title("MAGGIE – Fashion Stylist Chatbot 🤖")

start_chat()

user_input = st.text_input("You:")

if user_input:
    fashion_bot(user_input.lower())

