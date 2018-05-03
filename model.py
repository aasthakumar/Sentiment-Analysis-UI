from sklearn.externals import joblib
import sys 

def model(review_text):
    clf = joblib.load('filename.pkl') 
    review = []
    #print(review_text)
    review.append(review_text)
    val = clf.predict(review)
    return val

if __name__ == '__main__':
    cmdargs = sys.argv
    result = model(cmdargs[1])
    #print(result)
    if result == [0]:
        print("Negative")
    else:
        print("Positive")