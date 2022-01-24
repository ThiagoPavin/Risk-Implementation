:loop
	start "agent1" /min python Risk-Agents\monte_carlo_agent.py 1
	start "agent2" /min python Risk-Agents\cluster_based_agent.py 2
	timeout 1
	start "game" /min python game.py montecarlo_vs_cluster.txt
	
	timeout 20

	taskkill /FI "WindowTitle eq agent1*" /T /F
	taskkill /FI "WindowTitle eq agent2*" /T /F
	taskkill /FI "WindowTitle eq game*" /T /F
goto loop

FOR /L %%i in (0,1,35) DO (
	start "agent1" /min python Risk-Agents\monte_carlo_agent.py 1
	timeout 1
	start "agent2" /min python Risk-Agents\angry_based_agent.py 2
	timeout 1
	start "game" /W /min python game.py montecarlo_vs_angry.txt

	timeout 5

	taskkill /FI "WindowTitle eq agent1*" /T /F
	taskkill /FI "WindowTitle eq agent2*" /T /F
	taskkill /FI "WindowTitle eq game*" /T /F
) 

FOR /L %%i in (0,1,50) DO (
	start "agent1" /min python Risk-Agents\random_agent.py 1
	start "agent2" /min python Risk-Agents\monte_carlo_agent.py 2
	timeout 1
	start "game" /W /min python game.py random_vs_montecarlo.txt
 	
	timeout 5

	taskkill /FI "WindowTitle eq agent1*" /T /F
	taskkill /FI "WindowTitle eq agent2*" /T /F
	taskkill /FI "WindowTitle eq game*" /T /F
) 

FOR /L %%i in (0,1,50) DO (
	start "agent1" /min python Risk-Agents\monte_carlo_agent.py 1
	start "agent2" /min python Risk-Agents\random_agent.py 2
	timeout 1
	start "game" /W /min python game.py montecarlo_vs_random.txt

	timeout 5

	taskkill /FI "WindowTitle eq agent1*" /T /F
	taskkill /FI "WindowTitle eq agent2*" /T /F
	taskkill /FI "WindowTitle eq game*" /T /F
)

FOR /L %%i in (0,1,50) DO (
	start "agent1" /min python Risk-Agents\angry_based_agent.py 1
	start "agent2" /min python Risk-Agents\random_agent.py 2
	timeout 1
	start "game" /W /min python game.py angry_vs_random.txt

	timeout 5

	taskkill /FI "WindowTitle eq agent1*" /T /F
	taskkill /FI "WindowTitle eq agent2*" /T /F
	taskkill /FI "WindowTitle eq game*" /T /F
) 

FOR /L %%i in (0,1,50) DO (
	start "agent1" /min python Risk-Agents\random_agent.py 1
	start "agent2" /min python Risk-Agents\angry_based_agent.py 2
	timeout 1
	start "game" /W /min python game.py random_vs_angry.txt

	timeout 5

	taskkill /FI "WindowTitle eq agent1*" /T /F
	taskkill /FI "WindowTitle eq agent2*" /T /F
	taskkill /FI "WindowTitle eq game*" /T /F
)

FOR /L %%i in (0,1,50) DO (
	start "agent1" /min python Risk-Agents\random_agent.py 1
	start "agent2" /min python Risk-Agents\angry_based_agent.py 2
	timeout 1
	start "game" /W /min python game.py random_vs_random.txt

	timeout 5

	taskkill /FI "WindowTitle eq agent1*" /T /F
	taskkill /FI "WindowTitle eq agent2*" /T /F
	taskkill /FI "WindowTitle eq game*" /T /F
) 
	
pause