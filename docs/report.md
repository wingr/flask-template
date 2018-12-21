## Overview (1 asterisk)
Often when presenting machine learning results, we want the ability to present numerical results and also a place to discuss the results in more detail. This flask template shows how to display a `pdf` file.

The `pdf` could be results, something from a third party, or based off an `.md` file like this one. The source for this `pdf` file is the `docs/report.md` file. The next section gives the steps to create a `pdf` from a `.md` file in Atom.

The following sections show different markdown components rendered in `pdf` for illustration.

## Creating pdf files from .md files (2 asterisks)
In Atom:

* Go to the `Atom` menu -->  `Preferences...` --> `Install`
* Search for the package `markdown-pdf` and install
* After writing the `.md` file, go to the `Packages` menu in Atom, click on the `Markdown to PDF` package and chose `Convert`
* Move the generated `pdf` to the `app/static/` directory (possibly in a sub-directory like this file, e.g. `static/pdfs/`)

### Example medium heading (3 asterisks)
Ordered list
1. First
2. Second
3. Third

#### Example smaller heading (4 asterisks)
Example table

col1 | col2
---- | ----
a | b
c | d

##### Example Small heading (5 asterisks)
Example code

```python
def add_one(x: int) -> int:
    new_x = x + 1
    return new_x
```
