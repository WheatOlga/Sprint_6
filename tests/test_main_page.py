
import pytest
import allure
from locators.main_page_locators import MainPageLocators
from data import EXPECTED_ANSWERS


class TestFAQ:
    
    @allure.title("Проверка ответа на вопрос №{question_number} в FAQ")

    @pytest.mark.parametrize("question_number", range(1, 9))
    def test_faq_question_answer(self, main_page, question_number):
        
        with allure.step(f"Кликнуть на вопрос №{question_number}"):
            main_page.click_question(question_number)

        with allure.step(f"Получить текст ответа на вопрос №{question_number}"):
            actual_answer = main_page.get_answer_text(question_number)

        with allure.step(f"Получить ожидаемый ответ на вопрос №{question_number} из тестовых данных"):
            expected_answer = EXPECTED_ANSWERS[question_number]

        with allure.step(f"Сравнить фактический и ожидаемый ответ"):
            assert actual_answer == expected_answer, (
                f"Ответ на вопрос {question_number} не совпадает с ожидаемым. "
                f"Ожидалось: '{expected_answer}', а получено: '{actual_answer}'"
            )
    