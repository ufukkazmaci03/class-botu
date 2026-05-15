class Student:
    name = "Öğrenci"
    age = 15
    course = "Python lvl3"
    level = 1
    finished_courses = []



        
    

    def level_up(self):
        self.level += 1
        print("Seviye Atladın!")


    def bday(self):
        self.age += 1
        print("Mutlu Yıllar!")


    def finish_corse(self):
        print("Yaşasın! Kurs tamamlandı!")
        self.finished_courses.append(self.course)
        self.course = ""
        print("Yeni bir kurs seçin!")
