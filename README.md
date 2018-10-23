# Bot

Main class utility for [lunhg/WebWhatsapp-Wrapper](https://www.github.com/lunhg/WebWhatsapp-Wrapper)

# Download

```
$ git clone https://github.com/lunhg/WebWhatsapp-Wrapper-bot <path-to-clone>
```

# Usage

Create a class that implements this repo


```python
import sys
import os
import json
sys.path.append('<path-to-lunhg/WebWhatsapp-Wrapper-bot>')
import bot

# Implement a abstract bot
class Whatsapp(bot.Bot):

  def __init__(self, **kwargs):
    super(Foo, self).__init__(**kwargs)
    ...
    
  # A simple implementation of setup
  # loaded form configuration readed by a json file
  def setup(self):
    super.setup([ARGS])
    ...
    
  # A simple implementation of run with 0.1 seconds
  # between a call and another call, with
  # implementation of handle methods of logger plugin
  def run(self, handles=[]):
    ...
    super.run(frameTime=0.1, callbacks=handles)
    

if __name__ is '__main__':
  foobarbaz = Whatsapp(client='firefox', )
  
  # TODO build a config and a handle functions
  ...
  foobarbaz.setup(data)
  ...
  foobarbaz.run(handles=[])
```
