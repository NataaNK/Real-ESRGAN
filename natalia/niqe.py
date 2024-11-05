import os
from skimage import io, img_as_float
import skimage
from skimage.metrics import niqe
import matplotlib.pyplot as plt

def calculate_niqe_for_images(original_folder, superres_folder):
    # Diccionario para almacenar resultados
    results = {}

    # Recorrer cada imagen en la carpeta de resoluciones originales
    for filename in os.listdir(original_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # Cargar imagen original
            original_path = os.path.join(original_folder, filename)
            original_img = img_as_float(io.imread(original_path))

            # Cargar imagen superescalada
            superres_filename = filename.replace('.', '_out.')
            superres_path = os.path.join(superres_folder, superres_filename)
            if os.path.exists(superres_path):
                superres_img = img_as_float(io.imread(superres_path))

                # Calcular NIQE para la imagen superescalada
                niqe_score = niqe(superres_img)

                # Guardar el resultado con el tamaño de la imagen original
                original_resolution = f"{original_img.shape[1]}x{original_img.shape[0]}"
                results[original_resolution] = niqe_score
                print(f"Resolución original: {original_resolution}, NIQE: {niqe_score:.2f}")

    return results

def plot_niqe_results(results):
    # Ordenar por resolución original (ancho)
    resolutions = sorted(results.keys(), key=lambda x: int(x.split('x')[0]))
    niqe_scores = [results[res] for res in resolutions]

    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(resolutions, niqe_scores, marker='o')
    plt.xlabel('Resolución Original')
    plt.ylabel('NIQE de la Imagen Superescalada')
    plt.title('Calidad de Superresolución en función de la Resolución Original')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()

# Rutas de las carpetas
original_folder = 'C:/Users/nekos/OneDrive/Escritorio/MasOrange/Real-ESRGAN/natalia/resized'
superres_folder = 'C:/Users/nekos/OneDrive/Escritorio/MasOrange/Real-ESRGAN/natalia/scaled'

# Calcular NIQE y graficar resultados
results = calculate_niqe_for_images(original_folder, superres_folder)
plot_niqe_results(results)
