from random import sample
from flask import Flask, render_template
import math
import os
import numpy as np
import cmath

app = Flask(__name__)

def transform(samples):
    #t = np.fft.fft(10*np.cos(2 * np.pi * np.arange(sam) / 8) + 20j*np.sin(2*np.pi * np.arange(8) / 8)) / 
    t = np.fft.fft(samples) / len(samples)
    f = np.fft.fftfreq(len(samples))
    zipped = sorted(zip(f, t), key=lambda x: abs(x[0]))
    f = [x for (x, _) in zipped]
    t = [x for (_, x) in zipped]
    coefficients = list(abs(num) for num in t)
    thetas = list(cmath.phase(num) for num in t)
    print(f)
    print(coefficients)
    print(thetas)
    return (coefficients, thetas, f)

def samples(name):
    if name == 'sine':
        return 2*(30j*np.sin(2 * np.pi * np.arange(1000) / 1000) + np.arange(1000)/10 - 50)
    elif name == 'circle':
        return 100 * np.exp(2j * np.pi * np.arange(20) / 20)
    return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/draw/<name>')
def draw_svg(name: str):
    (coefficients, coefficients_theta, freq) = transform(samples(name))
    return render_template('draw.html', svg_name=name, coefficients_r=coefficients, coefficients_theta=coefficients_theta, freq=freq)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
