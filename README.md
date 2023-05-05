# CS361 Project. Stardew Velley Match
- This project is a UI for my Stardew Valley Match but also has the microservice for my partner.
# How to use the microservice
To **Request** data from the service you place the name of the item into a file named item_service.txt.
- Example Call:
```
        user_input = input('Give me an item: ')
        with open('item_service.txt', 'w', encoding='utf-8') as f:
            f.write(user_input)
```
To **Receive** data from the microservice you will need to open the file after the data from the 
microservice has been placed in the item_service.txt file and read it.
- Example Read:
```
        with open('item_service.txt', 'r+', encoding='utf-8') as f:
            item_text = f.read()
```

![CS361UMLsnip](https://user-images.githubusercontent.com/71857152/236573975-897c57e8-1b8a-473e-bee5-cc9c9838f29b.png)
