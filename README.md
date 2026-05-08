# Watermarks removal using DALL-E

1. To edit, we must provide local images.
2. _Inpainting_ requires square (1:1) PNG images with an Alpha channel.
3. Where the mask is Transparent (Alpha=0), the original pixels remain.
4. Where the mask is Opaque (Alpha=255), the model "removes" and fills the area.
