class Solution:
    def solveEquation(self, equation: str) -> str:
        NO = "No solution"
        INF = "Infinite solutions"
        dct = {
            "left":0,
            "right":0,
            "x1":0,
            "x2":0,
            "running":0,
            "neg":False,
            "after":False
        }
        def eva(x):
            if dct["neg"]:
                dct["running"] *= -1
            if dct["after"]:
                if x:
                    if dct["running"] != 0:
                        dct["x2"] += dct["running"]
                    elif dct["neg"]:
                        dct["x2"] -= 1
                    else:
                        dct["x2"] += 1
                else:
                    dct["right"] += dct["running"]
            else:
                if x:
                    if dct["running"] != 0:
                        dct["x1"] += dct["running"]
                    elif dct["neg"]:
                        dct["x1"] -= 1
                    else:
                        dct["x1"] += 1
                else:
                    dct["left"] += dct["running"]
            dct["running"] = 0
            dct["neg"] = False
            return
        for i in range(len(equation)):
            if equation[i] == "=":
                eva(False)
                dct["after"] = True
            elif equation[i] == "-":
                eva(False)
                dct["neg"] = True
            elif equation[i] == "+":
                eva(False)
            elif equation[i] == "x":
                if not (i > 0 and equation[i-1] == "0"):
                    eva(True)
            else:
                dct["running"] *= 10
                dct["running"] += int(equation[i])
        eva(False)
        dct["right"] -= dct["left"]
        dct["x1"] -= dct["x2"]
        if dct["right"] == 0:
            if dct["x1"] == 0:
                return INF
            return "x=0"
        if dct["x1"] == 0:
            return NO
        return "x=" + str(dct["right"] // dct["x1"])
