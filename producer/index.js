import amqp from './node_modules/amqplib/channel_api';
import fs from 'fs';

function throwData(data, i, channel) {
    setTimeout(() => {
        console.log(data[i])
        channel.sendToQueue('mobilityData', new Buffer(data[i]));
        throwData(data, ++i, channel)
    }, 1000)
}

export function startSending() {
    return amqp.connect('amqp://rabbitmq')
        .then((connection) => {
            return connection.createChannel()
        }).then((channel) => {
            const q = 'mobilityData';
            channel.assertQueue(q, { durable: false });

            let data = fs.readFileSync("./data/test.csv", {encoding: 'utf8'})
            data = data.split('\n')
            console.log(data.length)
            throwData(data, 1, channel)
        });
}

startSending()
