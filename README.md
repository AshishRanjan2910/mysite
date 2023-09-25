# mysite
 Updated to manage main app
 updates made in:
  + settings.py
  + urls.py

# main (App)
 App for handling To Do Lists (locations provided below are in respect to the "main" folder)
 -- models.py:
  + ToDoList: lets you create multiple sets of to do lists
     - name
  + Item: lets you make item for ToDoList object
     - todolist: foreign key
     - task
     - completed: to store and show the status of the task
 -- views.py (to render different screens):
  + index(/toDoListId): for showing, adding, and updating todos of a ToDoList (based on which ToDoList id we are visiting) , handles situation based response (validation applied, if okay updates in db, and renders henceforth)
  + home(/): root page
  + create(/create): lets you create a new ToDoLists for the user (say, we already have "errands" todo, and we want to add "practice" todo)
 -- urls.py (endpoints) included in mysite(project's)-urls.py:
  + home 
  + index
  + create
 -- forms.py leverage the form provided by django for "create" view & html page:
  + CreateNewList
    - name: name of the task
    - check: boolean
 -- Screens location: templates >> main (use of jinga2):
  + base.html (parent template): others extend this template
     - bootstraps
     - custom static CSS:: location: static/css/styles.css
  + home.html
  + lists.html
  + create.html
     
