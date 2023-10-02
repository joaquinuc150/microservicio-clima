# microservicio-clima
Microservicio de Clima para la aplicación Chatbot Granja

## Como usar

El sistema se debe ejecutar en el siguiente orden:

- Crear network:
  
      docker network create farm


- Primero ejecutar el message_broker en la carpeta message_broker

      // Servicio RabbitMQ
      cd message_broker
      docker-compose up --build
  
- Luego, ejecutar los dos servicios, clima y usuario (usuario siendo un servicio simple que solo recibe eventos)

      // Servicio Clima
      docker-compose up --build

      // Servicio Usuarios
      cd service_users
      docker-compose up --build
