# README #

ผมเองได้ทดลองเขียนโปรแกรมเพื่อควบคุมหลอดไฟ LED โดยที่ปุ่มกดเป็น Touch Screen ศึกษาและพัฒนาตามแนวทางขอเทคโนโลยี IoT ซึ่งตัว Touch Screen นั้นผมใช้ Raspberryp PI เป็นอุปกรณ์ Touch Screen เขียนด้วยภาษา Python ส่วนทางตัวควบคุมไฟ LED เป็น ESP32 ซึ่งเป็น Node MCU เป็นอุปกรณ์สำเร็จพร้อม WiFI ซึ่งจัดว่าอยู่ในตระกูล Adruino 
การสื่อสารใช้ Socket Program ระดับ Low Level API สื่อสารกันระหว่างภาษา Python กับภาษา C
https://www.youtube.com/watch?v=5cK3iBmE0Zs <== ท่านสามารถศึกษาดูตัวอย่างของผลการทดลองได้จากคลิปนี้

### What is this repository for? ###
เพื่อเก็บตัวอย่างโปรแกรม ที่ใช้สื่อสารระหว่างกัน โดยใช้เทคโนโลยี Socket Programming. ศึกษาเทคโนโลยีสื่อสารตรงระหว่างอุปกรณ์ 


### How do I get set up? ###
โปรแกรมนั้นจะประกอบด้วยอุปกรณ์สองส่วนคือ 
1. ESP32 ซึ่งเป็น NodeMCU มีอุปกรณ์ Wi-Fi ในตัว เป็น Wi-Fi ใน AP Mode ไม่พึ่งพาอาศัยตัวกลาง สื่อสารตรงกับอุปกรณ์ RaspberryPi
2. Raspberry PI ซึ่งเป็นระบบปฎิบัติการลีนุกซ์และต่อกับอุปกรณ์จอ Touch Screen 

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

ผู้พัฒนาโปรแกรมคือ นาย อวยชัย ไชยถา ประธานชมรมโอเพนซอร์สล้านนา ท่านสามารถติดต่อผู้พัฒนาได้ทางไลน์กลุ่มของชมรมโอเพนซอร์สล้านนา