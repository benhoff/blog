This is my personal blog.

It uses pelican and github pages. 

Cloning, creating a virtual environment (`python -m venv venv; source venv/bin/activate`) and running `python setup develop` should get you started

The articles can be made using the commands `$ make html`. Additionally the site can be locally previewed using `$ make serve`

Finally, to deploy the articles (assuming configuration is setup correctly), use `$ make github`

In order to configure correctly, need to ensure the `publish` remote is set. This repo needs the `publish` repo to be: `git remote add publish git@github.com:benhoff/benhoff.github.io`
