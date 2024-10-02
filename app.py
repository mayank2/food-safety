import gradio as gr
import google.generativeai as genai
from PIL import Image

# Configure the Generative AI model
genai.configure(api_key="AIzaSyDGnI5mLA7HEz_Zl5gr38uYEQ81GlsGzkw")
model = genai.GenerativeModel("gemini-1.5-flash")


# Function to generate text based on the image
def gen_text(image):
    pil_image = Image.fromarray(image)
    questions = """1. Nutritional Analysis - Higher presence of nutrients desired in low qty (fats, sugar, sodium, calories)
                2. How processed and nutrient deficit is the product?
                3. Harmful Ingredients present
                4. If people follow certain diets, does it comply with it
                5. Is it diabetes/allergen friendly
                6. Are there any claims made by brands that could be misleading """
    response = model.generate_content(
        [
            "you are a govt organization whose job is to tell the food safety rating of a packaged product based on the ingredients written on this image.",
            pil_image,
            "based on the ingredients, just provide the answer to these questions in a proper question-anser format",
            questions,
        ]
    )
    response.resolve()
    return response.text


# Input image

# Example images
examples = [
    r"ingredient-1.jpg",
    r"ingredient-2.jpg",
]

img_input = gr.Image(label="Upload Ingredient Image")

# output_text = gr.Markdown(label="Packaged food analysis")

# Create Gradio Blocks interface with Markdown
with gr.Blocks() as demo:
    # Add a markdown heading at the top
    gr.Markdown(
        """
    # Food Safety Analysis Tool
    Upload an image of a packaged food product's ingredients, and the AI will provide you the health impact of that product.
    """
    )

    # Create the interface within the Blocks
    intf = gr.Interface(
        fn=gen_text,
        inputs=img_input,
        outputs=gr.Markdown(label="Packaged food analysis"),
        examples=examples,
    )
#     intf.launch(inline=False)

demo.launch(inline=False, share=True)
