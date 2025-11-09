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

**Problema:**  
La empresa **Romen de Powerlifting**, dedicada a entender el panorama competitivo global, busca planificar su expansión y estrategia de eventos deportivos.

**Necesidad (Qué):**  
Identificar **patrones y tendencias** en la organización de competiciones de powerlifting. En particular:  
- 🌍 **Dónde:** países o estados con más eventos.  
- 🗓️ **Cuándo:** evolución temporal y estacionalidad.  
- 🏆 **Quién:** federaciones con mayor dominio regional.

**Para quién:**  
Dirigido a **directores de estrategia**, **organizadores de eventos** y **analistas de mercado deportivo**.

**Por qué requiere analítica:**  
El dataset contiene miles de registros (más de **8.400 eventos**). El análisis manual sería inviable, por lo que se requiere analítica de datos para:  
- 📈 Agregar datos por año y analizar tendencias de crecimiento.  
- 🗺️ Visualizar zonas geográficas con mayor actividad competitiva.  
- 🏅 Analizar participación y dominio de las federaciones en cada región.

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


---

## 📥 Evidencia de carga de datos  

<img width="1437" height="676" alt="Carga 1" src="https://github.com/user-attachments/assets/0d5f8358-57dc-423e-a708-0ab6944d209f" />

<img width="1469" height="723" alt="Carga 2" src="https://github.com/user-attachments/assets/113f87d8-4177-4714-921f-84cc374076d1" />

<img width="1279" height="614" alt="Carga 3" src="https://github.com/user-attachments/assets/534a8aeb-51f6-44a9-a614-a25387c779eb" />

---

## 🧾 Consultas SQL (Queries)

<img width="1067" height="743" alt="Consultas" src="https://github.com/user-attachments/assets/11ebfd86-8a3e-4b61-b222-813ff3e20465" />

📈 Se evidencia que la tabla **`competidor_powerlifting`** contiene un total de **8,432 registros cargados**.

---

## 🧮 Descripción de la estructura de datos

<img width="1186" height="860" alt="Estructura columnas" src="https://github.com/user-attachments/assets/f5547c8d-7ff9-48f8-971b-88ba249caa96" />  
🔹 Se muestran los nombres de las columnas, tipos de datos y descripción de cada campo.

---

## 📊 Resultados adicionales

<img width="1620" height="890" alt="Resultados" src="https://github.com/user-attachments/assets/f6f88fd7-f9b6-4b39-a37d-e2f36c119005" />

---

### ✅ Conclusión
El análisis permite comprender el comportamiento global del powerlifting a través del tiempo y regiones, apoyando la toma de decisiones estratégicas para la expansión de la empresa **Romen**.


Podemos evidenciar como hacemos una consulta con filtrado a una tabla.
