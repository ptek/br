from datetime import datetime
from message_broker import MessageBroker, Message, MessageType

def example_subscriber(message: Message):
    print(f"Received message on channel '{message.channel}':")
    print(f"  Timestamp: {message.timestamp}")
    print(f"  Conversation ID: {message.conversation_id}")
    print(f"  Type: {message.message_type.name}")
    print(f"  Content: {message.content}")
    print()

def main():
    broker = MessageBroker()

    # Subscribe to channels
    broker.subscribe("general", example_subscriber)
    broker.subscribe("alerts", example_subscriber)

    # Publish messages
    broker.publish(Message(
        timestamp=datetime.now(),
        channel="general",
        conversation_id="conv1",
        message_type=MessageType.INFO,
        content="Hello, world!"
    ))

    broker.publish(Message(
        timestamp=datetime.now(),
        channel="alerts",
        conversation_id="conv2",
        message_type=MessageType.WARNING,
        content="System resources running low"
    ))

    broker.publish(Message(
        timestamp=datetime.now(),
        channel="general",
        conversation_id="conv1",
        message_type=MessageType.DEBUG,
        content="Debugging information"
    ))

if __name__ == "__main__":
    main()
