import pyAgrum as gum
import pyAgrum.lib.image as gumimage

# IInfluence model implementation
model = gum.InfluenceDiagram()

# Add a decision node for cheat 1
cheat_1 = gum.LabelizedVariable('Cheat 1', 'Cheat 1', 2)
cheat_1.changeLabel(0, 'false')
cheat_1.changeLabel(1, 'true')
model.addDecisionNode(cheat_1)

# Add a decision node for cheat 2
cheat_2 = gum.LabelizedVariable('Cheat 2', 'Cheat 2', 2)
cheat_2.changeLabel(0, 'false')
cheat_2.changeLabel(1, 'true')
model.addDecisionNode(cheat_2)

# Add a chance node for result of trouble 1
result = gum.LabelizedVariable('Trouble 1', 'Trouble 1', 2)
result.changeLabel(0, 'false')
result.changeLabel(1, 'true')
model.addChanceNode(result)

# Add a chance node for result of trouble 2
result = gum.LabelizedVariable('Trouble 2', 'Trouble 2', 2)
result.changeLabel(0, 'false')
result.changeLabel(1, 'true')
model.addChanceNode(result)

# Add a chance node for result of watched
result = gum.LabelizedVariable('Watched', 'Watched', 2)
result.changeLabel(0, 'false')
result.changeLabel(1, 'true')
model.addChanceNode(result)

# Add an utility node
utility = gum.LabelizedVariable('Utility', 'Utility', 1)
model.addUtilityNode(utility)





