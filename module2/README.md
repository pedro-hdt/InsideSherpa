# JPMC Summer Internship SEP: InsideSherpa Module 2

## Sanctions screening

Please see the Jupyter notebook (`sanctions.ipynb`) for a description and
walkthrough of the solution. For a better experience of visualizing the notebook,
there is a version hosted on Google Colab: https://colab.research.google.com/drive/1_GvT0bTV5wkOQjT9eZRH51kxuNFXP7zY?usp=sharing

All the code in there is also in separate files.

The REST API is not in the notebook.

### Run Instructions

#### REST

To get the endpoint running on a dev server simply create a 'lists' directory and run
`sanctions_rest_api.py` as main.

The API supports:

- POST method on the root '/' to upload sanctions lists, which must have
  either .txt or .csv extensions
- GET method to '/list/search_name' where 'list' is
  the list to check against and 'search_name' is the name to screen.

The threshold here is always 75% and the logarithmic similarity is always used.

To perform some manual testing I just used Postman, so no automated version is available.

#### CLI

Requires numpy installed (`pip3 install numpy`). See the `--help` flag for details.

Unlike with the REST API, the CLI can be configured on startup

```
python3 sanctions_cli.py [--list=<sanctions_list_filename>]
    [--threshold=<threshold_limit>]
    [--basic>]
```
