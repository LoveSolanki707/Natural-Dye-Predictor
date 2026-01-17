import replicate

def generate_image(prompt):
    output = replicate.run(
        "stability-ai/stable-diffusion",
        input={
            "prompt": prompt,
            "num_outputs": 1,
            "guidance_scale": 7.5,
            "num_inference_steps": 30
        }
    )
    return output[0]  # URL of generated image
