import csv
import webbrowser
import time
import pyautogui

interval = 2
position = 1081,225
message="Automated"


# f = open('nums.csv','r')

# reader = csv.reader(f)

# tlf = []

# for row in reader:
#     try:
#         tlf = row
#         url = 'https://wa.me/{}?text={}'.format(tlf,message)
#         webbrowser.open(url)
#         time.sleep(3)
#         gui.click(position)
#         time.sleep(3)
#         gui.press('enter')
#         time.sleep(interval)



with open('nums.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    line_count = 0
    for row in csv_reader:
        tlf = ''
        tlf = tlf.join(row)
        tlf = tlf[1:]
        # if tlf != "lf_part":
        # tlf.replace('[','')
        # tlf.replace('+','')
        url = 'https://wa.me/{}?text={}'.format(tlf,message)
        # url = 'https://wa.me/34673574989?text=hola'
        # print(url)
        webbrowser.open(url)
        time.sleep(3)
        # gui.click(position)
        pyautogui.click(position)
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(interval)
        





# # numbers={917025674097, 919048525224}



# # for i in numbers:
# #  url = 'https://wa.me/{}?text={}'.format(i, message)
# #  webbrowser.open(url)
# #  time.sleep(3)
# #  gui.click(position)
# #  time.sleep(3)
# #  gui.press('enter')
# #  time.sleep(interval)