run:
	python3 main.py
	
clean: 
	find . -maxdepth 4 -type d -name __pycache__ -prune -exec rm -r {} +

