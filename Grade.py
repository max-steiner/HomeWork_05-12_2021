class Grade:

    gradeCurrent_index = 0
    sum_grades = 0

    def __init__(self, student_name, topic, grade):
        Grade.gradeCurrent_index += 1
        self.grade_index = Grade.gradeCurrent_index
        self.__student_name = student_name
        self.__topic = topic
        self.__grade = grade
        Grade.sum_grades += int(self.__grade)
        self.sum_grades = int(Grade.sum_grades)
        Grade.is_grade_higher_than_avr = Grade.is_grade_higher_than_avr
        if int(Grade.get_average()) < int(self.__grade):
            print(f"Well done, {self.__student_name}! The grade is higher than average!")

    @staticmethod
    def get_grade_current_index():
        return Grade.gradeCurrent_index

    @staticmethod
    def get_sum_grades(__grade):
        return Grade.sum_grades

    @staticmethod
    def get_average():
        return Grade.sum_grades / Grade.gradeCurrent_index

    @property
    def grade(self):
        return self.__grade

    @property
    def student_name(self):
        return self.__student_name

    @property
    def grade_current_index(self):
        return self.gradeCurrent_index

    @grade.setter
    def grade(self, new_grade):
        if isinstance(new_grade, int):
            self.__grade = new_grade
        else:
            print('Uncorrect data')

    @property
    def topic(self):
        return self.__topic

    @topic.setter
    def topic(self, new_topic):
        if new_topic in ["math", "python", "english"]:
            self.__topic = new_topic
        else:
            print('Uncorrect data')

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def is_grade_higher_than_avr(self):
        if self.get_average() < self.__grade:
            print(f"Well done, {self.__student_name}!")
