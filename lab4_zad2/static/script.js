document.addEventListener('DOMContentLoaded', function() {
    const taskInput = document.getElementById('taskInput');
    const addTaskBtn = document.getElementById('addTaskBtn');
    const taskList = document.getElementById('taskList');

    let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

    function renderTasks() {
        taskList.innerHTML = '';
        tasks.forEach((task, index) => {
            const li = document.createElement('li');
            li.classList.toggle('completed', task.completed);

            li.innerHTML = `
                <span>${task.name}</span>
                <button class="delete">Usuń</button>
                <button class="toggle">${task.completed ? 'Oznacz jako niezrobione' : 'Oznacz jako wykonane'}</button>
            `;
            taskList.appendChild(li);

            li.querySelector('.delete').addEventListener('click', function() {
                deleteTask(index);
            });

            li.querySelector('.toggle').addEventListener('click', function() {
                toggleTask(index);
            });
        });
    }

    function addTask() {
        const taskName = taskInput.value.trim();
        if (taskName) {
            tasks.push({ name: taskName, completed: false });
            taskInput.value = '';
            saveTasks(); //
            renderTasks(); //
        }
    }

    function deleteTask(index) {
        tasks.splice(index, 1);
        saveTasks();
        renderTasks();
    }

    function toggleTask(index) {
        tasks[index].completed = !tasks[index].completed;
        saveTasks();
        renderTasks();
    }

    function saveTasks() {
        localStorage.setItem('tasks', JSON.stringify(tasks));
    }

    addTaskBtn.addEventListener('click', addTask);

    renderTasks();
});