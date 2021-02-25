# License Manager

Name pending.

## Idea

A Django application that will allow you to track and manage software licenses and who is using them.

### Getting started

#### Backend

The backend runs in Django using the Django Rest Framework. To run that server use:
`python manage.py runserver`

#### Frontend

The frontend runs in react(current learning process). To run the react server use: 
`cd frontend/`

`npm start`

### Features and requirements

**Requirements per entry**
- Software name
- License key
- Date of entry
- Purchase date
- Renewal date(if there is one)
- Who the license is assigned to


## Implementation

- One piece of software can have multiple licenses `many-to-one`
- One license can have one user assigned to it `one-to-one`