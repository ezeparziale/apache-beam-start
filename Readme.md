# Ejemplo de pipeline Apache Beam

## Pasos

Crear ambiente
1. Clonar repo 

```
git clone https://github.com/ezeparziale/beam-start.git .
```

2. Crear ambiente
```
python -m venv beam_example
```

3. Activar ambiente
```
./beam_example/scripts/activate # Windows
```

4. Instalar requerimientos
```
pip install -r requirements.txt
```

5. Ejecutar
```
python main.py --input "data\the_raven_poe.txt" --output "outputs/prueba.txt" --n 1000 --runner DirectRunner
```

El main_reload.py es una version reducida del pipeline
```
python main_reload.py --input "data\the_raven_poe.txt" --output "outputs/prueba.txt" --n 1000 --runner DirectRunner
```

</br>

### Parametros

--input: ruta del archivo de entrada  
--ouput: ruta del archivo de salida  
-n: cantidad de palabras a mostrar  

</br>

# Ejemplos
En la carpeta examples estan todos las funciones para los pipelines de beam.

</br>

# Fuente de libros
https://www.gutenberg.org/cache/epub/17192/pg17192.txt
https://www.gutenberg.org/files/58221/58221-0.txt

