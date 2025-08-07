class AnonymousSurvey:
    ''' collects anonymous answers to a survey '''

    def __init__(self, questions):
        self.questions = questions
        self.responses = []

    def show_question(self):
        print(f"{self.questions}")

    def store_responses(self, new_responses):
        self.responses.append(new_responses)

    def show_results(self):
        print("Survey Results:")
        for response in self.responses:
            print(f"- {response}")