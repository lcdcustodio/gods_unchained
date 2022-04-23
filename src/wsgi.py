import os
from app import create_app

app = create_app("production")
if __name__ == "__main__":
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)    

    print("----------------------")
    print("Strategy API Started")
    print("----------------------")   

    app.run(port=5000,
            debug=False,
            host='0.0.0.0'
        )
