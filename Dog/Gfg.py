class Gfg:
    def __init__(self, topic):
        self._topic = topic  # Store parameter value in instance variable

    def topic(self):
        print("Topic:", self._topic)  # Access the renamed variable

# Creating an instance of gfg
ins = Gfg("Python")

# Calling the topic method
ins.topic()
