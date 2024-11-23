import random
import webbrowser
import pyttsx3

responses = {
          
          "hi": ["Hello", "How are you", "Hi there!", "Hey Baby", "Hi Sir"],
          "how are you": ["I'm doing well", "Thank you!", "I'm good", "It's Very Cold Today", "Fine"],
          "bye": ["Goodbye", "See Soon", "See you later", "Bye!", "See Ya!"],
          "can you help me": ["Yes I Can", "Very Easy", "Sure", "Absolutely", "Come on"],
          "open youtube": ["Okay Let's open", "Sure", "Open Youtube", "Open now", "ok"],
          "search google": ["Let's search", "On my way", "Travel", "Find", "Go Go Go"],
          "search map": ["Location", "Find Located", "Go to point", "Make direction", "Go went gone"]
}


engine = pyttsx3.init()


while True:

          user_input = input("User Text:")

          if user_input.lower() == 'exit':
                  print("Thank you")
                  break

          for key in responses:

                  if key in user_input.lower():
                          
                          if key == "hi":
                                  chatbot = random.choice(responses[key])
                                  engine.say(chatbot)
                                  engine.runAndWait()
                                  
                          elif key == "how are you":
                                  chatbot = random.choice(responses[key])
                                  engine.say(chatbot)
                                  engine.runAndWait()
                    
                          elif key == "bye":
                                  chatbot = random.choice(responses[key])
                                  engine.say(chatbot)
                                  engine.runAndWait()
                    
                          elif key == "can you help me":
                                  chatbot = random.choice(responses[key])
                                  engine.say(chatbot)
                                  engine.runAndWait()
                          

                          elif key == "open youtube":
                                  chatbot = random.choice(responses[key])
                                  print("Bot answer:" + " " + chatbot)
                                  engine.say(chatbot)
                                  engine.runAndWait()

                                  query = input("Enter your search in youtube:")
                                  print("Bot opening" + " " + query)
                                  engine.say(chatbot)
                                  engine.runAndWait()

                                  search_url = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
                                  webbrowser.open(search_url)

                           
                          elif key == "search google":
                                  chatbot = random.choice(responses[key])
                                  print("Bot answer:" + " " + chatbot)
                                  engine.say(chatbot)
                                  engine.runAndWait()

                                  query = input("Enter your search in google:")
                                  print("Bot opening" + " " + query)
                                  engine.say(chatbot)
                                  engine.runAndWait()

                                  search_url = "https://www.google.com/search?q=" + query.replace(" ", "+")
                                  webbrowser.open(search_url)
                    
                          elif key == "search map":
                                  
                                  chatbot = random.choice(responses[key])
                                  print("Bot answer:" + " " + chatbot)
                                  engine.say(chatbot)
                                  engine.runAndWait()

                                  query = input("Enter your search in google map:")
                                  print("Bot opening" + " " + query)
                                  engine.say(chatbot)
                                  engine.runAndWait()

                                  search_url = "https://www.google.com/maps/search/" + query.replace(" ", "+")
                                  webbrowser.open(search_url)

                    

                          print("Bot answer:" + " " + chatbot)
                          engine.say(chatbot)
                          engine.runAndWait()
                          break
          
          else:
                    print("Bot answer:" + " " + "Please try again")
                    engine.say(chatbot)
                    engine.runAndWait()









































































































