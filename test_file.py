from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="finiteautomata/bertweet-base-sentiment-analysis")
import predefined_model_test  as pmt
"""
text = "i will kill you"
print(sentiment_pipeline([text]))
"""

def sentiment_analysis(text, pipe):
    analysis = pipe([text])
    print(analysis)
    result = "Label : {a}\nScore : {b}".format(a=analysis[0]['label'], b=analysis[0]['score'])
    return result


while True:
    word = input("Enter a word : ")
    print(sentiment_analysis(word, sentiment_pipeline))
    print(pmt.sentiment_analysis(word, sentiment_pipeline))
