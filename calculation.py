def calculate(weight, base_weight):
    weight-=base_weight
    max_iterations = 100 # to avoid an infinite loop
    iterations = 0
    discs = [25,20,15,10,5,2.5,1.25]
    resoult = {'1.25':0,'2.5':0,'5':0,'10':0,'15':0,'20':0,'25':0}
    while True:
        iterations+=1
        for i in discs:
            if weight>=i*2:
                weight-=i*2
                resoult[str(i)] += 1
                break
        if weight == 0:
            return resoult
        if iterations==max_iterations:
            break

def error_handler(weight, base_weight):
    try:
        weight = float(weight)
        base_weight = float(base_weight)
    except:
        return None
    else:
        return calculate(weight,base_weight)