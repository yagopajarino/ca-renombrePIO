# ca-renombrePIO

Renombrar archivos PDF para presentación ante ENARGAS.

## Instalación 🔧

Software necesario:
<ul>
  <li>Python 3.6 o superior 👉 <a href="https://www.python.org/downloads/">descargar</a></li>
</ul>

Debe estar incluido en el PATH del sistema. <a href="https://www.java.com/es/download/help/path_es.html">Cómo cambiar variables del sistema</a>

Al momento de instalar python, ofrece la posibilidad de agregarlo al PATH del sistema (opción "Add Python 3.9 to PATH) 👇

![image](https://user-images.githubusercontent.com/84155397/126665001-5b8d2fe9-d690-4f3b-ac5a-45b2f6036e99.png)

## Descarga de archivos 📂
Descargar los archivos de este repositorio y extraer en alguna carpeta de la computadora. 

<a href="https://github.com/yagopajarino/ca-renombrePIO/archive/refs/heads/main.zip">Descargar archivos</a>

Luego se debe abrir un CMD (Simbolo del sistema) en la carpeta donde están descargados los archivos, para ello:
<ol>
<li>Ctrl + L dentro de la carpeta -> sombrea la barra de directorio en color azul</li>
<li>Borrar lo sombreado en azul</li>
<li>Escribir CMD</li>
<li>Enter</li>
</ol>

Se debe abrir una pantalla como esta 👇

![image](https://user-images.githubusercontent.com/84155397/126667543-787fb8a6-12aa-4a75-a4de-5e9cf466abc7.png)

que en lugar de C:\Users debe tener la ruta de la carpeta donde se descargaron los archivos.

Una vez tenemos el CMD ubicado en la carpeta donde estan los archivos descargados, utilizamos el siguiente comando:
```
pip install -r requirements.txt
```
![image](https://user-images.githubusercontent.com/84155397/126671901-76f11023-a516-4b52-a2da-78e71b291656.png)

Al dar enter, comienza la descarga e instalación de las librerias necesarias.

## Utilización

### Archivos PDF a renombrar

1. Crear una carpeta llamada <b>docs</b> en la misma ubicación donde se guardaron los archivos descargados
2. Guardar los archivos a renombrar, en el nombre debe figurar el número de orden de compra/pago.

### Completar excel nomenclatura.xlsx

<table>
<tr>
  <td>Columna</td>
  <td>Descripción</td>
</tr>
<tr>
  <td>From</td>
  <td>Número de orden de compra/pago. Debe ser el mismo que figura en el nombre del archivo PDF guardado en el paso anterior.</td>
</tr>
<tr>
  <td>To</td>
  <td>Nomenclatura para renombrar el archivo PDF.</td>
</tr>
</table>

No es necesario que en la columna From figure exactamente el nombre del archivo como fue guardado en la carpeta, sino que el programa utiliza <a href="https://es.wikipedia.org/wiki/Expresi%C3%B3n_regular">expresiones regulares</a> 
para encontrar el numero de orden de compra/pago en el nombre del PDF guardado.

### Ejecutar app.py

Dar doble click en app.py, abre una ventana negra y ejecuta las instrucciones del archivo, se cierra automáticamente al finalizar.
Una vez finalizado, debe figurar una carpeta llamada "Output" con los archivos PDF renombrados.

## Ejemplo de uso

#### nomenclatura.xlsx

<table>
<tr>
  <td>Columna</td>
  <td>Valor</td>
</tr>
<tr>
  <td>From</td>
  <td>4500001234</td>
</tr>
<tr>
  <td>To</td>
  <td>COD_PROY_202108_OC_4500001234</td>
</tr>
</table>

#### carpeta docs

* docs/
  * OC-4500001234-BLABLABLA

#### app.py
Luego de ejecutar la aplicación, se genera una carpeta Output con el archivo COD_PROY_202108_OC_4500001234.pdf

## Contacto
En caso de dudas, consutas, mejoras 👉 <a href="https://yagopajarino.github.io/repos-contact/?ca-renombrePIO" target="_blank">Get in touch</a>

## Invitame un cafecito :money_with_wings:
Este repositorio es de uso libre bajo licencia MIT pero tu donación ayuda a mantenero y mejorarlo.

[![Invitame un café en cafecito.app](https://cdn.cafecito.app/imgs/buttons/button_3.svg)](https://cafecito.app/yagopajarino)
