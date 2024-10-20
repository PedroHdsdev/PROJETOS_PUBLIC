from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

def connect_db():
    conn = psycopg2.connect(
        dbname="marchi_arquitetos", 
        user="PHS", 
        password="0509", 
        host="localhost", 
        port="5432"
    )
    return conn

conn = connect_db()
cur = conn.cursor()


@app.route('/')
def index():
        return render_template('index.html')

@app.route('/orcamento', methods=['GET', 'POST'])
def orcamento():
      if request.method == 'POST':
            tipo     = request.form['G01']
            ambiente = request.form['G02']
            quartos  = request.form['G03']
            garagem  = request.form['G04']
            list_ambientes = request.form.getlist('G05')
            print(tipo)

            goumet = hometheater = despejo = escritorio = academia = piscina = False

            for i in list_ambientes:
                  if i == 'area_goumet':
                        goumet = True
                  elif i == 'hometheaterr':
                        hometheater = True
                  elif i == 'despejo':
                        despejo = True
                  elif i == 'escritorio':
                        escritorio = True
                  elif i == 'academia':
                        academia = True
                  elif i == 'piscina':
                        piscina = True
            try:
                        # Defina a tabela e as colunas corretamente
                  query = sql.SQL("INSERT INTO orcamento (orc_tipo, orc_ambiente, orc_quartos,\
                                    orc_garagem, orc_goumet, orc_hometheater, orc_despejo, orc_escritorio,\
                                    orc_academia, orc_piscina) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                        
                  cur.execute(query, (tipo, ambiente,quartos,garagem,goumet,hometheater,despejo,escritorio,academia,piscina))
                  conn.commit()  # Confirma a transação
                
            except Exception as e:
                  conn.rollback()  # Em caso de erro, desfaz a transação
                  print(f"Erro ao inserir dados: {e}")

            return redirect(url_for('index.html'))
        
      return render_template('orc_index.html')


if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000,debug=True)

