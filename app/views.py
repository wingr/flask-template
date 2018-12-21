"""Flask server for displaying Ocotolingua evaluation results."""
from flask import redirect, render_template, request, url_for

from app.endpoint_utils import FlaskApp, EndpointUtils
from app.log_utils import LogUtils
from app.config import LOCAL_HOST, LOCAL_HOST_PORT


app = FlaskApp(__name__)
endpoint_utils = EndpointUtils()


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    """Render welcome/index page."""
    return render_template('index.html')

@app.route('/results')
def results():
    """Render results/data."""
    model_dc = {'titles': ['Make Selection', 'Model 1', 'Model 2']}
    return render_template('results.html', model_dc=model_dc)

@app.route('/api/endpoint', methods=['GET'])
def endpoint():
    """Return results for a given dataset."""
    result_set_title = request.args['result_set'].lower().replace(' ', '_')
    if result_set_title == 'make_selection':
        return render_template('directions.html')
    LogUtils().log_info("Result set chosen: {}".format(result_set_title))
    results_dc = endpoint_utils.get_results_dc(result_set_title)
    #LogUtils().log_info('{}'.format(results_dc))
    return render_template('endpoint.html', results_dc=results_dc)

@app.route('/report')
def report():
    """Render report."""
    return redirect(url_for('static', filename='pdfs/report.pdf'))


if __name__ == '__main__':
    app.run(host=LOCAL_HOST, port=LOCAL_HOST_PORT, debug=True)
