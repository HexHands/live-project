from PIL import Image, ImageDraw, ImageFont

def create_thumbnail(loves, favs, views):
    # Create a new image with the specified size and background color
    img = Image.new('RGB', (480, 360), color=(20, 21, 22))

    # Create a draw object to add text to the image
    draw = ImageDraw.Draw(img)

    # Set emoji and text size
    emoji_size = 50
    text_size = 40

    # Load the font and set its size
    font = ImageFont.truetype("seguiemj.ttf", text_size)

    # Define the emoji symbols and their positions
    love_emoji = "♥"
    fav_emoji = "⭐"
    view_emoji = "👀"

    y_offset = 100
    line_spacing = 70
    padding = 15
    box_margin = 10
    box_radius = 15

    # Helper function to draw centered text with a rounded background box
    def draw_centered_text_with_box(draw, text, y, font, fill, box_fill):
        text_width, text_height = draw.textsize(text, font=font)
        x = (img.width - text_width) // 2
        draw.rounded_rectangle([x - box_margin, y - box_margin, x + text_width + box_margin, y + text_height + box_margin], box_radius, fill=box_fill)
        draw.text((x, y), text, font=font, fill=fill)

    # Draw the emojis and the corresponding text
    draw_centered_text_with_box(draw, f"{love_emoji} Loves: {loves}", y_offset, font, (255, 255, 255), (93, 173, 226))
    draw_centered_text_with_box(draw, f"{fav_emoji} Favs: {favs}", y_offset + line_spacing, font, (255, 255, 255), (93, 173, 226))
    draw_centered_text_with_box(draw, f"{view_emoji} Views: {views}", y_offset + 2 * line_spacing, font, (255, 255, 255), (93, 173, 226))

    # Save the image as a PNG file
    img.save("thumbnail.png")

# Example usage
create_thumbnail(100, 50, 1000)
