import glob

import jinja2

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('template'))
template = jinja_env.get_template('base.html')

general_vars = {
    "presentation_date": "2021-07-21",
    "presentation_title": 'Title Here',
    "contact_url": "http://jennyn.ca",
    "contact_text": "Jenny Nguyen",
    "presentation_width": 1300,
    "presentation_height": 700,
    "email": "xxx@gmail.com"
}

color_vars = {
    'blue': '#5073B3',
    'aqua_blue': '#015D8E',
    'mustard': '#E58D05',
    'pink': '#EB9B94',
    'red': '#FC3E00',
    'tan': '#EDE6D4',
    'peach': '#E5CEAE',
    "box_color": "#00537F",
}

logos = glob.glob(r"assets/images/logos/logo_*.png")
logos = [i.replace("\\", "/") for i in logos]

home_vars = {
    "logos": logos,
    "jenny_avatar": "/assets/images/jennyn_theme/jenny_icon.svg",
    "mugsy_avatar": "/assets/images/jennyn_theme/mugsy_icon.svg",
    "home_bg": "/assets/images/jennyn_theme/geometric_orange_bg.svg",
}


jinja_vars = {**general_vars, **color_vars, **home_vars}


html_str = template.render(jinja_vars)
html_file= open("index.html","w")
html_file.write(html_str)
html_file.close()
