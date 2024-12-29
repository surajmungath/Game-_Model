import random
from collections import Counter

def algebra_practice_game():
    score = 0
    rounds = int(input("Enter the number of questions you want to solve: "))
    
    for _ in range(rounds):
        problem_type = random.choice(["one-step", "two-step"])

        if problem_type == "one-step":
            a = random.randint(-10, 10)
            b = random.randint(-10, 10)
            answer = a + b
            print(f"Solve: {a} + {b} = ?")

        elif problem_type == "two-step":
            a = random.randint(-10, 10)
            b = random.randint(-10, 10)
            c = random.randint(-10, 10)
            answer = a * b + c
            print(f"Solve: {a} * {b} + {c} = ?")

        user_answer = int(input("Your answer: "))
        if user_answer == answer:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer was {answer}.")

    print(f"Your score: {score}/{rounds}")

def hangman_game():
    someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut 
    watermelon cherry papaya berry peach lychee muskmelon kiwi blueberry raspberry 
    plum pomegranate tangerine guava nectarine fig quince date mulberry gooseberry 
    cantaloupe blackcurrant redcurrant gooseberry blackberry dragonfruit jackfruit 
    kiwano rambutan sapodilla'''

    someWords = someWords.split(' ')
    word = random.choice(someWords)

    print('Guess the word! HINT: word is a name of a fruit')

    for i in word:
        print('_', end=' ')
    print()

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0

    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess

            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                elif (Counter(letterGuessed) == Counter(word)):
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break
                else:
                    print('_', end=' ')

        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()

def question_game():
    test_questions = [
        {"question": "What is the capital of India?", "answer": "New Delhi"},
    {"question": "Who is known as the Father of the Nation in India?", "answer": "Mahatma Gandhi"},
    {"question": "What is the national animal of India?", "answer": "Tiger"},
    {"question": "In which year did India gain independence from British rule?", "answer": "1947"},
    {"question": "What is the national sport of India?", "answer": "Hockey"},
    {"question": "Who was the first Prime Minister of India?", "answer": "Jawaharlal Nehru"},
    {"question": "Which Indian city is known as the Silicon Valley of India?", "answer": "Bangalore"},
    {"question": "What is the official language of India?", "answer": "Hindi"},
    {"question": "Which river is considered the holiest in India?", "answer": "Ganges"},
    {"question": "What is the currency of India?", "answer": "Indian Rupee"},
    {"question": "Who was the first woman Prime Minister of India?", "answer": "Indira Gandhi"},
    {"question": "What is the national flower of India?", "answer": "Lotus"},
    {"question": "Who is the current President of India?", "answer": "Droupadi Murmu"},
    {"question": "What is the national bird of India?", "answer": "Peacock"},
    {"question": "Which Indian state is famous for tea plantations?", "answer": "Assam"},
    {"question": "In which city is the Taj Mahal located?", "answer": "Agra"},
    {"question": "Which is the largest state in India by area?", "answer": "Rajasthan"},
    {"question": "Who is known as the Missile Man of India?", "answer": "Dr. A.P.J. Abdul Kalam"},
    {"question": "What is the official name of India?", "answer": "Republic of India"},
    {"question": "Which Indian festival is known as the Festival of Lights?", "answer": "Diwali"},
    {"question": "Who wrote the Indian national anthem?", "answer": "Rabindranath Tagore"},
    {"question": "What is the highest civilian award in India?", "answer": "Bharat Ratna"},
    {"question": "Which city is known as the Pink City of India?", "answer": "Jaipur"},
    {"question": "What is the national tree of India?", "answer": "Banyan"},
    {"question": "Which mountain range forms the northern boundary of India?", "answer": "Himalayas"},
    {"question": "Which Indian city is famous for its film industry, often referred to as Bollywood?", "answer": "Mumbai"},
    {"question": "Who was the first Governor-General of independent India?", "answer": "Lord Mountbatten"},
    {"question": "Which city is known as the Garden City of India?", "answer": "Bangalore"},
    {"question": "What is the main language spoken in Kerala?", "answer": "Malayalam"},
    {"question": "Which Indian freedom fighter is also known as Netaji?", "answer": "Subhas Chandra Bose"},
    {"question": "Who is the father of the Indian Constitution?", "answer": "Dr. B.R. Ambedkar"},
    {"question": "Which river is considered the longest in India?", "answer": "Ganga"},
    {"question": "Which state is known as the Land of the Rising Sun in India?", "answer": "Arunachal Pradesh"},
    {"question": "What is the national game of India?", "answer": "Field Hockey"},
    {"question": "Which Indian state is known for its backwaters?", "answer": "Kerala"},
    {"question": "Which Indian city is known as the City of Joy?", "answer": "Kolkata"},
    {"question": "Who is known as the Iron Man of India?", "answer": "Sardar Vallabhbhai Patel"},
    {"question": "What is the famous dance form of Tamil Nadu?", "answer": "Bharatanatyam"},
    {"question": "Which famous Indian leader's birthday is celebrated as National Youth Day?", "answer": "Swami Vivekananda"},
    {"question": "Which state is known for its tea gardens and silk weaving?", "answer": "Assam"},
    {"question": "Which Indian leader gave the famous 'Tryst with Destiny' speech?", "answer": "Jawaharlal Nehru"},
    {"question": "In which city is the India Gate located?", "answer": "New Delhi"},
    {"question": "Which is the most populous state in India?", "answer": "Uttar Pradesh"},
    {"question": "What is the capital of Maharashtra?", "answer": "Mumbai"},
    {"question": "Which Indian state is known as the 'Land of the Seven Sisters'?", "answer": "Northeast India"},
    {"question": "What is the state animal of India?", "answer": "Lion"},
    {"question": "Who is the author of the book 'The Discovery of India'?", "answer": "Jawaharlal Nehru"},
    {"question": "Which famous fort is located in the city of Delhi?", "answer": "Red Fort"},
    {"question": "Which Indian festival marks the end of winter and the beginning of spring?", "answer": "Vasant Panchami"},
    {"question": "Who was the first woman to win a Nobel Prize from India?", "answer": "Mother Teresa"},
    {"question": "What is the state capital of Uttar Pradesh?", "answer": "Lucknow"},
    {"question": "Which is the largest river in South India?", "answer": "Godavari"},
    {"question": "What is the popular sweet made of condensed milk, often eaten in India?", "answer": "Gulab Jamun"},
    {"question": "Which Indian state is known for its large population of tigers?", "answer": "Madhya Pradesh"},
    {"question": "What is the national emblem of India?", "answer": "Lion Capital of Ashoka"},
    {"question": "Which Indian president is known for his role as the first Indian President after independence?", "answer": "Dr. Rajendra Prasad"},
    {"question": "Which is the smallest state by area in India?", "answer": "Goa"},
    {"question": "Who wrote the famous book 'The Immortals of Meluha'?", "answer": "Amish Tripathi"},
    {"question": "What is the name of the oldest active Indian film industry?", "answer": "Bengali cinema (Tollywood)"},
    {"question": "What is the capital of Punjab?", "answer": "Chandigarh"},
    {"question": "Which region in India is known for its coffee plantations?", "answer": "Coorg"},
    {"question": "Which Indian state is the only one with an official language, Malayalam?", "answer": "Kerala"},
    {"question": "Which famous museum is located in Kolkata?", "answer": "Indian Museum"},
    {"question": "Which is the longest railway station in India?", "answer": "Howrah Junction"},
    {"question": "Which famous temple is located in Varanasi?", "answer": "Kashi Vishwanath Temple"},
    {"question": "Who invented the first version of the Indian tricolor flag?", "answer": "Pingali Venkayya"},
    {"question": "Which state is the birthplace of Mahatma Gandhi?", "answer": "Gujarat"},
    {"question": "Which is the most popular language spoken in India?", "answer": "Hindi"},
    {"question": "Who is the founder of the Bhakshi Vidyalaya movement?", "answer": "Raja Rammohan Roy"},
    {"question": "Which is the largest lake in India?", "answer": "Vembanad Lake"},
    {"question": "Which famous Indian cricketer is known as 'Master Blaster'?", "answer": "Sachin Tendulkar"},
    {"question": "What is the national motto of India?", "answer": "Satyamev Jayate"},
    {"question": "Which state in India is famous for its 'Pukka Sahib' temples?", "answer": "Punjab"},
    {"question": "Which city is known for its famous Qutub Minar?", "answer": "Delhi"},
    {"question": "Which popular movie genre is India famous for?", "answer": "Bollywood"},
     {"question": "Who wrote '1984'?", "answer": "George Orwell"},
    {"question": "What is the capital of Canada?", "answer": "Ottawa"},
    {"question": "Who was the first person to walk on the moon?", "answer": "Neil Armstrong"},
    {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond"},
    {"question": "Who discovered penicillin?", "answer": "Alexander Fleming"},
    {"question": "What is the currency of Japan?", "answer": "Yen"},
    {"question": "What is the capital of Australia?", "answer": "Canberra"},
    {"question": "Who wrote 'Pride and Prejudice'?", "answer": "Jane Austen"},
    {"question": "What is the square root of 144?", "answer": "12"},
    {"question": "What is the longest river in the world?", "answer": "Nile"},
    {"question": "Who was the first president of the United States?", "answer": "George Washington"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "What is the capital of Germany?", "answer": "Berlin"},
    {"question": "Who discovered electricity?", "answer": "Benjamin Franklin"},
    {"question": "What is the smallest country in the world?", "answer": "Vatican City"},
    {"question": "What is the tallest building in the world?", "answer": "Burj Khalifa"},
    {"question": "What is the national flower of Japan?", "answer": "Cherry Blossom"},
    {"question": "What is the primary language spoken in Brazil?", "answer": "Portuguese"},
    {"question": "What year did World War I begin?", "answer": "1914"},
    {"question": "Who invented the telephone?", "answer": "Alexander Graham Bell"},
    {"question": "Who wrote 'The Great Gatsby'?", "answer": "F. Scott Fitzgerald"},
    {"question": "What is the largest desert in the world?", "answer": "Sahara"},
    {"question": "What is the capital of Spain?", "answer": "Madrid"},
    {"question": "What is the longest-running TV show?", "answer": "The Simpsons"},
    {"question": "Who invented the light bulb?", "answer": "Thomas Edison"},
    {"question": "What is the capital of Italy?", "answer": "Rome"},
    {"question": "What is the most spoken language in the world?", "answer": "Mandarin"},
    {"question": "What year did World War II end?", "answer": "1945"},
    {"question": "Who painted the Sistine Chapel?", "answer": "Michelangelo"},
    {"question": "What is the largest island in the world?", "answer": "Greenland"},
    {"question": "What is the name of the longest mountain range in the world?", "answer": "Andes"},
    {"question": "What is the boiling point of water?", "answer": "100°C"},
    {"question": "Who invented the airplane?", "answer": "Wright Brothers"},
    {"question": "What is the official language of Egypt?", "answer": "Arabic"},
    {"question": "What is the chemical symbol for oxygen?", "answer": "O"},
    {"question": "Who wrote 'Moby Dick'?", "answer": "Herman Melville"},
    {"question": "Who is known as the 'father of modern chemistry'?", "answer": "Antoine Lavoisier"},
    {"question": "What is the capital of India?", "answer": "New Delhi"},
    {"question": "Who discovered the theory of relativity?", "answer": "Albert Einstein"},
    {"question": "What is the largest city in the United States by population?", "answer": "New York City"},
    {"question": "What is the currency of the United Kingdom?", "answer": "Pound Sterling"},
    {"question": "What is the hardest rock?", "answer": "Diamond"},
    {"question": "Who was the first woman to win a Nobel Prize?", "answer": "Marie Curie"},
    {"question": "What is the most populous country in the world?", "answer": "China"},
    {"question": "Who wrote 'The Catcher in the Rye'?", "answer": "J.D. Salinger"},
    {"question": "What is the capital of Russia?", "answer": "Moscow"},
    {"question": "Who invented the printing press?", "answer": "Johannes Gutenberg"},
    {"question": "What is the national animal of Australia?", "answer": "Kangaroo"},
    {"question": "What is the currency of the United States?", "answer": "Dollar"},
    {"question": "What is the square root of 81?", "answer": "9"},
    {"question": "Who is known as the 'father of modern economics'?", "answer": "Adam Smith"},
    {"question": "What is the capital of South Korea?", "answer": "Seoul"},
    {"question": "What is the name of the longest river in South America?", "answer": "Amazon River"},
    {"question": "What is the tallest waterfall in the world?", "answer": "Angel Falls"},
    {"question": "Who discovered the law of gravity?", "answer": "Isaac Newton"},
    {"question": "What is the largest country by area?", "answer": "Russia"},
    {"question": "Who invented the steam engine?", "answer": "James Watt"},
    {"question": "What is the largest land animal?", "answer": "African Elephant"},
    {"question": "What is the national sport of Japan?", "answer": "Sumo Wrestling"},
    {"question": "What is the largest continent?", "answer": "Asia"},
    {"question": "What is the capital of Egypt?", "answer": "Cairo"},
    {"question": "Who wrote 'Frankenstein'?", "answer": "Mary Shelley"},
    {"question": "What is the deepest ocean in the world?", "answer": "Pacific Ocean"},
    {"question": "What is the chemical symbol for carbon?", "answer": "C"},
    {"question": "Who is known as the 'father of modern chemistry'?", "answer": "Antoine Lavoisier"},
    {"question": "What is the capital of Brazil?", "answer": "Brasília"},
    {"question": "Who invented the computer?", "answer": "Charles Babbage"},
    {"question": "What is the longest mountain range in North America?", "answer": "Rocky Mountains"},
    {"question": "What is the square root of 169?", "answer": "13"},
    {"question": "What is the capital of Turkey?", "answer": "Ankara"},
    {"question": "Who was the first female prime minister of the United Kingdom?", "answer": "Margaret Thatcher"},
    {"question": "What is the largest country in Africa?", "answer": "Algeria"},
    {"question": "What is the main ingredient in sushi?", "answer": "Rice"},
    {"question": "Who wrote 'Crime and Punishment'?", "answer": "Fyodor Dostoevsky"},
    {"question": "What is the capital of China?", "answer": "Beijing"},
    {"question": "Who developed the theory of evolution?", "answer": "Charles Darwin"},
    {"question": "What is the largest lake in Africa?", "answer": "Lake Victoria"},
    {"question": "Who wrote 'War and Peace'?", "answer": "Leo Tolstoy"},
    {"question": "What is the tallest building in the United States?", "answer": "One World Trade Center"},
    {"question": "What is the currency of France?", "answer": "Euro"},
    {"question": "What is the national flower of the United States?", "answer": "Rose"},
    {"question": "Who invented the polio vaccine?", "answer": "Jonas Salk"},
    {"question": "What is the longest river in Europe?", "answer": "Volga River"},
    {"question": "What is the national animal of India?", "answer": "Tiger"},
    {"question": "What is the square root of 225?", "answer": "15"},
    {"question": "Who wrote 'Jane Eyre'?", "answer": "Charlotte Bronte"},
    {"question": "What is the capital of Mexico?", "answer": "Mexico City"},
    {"question": "What is the name of the largest volcano in the world?", "answer": "Mauna Loa"},
    {"question": "Who invented the refrigerator?", "answer": "Jacob Perkins"},
    {"question": "What is the name of the largest island in the Mediterranean Sea?", "answer": "Sicily"},
    {"question": "What is the boiling point of water in Fahrenheit?", "answer": "212°F"},
    {"question": "Who invented the radio?", "answer": "Guglielmo Marconi"},
    {"question": "What is the national dish of Spain?", "answer": "Paella"},
    {"question": "Who wrote 'The Odyssey'?", "answer": "Homer"},
    {"question": "What is the capital of Thailand?", "answer": "Bangkok"},
    {"question": "Who invented the washing machine?", "answer": "Jacob Christian Schäffer"},
    {"question": "What is the name of the highest peak in Africa?", "answer": "Mount Kilimanjaro"},
    {"question": "What is the national animal of Russia?", "answer": "Brown Bear"},
    {"question": "What is the square root of 196?", "answer": "14"},
    {"question": "Who wrote 'Les Misérables'?", "answer": "Victor Hugo"},
    {"question": "What is the capital of Argentina?", "answer": "Buenos Aires"},
    {"question": "What is the national sport of Canada?", "answer": "Ice Hockey"},
    {"question": "Who invented the safety pin?", "answer": "Walter Hunt"},
    {"question": "What is the currency of Italy?", "answer": "Euro"},
    {"question": "What is the national flower of Australia?", "answer": "Golden Wattle"},
    {"question": "Who wrote 'Wuthering Heights'?", "answer": "Emily Bronte"},
    {"question": "What is the name of the largest desert in Asia?", "answer": "Gobi Desert"},
    {"question": "What is the boiling point of water in Celsius?", "answer": "100°C"},
    {"question": "Who invented the microphone?", "answer": "Emile Berliner"},
    {"question": "What is the capital of Saudi Arabia?", "answer": "Riyadh"},
    {"question": "Who invented the telegraph?", "answer": "Samuel Morse"},
    {"question": "What is the national animal of Germany?", "answer": "Eagle"},
    {"question": "What is the square root of 256?", "answer": "16"},
    {"question": "Who wrote 'The Count of Monte Cristo'?", "answer": "Alexandre Dumas"},
    {"question": "What is the capital of Colombia?", "answer": "Bogotá"},
    {"question": "What is the national sport of Brazil?", "answer": "Football"},
    {"question": "Who invented the sewing machine?", "answer": "Elias Howe"},
    {"question": "What is the currency of Spain?", "answer": "Euro"},
    {"question": "What is the national flower of Canada?", "answer": "Maple Leaf"},
    {"question": "Who wrote 'Dracula'?", "answer": "Bram Stoker"},
    {"question": "What is the name of the largest glacier in the world?", "answer": "Lambert Glacier"},
    {"question": "What is the boiling point of water in Kelvin?", "answer": "373.15K"},
    {"question": "Who invented the typewriter?", "answer": "Christopher Sholes"},
    {"question": "What is the national dish of Italy?", "answer": "Pasta"},
    {"question": "Who wrote 'The Hobbit'?", "answer": "J.R.R. Tolkien"},
    {"question": "What is the capital of South Africa?", "answer": "Pretoria"},
    {"question": "Who invented the fax machine?", "answer": "Alexander Bain"},
    {"question": "What is the name of the largest cave in the world?", "answer": "Son Doong Cave"},
    {"question": "What is the national animal of China?", "answer": "Giant Panda"},
    {"question": "What is the square root of 324?", "answer": "18"},
    {"question": "Who wrote 'The Divine Comedy'?", "answer": "Dante Alighieri"},
    {"question": "What is the capital of Chile?", "answer": "Santiago"},
    {"question": "Which is the first state to have its own law on Right to Information?", "answer": "Tamil Nadu"},
    {"question": "What is the name of India's first space satellite?", "answer": "Aryabhata"},
    {"question": "Which is the oldest university in India?", "answer": "Nalanda University"},
    {"question": "Who founded the 'Indian National Congress'?", "answer": "Allan Octavian Hume"},
    {"question": "What is the highest rank in the Indian Army?", "answer": "Field Marshal"},
    {"question": "Who is the first Indian to win a Nobel Prize in Physics?", "answer": "C.V. Raman"},
    {"question": "What is the popular name of the National Capital Region?", "answer": "NCR"},
    {"question": "Which is the first Indian film to win an Oscar?", "answer": "Mother India"},
    {"question": "What is the state fruit of West Bengal?", "answer": "Jackfruit"},
    {"question": "Who is the famous founder of the 'Bharatiya Janata Party'?", "answer": "Atal Bihari Vajpayee"}
]

    random.shuffle(test_questions)
    
    def is_correct(user_answer, correct_answer):
        return user_answer.strip().lower() == correct_answer.strip().lower()

    num_questions = int(input("How many questions would you like to answer? ")) 
    for question_data in test_questions[:num_questions]:
        question = question_data["question"]
        correct_answer = question_data["answer"]
        
        user_answer = input(f"Question: {question}\nYour answer: ")
        
        if is_correct(user_answer, correct_answer):
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}")

def main_menu():
    while True:
        print("\nSelect a game to play:")
        print("1. Algebra Practice Game")
        print("2. Hangman Game")
        print("3. Question Game")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            algebra_practice_game()
        elif choice == '2':
            hangman_game()
        elif choice == '3':
            question_game()
        elif choice == '4':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
