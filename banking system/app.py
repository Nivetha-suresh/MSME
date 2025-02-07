from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

class IndianBank:
    def __init__(self, name, accno, initbalance):
        self.name = name
        self.accno = accno
        self.balance = initbalance

    def check_balance(self):
        return self.balance

    def deposite(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return None

user = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global user
    if request.method == 'POST':
        if 'create_account' in request.form:
            name = request.form['name']
            acc_no = request.form['acc_no']
            user = IndianBank(name, acc_no, 0)
            flash('Account created successfully!')
        elif 'deposite' in request.form and user:
            amount = int(request.form['amount'])
            user.deposite(amount)
            flash(f'Rupees {amount} added to your account.')
        elif 'withdraw' in request.form and user:
            amount = int(request.form['amount'])
            if user.withdraw(amount) is None:
                flash('Insufficient balance.')
            else:
                flash(f'Rupees {amount} withdrawn from your account.')

    return render_template('index.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)