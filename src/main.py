import open3d as o3d
import os
import cv2

def load_images_from_folder(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            img_path = os.path.join(folder_path, filename)
            img = cv2.imread(img_path)
            if img is not None:
                images.append(img)
    return images

# Specify the folder containing the images
folder_path = "./photos"


# Load images (you need to implement this part)
images = load_images_from_folder(folder_path)

# Create a reconstruction pipeline
reconstruction = o3d.pipelines.integration.MultiFrameTSDFVolume()

# Add images to the reconstruction pipeline
for img in images:
    reconstruction.integrate(img)

# Extract the reconstructed surface
mesh = reconstruction.extract_triangle_mesh()

# Visualize the reconstructed surface
o3d.visualization.draw_geometries([mesh])