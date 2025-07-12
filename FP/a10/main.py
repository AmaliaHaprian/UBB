from jproperties import Properties

from game import RandomStrategy, AI, SmartStrategy
from UI.gui import GUI
from UI.ui import UI
from validators.validator import Validator

properties=Properties()
with open('settings.properties','rb') as f:
    properties.load(f)
interface=properties['interface'].data
strat=properties['strategy'].data
board_size=int(properties['size'].data)
if __name__=="__main__":
    validator=Validator()
    if strat =="Random Strategy":
        strategy=RandomStrategy
    elif strat == "AI":
        strategy=AI
    elif strat == "Smart Strategy":
        strategy=SmartStrategy

    if interface=="ui":
        ui=UI(board_size, validator, strategy)
        ui.play()
    elif interface=="gui":
        gui=GUI(board_size, strategy)


