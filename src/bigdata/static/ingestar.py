import os
import json
import zipfile
from pathlib import Path
from typing import List, Any

import numpy as np
import pandas as pd
import kagglehub


class Ingestar:
    """
    Clase Ingestar
    --------------
    Esta clase se encarga de:
    - Generar datos sintéticos (útil para pruebas).
    - Guardar y leer datos en formatos comunes (JSON, TXT, XLSX).
    - Descargar datasets desde Kaggle usando kagglehub.
    - Localizar y extraer archivos descargados (.zip).
    - Cargar datos reales del dataset (CSV o XLSX) en un DataFrame de pandas.
    - Realizar operaciones de limpieza simples.

    Está pensada para soportar el flujo de tu proyecto:
    Kaggle (.xlsx/.zip/.csv) -> DataFrame -> SQLite -> análisis.
    """

    def __init__(self):
        # Permite que ciertas funciones usen información contextual como nombres de columnas
        self.column_names: List[str] = []

    # ============================
    # 1. Utilidades de validación
    # ============================

    def _validar_limites(self, inferior, superior):
        """
        Valida que los límites sean numéricos y que inferior < superior.
        """
        if not (isinstance(inferior, (int, float)) and isinstance(superior, (int, float))):
            raise ValueError("Los límites deben ser numéricos (int o float).")
        if inferior >= superior:
            raise ValueError("El límite inferior debe ser menor que el límite superior.")

    # =====================================
    # 2. Generación de datos sintéticos
    # =====================================

    def generar_datos_completos(self, n, categorias, x=4, limite_inferior=1, limite_superior=100):
        """
        Genera un dataset sintético con columnas categóricas, enteras, decimales y reales.

        Parámetros:
        -----------
        n : int
            Número de filas a generar.
        categorias : list[str]
            Lista de categorías posibles para la columna categórica.
        x : int
            Número de columnas que se van a usar (máximo 4).
        limite_inferior : int/float
            Límite inferior para los enteros aleatorios.
        limite_superior : int/float
            Límite superior para los enteros aleatorios.

        Retorna:
        --------
        np.ndarray
            Datos generados (matriz).
        """
        self._validar_limites(limite_inferior, limite_superior)

        columna_categorica = np.random.choice(categorias, size=n)
        columna_enteros = np.random.randint(int(limite_inferior), int(limite_superior), size=n)
        columna_decimales = np.random.uniform(0, 1, size=n)
        columna_reales = np.random.normal(0, 1, size=n)

        columnas = [columna_categorica, columna_enteros, columna_decimales, columna_reales]
        nombres = ["categoria", "enteros", "decimal", "reales"]

        data = np.column_stack(columnas[:x])
        self.column_names = nombres[:x]
        return data

    # ==================================================
    # 3. Escritura y lectura en JSON / TXT / XLSX local
    # ==================================================

    def escribir_datos(self, data, tipo='json', ruta='datos_salida'):
        """
        Escribe 'data' en disco en formato JSON, TXT o XLSX.
        """
        Path(ruta).parent.mkdir(parents=True, exist_ok=True)

        if tipo == 'json':
            with open(f"{ruta}.json", 'w') as f:
                json.dump(data.tolist(), f)

        elif tipo == 'txt':
            np.savetxt(f"{ruta}.txt", data, fmt='%s')

        elif tipo == 'xlsx':
            columnas = getattr(self, 'column_names', [f"col_{i}" for i in range(data.shape[1])])
            df = pd.DataFrame(data, columns=columnas)
            df.to_excel(f"{ruta}.xlsx", index=False)

        else:
            raise ValueError("tipo debe ser 'json', 'txt' o 'xlsx'.")

    def leer_datos(self, tipo='json', ruta='datos_salida'):
        """
        Lee datos previamente guardados en JSON/TXT/XLSX.
        Devuelve numpy.array (para txt/json) o np.array derivado de DataFrame (xlsx).
        """
        if tipo == 'json':
            with open(f"{ruta}.json", 'r') as f:
                return np.array(json.load(f))

        elif tipo == 'txt':
            return np.loadtxt(f"{ruta}.txt", dtype=str)

        elif tipo == 'xlsx':
            df = pd.read_excel(f"{ruta}.xlsx")
            return df.to_numpy()

        else:
            raise ValueError("tipo debe ser 'json', 'txt' o 'xlsx'.")

    # ==================================================
    # 4. Lectura directa de un CSV local con separador ;
    # ==================================================

    def leer_ruta(self, ruta=""):
        """
        Lee un CSV local usando separador ';' y lo devuelve como DataFrame.
        (Esta función es útil si ya tienes un CSV limpio).
        """
        if not ruta:
            raise ValueError("Debes proporcionar la ruta del archivo CSV.")
        df = pd.read_csv(ruta, delimiter=";")
        return df

    # ============================================
    # 5. Descarga de dataset desde Kaggle (kagglehub)
    # ============================================

    def download_dataset_zip(self, kaggle_ref: str = ""):
        """
        Descarga un dataset de Kaggle usando kagglehub y devuelve
        la ruta local donde quedó el dataset.

        Ejemplo:
        --------
        dataset_path = ingestar.download_dataset_zip(
            "jlgrego/apartamentos-venda-na-cidade-de-sao-paulo-sp"
        )

        NOTA:
        kagglehub.dataset_download() por lo general descarga y descomprime
        en una carpeta tipo:
        ~/.cache/kagglehub/datasets/<user>/<dataset>/versions/<n>
        """
        if kaggle_ref == "":
            raise ValueError("Debes pasar el nombre del dataset de Kaggle, ej. 'usuario/dataset'.")

        print("Descargando dataset desde Kaggle...")
        dataset_path = kagglehub.dataset_download(kaggle_ref)
        print("Ruta al dataset:", dataset_path)
        return dataset_path

    # =========================================================
    # 6. Localización / extracción de archivos en la carpeta
    #    descargada desde Kaggle
    # =========================================================

    def extract_zip_files(self, dataset_path: str):
        """
        Revisa la carpeta descargada desde Kaggle y decide qué devolver.

        Casos soportados:
        - Si hay .zip  -> lo extrae a una subcarpeta y retorna esa subcarpeta.
        - Si hay .csv  -> retorna dataset_path.
        - Si hay .xlsx -> retorna dataset_path.  (CASO DE APARTAMENTOS SP)
        - Si no hay nada utilizable -> FileNotFoundError.
        """
        if not os.path.exists(dataset_path):
            raise FileNotFoundError(f"La ruta {dataset_path} no existe.")

        archivos = os.listdir(dataset_path)
        print("Archivos encontrados en la descarga:", archivos)

        # 1. Buscar .zip
        zip_files = [f for f in archivos if f.endswith(".zip")]
        if zip_files:
            zip_file = os.path.join(dataset_path, zip_files[0])
            extract_dir = os.path.join(dataset_path, "extracted")
            os.makedirs(extract_dir, exist_ok=True)
            print(f"Extrayendo {zip_file} en {extract_dir}...")
            with zipfile.ZipFile(zip_file, "r") as z:
                z.extractall(extract_dir)
            return extract_dir

        # 2. Buscar .csv
        csv_files = [f for f in archivos if f.endswith(".csv")]
        if csv_files:
            print("Se detectaron archivos CSV directamente en la carpeta descargada.")
            return dataset_path

        # 3. Buscar .xlsx
        xlsx_files = [f for f in archivos if f.endswith(".xlsx")]
        if xlsx_files:
            print("Se detectaron archivos XLSX directamente en la carpeta descargada.")
            return dataset_path

        # 4. Nada utilizable
        raise FileNotFoundError(
            "No se encontró ningún archivo .zip, .csv ni .xlsx en la ruta del dataset"
        )

    # =========================================================
    # 7. Cargar el contenido de la carpeta en un DataFrame
    # =========================================================

    def load_dataset_as_dataframe(self, data_dir: str) -> pd.DataFrame:
        """
        Lee todos los archivos CSV o XLSX en la carpeta `data_dir`
        y los concatena en un único DataFrame.

        Este método soporta:
        - CSVs separados por coma (usa pandas.read_csv).
        - Excels .xlsx (usa pandas.read_excel).

        Retorna:
        --------
        pandas.DataFrame
            Un DataFrame con todos los datos combinados.
        """
        if not os.path.exists(data_dir):
            raise FileNotFoundError(f"La ruta {data_dir} no existe.")

        archivos = os.listdir(data_dir)

        csv_files = [f for f in archivos if f.endswith('.csv')]
        xlsx_files = [f for f in archivos if f.endswith('.xlsx')]

        dfs = []

        # Cargar CSVs
        for file in csv_files:
            file_path = os.path.join(data_dir, file)
            print(f"Leyendo CSV {file_path} ...")
            try:
                df_temp = pd.read_csv(file_path, encoding="latin1")
            except Exception as e:
                print(f"Error al leer {file_path}: {e}")
                continue
            dfs.append(df_temp)

        # Cargar Excels
        for file in xlsx_files:
            file_path = os.path.join(data_dir, file)
            print(f"Leyendo Excel {file_path} ...")
            try:
                df_temp = pd.read_excel(file_path)
            except Exception as e:
                print(f"Error al leer {file_path}: {e}")
                continue
            dfs.append(df_temp)

        if not dfs:
            raise FileNotFoundError(
                "No se encontraron archivos CSV ni XLSX en el directorio proporcionado"
            )

        df_final = pd.concat(dfs, ignore_index=True)
        print("✅ Dataset cargado correctamente en DataFrame.")
        return df_final

    # =========================================================
    # 8. Limpieza y transformación básica
    # =========================================================

    def columna_regex(self, df_datos=pd.DataFrame(), reg=r"", columna="", n_columnas=[]):
        """
        Aplica una expresión regular sobre una columna de texto y extrae grupos
        en nuevas columnas.

        Ejemplo:
        --------
        df_nuevo = ingestar.columna_regex(
            df_datos=df_original,
            reg=r"(\\d+)-(\\d+)",
            columna="rango",
            n_columnas=["min", "max"]
        )
        """
        df = df_datos.copy()
        df[n_columnas] = df[columna].str.extract(reg).astype(int)
        return df

    def limpieza_nan_null(self, df_datos=pd.DataFrame(), name_col="", reemplezar=""):
        """
        Reemplaza valores nulos en una columna específica por un valor fijo.

        Imprime el conteo de nulos antes y después para dejar trazabilidad.
        """
        if name_col not in df_datos.columns:
            raise ValueError(f"La columna '{name_col}' no existe en el DataFrame.")

        nulos_antes = df_datos[name_col].isnull().sum()
        if nulos_antes > 0:
            df = df_datos.copy()
            df[name_col] = df[name_col].fillna(reemplezar)
            nulos_despues = df[name_col].isnull().sum()
            print(
                "cantidad antes {}/{}  despues {}/{}".format(
                    nulos_antes, len(df_datos), nulos_despues, len(df)
                )
            )
            return df

        print("no hay nulos en la columna indicada")
        return df_datos
