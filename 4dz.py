import copy
from memory_profiler import profile
from timeit import default_timer



@profile
def fn_1():
	a = {i: i*i for i in range(10000)}
	b = copy.deepcopy(a)
	return b


from timeit import default_timer
import memory_profiler

def check(fn):
    
    def wrapper():
        memory = memory_profiler.memory_usage()
        start_time = default_timer()
        result = fn()
        finish_time = default_timer()
        memory_2 = memory_profiler.memory_usage()
        print(f'Память: {memory_2[0] - memory[0]}, скорость: {finish_time  - start_time}')
        return result
    return wrapper


@check
def fn():
    a = []
    for i in range(10000):
        yield a.append(i)




fn_1()
fn()

#взято из курса основ 3 урок 4 задание