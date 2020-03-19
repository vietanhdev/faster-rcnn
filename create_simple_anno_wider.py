'''
Create simple annotations for WIDERFace dataset
Please download WIDERFace dataset and extract in following structure
+ data
___+ WIDER2015
______+ wider_face_split
______+ WIDER_test
______+ WIDER_train
______+ WIDER_val
'''


OUTPUT_FILE = "widerface.txt"
outF = open(OUTPUT_FILE, "w")

for sub_dataset in ["train", "val"]:
    anno_file = "./data/WIDER2015/wider_face_split/wider_face_{}_bbx_gt.txt".format(sub_dataset)

    # Open WIDER annotation file and process
    with open(anno_file) as fp:

        img_file = fp.readline()[:-1]
        while img_file:
            img_path = "./data/WIDER2015/WIDER_{}/images/{}".format(sub_dataset, img_file)
            n_objects = int(fp.readline())
            for i in range(n_objects):
                object_info = fp.readline().split()
                x1 = int(object_info[0])
                y1 = int(object_info[1])
                width = int(object_info[2])
                height = int(object_info[3])
                x2 = x1 + width
                y2 = y1 + height

                # Write line to output file
                outF.write("{},{},{},{},{},face".format(img_path, x1, y1, x2, y2))
                outF.write("\n")

            # Read a new image file
            img_file = fp.readline()[:-1]


# Close output file
outF.close()
