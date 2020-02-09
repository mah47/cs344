from gps import gps

#problem specification: GPS cant solve problem but humans can
#problem includes: fire, water and ice
#solution: each element meets their demise
#ice beats water, fire beats ice, water beats fire
#ice loses against fire, water loses against ice, fire loses against water
#GPS fails to realize that without ice, the water cant freeze. Without fire, the ice wont melt
# without water the fire won't stop
problem ={
    "start1": ["fire", "water", "snow" ],
    "finish1": ["no fire", "no water", "no snow"],

    "ops": [
        {
            "action": "fire beats ice",
            "preconds": [
                "fire",
                "ice"
            ],

            "add": [
                "no ice"
            ],

            "delete": [
                "ice"
            ]
        },
        {
            "action": "ice beats water",
            "preconds": [
                "ice",
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
        }
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