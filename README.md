# Task 1: Develop an Advanced Bank Account Management System

## Description
As a user, I want an advanced bank account management system that allows me to create and manage multiple bank accounts, perform transactions, and view account summaries so that I can handle my financial operations efficiently.

## Class diagram
![Снимок экрана 2024-12-18 191409](https://github.com/user-attachments/assets/4afe46d3-b6c2-4746-b8c6-600b4cb2a3c5)


# Task 2: Develop a To-Do List Application for Task Management

## Description
As a user, I want a To-Do List application that allows me to create and manage tasks so that I can stay organized and prioritize my workload effectively.

## Acceptance Criteria

### Task Creation
- A user can add a new task with the following attributes:
  - **Title**: A short name for the task.
  - **Description**: A detailed explanation of the task.
  - **Priority**: The importance of the task (1 - high, 2 - medium, 3 - low).
- The system must confirm the successful addition of a task.

### Task Completion
- A user can mark a task as completed.

### Task Deletion
- A user can remove a task from the list by its title.
- The system must confirm the successful removal of the task.

### Viewing Tasks
- A user can view all tasks in the list.
- Tasks can be sorted by priority in the order: High → Medium → Low.
- A user can view only pending tasks (tasks not yet marked as completed).

## Technical Notes
- Use a `Task` class to represent individual tasks.
- Use a `ToDoList` class to manage the list of tasks.
