# microservicio-clima
Microservicio de Clima para la aplicación Chatbot Granja

## Como usar

El sistema se debe ejecutar en el siguiente orden:

- Primero ejecutar el message_broker en la carpeta message_broker

      docker-compose -p message_broker up --build
  
- Luego, ejecutar los dos servicios, clima y usuario (usuario siendo un servicio simple que solo recibe eventos)

      docker-compose -p service_users up --build
      docker-compose up --build
