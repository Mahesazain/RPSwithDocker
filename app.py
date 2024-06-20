from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Inisialisasi skor
skor = {
    'menang': 0,
    'kalah': 0,
    'seri': 0
}

# Pilihan untuk permainan
pilihan = ['Batu', 'Kertas', 'Gunting']

@app.route('/')
def index():
    return render_template('index.html', skor=skor)

@app.route('/main', methods=['POST'])
def main():
    pilihan_pemain = request.form['pilihan']
    pilihan_computer = random.choice(pilihan)

    hasil = ""
    if pilihan_pemain == pilihan_computer:
        hasil = "Seri!"
        skor['seri'] += 1
    elif (pilihan_pemain == 'Batu' and pilihan_computer == 'Gunting') or \
         (pilihan_pemain == 'Kertas' and pilihan_computer == 'Batu') or \
         (pilihan_pemain == 'Gunting' and pilihan_computer == 'Kertas'):
        hasil = "Anda Menang!"
        skor['menang'] += 1
    else:
        hasil = "Komputer Menang!"
        skor['kalah'] += 1

    return render_template('index.html', hasil=hasil, pilihan_pemain=pilihan_pemain, pilihan_computer=pilihan_computer, skor=skor)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
