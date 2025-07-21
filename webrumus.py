from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html>
<head><title>Rumus Matematika</title></head>
<body>
    <h2>Pilih Rumus:</h2>
    <form method="post">
        <select name="menu">
            <option value="persegi">Luas Persegi</option>
            <option value="persegi_panjang">Luas Persegi Panjang</option>
            <option value="segitiga">Luas Segitiga</option>
            <option value="trapesium">Luas Trapesium</option>
            <option value="layang">Luas Layang-Layang</option>
            <option value="lingkaran">Luas Lingkaran</option>
            <option value="limas_persegi">Volume Limas Persegi</option>
            <option value="limas_segitiga">Volume Limas Segitiga</option>
            <option value="abc">Rumus ABC</option>
            <option value="kalkulator">Kalkulator</option>
        </select><br><br>
        <input type="text" name="input1" placeholder="Input 1"><br>
        <input type="text" name="input2" placeholder="Input 2 (jika perlu)"><br>
        <input type="text" name="input3" placeholder="Input 3 (jika perlu)"><br>
        <button type="submit">Hitung</button>
    </form>
    {% if result %}
    <h3>Hasil: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        menu = request.form["menu"]
        try:
            i1 = float(request.form.get("input1", 0) or 0)
            i2 = float(request.form.get("input2", 0) or 0)
            i3 = float(request.form.get("input3", 0) or 0)
            if menu == "persegi":
                result = f"Luas persegi: {i1 * i1} cm²"
            elif menu == "persegi_panjang":
                result = f"Luas persegi panjang: {i1 * i2} cm²"
            elif menu == "segitiga":
                result = f"Luas segitiga: {i1 * i2 * 0.5} cm²"
            elif menu == "trapesium":
                result = f"Luas trapesium: {0.5 * (i1 + i2) * i3} cm²"
            elif menu == "layang":
                result = f"Luas layang-layang: {0.5 * (i1 + i2)} cm²"
            elif menu == "lingkaran":
                result = f"Luas lingkaran: {3.14 * i1 * i1} cm²"
            elif menu == "limas_persegi":
                result = f"Volume limas persegi: {i1 * i1 * i2 / 3} cm³"
            elif menu == "limas_segitiga":
                luas_alas = i1 * i2 * 0.5
                result = f"Volume limas segitiga: {luas_alas * i3 / 3} cm³"
            elif menu == "abc":
                a, b, c = i1, i2, i3
                dua_a = 2 * a
                pangkatb = b * b
                penjumlahan_dalam = pangkatb - 4 * a * c
                if penjumlahan_dalam < 0:
                    result = "Tidak ada akar real."
                else:
                    akar = penjumlahan_dalam ** 0.5
                    x1 = (-b + akar) / dua_a
                    x2 = (-b - akar) / dua_a
                    result = f"x1 = {x1}, x2 = {x2}"
            elif menu == "kalkulator":
                result = f"Tambah: {i1 + i2}, Kurang: {i1 - i2}, Kali: {i1 * i2}, Bagi: {'Tidak bisa' if i2 == 0 else i1 / i2}"
        except Exception as e:
            result = f"Error: {e}"
    return render_template_string(HTML_FORM, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)