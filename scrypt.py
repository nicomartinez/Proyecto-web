#en este archivo se definiran los metodos del manejko de la base
import sqlite3 as db

try:
  con = db.connect("pacientes.db")
  con.execute("CREATE TABLE pacientes values(fisrstName varchar(20), lastName varchar(20), cc INT, prioridad varchar(10), tiempoIngreso Timestamp)")
  
  def agregarPaciente(firstName, lastName, cc, prioridad,tiempoIngreso):
      con.execute("INSERT INTO pacientes VALUES(" + fistName + ", " + lastName + ", " + cc + ", " + prioridad + ", " + tiempoIngreso + ")")
      
  def actualizarPaciente(firstName, lastName, cc, prioridad,tiempoIngreso):
      con.execute("UPDATE pacientes SET firstName = " + firtName +",  lastNme = " + lastName + ", cc = " + cc + ", prioridad = " + prioridad + ", tiempoIngreso = " + tiempoIngreso + "WHERE firstName = " + firstName")
      con.commit()
  def borrarPaciente(name):
      con.execute("DELETE FROM pacientes WHERE firstName = " + name)
      con.commit()
  def mostrarLista():
      con.execute("SELECT * FROM pacientes")
except:
  print "error"
