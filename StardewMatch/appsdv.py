# Author: Caleb Verstraete
# Date: 4/20/23
# CS361


def home_display():
    print('Welcome to\nFind Your Perfect Partner\nfor Stardew Valley\n\n'
          'Make your selection with the number next to the selection and press enter\n'
          '1. Find your match: Answer out questionnaire to find your perfect Stardew Valley bachelor or bachelorette.\n'
          '2. Bachelor/Bachelorette List: Select from a list to view information on the bachelors/bachelorettes.\n'
          '3. Create Profile: Create a Profile to save your match result and questionnaire answers.\n'
          '4. Login: Get to your Profile from here.\n'
          '5. About: Find out more about this app and the author.\n'
          '0. Home: This selection will take you to the Home Page\n'
          '9. Exit: Press 9 to quit the app when you are done.\n')


def nav_display():
    print('Make your selection with the number next to the selection and press enter\n'
          '1. Find your match\n'
          '2. Bachelor/Bachelorette List\n'
          '3. Create Profile\n'
          '4. Login\n'
          '5. About\n'
          '0. Home\n'
          '9. Exit\n')
    return


def bachelor_bachelorette_display():
    print('Here is a list of our amazing bachelors and bachelorettes. Use the number next to their name \n'
          'to view more information about them. Find out their personality, likes and dislikes.\n'
          'Bachelors:      Bachelorettes:\n'
          '11. Sam         17. Penny\n'
          '12. Harvey      18. Maru\n'
          '13. Shane       19. Abigail\n'
          '14. Sebastian   20. Leah\n'
          '15. Elliott     21. Emily\n'
          '16. Alex        22. Haley\n\n')
    nav_display()
    return


def about_display():
    print('About Page\n'
          'Mission: If you are like myself you are never quite sure who to romance when you play Stardew Valley. With\n'
          'this app I hope that someone who is new to the game or on their 100th play through will be able to find\n'
          'their perfect match in the game.\n\n'
          'History: I have been playing Stardew Valley for about 4 years and have put more than 200 hours into playing\n'
          'the game. It is a game I can get totally absorbed into and can put it down and come back at any time. I\n'
          'started programming back in 2020 at Oregon State University. Working on classes has provided a good challenge\n'
          'and creative opportunity. The program has kept me on my toes and moving forward. In the future I hope to\n'
          'apply my knowledge to other fulfilling project.\n\n'
          'Services: Find your match is an app to help you find your perfect Stardew Valley partner through a series\n'
          'of questions. Once done we take your answers and find who would be your best suited partner. If your like\n'
          'me and you forget things you can create a profile where we store your match and answers to the questionnaire.\n'
          'With the Bachelor/Bachelorette List you can explore the personalities, likes and dislikes of the people of\n'
          'Stardew Valley. So please take the app for a spin and thank you for your time.\n\n')
    nav_display()


def main():
    user_sel = None
    while True:
        if user_sel is None or user_sel == '0':
            home_display()
        elif user_sel == '1':
            print('Not done yet')
            user_sel = '0'
            home_display()
        elif user_sel == '2':
            bachelor_bachelorette_display()
        elif user_sel == '3':
            print('Not done yet')
            user_sel = '0'
            home_display()
        elif user_sel == '4':
            print('Not done yet')
            user_sel = '0'
            home_display()
        elif user_sel == '5':
            about_display()
        elif user_sel == '9':
            return
        else:
            print('invalid selection')
            user_sel = '0'
            home_display()

        user_sel = input('Selection: ')


if __name__ == '__main__':
    main()