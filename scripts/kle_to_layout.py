import json

###
# Exmaple: keyboard_layout.json
# [
# ["0,0","0,1","0,2","0,3","0,4","0,5","0,6","0,7","0,8","0,9","0,10","0,11","0,12",{w: 2},"0,13",{x: 0.5},"0,14","0,15"],
# [{w:1.5},"1,0","1,1","1,2","1,3","1,4","1,5","1,6","1,7","1,8","1,9","1,10","1,11","1,12",{w:1.5},"1,13",{x:0.5},"1,14","1,15"],
# [{w:1.75},"2,0","2,1","2,2","2,3","2,4","2,5","2,6","2,7","2,8","2,9","2,10","2,11",{w:2.25},"2,12"],
# [{w:2.25},"3,0","3,1","3,2","3,3","3,4","3,5","3,6","3,7","3,8","3,9","3,10",{w:2.75},"3,11",{x:0.5},"3,12"],
# [{w:1.25},"4,0",{w:1.25},"4,1",{w:1.25},"4,2",{w:6.25},"4,3",{w:1.25},"4,4",{w:1.25},"4,5",{w:1.25},"4,6",{x:0.75},"4,7","4,8","4,9"]
# ]
###

# Load JSON data from a file
with open("output.json", "r") as file:
    data = json.load(file)


output = []
width = 0
for row_idx, row in enumerate(data):
    col_idx = 0
    x_sum = 0
    for key in row:
        if isinstance(key, dict):
            width = key.get("w", 0)
            continue
        else:
            # Default width and position
            key_width = 1
            key_x = 0
            key_a = 1
            x_width = 1

        #
        # # Calculate the positions for each column of the key
        for col in range(int(float(key_width))):
            if width:
                x_width = width

            obj = {"matrix": [row_idx, col_idx + col], "x": x_sum + col, "y": row_idx}

            if width:
                obj["w"] = width
                width = 0

            output.append(obj)
        col_idx += int(float(key_width))
        x_sum += x_width


print(json.dumps(output))
