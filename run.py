#!/Users/ckirby/.virtualenvs/rack-rat/bin/python3
from app import app

if __name__ == 'main':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
