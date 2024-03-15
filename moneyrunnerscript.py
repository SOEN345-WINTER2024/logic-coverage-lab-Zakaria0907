# Imports the monkeyrunner modules used by this program.
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object.
device = MonkeyRunner.waitForConnection()

# Installs the Android package. Notice that this method returns a boolean, so you can test
# whether the installation worked.
device.installPackage('myproject/bin/MyCalculatorApp.apk')

# Sets a variable with the package's internal name. Adjust for your calculator app.
package = 'com.example.android.calculatorapp'

# Sets a variable with the name of an Activity in the package.
activity = 'com.example.android.calculatorapp.MainActivity'

# Sets the name of the component to start.
runComponent = package + '/' + activity

# Runs the component.
device.startActivity(component=runComponent)

# Initialize data structures for tracking coverage
nodes = set()
edges = set()
edge_pairs = set()
previous_action = None

# A list to represent the sequence of user interactions
# Each interaction is a tuple ('action_type', 'details')
# Example: [('press', 'KEYCODE_1'), ('press', 'KEYCODE_PLUS'), ...]
actions = [
    ('press', 'KEYCODE_1'),
    ('press', 'KEYCODE_PLUS'),
    ('press', 'KEYCODE_2'),
    ('press', 'KEYCODE_EQUALS')
]

# Function to execute actions and update coverage data
def execute_action(action, details):
    global previous_action
    # Execute the action
    if action == 'press':
        device.press(details, MonkeyDevice.DOWN_AND_UP)
    
    # Update nodes and edges
    nodes.add(details)
    if previous_action is not None:
        edge = (previous_action, details)
        edges.add(edge)
        
        # Update edge-pairs if there's a previous edge
        if len(edges) > 1:
            last_edge = list(edges)[-2]  # Get the second last edge added
            edge_pair = (last_edge, edge)
            edge_pairs.add(edge_pair)
    
    previous_action = details

# Loop through actions to simulate user interaction
for action, details in actions:
    execute_action(action, details)
    MonkeyRunner.sleep(1)  # Delay to simulate real user interaction

# Coverage metrics
node_coverage = len(nodes)
edge_coverage = len(edges)
edge_pair_coverage = len(edge_pairs)

# Output coverage information
print(f"Node Coverage: {node_coverage}")
print(f"Edge Coverage: {edge_coverage}")
print(f"Edge-Pair Coverage: {edge_pair_coverage}")

# Take a screenshot at the end of the test
result = device.takeSnapshot()
result.writeToFile('myproject/finalState.png', 'png')
