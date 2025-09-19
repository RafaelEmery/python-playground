daily-python-project:
	@echo "Running $(file)... ⚡️"
	python playground/daily_python_projects/$(file)

list-daily-python-projects:
	@echo "Listing all files... 🗂️"
	@find playground/daily_python_projects/ -type f