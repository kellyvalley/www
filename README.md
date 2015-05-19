# WWW for valleyrain.org

This project is for [http://www.valleyrain.org](http://www.valleyrain.org) website. Right now it is based on [Pelican Static Site Generator](http://docs.getpelican.com) using [pelican-bootstrap3](https://github.com/valleyrain-org/pelican-bootstrap3) theme.

The website is hosted as [GitHub Project Pages](https://pages.github.com), and the real content is on "gh-pages" branch. However, we don't need to touch gh-pages branch. All the developemnt work is on "master" branch right now.

## Installation

First:

[Fork this repo](https://help.github.com/articles/fork-a-repo) and then clone it:

`git clone --recursive https://github.com/<your-username>/www.git`

Then:

`pip install pelican markdown beautifulsoup4`

## Test

`make html`

`make serve`

Check web pages are OK ([http://127.0.0.1:8000](http://127.0.0.1:8000)).

## Send pull request

## Publish

(only for project owner)

`make github`
