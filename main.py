import torch
from diffusers import FluxPipeline
import csv

def create_image(promot, name):
    torch.cuda.empty_cache()

    # Load the model with bfloat16 precision
    pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-schnell", torch_dtype=torch.bfloat16)
    pipe.enable_sequential_cpu_offload()
    pipe.vae.enable_slicing()
    pipe.vae.enable_tiling()
    pipe.to(torch.float16)


    # Smaller resolution to reduce memory usage
    height, width = 512, 512  # Reducing resolution to reduce memory footprint

    prompt = promot
    out = pipe(
        prompt=prompt,
        guidance_scale=2.5,
        height=height,
        width=width,
        num_inference_steps=3,
    ).images[0]

    torch.cuda.empty_cache()  # Clear cache after generating the image

    # Save the image
    image_name = name + ".png"
    out.save(image_name)

# Path to your CSV file
csv_file = 'myPromo.csv'

# Open the CSV file and read the data
with open(csv_file, mode='r') as file:
    reader = csv.reader(file)
    
    # Skip the header if your CSV has one
    next(reader, None)  # Uncomment this if there is a header row
    i=1
    # Iterate over each row
    for row in reader:
        # name = row[0]  # Column A (first column)
        name=f"FluxE{i}"
        promot = row[0]  # Column B (second column)
        i+=1
        
        # Call the function with values from the row
        create_image(promot, name)