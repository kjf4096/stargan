import paddlehub as hub

stargan = hub.Module(name="stargan_celeba")

test_img_path = ["boy.jpg"]

style_list=[["Black_Hair"], ["Blond_Hair"], ["Brown_Hair"], ["Female"], ["Male"], ["Aged"] ]
trans_attr = ["Black_Hair"]
print(trans_attr)
for trans_attr in style_list:
        # set input dict
    print(trans_attr)
    input_dict = {"image": test_img_path, "style": trans_attr}

    # execute predict and print the result
    results = stargan.generate(data=input_dict)
    print(results)