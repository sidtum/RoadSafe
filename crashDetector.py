import cv2
import numpy as np
import os
from keras.models import model_from_json
from twilio.rest import Client
import time
from datetime import datetime
from datetime import date
import webPage

def callAuthorities():
    account_sid = "AC6b5b683619d323ac86c1c9798ecc6a6f"
    auth_token = "505bab243a6166f5acf2d0a52ebc0a2c"

    client = Client(account_sid, auth_token)

    call = client.calls.create(
        to = "+16146870884",
        from_ = "+18448882951",
        twiml='<Response><Say>A vehicular accident has been detected on the feed.</Say></Response>')

    print(call.sid)

first = True 

classes = ['Accident Occuring', "No Accident Detected"]

json_file = open("model.json", "r")
model = model_from_json(json_file.read())

table_rows = []
webPage.generatePage(table_rows)

model.load_weights('model_weights.h5')
model.make_predict_function()

font = cv2.FONT_HERSHEY_SIMPLEX

start = time.time()

crash_confidence_threshold = 86.5
alert_authorities_threshold = 94

video = cv2.VideoCapture("/Users/siddarth/Library/Mobile Documents/com~apple~CloudDocs/RoadSafe/CarCrashCompV9.MP4")
while True:
    ret, frame = video.read()
    if ret is False:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(gray_frame, (250, 250))

    probability = model.predict(roi[np.newaxis, :, :])
    prediction = classes[np.argmax(probability)]
    rounded_prob = round(probability[0][0] * 100, 2)

    if(rounded_prob > crash_confidence_threshold):
        cv2.rectangle(frame, (0, 0), (600, 40), (0, 0, 0), -1)
        cv2.putText(frame, "Potential Accident Detected " + str(rounded_prob) + "%", (20, 30), font, 1, (255, 255, 0), 2)
        if(rounded_prob > alert_authorities_threshold):
            end = time.time()
            if(end - start > 15 or first):
                first = False
                print("Calling")
                callAuthorities()
                now = datetime.now()
                today = date.today()
                currentDate = today.strftime("%B %d, %Y")
                currentTime = now.strftime("%H:%M:%S %p")
                outputTime = currentDate + ' at ' + currentTime
                
                table_rows.append(f'<tr><td>{"Vehicle Accident"}</td><td>{outputTime}</td></tr>')

                webPage.generatePage(table_rows)
                start = time.time()
    else:
        cv2.rectangle(frame, (0, 0), (375, 40), (0, 0, 0), -1)
        cv2.putText(frame, "No Accident Detected", (20, 30), font, 1, (255, 255, 0), 2)

    cv2.imshow('RoadSafe Accident Detection', frame)
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

json_file.close()
video.release()
cv2.destroyAllWindows()
