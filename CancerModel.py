import numpy as np
import pytesseract
from PIL import Image
import cv2
import re
import pickle
import os
import warnings
from termcolor import colored


pytesseract.pytesseract.tesseract_cmd = r"D:\Software Setups\Tesseract-OCR\tesseract.exe"
warnings.filterwarnings('ignore')

ImagePath1 = "D:\IT\Hackathon\Impulse\Prediction\Breast Cancer Prediction\Images\LabReport.png"
ImagePath2 = "D:\IT\Hackathon\Impulse\Prediction\Breast Cancer Prediction\Images\LabReport1.png"
ImagePath3 = "D: \IT\Hackathon\Impulse\ML Frontend\Test1.png"


def get_string(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    # cv2.imwrite("removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite("thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open("thres.png"))

    os.remove("thres.png")

    return result


def Predict(ImagePath1):
    result = get_string(ImagePath1)

    result = result.split("\n")
    print(result)
    final = []

    final = result[-29:]
    # for sentence in result:
    #     pattern = ".* : (.*)"
    #     output = re.search(pattern, sentence)
    #     if output:
    #         final.append(output.group(1))

    print()
    # name = final[0]
    # age = final[1]
    # sex = final[2]
    # reportID = final[3]

    # final = final[:-29]
    # final = final[2:]
    print(final)
    print("\n\n\n")

    # print("Name : ", name, "\nAge : ", age, "\nSex : ", sex)
    print()
    print("Report final resuls :- \n", final)

    with open("Models/BreastCancer", "rb") as f:
        randomForest = pickle.load(f)

    pred = randomForest.predict([final])
    print(pred)
    if pred[0]:
        print()
        print(colored("The cell is Malignant i.e its cancerus cell", "red"))
        return 1
    else:
        print()
        print(colored("The cell is Benign i.e the patient is safe", "green"))
        return 0


if __name__ == '__main__':
    # Predict("Test2.png")
    pass
