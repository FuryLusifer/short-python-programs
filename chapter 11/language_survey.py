from survey import AnonymousSurvey

question = "What language did you first learn to speak? "
language_survey = AnonymousSurvey(question)

language_survey.show_question()

print("Enter 'q' to quit: \n")
while True:
    response = input("Language: ")
    if response.lower() == 'q':
        break
    language_survey.store_responses(response.title())

print("\nThank you everyone for participating in this survey.")
language_survey.show_results()