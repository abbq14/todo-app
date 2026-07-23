tasks = [
    {"title": "read Python", "done": "0"},
    {"title": "buy bread", "done": "1"},
]
def show_tasks(tasks):
    i = 0
    if len(tasks) == 0 : 
        print("no tasks yet ")
        return
    for task in tasks : 
        if task["done"] == "1" : 
            i=i+1 
            print(f"{i}.[x] {task['title']}")
            
        else : 
            i=i+1 
            print(f"{i}.[ ] {task['title']}")
    if i== 0 : 
        print("no tasks yet ")
    
        
def save_tasks (tasks , filename ) : 
    with open(filename, "w", encoding="utf-8") as f:
        for task in tasks : 
            if task["done"] == "1" : 
                f.write(f"1|{task['title']}\n")
                
            else : 
                f.write(f"0|{task['title']}\n")

def load_tasks (filename) : 
    tasks = []
    try : 
        with open ( filename, "r" , encoding="utf-8" ) as f : 
            tasks_temp = f.read() 
            tasks_temp = tasks_temp.split("\n")
            for task_temp in tasks_temp : 
                task_temp = task_temp.strip().split("|")
                if (task_temp[0]==""):
                    break 
                task = {"title": task_temp[1] ,"done" :  task_temp[0]}
                tasks.append(task)
    except FileNotFoundError : 
        print (" u are lucky u have no taskss")
    return tasks   

while True:
    print("1) show  \n2) add  \n3) save  \n4) quit")
    choice = input("choose: ")
    if choice == "1" : 
        loaded_tasks = load_tasks("tasks.txt")
        show_tasks(loaded_tasks)
    elif choice == "2" : 
        new_task = input ("enter the new task")
        task = {'title' : new_task , 'done' : '0'}
        tasks.append(task)
        save_tasks(tasks ,"tasks.txt")
    elif choice == "3":
        save_tasks(tasks ,"tasks.txt")
    elif choice == "4":
        print("byyy")
        break      