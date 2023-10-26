from flask import Flask, jsonify, request, make_response
import uuid
import time

app = Flask(__name__)
token = {}


# Flask
@app.route('/api/login', methods=['POST'])
def login():
  # Nhận dữ liệu đầu vào từ yêu cầu
  username = request.json['username']
  password = request.json['password']

  # Kiểm tra mật khẩu
  if (username != 'user' or password != '111111'):
    return make_response(jsonify({'error': 'error'}), 400)

  t = uuid.uuid4()
  token.clear()
  token[str(t)] = time.time_ns()
  return jsonify({'token': t})


@app.route('/api/txn/<txn_id>', methods=['GET'])
def getTxnStatus(txn_id):
  try:
    result = checkToken(request)
    if (result is not None):
      return result

    # logic
    id = txn_id
    if (int(id) % 2 == 0):
      return make_response(jsonify({'status': 'PENDING'}), 200)
    if (int(id) % 3 == 0):
      return make_response(jsonify({'status': 'COMPLETED'}), 200)
    if (int(id) % 6 == 0):
      return make_response(jsonify({'status': 'WAITING_APPROVE'}), 200)
    raise Exception
  except:
    return make_response(jsonify({'error': 'internal server'}), 500)


@app.route('/api/txn/<txn_id>', methods=['DELETE'])
def delTxn(txn_id):
  try:
    result = checkToken(request)
    if (result is not None):
      return result

    # logic
    id = txn_id
    if (int(id) % 2 == 0):
      return make_response(jsonify({'status': 'DELETED'}), 200)
    raise Exception
  except:
    return make_response(jsonify({'error': 'internal server'}), 500)


@app.route('/api/txn', methods=['POST'])
def createTxn():
  try:
    result = checkToken(request)
    if (result is not None):
      return result

    # logic
    id = request.json['txn_id']
    if (int(id) % 2 == 0):
      return make_response(jsonify({'status': 'SUCCESS with txn_id:{}'.format(id)}), 200)
    raise Exception
  except:
    return make_response(jsonify({'error': 'internal server with txn_id:{}'.format(id)}), 500)


@app.route('/api/txn/<txn_id>', methods=['PUT'])
def execTxn(txn_id):
  try:
    result = checkToken(request)
    if (result is not None):
      return result

    # logic
    action = request.json['action']
    if (action != 'EXEC'):
      return make_response(jsonify({'status': 'Action is valid'}), 400)

    if (int(txn_id) % 2 == 0):
      return make_response(jsonify({'status': 'SUCCESS with txn_id:{}'.format(txn_id)}), 200)
    raise Exception
  except:
    return make_response(jsonify({'error': 'internal server with txn_id:{}'.format(txn_id)}), 500)


@app.route('/api/txn/<txn_id>', methods=['PATCH'])
def approveTxn(txn_id):
  try:
    result = checkToken(request)
    if (result is not None):
      return result

    # logic
    action = request.json['action']
    if (action != 'APPROVE'):
      return make_response(jsonify({'status': 'Action is valid'}), 400)

    if (int(txn_id) % 2 == 0):
      return make_response(jsonify({'status': 'SUCCESS with txn_id:{}'.format(txn_id)}), 200)
    raise Exception
  except:
    return make_response(jsonify({'error': 'internal server with txn_id:{}'.format(txn_id)}), 500)

def checkToken(request):
  t = request.headers.get('Authorization')
  if (t == None or t == "" or len(token) == 0 or token[str(t)] == None):
    return make_response(jsonify({'error': 'token invalid'}), 401)
  if (time.time_ns() >= token[t] + 300 * 1000000000):
    return make_response(jsonify({'error': 'token time out'}), 401)
  return None


if __name__ == "__main__":
  app.run(debug=True)
