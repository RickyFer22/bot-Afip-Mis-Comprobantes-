# Bot de Descarga de Comprobantes desde Mis Comprobantes (AFIP)

Este bot automatiza la descarga de comprobantes desde el sitio web de AFIP (Administración Federal de Ingresos Públicos) para contribuyentes Responsables Inscriptos. 
Utiliza una lista de CUIT y claves fiscales proporcionada en un archivo Excel para acceder a las cuentas de los contribuyentes y descargar los comprobantes emitidos y recibidos del mes anterior en formato XLS.

## Instrucciones

1. **Instalación de Python:** Si no tienes instalado Python 3.8.5 o superior, descárgalo e instálalo desde [www.python.org/downloads](https://www.python.org/downloads). Durante la instalación, asegúrate de agregar Python al PATH.

2. **Descargar Archivos:** Descarga los archivos `bot_descarga.py`, `claves.xlsx` y `requirements.txt` desde este repositorio. Colócalos en una misma carpeta.

3. **ChromeDriver:** Descarga ChromeDriver según la versión de Google Chrome que uses desde [chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) y colócalo en la misma carpeta mencionada en el paso anterior.

4. **Instalar Dependencias:** Abre la línea de comandos, navega hasta la carpeta creada y ejecuta el siguiente comando para instalar las librerías requeridas:

   ```bash
   pip install -r requirements.txt

Modificar Archivo Excel: Abre el archivo claves.xlsxy completa la lista de CUIT y claves fiscales que desea utilizar.
Cada par debe estar en una fila separada. Guarda los cambios.
