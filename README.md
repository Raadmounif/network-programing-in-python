
# network programing in python

how to do tcp/udp client/ server
Using Python Socket Module: Making simple Echo Client/ Server
• The client read message from user input and send it to the server
• the server receives the message, print it, and echo it back to client
• the client repeats sending and receiving until user input=='exit'
• when server receives exit msg from client it closes the current
client socket, and wait for new client connection
ملخص عمل البرنامج :
سيقوم الclient بتحديد ال  port number وال ip address للسيرفر المراد الاتصال به ,فان لم ينجح العنوان سيطلب من الclient إعادة ادخال عنوان جديد بدل من فشل البرنامح وذلك باستخدام try/except الشكل (4) ,وان كان صحيحا سيتم انشاء الاتصال والطلب من الclient  كتابة شيئ ما للسيرفر وسيطبع السيرفر ما قاله الclient ويرد عليه بنفس الكلمه,وكلمة Exit هي مفتاح الخروج من جلسة الاتصال وسيتم اعلام الclient  بهذا التفصيل
