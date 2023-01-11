FROM golang:latest

WORKDIR /go/src/app

COPY . .

RUN go mod init

RUN go get github.com/streadway/amqp@latest

RUN go build -o main .

CMD ["./main"]
