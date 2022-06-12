from flask import Flask, render_template
import math
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/draw/<svg>')
def draw_svg(svg: str):
    coefficients = [200, 30, 10]
    coefficients_theta = [math.pi/4, 1, 1]
    return render_template('draw.html', svg_name=svg, coefficients_r=coefficients, coefficients_theta=coefficients_theta)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
