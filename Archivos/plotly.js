<!DOCTYPE html>
<html>
<head>
  <!-- Incluir la biblioteca de Plotly.js -->
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
  <!-- Elemento div donde se mostrará el gráfico -->
  <div id="scatterPlot"></div>

  <script>
    // Datos para el gráfico
    var data = [
      {
        x: [1, 2, 3, 4, 5],  // Valores en el eje x
        y: [2, 4, 1, 5, 3],  // Valores en el eje y
        mode: 'markers',     // Tipo de marcadores
        type: 'scatter'      // Tipo de gráfico de dispersión
      }
    ];

    // Configuración del diseño del gráfico
    var layout = {
      title: 'Gráfico de dispersión',
      xaxis: {title: 'Eje X'},
      yaxis: {title: 'Eje Y'}
    };

    // Crear el gráfico
    Plotly.newPlot('scatterPlot', data, layout);

    var data = [
    {
        x: ['giraffes', 'orangutans', 'monkeys'],
        y: [20, 14, 23],
        type: 'bar'
    }
    ];

    Plotly.newPlot('myDiv', data);

  </script>
</body>
</html>
