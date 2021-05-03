problem_name=$1
g++-10 -std=gnu++17 ${problem_name}.cpp -o ${problem_name}.out
./${problem_name}.out
