from flask import Flask, request, send_file
from flask_swagger import swagger

app = Flask(name)

# Echo back the input
@app.route('/echo', methods=['GET'])
def echo():
    msg = request.args.get('msg', '')
    return {'msg': "The message is: '" + msg + "'"}

# Return the sum of two numbers
@app.route('/excel', methods=['POST'])
def excel():
    df = request.get_json()
    data = pd.DataFrame(df)
    
    # Create path to a tempfile for excel output and zip
    path_xlsx = tempfile.NamedTemporaryFile(suffix='.xlsx').name
    
    # Write data frame
    data.to_excel(path_xlsx, index=False)
    
    attachment_string = "attachment; filename=Output_File.xlsx"
    return send_file(path_xlsx, as_attachment=True, attachment_filename=attachment_string)

# Swagger API documentation
@app.route('/spec')
def spec():
    swag = swagger(app)
    swag['info']['title'] = "Plumber Example API"
    return swag

if name == 'main':
    app.run()
