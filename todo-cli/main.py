import click # type: ignore # Import the click module
import json # Import the json module
import os # Import the os module

TODO_FILE ="todo.json" # Define the path to the todo.json file

def load_todos(): # Define the load_todos function
    if not os.path.exists(TODO_FILE): # If the todo.json file does not exist
        return [] # Return an empty list
    with open(os.path.expanduser(TODO_FILE), "r") as f: # Open the todo.json file in read mode
        return json.load(f) # Return the contents of the todo.json file

def save_todos(todos): # Define the save_todos function
    with open(os.path.expanduser(TODO_FILE), "w") as f: # Open the todo.json file in write mode
        json.dump(todos, f,indent=4) # Write the todos list to the todo.json file

# buildin decorater
@click.group() # Define a click group
def cli():
    """Simple todo manager""" # Print a message
    pass

# buildin decorater
@click.command() # Define a click command
@click.argument("task") # Define a click argument
def add(task):
    """Add a new task to the list"""
    tasks=load_todos() # Load the todos list
    tasks.append({"task":task, "done":False})
    save_todos(tasks) # Save the todos list

    click.echo(f"Task '{task}' added to the list succesfully") # Print a message



@click.command() # Define a click command
def list():
    """List all tasks"""
    tasks = load_todos()
    if not tasks:
        click.echo("No tasks")
        return
    for i, task in enumerate(tasks, 1): # Loop over the tasks list
        status = "✔" if task["done"] else "❌ "
        click.echo(f"{i}.  {task['task']} {status}") # Print the task



@click.command() # Define a click command
@click.argument("task_number", type=int) # Define a click argument
def done(task_number): # Define the done function
    """Mark a task as done"""
    tasks = load_todos()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_todos(tasks)
        click.echo(f"Task {task_number} marked as done")
    else:
        click.echo("Invalid task number")

@click.command() # Define a click command
@click.argument("task_number", type=int) # Define a click argument
def delete(task_number):
    """Delete a task"""
    tasks = load_todos()
    if 0 < task_number <= len(tasks):
        del_task = tasks.pop(task_number - 1)
        save_todos(tasks)
        click.echo(f"Task '{del_task['task']}' deleted")
    else:
        click.echo("Invalid task number")
        
cli.add_command(delete) # Add the delete command to the click group
cli.add_command(list) # Add the list command to the click group
cli.add_command(done) # Add the done command to the click group
cli.add_command(add) # Add the add command to the click group

if __name__ == "__main__": # If the script is run directly
    cli() # Run the click group