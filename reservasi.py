from flask import Flask, request, jsonify

app = Flask(__name__)
reservasi_db = []

@app.route('/jadwalReservasi', methods=['GET'])
def tampil_reservasi():
    nama_dokter = []
    klinik = []
    hari = []
    jam_praktek = []
    for x in reservasi_db:
        nama_dokter.append(x[0])
        klinik.append(x[1])
        hari.append(x[2])
        jam_praktek.append(x[3])

    return jsonify({
        "chats": [
            {
                "text": "Jadwal reservasi \n\nNama Dokter : " + ", ".join(nama_dokter),
                "type": "text"
            },
            {
                "text": "Klinik : " + ", ".join(klinik),
                "type": "text"
            },
            {
                "text": "Hari : " + ", ".join(hari),
                "type": "text"
            },
             {
                "text": "Pukul : " + ", ".join(jam_praktek),
                "type": "text"
            }
        ]
    })


@app.route('/jadwalReservasi', methods=['POST'])
def tambah_reservasi():
    data = request.get_json()
    reservasi_db.append([data["nama_dokter"], data["klinik"], data["hari"], data["jam_praktek"]])

    return jsonify({
        "chats": [
            {
                "text": "Data reservasi berhasil disimpan",
                "type": "text"
            }
        ]
    })


if __name__ == '__main__':
    app.run(port=5000)

