# Pill Dispenser AI Agent Code
from icode_nexus import ask

current_weight = 100
pill_color = "Red"
print(current_weight,pill_color)

SYSTEM_INSTRUCTION=""" The agent takes the data from the weight and color sensor and sends an email to the patient's doctor. It sends a text message to the caretaker or family member if they didn't take their pill. """

chat_history=[]

def get_medbot_response(user_message):
    response = ask(user_message, system_instruction=SYSTEM_INSTRUCTION, history=chat_history)
    return response

while True:
    user_input = input("User: ")
    if user_input == 'exit':
        break
    print(get_medbot_response(user_input))