from django.contrib.auth.models import User
from django.db import models

# Create your models here.
GENERO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
        )
class Paises(models.Model):
    id_pais = models.IntegerField(blank=True,null=True)
    pais = models.CharField(max_length=70, default='')
    def __str__(self):
        return self.pais
class Estados(models.Model):
    id_estado = models.IntegerField(blank=True,null=True)
    pais = models.ForeignKey(Paises,on_delete=models.CASCADE,default = "", blank = True,null= True)
    estado = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.estado
class Municipios(models.Model):
    estado = models.ForeignKey(Estados,on_delete=models.CASCADE,default = "", blank = True,null= True)
    municipio = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.municipio
class Sexos(models.Model):
    sexo = models.CharField(max_length=20, default='')
    def __str__(self):
        return str(self.sexo)
class Sectores(models.Model):
    sector = models.CharField(max_length=70, default='')
    def __str__(self):
        return self.sector
class Subsectores(models.Model):
    sector = models.ForeignKey(Sectores,on_delete=models.CASCADE,default = "", blank = True,null= True)
    subsector = models.CharField(max_length=70, default='')  
    def __str__(self):
        return self.subsector  

class Como_te_enteraste(models.Model):
    opcion = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.opcion
                
class Ocupaciones(models.Model):
    ocupacion = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.ocupacion

class Numero_Empleados(models.Model):
    numero_empleados = models.CharField(max_length=20, default='')
    def __str__(self):
        return self.numero_empleados

class Tipo_Usuario(models.Model):
    url = models.CharField(max_length=19,default='',blank=True)
    tipo = models.CharField(max_length=19,default='',blank=True)
    def __str__(self):
        return self.tipo

class UserProfile(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    apellidoP = models.CharField(max_length=50,default='')
    apellidoM = models.CharField(max_length=50,default='')
    genero = models.ForeignKey(Sexos,on_delete=models.CASCADE,default = "", blank = True,null= True)
    otro_genero = models.CharField(max_length=100, default='',blank=True)
    fecha_nacimiento = models.CharField(max_length=30,default='')
    curp= models.CharField(max_length=19,default='')
    cp = models.CharField(max_length=8, default='')
    calle = models.CharField(max_length=50, default='')
    colonia = models.CharField(max_length=50, default='')
    ciudad = models.CharField(max_length=50, default='')
    celular = models.CharField(max_length=20, default='')
    imagen = models.ImageField(upload_to='perfil_imagen', blank=True)
    #datos de loren
    correo_secundario = models.CharField(max_length=50,default='',blank=True)
    edad = models.CharField(max_length=5,default='',blank=True)
    dni = models.CharField(max_length=19,default='',blank=True)
    pais = models.ForeignKey(Paises,on_delete=models.CASCADE,default = "", blank = True,null= True)
    estado = models.ForeignKey(Estados,on_delete=models.CASCADE,default = "", blank = True,null= True)
    municipio = models.ForeignKey(Municipios,on_delete=models.CASCADE,default = "", blank = True,null= True)
    ocupacion = models.ForeignKey(Ocupaciones,on_delete=models.CASCADE,default = "", blank = True,null= True)
    otra_ocupacion = models.CharField(max_length=100, default='',blank=True)
    institucion = models.CharField(max_length=100, default='',blank=True)
    num_empleados = models.ForeignKey(Numero_Empleados,on_delete=models.CASCADE,default = "", blank = True,null= True)
    sector = models.ForeignKey(Sectores,on_delete=models.CASCADE,default = "", blank = True,null= True)
    subsector = models.ForeignKey(Subsectores,on_delete=models.CASCADE,default = "", blank = True,null= True)
    otro_subsector = models.CharField(max_length=100, default='',blank=True)
    carrera = models.CharField(max_length=100, default='',blank=True)
    como_te_enteraste = models.ForeignKey(Como_te_enteraste,on_delete=models.CASCADE,default = "", blank = True,null= True)
    otro_como_te_enteraste = models.CharField(max_length=100, default='',blank=True)
    json_temas_de_interes=models.CharField(max_length=800, default='',blank=True)
    otro_tema_de_interes=models.CharField(max_length=100, default='',blank=True)
    ultimo_curso = models.CharField(max_length=200,default='',blank=True)
    terminos_y_condiciones = models.BooleanField(default=False)
    tipo_usuario = models.ForeignKey(Tipo_Usuario,on_delete=models.CASCADE,default = "", blank = True,null= True)

    class Meta:
        managed = False
        db_table = 'usuarios_userprofile'

    def __str__(self):
        return self.user.username
    
class UsuarioAcademic(models.Model):
    id_alumno = models.IntegerField(blank = True,null= True)
    curp = models.CharField(max_length=255,blank = True,null= True)
    nombre = models.CharField(max_length=200,blank = True,null= True)
    apellido_paterno = models.CharField(max_length=200,blank = True,null= True)
    apellido_materno = models.CharField(max_length=200,blank = True,null= True)
    correo_electronico = models.CharField(max_length=100,blank = True,null= True)
    matricula = models.CharField(max_length=11,blank = True,null= True)
    fecha_ingreso = models.CharField(max_length=30,null= True,blank=True)
    oferta_educativa = models.TextField(blank=True,null= True)
    periodo= models.CharField(max_length=50,null= True,blank=True)
    fecha_inicio_periodo = models.CharField(max_length=30,null= True,blank=True)
    fecha_fin_periodo = models.CharField(max_length=30,null= True,blank=True)
    estatus = models.TextField(blank=True,null= True)

    class Meta:
        managed = False
        db_table = 'usuarios_usuarioacademic'