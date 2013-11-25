#en este archivo se definiran los metodos del manejko de la base
import MySQLdb as db

try:
  con = db.connect("Pacientes.db")
  con.execute("CREATE TABLE pacientes values()")
  
  def agregarPaciente(firstName, lastname, cc, prioridad,tiempoIngreso):
      con.execute("")
      
  def agregarPaciente(firstName, lastname, cc, prioridad,tiempoIngreso):
      con.execute("UPDATE ")
    
except:
  print "error"
