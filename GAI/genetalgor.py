import numpy as np
from geneticalgorithm import geneticalgorithm


# variables[0] type_city;
# variables[1] type_limo;
# variables[2] type_combi;
# variables[3] type_xdrive;

# variables[4] fuel_4;
# variables[5] fuel_6;
# variables[6] fuel_10;

# variables[7] skibag;
# variables[8] four_wheel;
# variables[9] pdc;
def f(variables):
    constraints = np.array([False] * 7)

    # exactly one type has to be true
    constraints[0] = (variables[0] + variables[1] + variables[2] + variables[3] == 1)

    # exactly one fuel type has to be true
    constraints[1] = (variables[4] + variables[5] + variables[6] == 1)

    # %c1
    # constraint four_wheel = 1 -> type_xdrive = 1; implication is equivalent to: not(A) or B <==> A -> B 
    constraints[2] = (not(variables[8]) or variables[3])

    # %c2
    # constraint skibag = 1 -> type_city = 0;
    constraints[3] = (not(variables[7]) or not(variables[0]))

    # %c3
    # constraint fuel_4 = 1 -> type_city = 1;
    constraints[4] = (not(variables[4]) or (variables[0]))

    # %c4
    # constraint fuel_6 = 1 -> type_xdrive = 0;
    constraints[5] = (not(variables[5]) or not(variables[3]))

    # %c5
    # constraint type_city = 1 -> fuel_10 = 0;
    constraints[6] = (not(variables[0]) or not(variables[6]))

    return -np.sum(constraints)

task_e_model=geneticalgorithm(function=f,dimension=10,variable_type='bool')
variables = task_e_model.run()

print(task_e_model.best_variable[0], "type_city\n",
task_e_model.best_variable[1], "type_limo\n",
task_e_model.best_variable[2], "type_combi\n",
task_e_model.best_variable[3], "type_xdrive\n",
task_e_model.best_variable[4], "fuel_4\n",
task_e_model.best_variable[5], "fuel_6\n",
task_e_model.best_variable[6], "fuel_10\n",
task_e_model.best_variable[7], "skibag\n",
task_e_model.best_variable[8], "four_wheel\n",
task_e_model.best_variable[9], "pdc")
