from flask import Flask
from flask import render_template
from datetime import time
 
 
app = Flask(__name__, static_url_path='/static')
 
 
@app.route("/")
def chart():
    # legend = 'Monthly Data'
    # labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    # values = [10, 9, 8, 7, 6, 4, 7, 8]
    # return render_template('test.html', values=values, labels=labels, legend=legend)
 
    file = open("testfile.txt", "r") 
    lista = file.readlines()
    #naprawa (usuwanie "\n" z wartosci)
    for i in range (0, len(lista)):
        lista[i] = lista[i][0:-1]
    
    lista = lista [-72:]
    odleglosci = lista[0::3]
    odleglosci = [round(float(i),2) for i in odleglosci]
    temperatury = lista[1::3]
    temperatury = [round(float(i),2) for i in temperatury]
    daty = lista[2::3]
    legenda = 'Poziom wody [cm]'

    akt_odl = odleglosci[-1]
    akt_tmp = temperatury[-1]
    akt_data = daty[-1]
    file.close()

    

    return render_template('index.html', values = odleglosci, labels = daty, legend = legenda, tmp = temperatury, akt_odl = akt_odl, akt_tmp = akt_tmp, akt_data = akt_data)


if __name__ == "__main__":
    app.run(debug=True)