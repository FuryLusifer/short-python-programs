import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    # question = "What language did you first learn to speak?"
    # language_survey = AnonymousSurvey(question)
    language_survey.store_responses('english')
    assert 'english' in language_survey.responses

def test_store_multiple_response(language_survey):
    # question = "What language did you first learn to speak?"
    # language_survey = AnonymousSurvey(question)

    responses = ['english', 'mandarin', 'maithili']

    for response in responses:
        language_survey.store_responses(response)

    for response in responses:
        assert response in language_survey.responses