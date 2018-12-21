"""Configuration for Flask app."""
import os


# Global variables
WORK_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_FOLDER = os.path.join(WORK_DIR, 'templates')
LOCAL_HOST = os.getenv('LOCAL_HOST', '0.0.0.0')
LOCAL_HOST_PORT = os.getenv('LOCAL_HOST_PORT', 5000)

# Model files
RESULTS_META_DC = {
                    'model_1': 
                        {
                            'path': 'app/local_data/model1_results.json',
                            'metrics_ls': ['f1', 'precision', 'recall'],
                            'global_key': 'global_scores',
                            'class_key': 'per_class_scores'
                        },
                    'model_2':
                        {
                            'path': 'app/local_data/model2_results.json',
                            'metrics_ls': ['f1', 'precision', 'recall'],
                            'global_key': 'global_scores',
                            'class_key': 'per_class_scores'
                        }
                    }

# Style
COLOR_CHOICE_LS = ['#8000FF', '#3498DB', '#FF5733', '#223AE6', '#2ECC71', '#5F6A6A', '#6C22E6',
                   '#CE22E6', '#ACB02E', '#B18904', '#848484', '#04B404', '#5882FA', '#FF0080',
                   '#0489B1', '#FA5858', '#DBA901', '#00b4ff', '#008080', '#003366', '#725394']
