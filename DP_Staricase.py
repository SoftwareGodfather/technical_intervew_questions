def Recursive_StaircaseProblem(num_of_stairs, step_list):
    if num_of_stairs <= 1:
        return 1
    total = 0
    for step in step_list:
        sub = num_of_stairs - step
        if sub >= 0:
            total += Recursive_StaircaseProblem(sub, step_list)
    return total

def DP_StaircaseProblem(num_of_stairs, step_list, memResults):
    if num_of_stairs <= 1:
        return 1
    total = 0
    for step in step_list:
        sub = num_of_stairs - step
        if sub >= 0:
            if sub in memResults.keys():
                total += memResults[sub]
            else:
                total += DP_StaircaseProblem(sub, step_list, memResults)
    
    memResults[num_of_stairs] = total
    return total

########### STDOUT ###########

num_of_stairs = 30
step_list = {1,2}

print('Start Recursive_StaircaseProblem')
res = Recursive_StaircaseProblem(num_of_stairs, step_list)
print(res)

print('Start DP_StaircaseProblem')
memResults = dict()
res = DP_StaircaseProblem(num_of_stairs, step_list, memResults)
print(res)
