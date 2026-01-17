import replicate

SDXL_VERSION = "2b017d8c7c2f7a7dbf6a1c71f8bdf3c1f9a7f92bb9e3b3a9cfa8f0c7e4f0f9c5"

def generate_image(prompt):
    output = replicate.run(
        f"stability-ai/sdxl:{SDXL_VERSION}",
        input={
            "prompt": prompt,
            "num_outputs": 1,
            "guidance_scale": 7.5,
            "num_inference_steps": 30
        }
    )
    return output[0]
