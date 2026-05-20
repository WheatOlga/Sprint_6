
import pytest
from locators.main_page_locators import MainPageLocators
from data import EXPECTED_ANSWERS

@pytest.mark.parametrize("question_number", range(1, 9))
def test_faq_question_answer(main_page, question_number):

    main_page.click_question(question_number)

    actual_answer = main_page.get_answer_text(question_number)

    expected_answer = EXPECTED_ANSWERS[question_number]

    assert actual_answer == expected_answer, (
        f"Ответ на вопрос {question_number} не совпадает с ожидаемым. "
        f"Ожидалось: '{expected_answer}', а получено: '{actual_answer}'"
    )
    