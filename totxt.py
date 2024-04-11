
from PIL import Image
import pytesseract as tess
import os


class Totxt:
    def __init__(self):
        tess.pytesseract.tesseract_cmd ="C:/Program Files/Tesseract-OCR/tesseract.exe"

        self.caseImgPath = r'C:\Users\Tamer\Desktop\projeler\AI\Interview_Killer\Screen_Shots\shot1.png'
        self.codeImgPath = r'C:\Users\Tamer\Desktop\projeler\AI\Interview_Killer\Screen_Shots\shot2.png'

        self.shot1Exist = os.path.exists(self.caseImgPath)
        self.shot2Exist = os.path.exists(self.codeImgPath)

    def caseToText(self): 
        caseImg = Image.open(self.caseImgPath)
        caseText = "Solve this question, ignore all other irrelevant text " + tess.image_to_string(caseImg)
        return caseText

    def codeToText(self):
        codeImg = Image.open(self.codeImgPath)
        codeText = "       " + tess.image_to_string(codeImg)
        return codeText

    def merge_texts(self):
        mergedText = self.caseToText() + " " + self.codeToText()
        return mergedText

    def no_shot(self):
        return "no screenshot found"
    
    def imgToTxt(self):
        if self.shot1Exist and self.shot2Exist:
            return self.merge_texts()
        
        elif self.shot1Exist and not self.shot2Exist:
            return self.caseToText()
        
        elif not self.shot1Exist and self.shot2Exist:
            return self.codeToText()
        
        else:
            return self.no_shot()



        

        





    
    









