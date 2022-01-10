
from PIL import Image

word_matrix = Image.open("word_matrix.png")

mask = Image.open("mask.png")

#size of images

print("mask size: {}".format(mask.size))
print("matrix size: {}".format(word_matrix.size))

#calculate resize factors
w_matrix = word_matrix.size[0]
h_matrix = word_matrix.size[1]

resized_mask = mask.resize((w_matrix,h_matrix))

resized_mask.show()
word_matrix.show()


resized_mask.putalpha(100)

word_matrix.paste(resized_mask, box = (0,0), mask = resized_mask)






word_matrix.show()