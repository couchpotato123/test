class Students:
    def __init__(self,fname="",lname="" ,id="",course=None,year=None,cgpa=None,uni=None, email=None):
        self.set_sid=id
        self.set_fname=fname
        self.set_lname=lname
        self.set_course=course
        self.set_year=year
        self.set_cgpa=cgpa
        self.set_uni=uni
        self.set_email=email
    def set_fname(self,fname):
        self.set_fname = fname
    def get_fname(self,fname):
        return self.set_fname
    def set_lname(self,lname):
        self.set_fname = lname
    def get_lname(self,lname):
        return self.set_lname
    def set_sid(self,id):
        self.set_fname = id
    def get_sid(self,id):
        return self.set_id
    def set_course(self,course):
        self.set_fname = course
    def get_course(self,course):
        return self.set_course
    def set_year(self,year):
        self.set_fname = year
    def get_year(self,year):
        return self.set_year
    def set_cgpa(self,cgpa):
        self.set_fname = cgpa
    def get_cgpa(self,cgpa):
        return self.set_cgpa
    def set_uni(self,uni):
        self.set_fname = uni
    def get_uni(self,uni):
        return self.set_uni
    def set_email(self,email):
        self.set_fname = email
    def get_email(self,email):
        return self.set_email
    def main(self):
        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        print("\n")
        gmail = "Hi!"+fname+lname+"@gmail.com"
        print(gmail)
stud = Students()
stud.main()

