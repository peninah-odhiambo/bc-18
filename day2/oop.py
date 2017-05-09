spacer = " "

class Person (object):

    """ Fellow and Staff inherit from the Class Person"""

    def __init__(self, id, first_name, last_name, designation):

        self.id = person_id
        self.name = first_name + spacer + last_name  


class Staff(Person):

    job_type = "Staff"

    def __init__(self, person_id, first_name, last_name, designation):

        self.first_name = first_name
        self.last_name = last_name
        self.designation = designation
        self.person_id = person_id

        if self.designation > "Manager":
            return "Earns over eighty thousand"
        else:
            False


class Fellow(Person):

    job_type = "Fellow"

    def __init__(self, person_id, first_name, last_name, designation):
        self.first_name = first_name
        self.last_name = last_name
        self.designation = designation
        self.person_id = person_id

        if self.designation == "LFA":
            return "Earns above fifty thousand"
        else:
            return "Earns less than fifty thousand"




