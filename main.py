from flask import Flask, render_template, url_for
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/top15/<page_id>')
def top_15(page_id):
    page_id = int(page_id)
    try:
        offset = int(page_id) * 15
        top_15_shows = queries.get_top_15_shows(offset)
        return render_template('top-15.html',
                               page_id=page_id,
                               top_15_shows=top_15_shows)
    except:
        page_id = 0
        offset = int(page_id) * 15
        top_15_shows = queries.get_top_15_shows(offset)
        return render_template('top-15.html',
                               page_id=page_id,
                               top_15_shows=top_15_shows)


@app.route('/tv-show/<show_id>')
def display_show(show_id):
    show = queries.get_show_by_id(show_id)[0]
    show_trailer_beta = show['trailer'].replace('http', 'https')
    show_trailer = show_trailer_beta.replace('watch?v=', 'embed/')
    return render_template('show.html',
                           show=show,
                           show_trailer=show_trailer)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
