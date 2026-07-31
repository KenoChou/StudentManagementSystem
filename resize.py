from PIL import Image

img = Image.open("plane.png")

# 缩小到 80×80
img = img.resize((80,80))

img.save("plane_small.png")

print("完成")