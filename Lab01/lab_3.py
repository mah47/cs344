from gps import gps

#Marcos Hernandez
#CS344


#problem specification: GPS cant solve problem but humans can
#problem includes: fire, water and earth
#solution: each element meets their demise (element weakness)
#earth beats water, water beats fire, fire and water can't beat earth
#GPS fails to realize fire and water doesn't beat earth. Fire and water are not compatible
#if you change the order in finish1 then the GPS will encounter a solution, but in this case the GPS fails to meet conditions
#decided to make an elemental weakness GPS based on games I played
problem ={
    "start1": ["earth", "water", "fire" ],
    "finish1": ["no water", "no fire", "earth"],

    "ops": [
        {
            "action": "earth beats water",
            "preconds": [
                "earth",
                "water"
            ],

            "add": [
                "no water"
            ],

            "delete": [
                "water"
            ]
        },
        {
            "action": "water beats fire",
            "preconds": [
                "water",
                "fire"
            ],

            "add": [
                "no fire"
            ],

            "delete": [
                "fire"
            ]
        },

    ]
}

#
def main():
    start = problem['start1']
    finish = problem['finish1']
    ops = problem['ops']
    actionSequence = gps(start, finish, ops)
    if actionSequence is None:
        print("plan failure...")
        return
    for action in actionSequence:
        print(action)

if __name__ == '__main__':
    main()