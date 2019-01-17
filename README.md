## Overview
This repository provides a quick flask app template for serving data-centric results from within a Docker container.

## Setup
1. Clone the repository
2. Create a `.env` file in the `script/` directory (you can just use `$ touch script/.env`)
3. Build the Docker container, `$ script/bootstrap`
4. Test that the container is setup correctly, `$ script/test`

## Local deploy
To test and/or deploy the app locally:
1. Follow [Setup](#setup) above
2. Execute `$ script/server`
3. The Web GUI should be available in your browser at `0.0.0.0:5000`.
