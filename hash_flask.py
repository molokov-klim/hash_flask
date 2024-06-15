from flask import Flask, request, jsonify
import subprocess
import logging

app = Flask(__name__)

# Путь к файлу deploy.sh
deploy_script_path = "/home/hash/hash_flask/deploy.sh"
reboot_sigma10 = 0
scanner_command = 0


@app.route('/deploy', methods=['GET'])
def deploy():
    try:
        # Вызываем скрипт deploy.sh
        subprocess.Popen(["bash", deploy_script_path])
        return 'OK', 200
    except subprocess.CalledProcessError:
        return 'deploy error', 200


@app.route('/get_reboot_sigma10', methods=['GET'])
def get_command_sigma10():
    global reboot_sigma10
    if not reboot_sigma10 == 1:
        return '0', 200
    reboot_sigma10 = 0
    return '1', 200


@app.route('/set_reboot_sigma10', methods=['GET'])
def set_reboot_sigma10():
    global reboot_sigma10
    reboot_sigma10 = 1
    return 'OK', 200


@app.route('/get_scanner_command', methods=['GET'])
def get_scanner_command():
    global scanner_command
    if not scanner_command == 1:
        return '0', 200
    scanner_command = 0
    return '1', 200


@app.route('/set_scanner_command', methods=['GET'])
def set_scanner_command():
    global scanner_command
    scanner_command = 1
    return 'OK', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)






















