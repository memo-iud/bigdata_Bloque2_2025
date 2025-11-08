# bigdata_Bloque2_2025
# Act1_big_data
Guillermo León Loaiza Mesa.

Robinson Marin Morales.

Ruta Data set: https://www.kaggle.com/datasets/dansbecker/powerlifting-database?resource=download

Problema: somos la empresa Romen de powerlifting, dedicados a entender el panorama competitivo global para planificar su expansión y estrategia de eventos. 

Qué (La necesidad): Identificar patrones y tendencias en la organización de competiciones de powerlifting. Específicamente, necesitan saber dónde (países, estados) se concentran los eventos, cuándo (evolución temporal, estacionalidad) ocurren y quién (federaciones) domina el mercado en distintas regiones.

Para quién: Directores de estrategia de federaciones deportivas, organizadores de eventos y analistas de mercado deportivo.

Por qué requiere analítica: El archivo contiene miles de registros de eventos (más de 8,400 según el fragmento). Es imposible para una persona identificar tendencias complejas manualmente. Se necesita analítica de datos para:

Agregar datos por fecha y ver el crecimiento (o declive) de eventos por año.

Visualizar geográficamente las "zonas calientes" (países/estados con más competiciones).

Segmentar el mercado por federación para analizar la cuota de mercado y la competencia regional.

###Variables Relevantes.

Variables de Identificación: IdEncuentro, rutaEncuentro.

Variable Categórica Principal: Federación.

Variable Temporal: Fecha.

Variables Geográficas: PaisEncuentro, estadoEncuentro, ciudadEncuentro.

Variable Descriptiva: NombreReunion.

### Modelo ER 
<img width="1250" height="872" alt="image" src="https://github.com/user-attachments/assets/aeb3a9cd-25f1-4713-a2d7-0e1cb208a5f5" />


### Evidencia de carga.

<img width="1437" height="676" alt="image" src="https://github.com/user-attachments/assets/0d5f8358-57dc-423e-a708-0ab6944d209f" />


<img width="1469" height="723" alt="image" src="https://github.com/user-attachments/assets/113f87d8-4177-4714-921f-84cc374076d1" />


<img width="1626" height="921" alt="image" src="https://github.com/user-attachments/assets/415b0eea-46cd-48f6-a2df-c7dcaa705b25" />

### QUERYS
<img width="1067" height="743" alt="image" src="https://github.com/user-attachments/assets/11ebfd86-8a3e-4b61-b222-813ff3e20465" />


Se evidencia que nuestra tabla competidor_powerlifting tiene una totalidad de 8432 registros cargados.


<img width="1186" height="860" alt="image" src="https://github.com/user-attachments/assets/f5547c8d-7ff9-48f8-971b-88ba249caa96" />
Se evidencia el nombre de las columnas, su tipo de dato y una breve descripción de su contenido.


<img width="1620" height="890" alt="image" src="https://github.com/user-attachments/assets/f6f88fd7-f9b6-4b39-a37d-e2f36c119005" />

Podemos evidenciar como hacemos una consulta con filtrado a una tabla.
