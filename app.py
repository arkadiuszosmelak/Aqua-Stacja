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

    odleglosci1 = odleglosci[-24:]
    odleglosci2 = odleglosci[-144:]
    odleglosci3 = odleglosci[-288:]

    print(odleglosci1, odleglosci2, odleglosci3)
    temperatury1 = temperatury[-24:]
    temperatury2 = temperatury[-144:]
    temperatury3 = temperatury[-288:]

    daty1 = daty[-24:]
    daty2 = daty[-144:]
    daty3 = daty[-288:]

    # return render_template('index.html', odleglosci1 = odleglosci, labels1 = daty, legend = legenda, tmp1 = temperatury,  akt_odl = akt_odl, akt_tmp = akt_tmp, akt_data = akt_data)
    # return render_template ('index.html')
    return render_template('index.html', odleglosci1 = odleglosci1, odleglosci2 = odleglosci2, odleglosci3 = odleglosci3, labels1 = daty1, labels2 = daty2, labels3 = daty3, legend = legenda, tmp1 = temperatury1, tmp2 = temperatury2, tmp3 = temperatury3, akt_odl = akt_odl, akt_tmp = akt_tmp, akt_data = akt_data)


if __name__ == "__main__":
    app.run(debug=True)