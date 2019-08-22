FROM openjdk:14-jdk-alpine3.10


RUN mkdir -p /opt/myapp
WORKDIR /opt/myapp

COPY . .
ENV JAVA_OPTS="-Xms128m -Xmx256m"

CMD ["java", "-jar","springboot-futureprogram-web.jar"]
