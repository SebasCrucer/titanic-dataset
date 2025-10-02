# Funcion para descargar el pronostico 
# (USAR COMO y_pred UN PREDICT SOBRE LOS DATOS DE TEST)

import pandas as pd

def download_output(y_pred, name):
  output = pd.DataFrame({'PassengerId': test.PassengerId, 
                         'Survived': y_pred})
  output.to_csv(name, index=False)

  # Ejemplo de uso (cambiar el nombre por el suyo)
  download_output(y_pred_test, 'martin_pred.csv')