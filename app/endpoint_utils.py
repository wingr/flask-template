"""Utils modules for flask app."""
import re
import json
from typing import List

from flask import Flask

from app.log_utils import LogUtils
from app.config import TEMPLATES_FOLDER, RESULTS_META_DC


class FlaskApp(Flask):
    """Wrapper around Flask class."""

    def __init__(self, name: str) -> None:
        """Initialize class."""
        super().__init__(__name__, template_folder=TEMPLATES_FOLDER)
        self.config['TEMPLATES_AUTO_RELOAD'] = True


class EndpointUtils():
    """Utility class for serving results in the app."""

    def natural_sort(self, str_ls: List[str]) -> List[str]: 
        convert = lambda text: int(text) if text.isdigit() else text.lower() 
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)] 
        return sorted(str_ls, key = alphanum_key)

    def get_results_dc(self, model: str) -> dict:
        """Load results for the given model.

        Example model results file:
            {
                global_scores: 
                    {
                        "f1": 0.5,
                        "precision": 0.5,
                        "recall": 0.5
                    },
                per_class_scores:
                    {
                        "class1": 
                            {
                                "f1": 0.5,
                                "precision": 0.5,
                                "recall": 0.5
                            },
                        "class2": 
                            {
                                "f1": 0.5,
                                "precision": 0.5,
                                "recall": 0.5
                            },
                        ...
                    }
            }

        Args:
            model       : The name of the model to load results for
        Return:
            retults_dc  : The dictionary of model results
        """
        path = RESULTS_META_DC[model]['path']
        class_key = RESULTS_META_DC[model]['class_key']

        with open(path, 'rt') as f:
            results_dc = json.load(f)

        results_dc['model'] = model.title().replace('_', ' ')
        results_dc['sorted_class_keys'] = self.natural_sort(list(results_dc[class_key].keys()))
        return results_dc
