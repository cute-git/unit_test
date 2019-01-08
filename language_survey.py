from survey import AnonymousServey

question = "What language did you first learn to speak"
my_survey = AnonymousServey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == "q":
        break
    my_survey.store_response(response)

print("\nThank you !")
my_survey.show_results()