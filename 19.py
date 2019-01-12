# http://www.pythonchallenge.com/pc/hex/bin.html
import email
import wave

email_content = open('assets/19-email.txt', 'rb').read().decode()

mail = email.message_from_string(email_content)
audio = mail.get_payload(0).get_payload(decode=True)
wav_file = 'assets/indian.wav'
wav_final_file = 'assets/indian_final.wav'
f = open(wav_file, 'wb')
f.write(audio)
f.close()

w_in = wave.open(wav_file, 'rb')
w_out = wave.open(wav_final_file, 'wb')

print(w_in.getnchannels())
print(w_in.getsampwidth())
print(w_in.getframerate())
w_out.setnchannels(w_in.getnchannels())
w_out.setsampwidth(w_in.getsampwidth()//2)
w_out.setframerate(w_in.getframerate()*2)
frames = w_in.readframes(w_in.getnframes())
wave.big_endiana = 1
w_out.writeframes(frames)

w_out.close()
w_in.close()

