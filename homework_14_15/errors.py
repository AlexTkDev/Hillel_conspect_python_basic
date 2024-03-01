ERROR_404 = ""
ERROR_MAX_STUDENT_IN_GROUP = "Max number of students reached"


class MaxStudentsReachedError(Exception):
    def __init__(self, message=ERROR_MAX_STUDENT_IN_GROUP):
        self.message = message
        super().__init__(self.message)



# Gruop
# StudetGroup
# Student_Group