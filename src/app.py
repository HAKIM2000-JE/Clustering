import pandas as pd
from flask import jsonify, Flask, request

from service import Service






import engine
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# Service data
ServiceData = Service()






@app.route("/recommendations", methods=['POST'])
def getRecommendation():
    request_data = request.get_json()

    RecommendationFinale=engine.get_Recommendation(request_data['propertyBookingId'])

    print(RecommendationFinale)

    return  str(RecommendationFinale)



if __name__ == "__main__":



    app.run(debug=False)

    # test in POST MAN :

    # http://127.0.0.1:5000/data

    # http://127.0.0.1:5000/data

