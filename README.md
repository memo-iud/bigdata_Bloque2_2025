## 👥 Autores  
- **Guillermo León Loaiza Mesa**  
- **Robinson Marín Morales**

📘 **Materia:** Big Data  
🏫 **Institución:** IUDigital de Antioquia  
👨‍🏫 **Docente:** Andrés Felipe Callejas Jaramillo  
☁️ **Plataforma:** Databricks (Free Edition)

---

## 🔗 Recursos y enlaces  
📂 **Dataset (Kaggle):** [Powerlifting Database](https://www.kaggle.com/datasets/dansbecker/powerlifting-database?resource=download)  
🧠 **Workspace Databricks:** [Notebook en Databricks](https://dbc-2c10204f-96c0.cloud.databricks.com/editor/notebooks/1545643167989994?o=3299575563036138#command/6792127430818917)

---

## 🧠 Descripción del proyecto  

Problema (El Desafío): La empresa Romen de Powerlifting enfrenta un desafío de datos descentralizados. Actualmente, sus registros históricos de eventos (meets.csv) y los resultados detallados de los atletas (openpowerlifting.csv) existen en archivos CSV planos, aislados y propensos a la desnormalización y errores de consistencia, impidiendo un análisis estratégico.

Necesidad (Qué): Construir un pipeline de datos (ETL) que ingiera estas fuentes dispares, las limpie, las estructure según un modelo relacional (E-R) y las centralice en un Data Warehouse escalable en la nube (Databricks) para el uso de Romen.

Para quién: Dirigido al equipo de Ingeniería de Datos de Romen (que construye el pipeline) y a sus Analistas de Estrategia (que necesitan una fuente única de verdad para consumir los datos).

Por qué requiere Big Data: El desafío no es el volumen de datos, sino la complejidad de la ingeniería requerida:

📈 Ingesta y Transformación: Se requiere un proceso para leer, limpiar, estandarizar y transformar los datos de los CSV.

🔗 Modelado Relacional: Los datos deben cargarse en tablas distintas (encuentro, competidor_powerlifting) respetando las llaves primarias y foráneas del modelo E-R.

☁️ Almacenamiento Escalable: Se utiliza una plataforma de Big Data (Databricks) para construir un almacén que pueda escalar a millones de registros y habilitar análisis complejos.

---

## 📊 Variables relevantes  

| Tipo | Variables | Descripción |
|------|------------|-------------|
| 🆔 Identificación | `IdEncuentro`, `rutaEncuentro` | Identifican cada evento |
| 🏛️ Categórica | `Federación` | Federación que organiza el evento |
| ⏰ Temporal | `Fecha` | Fecha del encuentro |
| 🌎 Geográficas | `PaisEncuentro`, `EstadoEncuentro`, `CiudadEncuentro` | Ubicación del evento |
| 🏋️ Descriptiva | `NombreReunion` | Nombre del encuentro deportivo |

---

## 🧱 Modelo Entidad-Relación  

📌 **Modelo ER:**  
<img width="914" height="719" alt="Captura de pantalla 2025-11-08 a las 8 26 42 p m" src="https://github.com/user-attachments/assets/10727165-3312-476b-9a7c-1c937c607de9" />

El modelo se centra en tres tablas:

encuentro: Almacena la información de cada evento (federación, fecha, ubicación). Su llave primaria (PK) es IdEncuentro.

competidor_powerlifting: Almacena un registro único para cada atleta (nombre, sexo, edad). Su llave primaria (PK) es IdCompetidor.

encuentro_competidor_powerlifting: Esta es la tabla de unión que implementa la relación Muchos a Muchos (N:M). Conecta a un competidor con un encuentro usando dos llaves foráneas (FKs): IdEncuentro y IdCompetidor. Esta tabla también almacena los resultados específicos de esa participación (levantamientos, total, puesto).


## 📥 Evidencia de carga de datos  

<img width="1437" height="676" alt="Carga 1" src="https://github.com/user-attachments/assets/0d5f8358-57dc-423e-a708-0ab6944d209f" />

<img width="1469" height="723" alt="Carga 2" src="https://github.com/user-attachments/assets/113f87d8-4177-4714-921f-84cc374076d1" />

<img width="1279" height="614" alt="Carga 3" src="https://github.com/user-attachments/assets/534a8aeb-51f6-44a9-a614-a25387c779eb" />

---

## 🧾 Consultas SQL (Queries)

<img width="1067" height="743" alt="Consultas" src="https://github.com/user-attachments/assets/11ebfd86-8a3e-4b61-b222-813ff3e20465" />

📈 Se evidencia que la tbl_competidor_powerlifting contiene un total de **8,482 registros cargados**.

---

## 🧮 Descripción de la estructura de datos

<img width="1186" height="860" alt="Estructura columnas" src="https://github.com/user-attachments/assets/f5547c8d-7ff9-48f8-971b-88ba249caa96" />  
🔹 Se muestra el esquema de la tbl_competidor_powerlifting, detallando nombres de columnas, tipos de datos y si aceptan nulos.
---

## 📊 Consulta con filtro

<img width="1620" height="890" alt="Resultados" src="https://github.com/user-attachments/assets/f6f88fd7-f9b6-4b39-a37d-e2f36c119005" />
🔹 se realiza consulta a la tbl_competidor_powerlifting con el filtro a la federacion de nombre APA, dando como resultado todos los datos solicitados

---
### ✅ Conclusión
Se completó con éxito el pipeline de ingesta de datos. Los archivos CSV de origen se han extraído, transformado y cargado en un Data Warehouse estructurado en Databricks, basado en el modelo Entidad-Relación.

Las tablas encuentro, competidor_powerlifting, están pobladas y operativas, como lo demuestran las consultas SQL. El proyecto establece una base de datos robusta (fuente única de verdad), que ahora está lista para ser consumida por herramientas de analítica y Business Intelligence para la toma de decisiones estratégicas.
