from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

plants = [
    {"name": "Monstera", "type": "Szobanövény", "feature": "Nagyméretű levelek"},
    {"name": "Bambusz", "type": "Dísznövény", "feature": "Gyors növekedés"},
    {"name": "Kaktusz", "type": "Pozsgás", "feature": "Szárazságtűrő"}
]

@app.route('/tabla', methods=["GET"])
def tabla():
    return render_template('tabla.html')

    
if __name__ == "__main__":
    app.run(debug=True)