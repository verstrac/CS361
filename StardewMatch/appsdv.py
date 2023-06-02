# Author: Caleb Verstraete
# Date: 6/2/23
# CS361
import time
import statistics


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
    return


def bachelor_request(user_sel):
    with open('bachelor.txt', 'w', encoding='utf-8') as f:
        f.write(user_sel)
        time.sleep(1)
    while True:
        with open('bachelor.txt', 'r+', encoding='utf-8') as f:
            bachelor = f.read()
            if bachelor != user_sel:
                print(bachelor)
                f.truncate(0)
                f.seek(0)
                break
            else:
                time.sleep(1)
    nav_display()
    return


def mini_nav():
    """Navigation display while taking the questionnaire."""
    print('\n\nP. Previous Question\n'
          '0. Home\n'
          '9. Exit\n')


def exit_check():
    if input('\nAre you sure you want to exit the app.\n'
             'Y/N\n'
             'Selection: ').upper() == 'Y':
        return True
    else:
        return False


def home_check():
    if input('\nAre you sure you want to return to the home screen.\n'
             'You answers will not be saved.\n'
             'Y/N\n'
             'Selection: ').upper() == 'Y':
        return True
    else:
        return False


def calc_match(questionnaire_result):
    male_convert = {'A': ['11', 'Sam'],
                    'B': ['14', 'Sebastian'],
                    'C': ['15', 'Elliot'],
                    'D': ['12', 'Harvey'],
                    'E': ['16', 'Alex'],
                    'F': ['13', 'Shane']}
    female_convert = {'A': ['19', 'Abigail'],
                      'B': ['21', 'Emily'],
                      'C': ['22', 'Haley'],
                      'D': ['18', 'Maru'],
                      'E': ['17', 'Penny'],
                      'F': ['20', 'Leah']}
    most_result = statistics.mode(questionnaire_result[1:])
    if questionnaire_result[0] == 'A':
        bachelor_request(male_convert[most_result][0])
    else:
        bachelor_request(female_convert[most_result][0])


def question_display(questionnaire_result, q_index):
    male_questions = [
        '\nQ2.\n'
        'What kind of personality do you find most attractive?\n\n'
        'A) Adventurous and outgoing.\n'
        'B) Intellectual and ambitious.\n'
        'C) Artistic and creative.\n'
        'D) Kind-hearted and empathetic.\n'
        'E) Laid-back and easygoing.\n'
        'F) Practical and hardworking.\n',
        '\nQ3.\n'
        'How do you envision spending quality time with your partner?\n\n'
        'A) Rocking with your band or going on exciting adventures together.\n'
        'B) Playing games with friends or riding your motorcycle.\n'
        'C) Appreciating art, music, or other creative activities together.\n'
        'D) Caring for animals or helping out the community.\n'
        'E) Watching Girdball or spending time at the beach.\n'
        'F) Relaxing and enjoying simple, leisurely activities together.\n',
        '\nQ4.\n'
        'Which of these qualities is most important to you in a partner?\n\n'
        'A) Easygoing nature and a good sense of humor.\n'
        'B) Intelligence and a strong sense of self.\n'
        'C) Artistic talent and self-expression.\n'
        'D) Empathy and compassion.\n'
        'E) Confidence and a sense of adventure.\n'
        'F) Reliability and a strong work ethic.\n',
        '\nQ5.\n'
        'How do you handle conflicts or disagreements in a relationship?\n\n'
        'A) I use humor and try to maintain a calm and relaxed atmosphere.\n'
        'B) I approach them with logic and reason, seeking a fair solution.\n'
        'C) I express myself creatively and seek a compromise.\n'
        'D) I prioritize open communication and understanding.\n'
        'E) I address them directly and try to find a resolution.\n'
        'F) I work through them with patience and dedication.\n',
        '\nQ6.\n'
        'What are you looking for in a potential partner?\n\n'
        'A) Someone who can keep up with my sense of adventure.\n'
        'B) Someone who challenges me intellectually and supports my goals.\n'
        'C) Someone who appreciates and shares my love for the arts.\n'
        'D) Someone who is caring, understanding, and emotionally available.\n'
        'E) Someone who is easygoing and can bring laughter and joy to my life.\n'
        'F) Someone who is hardworking and committed to building a future together.\n'
    ]
    female_questions = [
        '\nQ2.\n'
        'How would you describe your ideal day?\n\n'
        'A) Exploring the outdoors and discovering new things.\n'
        'B) Creating new fashion or meditating in the garden.\n'
        'C) Taking photos and capturing beautiful moments.\n'
        'D) Working on a personal project or tinkering with gadgets.\n'
        'E) Helping others and spending time with loved ones.\n'
        'F) Relaxing in nature and working on your art.\n',
        '\nQ3.\n'
        'Which of these activities appeals to you the most?\n\n'
        'A) Playing video games or adventuring in the mines.\n'
        'B) Attending local festivals and social events.\n'
        'C) Caring for animals or tending to a garden.\n'
        'D) Experimenting with science or technology.\n'
        'E) Volunteering or supporting community causes.\n'
        'F) Exploring nature and hiking through the forest.\n',
        '\nQ4.\n'
        'What type of personality do you find most intriguing?\n\n'
        'A) Adventurous and independent.\n'
        'B) Creative and free-spirited.\n'
        'C) Cheerful and outgoing.\n'
        'D) Intelligent and curious.\n'
        'E) Kind-hearted and compassionate.\n'
        'F) Relaxed and laid-back.\n',
        '\nQ5.\n'
        'How do you handle challenges or setbacks in life?\n\n'
        'A) I face them head-on and push through with determination.\n'
        'B) I find solace in art, literature, or other creative outlets.\n'
        'C) I seek support from friends and loved ones to overcome them.\n'
        'D) I analyze the situation and approach it with a logical mindset.\n'
        'E) I try to help others and find strength in supporting them.\n'
        'F) I take a step back and find ways to relax and destress.\n',
        '\nQ6.\n'
        'What are you looking for in a potential partner?\n\n'
        'A) Someone who shares my sense of adventure and curiosity.\n'
        'B) Someone who appreciates self-expression, art, and beauty.\n'
        'C) Someone who is fun-loving, social, and enjoys making memories.\n'
        'D) Someone who is intelligent, ambitious, and shares my interests.\n'
        'E) Someone who is caring, empathetic, and values kindness.\n'
        'F) Someone who is laid-back, easygoing, and enjoys the simple things.\n'
    ]

    if q_index == 0:
        print('\nQ1.\n'
              'Do you prefer a male or female partner?\n\n'
              'A. Male\n'
              'B. Female\n')
    elif q_index > 0 and questionnaire_result[0] == 'A':
        print(male_questions[q_index - 1])
    elif q_index > 0 and questionnaire_result[0] == 'B':
        print(female_questions[q_index - 1])


def match_questionnaire(questionnaire_result):
    q_index = 0

    while True:
        if q_index == 6:
            calc_match(questionnaire_result)
            return
        question_display(questionnaire_result, q_index)
        mini_nav()

        q_answer = input('Make selection with upper or lower case or numbers: ').upper()
        if q_answer in 'ABCDEF' and q_answer != '':
            questionnaire_result[q_index] = q_answer
            q_index += 1
        elif q_answer == 'P' and q_index != 0:
            q_index -= 1
            questionnaire_result[q_index] = None
        elif q_answer == '0' and home_check():
            home_display()
            return
        elif q_answer == '9' and exit_check():
            quit()


def main():
    user_sel = None
    previous_sel = None
    questionnaire_result = [None for i in range(6)]
    while True:
        if user_sel is None or user_sel == 0:
            home_display()
        elif user_sel == 1:
            match_questionnaire(questionnaire_result)
        elif user_sel == 2:
            bachelor_bachelorette_display()
        elif user_sel == 3:
            print('Not done yet')
            user_sel = 0
            home_display()
        elif user_sel == 4:
            print('Not done yet')
            user_sel = 0
            home_display()
        elif user_sel == 5:
            about_display()
        elif user_sel == 9 and exit_check():
            return
        elif previous_sel == 2 and 11 <= user_sel <= 22:
            print('Call to Bachelor microservice with: %d\n\n' % user_sel)
            bachelor_request(str(user_sel))
        else:
            print('invalid selection')
            user_sel = '0'
            home_display()

        previous_sel = user_sel
        user_sel = int(input('Selection: '))


if __name__ == '__main__':
    main()
