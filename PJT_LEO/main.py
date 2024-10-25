from flask import Flask, render_template, request, redirect, url_for
#import psycopg2
#from psycopg2 import sql

app = Flask(__name__)

#def connect_db():
#    conn = psycopg2.connect(
#        dbname="marchi_arquitetos", 
#        user="PHS", 
#        password="0509", 
#        host="localhost", 
#        port="5432"
#    )
#    return conn

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

            vl_area = get_valor(tipo, ambiente, quartos, garagem)
            vl_total, goumet, hometheater, despejo, escritorio, academia, piscina = get_list_valortotal(vl_area, list_ambientes)
            print(vl_total, list_ambientes, goumet, hometheater, despejo, escritorio, academia, piscina)
#            try:
#                  query = sql.SQL("INSERT INTO orcamento (orc_tipo, orc_ambiente, orc_quartos,\
#                                    orc_garagem, orc_goumet, orc_hometheater, orc_despejo, orc_escritorio,\
#                                    orc_academia, orc_piscina) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
#                  conn = connect_db()
#                  cur = conn.cursor()
#                  cur.execute(query, (tipo, ambiente,quartos,garagem,goumet,hometheater,despejo,escritorio,academia,piscina))
#                  conn.commit()
#                  cur.close()
#                  conn.close()
                
#            except Exception as e:
#                  conn.rollback() 
#                  print(f"Erro ao inserir dados: {e}")

            return redirect(url_for('resultado', vl_area=vl_area, vl_total=vl_total))
      return render_template('orc_index.html')

@app.route('/resultado')
def resultado():
      vl_area = request.args.get('vl_area')
      vl_total = request.args.get('vl_total')
      return render_template('res_index.html', vl_area=vl_area, vl_total=vl_total)

def get_valor(tipo, ambiente, quartos, garagem):

      vl_area = 0
      
      if tipo == 'Térreo':
            vl_area += 60
      else:
            vl_area += 120

      if ambiente == 'medio':
            vl_area += 20
      elif ambiente == 'grande':
            vl_area += 40
      else:
            vl_area += 60

      if  quartos == 3:
             vl_area += 60
      elif quartos == 4:
             vl_area += 80   
      else:
             vl_area += 90

      if garagem == 2:
             vl_area += 25
      elif garagem == 3:
             vl_area += 45
      else:
             vl_area += 65
      
      return vl_area

def get_list_valortotal(vl_area, list_ambientes):
      goumet = hometheater = despejo = escritorio = academia = piscina = False

      for i in list_ambientes:
            if i == 'area_goumet':
                  goumet   = True
                  vl_area += 30
            elif i == 'hometheater':
                  hometheater = True
                  vl_area   += 20
            elif i == 'despejo':
                  despejo  = True
                  vl_area += 5
            elif i == 'escritorio':
                  escritorio = True
                  vl_area   += 30
            elif i == 'academia':
                  academia = True
                  vl_area += 14
            elif i == 'piscina':
                  piscina = True
                  vl_area += 20
      
      vl_total = vl_area * 35.00
      return vl_total, goumet, hometheater, despejo, escritorio, academia, piscina    


if __name__ == '__main__': 
      app.run(debug=True)

