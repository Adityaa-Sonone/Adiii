Head="Welcome to KBC"
x = Head.center(35)
print(x)
print("\nPlease click on enter to start the Game\n")
Questions = [
  ["What is capital of India ?", "Mumbai", "Kolkata", "Delhi", "Nagpur", 3],
  ["How many State in India", "27", "28", "29", "30", 3],
  ["Who is the first president of India ?", "Rajendra Prasad", "Jawaharlal Nehru", "krishnapalli Radhakrishnan", "Mahatma Gandhi", 1],
  ["Facebook is developed by ?", "Java", "Php", "Python", "C++", 2],
  ["How many countries are there in the world ?", "169", "195", "200,", "210", 2],
  ["What is the capital of Japan", "Burlin", "Osaka", "Tokyo", "Hiroshima", 3],
  ["Which year did Wolrd War 2 end ?", "1930", "1940","1950", "1945", 4],
  ["Which is the biggest continent in the wolrd", "Asia", "Africa", "Europe", "North korea", 1],
  ["What is the name of India's first satellite ?", "Apollo 14", "Apollo 15", "Aryabhata", "HAMSAT",3],
  ["Who developed Python language ?", "Guido van Rossum", "James Gosling", "Bjarne Stroustroup", "Dennis Rechie", 1]]

level = [1000, 5000, 20000, 50000, 100000, 300000, 700000, 2000000, 5000000, 10000000]
money = 0
a=str(input(""))
if (a==""):
  for i in range(0, len(Questions)):
    Question = Questions[i]
    print(f"Question for Rs. {level[i]}\n \n{Question[0]}")
    print(f"\n1. {Question[1]}     2. {Question[2]}")
    print(f"3. {Question[3]}     4. {Question[4]}")
    reply = int(input("\nEnter your answer "))
    if(reply == Question[-1]):
      print(f"\nCorrect Answer , You won Rs. {level[i]}\n\n\n")
    else:
      b = "Wrong Answer\n\n"
      print("\n\n")
      print(b.center(30))
      break

