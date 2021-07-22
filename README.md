# Template of reveal.js with Bootstrap 5 and Jinja2 integration

## Live Demo
View the live demo of the website [here](https://nguyenjenny.github.io/revealjs_bootstrap_template/).

## Requirements
- install [reveal.js](https://revealjs.com/)
- install [npm](https://www.npmjs.com/)
- install [gulp](https://gulpjs.com/)
- install [python](https://www.anaconda.com/)
- install [Jinja2](https://jinja.palletsprojects.com/)


## Bootstrap Themes
- The SASS files for the Bootstrap theme are located in `css>theme>source>bootstrap_jennyn.scss`
- The SASS files reveal.js theme are located in `css>theme>source>jennyn.scss`
- To build the theme run `gulp build`
- The CSS files are located  in `dist>theme`

## Adding Pages using Jinja2
- To add pages use the `{% insert 'page_path.html' %}` to the `base.html`

```
		<div class="reveal">
			<div class="slides">
				{% include 'title_cards/home.html' %}
				<section>
					{% include 'title_cards/template.html' %}
					{% include 'templates/list_groups.html' %}
					{% include 'templates/three_col.html' %}
					{% include 'templates/three_col_bg.html' %}
					{% include 'templates/left_photo.html' %}
					{% include 'templates/right_photo.html' %}
				</section>
				<section>
					{% include 'title_cards/intro.html' %}
				</section>
				<section>
					{% include 'title_cards/results.html' %}
				</section>
				<section>
					{% include 'title_cards/conclusion.html' %}
				</section>
				{% include 'title_cards/end.html' %}
			</div>
		</div>
```
- To build the `index.html` page run `python render.py` in the terminal