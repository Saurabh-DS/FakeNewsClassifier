# from sklearn.externals import joblib
# import sklearn.external.joblib as extjoblib
import joblib
from flask import Flask, request, render_template

pipeline = joblib.load('./pipeline.sav')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


def get_all_query(query_title, query_author, query_text):
    pass


@app.route('/api',methods=['POST'])
def get_delay():

    result=request.form
    query_title = result['title']
    query_author = result['author']
    query_text = result['maintext']
    print(query_text)
    query = [query_title] + [query_author] + [query_text] #[query_text]#get_all_query(query_title, query_author, query_text)
    user_input = {'query':query}
    pred = pipeline.predict(query)
    print(pred)
#     dic = {1:'real',0:'fake'}
#     return f'<html><body><h1>{dic[pred[0]]}</h1> <form action="/"> <button type="submit">back </button> </form></body></html>'

    output = round(pred[0], 2)
    if output == 1:
        return render_template('index.html', prediction_text="Great! It's a real news!")
    else:
        return render_template('index.html', prediction_text="Sorry! It's a fake news.")

if __name__ == '__main__':
    app.run(port=8080, debug=True)
