import os
import subprocess

# Directorios
input_dir = r"C:\Users\nekos\OneDrive\Escritorio\MasOrange\originales\Set14_LR"
output_dir = r"C:\Users\nekos\OneDrive\Escritorio\MasOrange\Real-ESRGAN\scaled_set14_x4"

# Parámetros del comando
model = "RealESRGAN_x4plus"
scale_factor = 4.0  # Factor de escala
suffix = "_x4"

# Crear la carpeta de salida si no existe
os.makedirs(output_dir, exist_ok=True)

# Listar las imágenes en la carpeta
images = sorted(os.listdir(input_dir))  # Ordenar para procesarlas en orden
processed_count = 0

for image in images:
    # Procesar solo archivos con extensiones válidas
    if image.lower().endswith(('.jpg', '.jpeg', '.png')):
        # Ruta completa del archivo de entrada
        input_path = os.path.join(input_dir, image)

        # Generar nombre de archivo de salida
        base_name, ext = os.path.splitext(image)
        output_name = f"{base_name}{suffix}{ext}"
        output_path = os.path.join(output_dir, output_name)

        # Construir el comando
        command = [
            "python", "inference_realesrgan.py",
            "-n", model,
            "-i", input_path,
            "-o", output_dir,
            "--fp32",
            "--outscale", str(scale_factor)
        ]

        # Ejecutar el comando
        try:
            print(f"Procesando: {image} -> {output_name}")
            subprocess.run(command, check=True)
            processed_count += 1
        except subprocess.CalledProcessError as e:
            print(f"Error al procesar {image}: {e}")

        # Detener después de 44 imágenes
        if processed_count >= 14:
            print("Se han procesado las primeras 44 imágenes. Deteniendo...")
            break