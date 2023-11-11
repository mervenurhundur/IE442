from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/get_response', methods=['GET'])
def get_response():
    url = request.args.get('https://www.google.com/')  # Parametre olarak gelen URL'i al

    if url:  # Eğer URL parametresi varsa
        response = requests.get(url)  # GET isteği gönder
        return response.text, response.status_code  # Yanıtı ve durum kodunu döndür
    else:
        return "URL parametresi belirtilmedi", 400  # URL parametresi belirtilmediyse hata döndür

if __name__ == '__main__':
    app.run(debug=True)
