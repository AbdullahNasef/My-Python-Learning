import pandas as pd
import webbrowser as web
import pyautogui as pg
import time


# 1.Download ____data
file_path = 'name_atomate' \
    '.xlsx'

df = pd.read_excel(file_path)

print("Sending process started")
time.sleep(5)

for index, row in df.iterrows():
    phone = str(row['Phone'])
    name = row['Name']
    Grade = row['Grade']
    Absence = row['Absence']


    message = (
        f"السلام عليكم ورحمة الله، {name}  \n"
        f"درجتك في الامتحان هي: ({Grade}) \n"
        f"و عدد أيام الغياب: ({Absence}) \n"
        f"بالتوفيق إن شاء الله. \n"
        f"هذه رسالة تجريبية مؤتمتة. "
    )


    # 2.protocol__open the conversation
    phone_url = f"whatsapp://send?phone={phone}&text={message}"
    web.open(phone_url)


    # 3_timing
    if index == 0:
        time.sleep(10)
    else:
        time.sleep(6)


    # 4 pressing Enter to send
    pg.press('enter')
    print(f"[{index + 1}] Sent to: ({phone})")

    

    time.sleep(2)
print("\n messages have been successfully sent!")
