# Netflix Data Visor

Un programa en Python que lee tus datos de visualización y facturación de Netflix y te muestra estadísticas interesantes. Creado para CS50P de Harvard.

## Qué Hace

Netflix te permite descargar todos tus datos — cada serie que has visto, cada dólar que has gastado. Pero los archivos son solo CSVs sin procesar. Este programa los hace legibles.

Elegís un perfil (o todos), y después seleccionás una opción del menú:

1. **Total Gastado** — cuánto has pagado desde que te uniste. Pregunta si querés convertir a PYG.
2. **Series Más Vistas** — top 5 series ordenadas por tiempo de visualización.
3. **Películas Más Vistas** — lo mismo, pero para películas.
4. **Tiempo Total Visto** — todas tus horas combinadas en un solo número.
5. **Costo Por Hora** — total gastado dividido por total de horas.

Automáticamente omite trailers, hooks y vistas previas de autoplay para que tu tiempo real de visualización no se infle.

## Cómo Obtener Tus Datos de Netflix

1. Netflix → Cuenta → Descargar tu información personal
2. Esperá el correo (normalmente menos de un día)
3. Descargá y descomprimí el archivo
4. Vas a obtener una carpeta con un nombre como `1343059170`
5. Dentro, el programa usa dos carpetas:
      CONTENT_INTERACTION/ViewingActivity.csv
      PAYMENT_AND_BILLING/BillingHistory.csv

## Cómo Ejecutar

```bash
pip install -r requirements.txt
python project.py C:\Users\you\Downloads\1343059170
```

O simplemente python project.py y escribí la ruta cuando te la pida.

## Archivos

   project.py — el programa completo. Menú, funciones de análisis, todo.
   test_project.py — tests para las funciones principales (pendiente).
   requirements.txt — las dos bibliotecas necesarias: pandas y requests.

## Datos de Muestra

La carpeta `sample_data/` contiene datos falsos de ejemplo. Probalos con:

```bash
python project.py sample_data
```