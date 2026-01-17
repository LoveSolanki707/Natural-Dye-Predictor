def generate_explanation(ingredient, placement):
    text = f"The {ingredient} releases natural pigments during boiling. "

    if placement == "center":
        text += "Central placement creates darker concentration."
    elif placement == "scattered":
        text += "Scattered placement creates organic eco-print patterns."
    elif placement == "border":
        text += "Border placement gives traditional textile aesthetics."

    text += " Color will soften after washing."

    return text
