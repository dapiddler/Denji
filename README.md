# Denji
https://www.piddlerintheroot.com/project-denji/
#### Origin: Japan. Meaning: One who has electromagnetic powers

## Synopsis

A 17DOF Biped Robot that utilizes a Raspberry Pi Zero and Maestro Servo Controller. Designed with a microservices architecture in mind.

## Code Example

```python
class Step(Resource):
    def get(self):
        servo.runScriptSub(2)
        print("step")
        return {'postion': 'forward step'}
api.add_resource(Step, '/step')
```

## Motivation

Create a biped robot platform that utilizes the python programming language that can be easily built upon:
1. API
2. Wifi/Voice Control
3. Camera (future)
4. Integrate Gyroscope/Reinforcment Learning (future)

## Installation
1. Configure Serial Interface for RPI Zero and upload "denji_maestro_script.txt" to servo controller: https://www.youtube.com/watch?v=6EGSsxPzXO0

2. Clone Repo to RPI

3. Install Dependencies

```
pip install requirements.txt
```

4. Edit denji_client.py with RPI hostname

5. Run denji_server.py on RPI and denji.client.py on remote computer (LAN)

## Maestro Library
https://github.com/FRC4564/Maestro

## Usage

Keyboard controls:
* W - Take a Step
* C - Crouch
* S - Neutral Standing Position
* T - Taunt


## License

MIT




