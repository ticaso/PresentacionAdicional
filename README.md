# PresentacionAdicional
1. Para empezar, clonar este repositorio. Luego, en la raiz de la carpeta del repositorio levantar los contenedores de docker usando "docker-compose up -d".
2. Luego, abrir 4 terminales distintas.
3. Elegir que terminales van abrir los productores y cuáles los consumidores.
4. Para ejecutar el productor de rabbitmq escribir en la terminal "python rabbitmq_producer.py"
5. Para ejecutar el productor de kafka escribir en la terminal "python kafka-producer.py"
6. Para ejecutar el consumidor de rabbitmq escribir en la terminal "python rabbitmq_consumer.py"
7. Para ejecutar el consumidor de kafka escribir en la terminal "python kafka_consumer.py"

# Instrucciones para el orden de ejecución de consumidor y productor
1. Primero ejecutar el consumidor de la cola a probar
2. Ejecutar el productor de la cola a probar
