# fpcashflow
Solución Financiera para la Empresa Five Pack Alliance.

### Instalar requerimientos con sus versiones respectivas
`pip install --upgrade pip
pip install -r requirements.txt`
De esta forma tendrán instalado lo necesario

### Cambiar requerimientos (NO HACER - SOLO EL S**CUM** MASTER)
`pip list --format=freeze > requirements.txt`

### Correr la app
`streamlit run Flujo_de_Caja.py`

## ¡¡¡¡¡PAUTAS IMPORTANTES!!!!!
### Verificar autenticación en cada página. 🚫 Metidos 🚫
```python
from utils.auth0 import getAuth0
user_info = getAuth0()
if user_info:
    print('Está logueado y user almacena sus datos')
else:
    print('No está logueado')
```
### Explicaciones
- `utils/auth0.py` contiene funciones relacionadas al flujo de autenticación.
- `utils/store.py` contiene los dataframes de los datos que vamos a usar.
- `utils/env.py` contiene la configuración de las variables de entorno.