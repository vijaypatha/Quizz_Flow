class Question:
    """
    Creating a class that will allow us to construct an object with two attributes: text and answer

    An another object will take in object of question from this object and fulfill User Journey / Experience
    """
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

