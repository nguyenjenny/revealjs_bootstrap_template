# Template of reveal.js with Bootstrap 5 and Jinja2 integration

## Live Demo
View the live demo of the slides [here](https://nguyenjenny.github.io/revealjs_bootstrap_template/).

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

## Using Jinja2 

### Adding Pages using Jinja2
- To add pages add the command `{% include 'page_path.html' %}` to the `base.html`

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
### Updating variables
You can update variables in the `base.py` page

```
        general_vars = {
            "presentation_date": "2021-07-21",
            "presentation_title": "Title Here",
            "contact_url": "http://jennyn.ca",
            "contact_text": "Contact Me",
            "presentation_width": 1300,
            "presentation_height": 700,
            "email": "xxx@gmail.com",
        }

        color_vars = {
            "blue": "#5073B3",
            "aqua_blue": "#015D8E",
            "mustard": "#E58D05",
            "pink": "#EB9B94",
            "red": "#FC3E00",
            "tan": "#EDE6D4",
            "peach": "#E5CEAE",
            "box_color": "#294F7C",
            "purple": "#563D7C",
        }
```

### Using macros to quickly build bootstrap elements
Jinja2 macros are used to make building bootstrap elements easier.

![Templates demo](assets/gifs/templates_demo.gif)

To call a macro, you must first import it using the `{% from "FILE_PATH_HERE" import NAME_OF_MACRO %}`. Once you have imported the macro you can then call it: `{{ NAME_OF_MACRO(parameter1, parameter2, parametern)}}`


```
    {% from "macros/columns_macro.html" import get_accordion %}

    <section data-background-color="{{blue}}">

    {% set items = [
        [ 'Title', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Fusce interdum nisi non ornare blandit. Pellentesque luctus commodo arcu non rutrum. 
        Nullam rhoncus tempus elementum. 
        Mauris mollis bibendum semper. 
        Sed justo ex, malesuada vitae suscipit sit amet, consectetur sit amet velit.'],
        [ 'Title', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Fusce interdum nisi non ornare blandit. Pellentesque luctus commodo arcu non rutrum. 
        Nullam rhoncus tempus elementum. 
        Mauris mollis bibendum semper. 
        Sed justo ex, malesuada vitae suscipit sit amet, consectetur sit amet velit.'],
        [ 'Title', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Fusce interdum nisi non ornare blandit. Pellentesque luctus commodo arcu non rutrum. 
        Nullam rhoncus tempus elementum. 
        Mauris mollis bibendum semper. 
        Sed justo ex, malesuada vitae suscipit sit amet, consectetur sit amet velit.'],
    ] %}
    {{ get_accordion(items, "accordian_example")}}

    </section>
```


Macros are located in the `slides/macros` folder.





### Building the `index.html` page
- To build the `index.html` page, run `python render.py` in the terminal