# Caleb Verstraete
# 5/4/23
# CS361: Microservice to which well receive requests for Runescape items in the txt file. Microservice
import time
import json


def main():
    bachelors = {'16': 'Name: Alex\n'
                       'Personality: Alex loves sports and hanging out at the beach. He is quite arrogant and brags\n'
                       'to everyone that he is going to be a professional athlete. Is his cockiness just a facade to\n'
                       'mask his crushing self-doubt? Is he using his sports dream to fill the void left by the\n'
                       'disappearance of his parents? Or is he just a brazen youth trying to "look cool?"\n\n'
                       'Likes: Complete Breakfast, Salmon Dinner\n'
                       'Dislikes: Holly, Quartz\n',
                 '15': 'Name: Elliott\n'
                       'Personality: Elliott lives alone in a cabin on the beach. He is a writer who dreams of one\n'
                       'day writing a magnificent novel. He is a sentimental “romantic” with a tendency to go off\n'
                       'onto flowery, poetic tangents. When he can afford it, he enjoys a strong beverage at the\n'
                       'Stardrop Saloon. Could a humble farmer such as yourself be the inspiration Elliott is \n'
                       'looking for? There’s only one way to find out…\n\n'
                       'Likes: Crab Cakes, Duck Feather, Lobster, Pomegranate, Squid ink, Tom Kha Soup\n'
                       'Dislikes: Amaranth, Quartz, Salmonberry, Sea Cucumber\n',
                 '12': 'Name: Harvey\n'
                       'Personality: Harvey is the town doctor. He\'s a little old for a bachelor, but he has a kind\n'
                       'heart and a respected position in the community. He lives in a small apartment above the\n'
                       'medical clinic, but spends most of his time working. You can sense a sadness about him, as\n'
                       'if there’s something he’s not telling you…\n\n'
                       'Likes: Coffee, Pickles, Super Meal, Truffle Oil, Wine\n'
                       'Dislikes: Coral, Nautilus Shell, Rainbow Shell, Salmonberry, Spice Berry\n',
                 '11': 'Name: Sam\n'
                       'Personality: Sam is an outgoing, friendly guy who is brimming with youthful energy. He\n'
                       'plays guitar and drums, and wants to start a band with Sebastian as soon as he has\n'
                       'enough songs together. However, he does have a habit of starting ambitious projects\n'
                       'and not finishing them. Sam is a little stressed about the impending return of his\n'
                       'father, who has been away for years due to his line of work.\n\n'
                       'Likes: Cactus Fruit, Maple Bar, Pizza, Tigerseye\n'
                       'Dislikes: Coal, Mayonnaise, Pickles, Copper Bar, Refined Quartz\n',
                 '14': 'Name: Sebastian\n'
                       'Personality: Sebastian is a rebellious loner who lives in his parent’s basement. He is\n'
                       'Maru’s older half-brother, and feels like his sister gets all the attention and adoration,\n'
                       'while he is left to rot in the dark. He tends to get deeply absorbed in his work, computer\n'
                       'games, comic books, sci-fi novels, and will sometimes spend great lengths of time pursuing\n'
                       'these hobbies alone in his room. He can be a bit unfriendly to people he doesn\'t know.\n'
                       'Could a charming new farmer cultivate the wasteland of his heart? Who knows?\n\n'
                       'Likes: Frozen Tear, Obsidian, Pumpkin Soup, Sashimi, Void Egg\n'
                       'Dislikes: Clay, Complete Breakfast, Farmer\'s Lunch, Omelet\n',
                 '13': 'Name: Shane\n'
                       'Personality: I\'m renting my room from Marnie at a really good price. It\'s small but I\n'
                       'can\'t complain. If I could reset my life maybe I\'d start a chicken farm. Only free-range\n'
                       'eggs of course.\n\n'
                       'Likes: Beer, Hot Pepper, Pepper Poppers, Pizza\n'
                       'Dislikes: Pickles, Quartz\n',
                 '19': 'Name: Abigail\n'
                       'Personality: Abigail lives at the general store with her parents. She sometimes fights\n'
                       'with her mom, who worries about Abigail’s “alternative lifestyle”. Her mom has the\n'
                       'following to say: “I wish Abby would dress more appropriately and stop dyeing her hair\n'
                       'blue. She has such a wonderful natural hair color, just like her grandmother did.\n'
                       'Oh, and I wish she’d find some wholesome interests instead of this occult nonsense\n'
                       'she’s into.” You might find Abigail alone in the graveyard, or maybe out in a rainstorm\n'
                       'looking for frogs.\n\n'
                       'Likes: Amethyst, Banana Pudding, Blackberry Cobbler, Chocolate Cake, Pufferfish, Pumpkin\n'
                       'Spicy Eel\n'
                       'Dislikes: Clay, Holly\n',
                 '21': 'Name: Emily\n'
                       'Personality: I\'m just working at Gus\' to make ends meet... but my real passion is\n'
                       'tailoring. I made these clothes from scratch.\n\n'
                       'Likes: Amethyst, Aquamarine, Cloth, Emerald, Jade, Ruby, Survival Burger, Topaz, Wool\n'
                       'Dislikes: Fish Taco, Holly, Maki Roll, Salmon Dinner, Sashimi\n',
                 '22': 'Name: Haley\n'
                       'Personality: Being wealthy and popular throughout high school has made Haley a little\n'
                       'conceited and self-centered. She has a tendency to judge people for superficial reasons.\n'
                       'But is it too late for her to discover a deeper meaning to life? Is there a fun,\n'
                       'open-minded young woman hidden within that candy-coated shell?\n\n'
                       'Likes: Coconut, Fruit Salad, Pink Cake, Sunflower\n'
                       'Dislikes: Clay, Prismatic Shard, Wild Horseradish\n',
                 '20': 'Name: Leah\n'
                       'Personality: Leah lives alone in a small cabin just outside of town. She loves to spend\n'
                       'time outside, foraging for a wild meal or simply enjoying the gifts of the season. She’s\n'
                       'a talented artist with a large portfolio of work… yet she’s too nervous to display it to\n'
                       'the public. Maybe you can give her a little confidence boost?\n\n'
                       'Likes: Goat Cheese, Poppyseed Muffin, Salad, Stir Fry, Truffle, Vegetable Medley, Wine\n'
                       'Dislikes: Bread, Hashbrowns, Pancakes, Pizza, Void Egg\n',
                 '18': 'Name: Maru\n'
                       'Personality: Growing up with a carpenter and a scientist for parents, Maru acquired a\n'
                       'passion for creating gadgets at a young age. When she isn’t in her room, fiddling with\n'
                       'tools and machinery, she sometimes does odd jobs at the local clinic. Friendly, outgoing,\n'
                       'and ambitious, Maru would be quite a lucky match for a lowly newcomer such as yourself…\n'
                       'Can you win her heart, or will she slip through your fingers and disappear from your\n'
                       'life forever?\n\n'
                       'Likes: Battery Pack, Cauliflower, Cheese Cauliflower, Diamond, Miners\'s Treat, Pepper Poppers\n'
                       'Radioactive Bar, Rhubarb Pie, Strawberry\n'
                       'Dislikes: Holly, Honey, Pickles, Snow Yam, Truffle\n',
                 '17': 'Name: Penny\n'
                       'Personality: Penny lives with her mom, Pam, in a little trailer by the river. While Pam is\n'
                       'out carousing at the saloon, Penny quietly tends to her chores in the dim, stuffy room she\n'
                       'is forced to call home. She is shy and modest, without any grand ambitions for life other\n'
                       'than settling in and starting a family. She likes to cook (although her skills are\n'
                       'questionable) and read books from the local library.\n\n'
                       'Likes: Diamond, Emerald, Melon, Poppy, Poppyseed Muffin, Red Plate, Roots Platter,\n'
                       'Sandfish, Tom Kha Soup\n'
                       'Dislikes: Beer, Grape, Holly, Hops, Mead, Pale Ale, Pina Colada, Rabbit\'s Foot, Wine\n'}

    print('Bachelor Microservice up and running. Waiting for requests.')
    while True:
        time.sleep(2)
        with open('bachelor.txt', 'r+', encoding='utf-8') as f:
            image_text = f.read()

            if image_text != '' and image_text != 'Not a valid bachelor or bachelorette.':
                print('person requested is: ' + image_text)
                if image_text in bachelors.keys():
                    f.truncate(0)
                    f.seek(0)
                    f.write(bachelors[image_text])
                else:
                    f.truncate(0)
                    f.seek(0)
                    f.write('Not a valid bachelor or bachelorette.')


if __name__ == '__main__':
    main()
