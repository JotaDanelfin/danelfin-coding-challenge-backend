from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open("data.json") as f:
    data = json.load(f)

@app.route('/stocks', methods=['GET'])
def stocks():
    try:
        limit = request.args.get('limit', default=10, type=int)
        offset = request.args.get('offset', default=0, type=int)
        order_by = request.args.get('order_by', default=None, type=str)
        order_dir = request.args.get('order_dir', default='asc', type=str).lower()

        filters = {
            key: value for key, value in request.args.items()
            if key not in ['limit', 'offset', 'order_by', 'order_dir']
        }

        filtered_data = data
        for key, value in filters.items():
            if value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False

            filtered_data = [item for item in filtered_data if str(item.get(key)) == str(value)]

        if order_by:
            filtered_data.sort(
                key=lambda x: x.get(order_by, None),
                reverse=(order_dir == 'desc')
            )

        paginated_data = filtered_data[offset:offset + limit]

        return jsonify({
            "data": paginated_data,
            "total": len(filtered_data),
            "limit": limit,
            "offset": offset,
            "order_by": order_by,
            "order_dir": order_dir
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
