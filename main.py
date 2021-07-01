from typing import Text
from playsound import playsound
import gtts
import csv,os


# def audio_generator(source_address, destination_address, via_address, platform_number, train_number, train_name):
#     SPEECH = f" कृप्या ध्यान दीजिये,    {source_address}  से चलकर,   {via_address}  के रस्ते,  {destination_address} को जाने वाली, गाडी संख्या {' '.join(str(train_number))}, {train_name}, कुछ ही समय में प्लेटफार्म संख्या {platform_number} पर, आ रही है"
#     audio_file = gtts.gTTS(SPEECH, lang='hi', slow=False)
#     audio_file.save("audio.mp3")
#     return True


def speakHindi(source_address, destination_address,via_address, platform_number, train_number, train_name):
    gtts.gTTS(f"   {source_address}  से चलकर,   {via_address}  के रस्ते,  {destination_address} को जाने वाली, ", lang='hi', slow=False).save("generated_info1.mp3")
    gtts.gTTS(f"  {' '.join(str(train_number))}, {train_name}, ", lang='hi', slow=False).save("generated_info2.mp3")
    gtts.gTTS(f"  {platform_number}, ", lang='hi', slow=False).save("generated_info3.mp3")
    playsound("0startup.mp3")
    playsound("generated_info1.mp3")
    playsound("1gadiNumber.mp3")
    playsound("generated_info2.mp3")
    playsound("2ThodiHiDerMe.mp3")
    playsound("3platformNumber.mp3")
    playsound("generated_info3.mp3")
    playsound("4parAayegi.mp3")
    os.remove("generated_info1.mp3")
    os.remove("generated_info2.mp3")
    os.remove("generated_info3.mp3")




trains = [['29873', 'Chennai Express', 'jabalpur', 'mumbai', 'kota', '9'], ['56682', 'Purushottam Express', 'tatanagar', 'puri', 'vijaywada', '6'], ['79925', 'Amaravati Express', 'howrah', 'vasco', 'raipur', '3'], ['33964', 'punjab Mail', 'Secunderabad', 'delhi', 'sealdah', '7'], ['46653', 'Rajdhani Express', 'Dhanbad', 'lucknow', 'tirupati', '4'], ['75536', 'Tea Garden Express', 'Bangalore', 'balughat', 'new delhi', '6'], ['73497', 'Tippu Express', 'Gwalior', 'bhubneshwar', 'mysore', '2'], ['55798', 'Udyan Express', 'dadar', 'vishakhapatnam', '', '3'], ['12795', 'Veer Bhumi Chittaurgarh Express', 'mathura', 'hydrabad', 'firojpur', '2']]

with open("train_on_station.csv", "a", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(trains)
os.system("start excel train_on_station.csv")

with open("train_on_station.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        sAdd = row[2]
        via = row[4]
        dAdd = row[3]
        train_no = str(row[0])
        train_name = row[1]
        platform = int(row[5])
        speakHindi(sAdd,dAdd,via,platform,train_no,train_name)
        # audio_generator(sAdd,dAdd,via,platform,train_no,train_name)


