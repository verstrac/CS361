# CS361 Project. Stardew Velley Match
- This project is a UI for my Stardew Valley Match but also has the microservice for my partner.
# How to use the microservice
- To request data from the service you place the name of the item into a file named item_service.txt.
- Example Call:
user_input = input('Give me an item: ')
with open('item_service.txt', 'w', encoding='utf-8') as f:
  f.write(user_input)
