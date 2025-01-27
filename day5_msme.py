#MCQ PROGRAM

questions=("1.What is the capital of India?","2.How many states in India?","3.Who is the first Governer of TamilNadu?","4.Who is the current president of India?")
choices=(('A:delhi','B:kerala','C:tamilnadu','D:punjab'),('A:28','B:27','C:25','D:29'),('A:Ujjal Singh','B:K.K.Shah','C:Mohan Lal','D:Annadurai'),('A:Droupadi Murmu','B:Ramnath Govind','C:Jaswanth Singh','D:Abdul Kalam'))

i=0
answers = ("A","A","A","A")
for que in questions:
    print(que)
    for cho in choices[i]:
        print(cho)
    ans_input=input("enter your answer:")
    if answers[i]==ans_input:
        print("correct answer")
    else:
        print("wrong answer!")
    i=i+1
