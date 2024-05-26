/*<div class="task-container">
            <ul class="list-unstyled">
                {% for task in tasks %}
                <li {% if task['checked'] %} class="list-group-item list-group-item-action list-group-item-primary rounded" {% endif %}>
                    <span class="taskTitle">{{ task['taskTitle'] }}</span>
                    <span>Created: {{ task['currentDate'] }}</span>
                    <span class="fw-normal">{{ task['description'] }}</span>
                    <div class="task-options d-flex flex-wrap gap-2 mt-2">
                        <a class="btn btn-outline-primary btn-sm" href="{{ url_for('status', id=task['id']) }}">Checked</a>
                        <a class="btn btn-outline-primary btn-sm" href="{{ url_for('edit', id=task['id']) }}">Edit</a>
                        <a class="btn btn-outline-primary btn-sm" href="{{ url_for('delete', id=task['id']) }}">Delete</a>
                    </div>
                    {% if task['checked'] %}
                    <p>Completed!</p>
                    {% endif %}
                </li>
                {% endfor %}
            </ul>
        </div>*/

        /*href="{{ url_for('sort',s=1)}}"*/