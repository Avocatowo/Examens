from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Examen</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
    }
    .contenedor {
      max-width: 500px;
      margin: 0 auto;
      border: 1px solid #ccc;
      padding: 20px;
      text-align: center;
    }
    h1 {
      margin-top: 0;
    }
    p {
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <div class="contenedor">
    <h1>YOPIMIX</h1>
    <img src="https://png.pngtree.com/png-clipart/20190516/original/pngtree-users-vector-icon-png-image_3725294.jpg" alt="Mi imagen" width="200" height="150" title="Esta es una imagen">
    <p>Mi nombre es ASG. Soy Estudiante de desarollo de sitemeas en el instituto continental.</p>
    <p>Me apasiona la programacion y .</p>
    <p>Puedes contactarme a través whtps 985665871.</p>
  </div>
</body>
</html>
"""
  return html_content


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
