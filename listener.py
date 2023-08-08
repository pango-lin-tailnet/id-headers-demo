import os

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def greet():
    tailscale_user_name  = request.headers.get('Tailscale-User-Name',  '')
    tailscale_user_login = request.headers.get('Tailscale-User-Login', '')

    if not (tailscale_user_name or tailscale_user_login):
        serve_options = {'identified'      : False,
                         'background_color': '#e3c666',
                         'color'           : '#282828',
                        }
    else:
        serve_options = {'identified'      : True,
                         'background_color': '#3c7b5f',
                         'color'           : '#fff',
                        }

    serve_options['invite_link'] = os.environ.get('DEMO_INVITE_LINK')
    serve_options['tailscale_url'] = os.environ.get('TAILSCALE_URL')
    serve_options['headers'] = dict(request.headers)

    return render_template('index.html', **serve_options)

if __name__ == '__main__':
    app.run()
