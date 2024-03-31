# Observer Pattern Example: Students and Courses

## Overview

The Observer pattern is a behavioral design pattern that establishes a one-to-many dependency between objects. In this pattern, when one object (the subject) changes its state, all its dependents (observers) are notified and updated automatically. This promotes loose coupling between objects, allowing for a more modular and extensible design.

In this example, we demonstrate the Observer pattern using a scenario of students enrolling in courses. Each course can be observed by multiple students. When a course becomes available or unavailable, all subscribed students are notified accordingly.

## Get Started

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/Farha-Dahman/observer_pattern.git
    ```
2. Navigate to the project directory:
    ```
    cd observer_pattern
    ```
3. Run the main script to start the application:
    ```
    python main.py
    ```
