#!/bin/bash
# ./run.sh Risk-Agents/angry_based_agent.py Risk-Agents/angry_based_agent.py 10

if [ $# -ne 3 ];
then
    echo "Arguments required: agent_1_path agent_2_path n_executions"
    exit
fi

# trap ctrl-c and call ctrl_c()
trap ctrl_c INT

function ctrl_c() {
    kill -9 ${pids[0]}
    kill -9 ${pids[1]}
    kill -9 ${pids[2]}
    echo "Killed ${pids[@]}" 
    exit
}

agent_1=$1
agent_2=$2

pids=()

echo "$agent_1 vs $agent_2" 

for i in $(seq "$3");
do
    echo "Executing $i..."
    python $agent_1 1 &
    pids[0]=$!
    python $agent_2 2 &
    pids[1]=$!
    python game.py &
    pids[2]=$!

    wait 
done

echo "$agent_2 vs $agent_1"

for i in $(seq "$3");
do
    echo "Executing $i..."
    python $agent_2 1 &
    pids[0]=$!
    python $agent_1 2 &
    pids[1]=$!
    python game.py &
    pids[2]=$!

    wait 
done

echo "$agent_1 vs $agent_1"

for i in $(seq "$3");
do
    echo "Executing $i..."
    python $agent_1 1 &
    pids[0]=$!
    python $agent_1 2 &
    pids[1]=$!
    python game.py &
    pids[2]=$!

    wait 
done

echo "$agent_2 vs $agent_2"

for i in $(seq "$3");
do
    echo "Executing $i..."
    python $agent_2 1 &
    pids[0]=$!
    python $agent_2 2 &
    pids[1]=$!
    python game.py &
    pids[2]=$!

    wait 
done

# None_type has not a type n_troops na função attack