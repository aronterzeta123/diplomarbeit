#!/usr/bin/python3
import cv2

class CompareImage(object):
#image_1_path=cv2.imread('harden.jpeg',0)
#image_2_path=cv2.imread('harden1.jpeg',0)
    def __init__(self,image_1_path, image_2_path):
        self.minimum_commutative_image_diff = 1
        self.image_1_path = 'harden.jpeg'
        #self.image_2_path = 'harden_isoj.jpeg'
        self.image_2_path = 'harden1.jpeg'
    def compare_image(self):
        image_1 = cv2.imread(self.image_1_path, 0)
        image_2 = cv2.imread(self.image_2_path, 0)
        commutative_image_diff = self.get_image_difference(image_1, image_2)

        if commutative_image_diff < self.minimum_commutative_image_diff:
            print ("Matched")
            return commutative_image_diff
        return 10000 #random failure value

    @staticmethod
    def get_image_difference(image_1, image_2):
        first_image_hist = cv2.calcHist([image_1], [0], None, [256], [0, 256])
        second_image_hist = cv2.calcHist([image_2], [0], None, [256], [0, 256])

        img_hist_diff = cv2.compareHist(first_image_hist, second_image_hist, cv2.HISTCMP_BHATTACHARYYA)
        img_template_probability_match = cv2.matchTemplate(first_image_hist, second_image_hist, cv2.TM_CCOEFF_NORMED)[0][0]
        img_template_diff = 1 - img_template_probability_match

        # taking only 10% of histogram diff, since it's less accurate than template method
        commutative_image_diff = (img_hist_diff / 10) + img_template_diff
        return commutative_image_diff

#compare_image = CompareImage('harden.jpeg','harden_isoj.jpeg')
compare_image = CompareImage('harden.jpeg','harden1.jpeg')
image_difference = compare_image.compare_image()
print (image_difference)
