import amqp from './node_modules/amqplib/channel_api';

export function startSending() {
    return amqp.connect('amqp://rabbitmq')
        .then((connection) => {
            return connection.createChannel()
        }).then((channel) => {
            const queue = 'task_queue';
            for(let i = 0; i < 10; i ++) {
                let msg = `${i} function .....`;
    
                channel.assertExchange('logs1', 'fanout', {
                    durable: false
                });
                channel.publish('logs1', '', Buffer.from(msg));
                console.log(" [x] Sent '%s'", msg);
            }
        });
}

startSending()