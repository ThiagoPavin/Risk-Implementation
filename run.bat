:loop
	start "agent1" /min python Risk-Agents\monte_carlo_agent.py 1
	start "agent2" /min python Risk-Agents\cluster_based_agent.py 2
	timeout 1
	start "game" /min python game.py

	timeout 15
	
	taskkill /FI "WindowTitle eq agent1*" /T /F
	taskkill /FI "WindowTitle eq agent2*" /T /F
	taskkill /FI "WindowTitle eq game*" /T /F
goto loop
	
pause