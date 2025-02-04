'''
-- Instalación de Pandas

Si ya tienes Python y PIP instalados en tu sistema, la instalación de Pandas es muy sencilla.

Instálalo con el siguiente comando:

pip install pandas

Si este comando falla, usa una distribución de Python que ya tenga Pandas instalado, como Anaconda o Spyder.

-- Importar Pandas

Una vez instalado Pandas, impórtalo en tus aplicaciones con la palabra clave import:

import pandas

Ahora Pandas está listo para usarse.

Ejemplo
'''

import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

'''
-- Pandas como pd

Pandas suele importarse con el alias pd.

Alias: En Python, un alias es un nombre alternativo para referirse a la misma cosa.

Puedes crear un alias con la palabra clave as al importar:

import pandas as pd

Ahora puedes referirte al paquete Pandas como pd en lugar de pandas.

Ejemplo
'''

import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

'''
-- Verificar la versión de Pandas

La versión de Pandas está almacenada en el atributo __version__.

Ejemplo
'''

import pandas as pd

print(pd.__version__)