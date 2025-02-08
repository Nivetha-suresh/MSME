from flask import Flask, render_template, request
app = Flask(__name__)

class Student:
    def __init__(self, name, regno, phy, chem, math, csc, eng, tam):
        self.name = name
        self.regno = regno
        self.phy = phy
        self.chem = chem
        self.math = math
        self.csc = csc
        self.eng = eng
        self.tam = tam

    def tot_m(self):
        self.total = self.phy + self.chem + self.math + self.csc + self.eng + self.tam
        return self.total

    def avg_m(self):
        self.avg = self.total / 6
        return self.avg

    def grade(self):
        subjects = [self.phy, self.chem, self.math, self.csc, self.eng, self.tam]
        self.print_grade = []
        for i in subjects:
            if i >= 90:
                self.print_grade.append("O")
            elif i >= 80:
                self.print_grade.append("A+")
            elif i >= 70:
                self.print_grade.append("A")
            elif i >= 60:
                self.print_grade.append("B+")
            elif i >= 50:
                self.print_grade.append("B")
            else:
                self.print_grade.append("U")
        return self.print_grade

    def result(self):
        return "Pass" if "U" not in self.print_grade else "Fail"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        regno = request.form['regno']
        phy = int(request.form['phy'])
        chem = int(request.form['chem'])
        math = int(request.form['math'])
        eng = int(request.form['eng'])
        csc = int(request.form['csc'])
        tam = int(request.form['tam'])

        student = Student(name, regno, phy, chem, math, csc, eng, tam)
        total = student.tot_m()
        avg = student.avg_m()
        grades = student.grade()
        result = student.result()

        return render_template('result.html', student=student, total=total, avg=avg, grades=grades, result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
