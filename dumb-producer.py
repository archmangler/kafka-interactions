from confluent_kafka import Producer

p = Producer( { 'bootstrap.servers': 'localhost:9092' } )

p.produce('yourtopic',key='hello',value='world')

p.flush(30)
