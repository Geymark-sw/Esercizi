cities: dict[str:str] = {"Roma":"Nazione: Italia\nPopolazione: 2.8 milioni\nCaratteristica: "
                         "Roma è famosa per il suo patrimonio storico e culturale. È conosciuta come la 'Città Eterna' per i suoi monumenti antichi e l'importanza storica, tra cui il Colosseo, il Pantheon e il Vaticano.",
                         
                         "Los Angeles":"Nazione: Stati Uniti\nPopolazione: 4 Milioni\nCaratteristica:"
                         "Los Angeles è conosciuta come la capitale mondiale dell'intrattenimento. È il centro dell'industria cinematografica e televisiva, ospitando Hollywood, una delle icone più riconoscibili al mondo.",
                         
                         "Manila":"Nazione: Filippine\nPopolazione:1.8 Milioni\nCaratteristica:"
                         "Manila è una città vivace e densamente popolata, famosa per il suo mix di cultura storica e moderna. È conosciuta per il suo lungomare, Intramuros (la città fortificata storica) e il porto di Manila, uno dei più importanti del sud-est asiatico."}


for i in cities.keys():

    print(f"{i}:\n{cities[i]}\n")