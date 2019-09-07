from flask import Flask, render_template

app = Flask(__name__)
# python app.py

@app.route('/')
def checkout():
    # Step 1: JWT Creation
    #   > jwt.io
    #   > Pass to frontend
    # Step 10: JWT Validation
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
