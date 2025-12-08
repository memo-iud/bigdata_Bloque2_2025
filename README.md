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
---
###   📊 ACTIVIDAD 2

## 🧱 Diseño Schema del proyeco

<img width="1045" height="727" alt="catalogo" src="https://github.com/user-attachments/assets/c3dce495-c62b-45d6-af23-11b2743309d7" />

Se puede apresiar el Metastore, catalogo, el Schema, tablas, con sus atributos y tipo de dato.

--
## 🧠 Levantar un servidor en databricks

loqin en databricks, en el menu principal ingresamos a (compute) para crear una capacidad de computo (create compute), levantar un nodo de un servidor, (databricks runtime version) despliega una ventana emergente procedemos a darle un nombre,luego defino el tipo de cluster a levantar Standar o Machime learning

<img width="1065" height="868" alt="comp" src="https://github.com/user-attachments/assets/225a24f0-d885-4b58-9f87-535b08879b97" />

Standar que tenga Scala(el environment del servidor va ser java), recomendado escoger las que tienen LTS(Last Time Support)servidor de soporte largo.
ML(Machime learning) el cual tiene las librerias y todas las configuraciones de ML para procesamiento distribuido.

<img width="661" height="490" alt="MLpng" src="https://github.com/user-attachments/assets/943d0edf-3058-499d-bf6f-082f74323dff" />

el sistema proporciona 15GB de almacenamiento finalizamos con click en (Create Compute)

<img width="1286" height="251" alt="servidor" src="https://github.com/user-attachments/assets/d30d3846-bf02-4eb9-afc0-69bf56b760d2" />
--

## 📊 Se crea el Catalogo, Schema y tablas 

<img width="1303" height="787" alt="image" src="https://github.com/user-attachments/assets/6b3330ea-4576-4853-9174-d5bc11ead746" />

--
## 📥 Evidencia de carga de datos  

<img width="1310" height="759" alt="image" src="https://github.com/user-attachments/assets/0266b823-ee60-4ab8-84f1-b414c4f698d4" />

--
## 🧮 Show create table, describe table

<img width="1082" height="851" alt="image" src="https://github.com/user-attachments/assets/974bb4b0-de94-46ae-bcf1-6edc49638671" />

--

## 📊 select

<img width="1302" height="465" alt="image" src="https://github.com/user-attachments/assets/eb35bf77-08cf-4d42-a7bd-5e64fe38e191" />

--
## 🧾 insert into

<img width="1307" height="554" alt="image" src="https://github.com/user-attachments/assets/1ff80a11-8bea-492c-8903-9664e47dac5e" />

--
## 📌 select con filtro

<img width="1311" height="692" alt="image" src="https://github.com/user-attachments/assets/deaff1d3-95f2-463b-a3f5-83b6a9f79334" />

--
## 🧠 select from group by

<img width="1129" height="504" alt="image" src="https://github.com/user-attachments/assets/ff819629-bba6-4a04-bc51-1767700fb603" />

--
### ✅ Spark vs SQL

<img width="799" height="680" alt="image" src="https://github.com/user-attachments/assets/d9305f0a-b87b-4a23-98b6-05273643ab7a" />

###   📊 ACTIVIDAD 3

[![Ver video](https://img.shields.io/badge/Ver%20Video-Google%20Drive-blue?style=for-the-badge&logo=google-drive)](https://drive.google.com/file/d/1GT_f4G-h7qBL33IsmxbGrgJp9LfJ__b7/view?usp=drive_link)

## 🧱 Transformaciones de fecha

<img width="1013" height="829" alt="image" src="https://github.com/user-attachments/assets/e11312bb-b6fc-4dfb-917a-5e544b626592" />

<img width="712" height="800" alt="image" src="https://github.com/user-attachments/assets/3b459e81-77f6-480a-a842-70411bd1508d" />

<img width="1013" height="821" alt="image" src="https://github.com/user-attachments/assets/c672472e-cc51-44f0-8c2b-02f88a5e5fb9" />

## 🧮 Resumen Mensual

<img width="810" height="778" alt="image" src="https://github.com/user-attachments/assets/c8b5038d-0337-4591-abf6-1dfe06653339" />

## 📥 Limpiesa de datos

<img width="749" height="787" alt="image" src="https://github.com/user-attachments/assets/4a44876f-ad4e-4705-842a-81ef3febe8fe" />

<img width="1341" height="869" alt="image" src="https://github.com/user-attachments/assets/53f2adbd-ee20-4818-9b9c-a798c878139e" />


## 📊 Visualizacion Graficas en SQL
<img width="727" height="781" alt="image" src="https://github.com/user-attachments/assets/eb505840-7f7c-40bb-8e27-0edbe21a6b75" />

<img width="1884" height="768" alt="image" src="https://github.com/user-attachments/assets/526e0eed-2545-4dde-81e3-2f38badda343" />
<img width="1888" height="841" alt="image" src="https://github.com/user-attachments/assets/0deb7f57-07f8-4cf7-a4ab-c23aa9e3ca47" />

## 📊 Visualizacion con librerias 

<img width="1144" height="819" alt="image" src="https://github.com/user-attachments/assets/3956e3d2-21ad-48e2-ae46-7e903915e6bb" />

<img width="1227" height="759" alt="image" src="https://github.com/user-attachments/assets/9048827e-da62-49c8-b0b4-66b28d1b6ad4" />

<img width="1285" height="825" alt="image" src="https://github.com/user-attachments/assets/58c67ea0-baec-4cfc-a6f7-e8dcdbc60dbf" />

<img width="1193" height="774" alt="image" src="https://github.com/user-attachments/assets/b07b2041-83ae-4916-88ba-cf2e590cc6c2" />


## 🧠 Lenguaje de trabajo

<img width="1226" height="719" alt="image" src="https://github.com/user-attachments/assets/c7c935bb-f0bd-435d-b14a-4879dfff4b80" />

<img width="1293" height="850" alt="image" src="https://github.com/user-attachments/assets/28cbe619-62b9-4853-9bd9-57086262d95e" />














  

