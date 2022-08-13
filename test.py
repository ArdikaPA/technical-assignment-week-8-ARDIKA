from flask import Flask, request
from mongo import save_data

app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST'])
def data2():
    kecepatan = request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    save_data(kecepatan=kecepatan, latitude=latitude, longitude=longitude)
    return{
        "message": "Sukses memasukkan data INPO ke dalam DATABASE"
    }


if __name__ == '__main__':
    app.run(debug=True)