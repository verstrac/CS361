# This is to show how to request items from the microservice
import time

def main():
    user_input = input('Give me an item: ')
    with open('item_service.txt', 'w', encoding='utf-8') as f:
        f.write(user_input)
        time.sleep(1)
    while True:
        with open('item_service.txt', 'r+', encoding='utf-8') as f:
            item_text = f.read()
            if item_text != user_input:
                print(item_text)
                f.truncate(0)
                f.seek(0)
                break
            else:
                time.sleep(1)


if __name__ == '__main__':
    main()