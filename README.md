##Sensor TMP

Idea muy simple que consiste en controlar la temperatura de una habitación.
La información se guardará bajo cierta lógica en una base de datos y servirá para dar información de interés, como medias, máximos y minimos, etc.

###Hardware:

Para ello la idea es usar una Raspberry Pi que haga de servidor web para poder ofrecer la información de forma muy simple. Además de esto enviará y recibirá información a y desde una placa arduino conectada a ella a través de cable USB que será la que tendrá el circuito del sensor y lo que este necesite y que tendrá cargado el programa que gestiona el sensor.

###Software:

Como es algo simple se usará un WSGI sencillo como webapp2 para montar la web y algunas librerías para hacerla bonita como UIKit y HichCharts.js . Los datos serán almacenados en una base de datos MongoDB (por ganas de probarla) y arduino ejecutará un Sketch muy simple.
Además de esto la Raspberry Pi estará configurada para tener siempre una IP fina en lugar de pedirla al DHCP del router y se configurará un script de arranque para que no haya que iniciar ningún servicio si temporalmente se desconecte (haciéndola plug and play). Junto a esto se configurará un servicio de dominio como no-ip para que pueda ser accesible desde fuera desde la misma dirección o nombre de dominio independientemente de los cambios del router.
