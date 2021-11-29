from flask import Flask, render_template, request
import predict 

app = Flask(__name__)

@app.route("/",methods = ['GET', 'POST'])
def index():
    #try:
    if request.method == "POST":
        pregnancies = request.form.get("pregnancies")
        glucose = request.form.get("glucose")
        bloodpressure = request.form.get("bloodpressure")
        skinthinkness = request.form.get("skinthinkness")
        insulin = request.form.get("insulin")
        bmi = request.form.get("bmi")
        dpfunc = request.form.get("dpfunc")
        age = request.form.get("age")
        model = request.form.get("model")
            
            
        print("result : ",pregnancies,glucose,bloodpressure,skinthinkness,insulin, bmi ,dpfunc,age,model)
        result_pred = predict.predict(pregnancies, glucose, bloodpressure,skinthinkness, insulin, bmi, dpfunc, age, model)
        print(result_pred)
            
        if result_pred == 1:
            result1= "It seems you may have diabetes, ¡Consult your Doctor!"
        else:
            result1 = "It seems you are free from diabetes. Eat Healthy and Stay Healthy"
            
        
        return render_template("index.html", data = [{"result":result1}])
    #except:
        #return "Se produjo un problema"
    
    return render_template("index.html")
    



if __name__=="__main__":
    app.run()