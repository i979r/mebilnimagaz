from flask import Flask, jsonyfy, request
app = Flask(__name__)
order = []
@app.route('/icecream/order', methods=['POST'])
def save_order():
    data = request.jons 
    flover = data.get('flavor')
    quantity = data.get('quantity')
    if flavor and quantity > 0:
        order.append({'flover': flavor, 'quantity': quantity})
        return jsonyfy({'message': f'kol. {quantity} por {flover} mor'})
    return jsonyfy ({'error': Invalid order}), 408
if __name__ == '__main__':
    app.run(degub=True)