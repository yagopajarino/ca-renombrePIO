import re
import os
import shutil
import pandas as pd

# Lectura del excel
df = pd.read_excel("nomenclatura.xlsx")
q = df.shape[0]

# Lista de documentos en /docs
dirs = os.listdir("docs")

try:
    os.mkdir("Output")
except:
    pass

# Loop para cada linea del excel copia los archivos con nombre From de /docs y pega en /Output con nombre To
for x in range(q):
    nro = df["From"][x]
    doc_regex = ".*({}).*".format(nro)
    for y in dirs:
        finds = re.findall(doc_regex, y)
        if len(finds) > 0:
            new_name = df["To"][x] + ".pdf"
            shutil.copy(os.path.join("docs", y), os.path.join("Output", new_name))

