from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi', methods=['GET'])
def bmi_get():
    return redirect('/')

@app.route('/bmi', methods=['POST'])
def bmi():
    if 'name' in request.form and 'height' in request.form and 'weight' in request.form :
        try:
            name   = request.form['name']
            height = float(request.form['height']) / 100
            weight = float(request.form['weight'])
            bmi    = round(weight / height**2, 1)
            appropriate_weight = round(height**2 * 22, 1)
            return render_template('bmi.html', name=name, bmi=bmi, appropriate_weight=appropriate_weight)
        except :
            return redirect('/')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)