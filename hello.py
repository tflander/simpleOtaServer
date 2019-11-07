from flask import Flask, request, send_from_directory

# artifact_path = '/Users/toddflanders/esp/esp-idf/examples/system/ota/simple_ota_example/build'
artifact_path = 'builds/simpleOta'

app = Flask(__name__, static_folder=artifact_path, static_url_path='')

# https://127.0.0.1:5000/

@app.route('/config')
def setArtifactVersion():
    return 'TODO'

@app.route('/')
def hello():
    print(request.path)
    print("-------------")
    return "Hello World!"

@app.route('/simple_ota.bin')
def get_artifact():
    print(request.path)
    print("-------------")
    # return "Hello World!"
    print(request.path[1:])
    return send_from_directory(app.static_folder, request.path[1:])

if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'))