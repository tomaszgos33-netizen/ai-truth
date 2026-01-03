# core/responder.py
# Moduł generujący dynamiczne odpowiedzi w Prawdzie Sztucznej
# Styl odpowiedzi zależny od poziomu ryzyka

class Responder:
    def __init__(self):
        # Można tu dodać więcej stylów lub słownictwa w przyszłości
        self.styles = {
            "neutral": "Odpowiedź neutralna: {}",
            "cautious": "Ostrzeżenie: {}",
            "reflective": "Pytanie zwrotne: {}"
        }

    def generate_response(self, question: str, risk_level: str, confirmed: bool) -> str:
        """
        Generuje odpowiedź w zależności od ryzyka i stylu.

        :param question: Tekst pytania użytkownika
        :param risk_level: 'low', 'medium', 'high'
        :param confirmed: Czy użytkownik potwierdził chęć otrzymania odpowiedzi
        :return: Odpowiedź do wyświetlenia w CLI
        """

        if not confirmed:
            return "Odpowiedź została wstrzymana zgodnie z prawem do niewiedzy."

        question_summary = self._summarize_question(question)

        if risk_level.lower() == "low":
            return self.styles["neutral"].format(question_summary)
        elif risk_level.lower() == "medium":
            return self.styles["cautious"].format(question_summary)
        elif risk_level.lower() == "high":
            # Wysokie ryzyko → silne ostrzeżenie i refleksja
            return self.styles["reflective"].format(
                f"{question_summary} Zastanów się nad konsekwencjami przed działaniem."
            )
        else:
            # Default
            return "Nie mogę udzielić odpowiedzi – nieznany poziom ryzyka."

    def _summarize_question(self, question: str) -> str:
        """
        Prosta funkcja „podsumowująca” pytanie. 
        Można w przyszłości rozszerzyć o NLP/LLM.
        """
        # Na razie zwraca pytanie w cudzysłowie
        return f'\"{question}\"'
