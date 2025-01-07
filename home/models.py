from django.contrib.auth.models import User
from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
GENERO = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
        )
DEPENDENCIAS = [
        ('G','General'),
        ('P','PLAi'),
        ('ST','Secretaría de Turismo'),
        ('SEM','Semadet'),
        ('JAL','Jaltec'),
        ('CA','Canieti'),
        ('OOL','Oolinvaders'),
        ('CO','Continental'),
        ('BIO','Biomedica'),
        ('INGL','Mejoratuingles'),
        ('DYM','Desarrollo y mejora'),
        ('WL','Wizeline'),
        ('X','Sin Dependencia')
    ]
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
        
class Ejes_tematicos(models.Model):
    eje_tematico = models.CharField(max_length=80)
    dependencia = models.CharField(max_length=50,default='X',null=True,choices=DEPENDENCIAS)
    oferta_id = models.IntegerField(default=0,blank=False)

    def __str__(self):
        return self.eje_tematico + ",  Dependencia: "+ str(self.get_dependencia_display())

    class Meta:
        managed = False
        db_table = 'panelDeControl_ejes_tematicos'

class Niveles(models.Model):
    nivel = models.CharField(max_length=80)

    def __str__(self):
        return self.nivel
    class Meta:
        managed = False
        db_table = 'panelDeControl_niveles'


class Modalidades(models.Model):
    modalidad = models.CharField(max_length=80)

    def __str__(self):
        return self.modalidad
    class Meta:
        managed = False
        db_table = 'panelDeControl_modalidades'

class Idiomas(models.Model):
    idiomas = models.CharField(max_length=80)

    def __str__(self):
        return self.idiomas
    class Meta:
        managed = False
        db_table = 'panelDeControl_idiomas'

class Implementaciones(models.Model):
    implementacion = models.CharField(max_length=80)

    def __str__(self):
        return self.implementacion
    class Meta:
        managed = False
        db_table = 'panelDeControl_implementaciones'

class Periodos(models.Model):
    periodo_id= models.CharField(max_length=10,default="")
    periodo = models.CharField(max_length=80)

    def __str__(self):
        return self.periodo
    class Meta:
        managed = False
        db_table = 'panelDeControl_periodos'

class Grados(models.Model):
    grado = models.CharField(max_length=80)

    def __str__(self):
        return self.grado
    class Meta:
        managed = False
        db_table = 'panelDeControl_grados'

class Palabras_claves(models.Model):
    palabra_clave = models.CharField(max_length=80)

    def __str__(self):
        return self.palabra_clave
    class Meta:
        managed = False
        db_table = 'panelDeControl_palabras_clave'

class Tipo_de_cupo(models.Model):
    tipo_cupo = models.CharField(max_length=80)

    def __str__(self):
        return self.tipo_cupo
    class Meta:
        managed = False
        db_table = 'panelDeControl_tipo_de_cupo'

class Reconocimientos(models.Model):
    reconocimiento_id = models.CharField(max_length=10)
    reconocimiento = models.CharField(max_length=80)

    def __str__(self):
        return self.reconocimiento
    class Meta:
        managed = False
        db_table = 'panelDeControl_reconocimientos'

class Tipos(models.Model):
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return self.tipo
    class Meta:
        managed = False
        db_table = 'panelDeControl_tipos'

class Grupos(models.Model):
    grupo_municipio = models.CharField(max_length=255,default="",null=False)
    def __str__(self):
        return self.grupo_municipio
    class Meta:
        managed = False
        db_table = 'panelDeControl_grupos'

class PreguntasFrecuentes(models.Model):
    pregunta = models.CharField(max_length=100,blank=True,null=True, default='')
    respuesta = models.TextField(blank=True,null=True,default='')
    class Meta:
        managed = False
        db_table = 'panelDeControl_prreguntasfrecuentes'

class Detalles_botones(models.Model):
    color_fondo = models.CharField(max_length=10, default='')
    color_fuente = models.CharField(max_length=10, default='')
    texto = models.CharField(max_length=20, default='')
    descripcion = models.CharField(max_length=12, default='')
    url = models.CharField(max_length=200, default='')
    estatus = models.CharField(max_length=20, default='Activo')
    class Meta:
        managed = False
        db_table = 'panelDeControl_detalles_botones'

class UserProfile(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    apellidoP = models.CharField(max_length=50,default='',blank=True)
    apellidoM = models.CharField(max_length=50,default='',blank=True)
    genero = models.ForeignKey(Sexos,on_delete=models.CASCADE,default = "", blank = True,null= True)
    otro_genero = models.CharField(max_length=100, default='',blank=True)
    fecha_nacimiento = models.CharField(max_length=30,default='',blank=True)
    curp= models.CharField(max_length=19,default='',blank=True)
    cp = models.CharField(max_length=8, default='',blank=True)
    calle = models.CharField(max_length=50, default='',blank=True)
    colonia = models.CharField(max_length=50, default='',blank=True)
    ciudad = models.CharField(max_length=50, default='',blank=True)
    celular = models.CharField(max_length=20, default='',blank=True)
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
    json_temas_de_interes = models.TextField(blank=True)
    otro_tema_de_interes=models.CharField(max_length=100, default='',blank=True)
    ultimo_curso = models.CharField(max_length=200,default='',blank=True)
    terminos_y_condiciones = models.BooleanField(default=False)
    tipo_usuario = models.ForeignKey(Tipo_Usuario,on_delete=models.CASCADE,default = "", blank = True,null= True)
    confirma_perfil = models.BooleanField(default=False)
    matricula = models.CharField(max_length=10,blank=True,null=True, default="")

    class Meta:
        managed = False
        db_table = 'usuarios_userprofile'

    def __str__(self):
        return self.user.username
class Programas(models.Model):
    
    dependencia = models.CharField(max_length=50,default='X',null=True,choices=DEPENDENCIAS,blank=True)
    implementacion = models.TextField(blank=True)
    edicion = models.CharField(max_length=80,blank=True)
    titulo = models.CharField(max_length=165,blank=True)
    imagen_programa = models.ImageField(upload_to='programas/imagenes',blank=True)
    estatus = models.CharField(max_length=20, default='Activo',blank=True)
    descripcion_corta = models.CharField(max_length=255,blank=True, null=True)
    duracion = models.CharField(max_length=50,blank=True)
    reconocimiento = models.TextField(blank=True)
    inversion = models.BooleanField(blank=True, null=True)
    fecha_inicio = models.CharField(max_length=30,blank=True)
    fecha_fin = models.CharField(max_length=30, null=True,blank=True)
    precio = models.CharField(max_length=30, null=True,blank=True)
    fecha_creacion = models.DateField(auto_now_add=True,blank=True)
    descripcion_general = RichTextUploadingField(blank=True, null=True, config_name='textoPlano')
    url = models.CharField(max_length=200, blank=True, null=True)
    tutor = models.CharField(max_length=100, default=None,blank=True, null=True)
    descripcion_tutor= RichTextUploadingField(blank=True, null=True)
    imagen_tutor = models.ImageField(upload_to='tutores/imagenes',blank=True)
    institucion= models.CharField(max_length=50, default=None,blank=True, null=True)
    imagen_institucion=models.ImageField(upload_to='instituciones/imagenes',blank=True)
    idioma = models.TextField(blank=True)
    cupo = models.CharField(max_length=80,default=None,blank=True, null=True)
    palabras_clave = models.TextField(null=True,blank=True)
    turno = models.CharField(max_length=50,default=None,blank=True)
    grado = models.CharField(max_length=50,default=None,blank=True)
    periodo = models.CharField(max_length=50,default=None,blank=True)
    direccion = models.CharField(max_length=255,default=None,null=True,blank=True)
    latitud = models.CharField(max_length=20,default=None,null=True,blank=True)
    longitud = models.CharField(max_length=20,default=None, null=True,blank=True)
    objetivos = RichTextUploadingField(blank=True, null=True, config_name='textoPlanoVi')
    contenidos = RichTextUploadingField(blank=True, null=True, config_name='textoPlanoVi')
    a_quien_va_dirigido = RichTextUploadingField(blank=True, null=True, config_name='textoPlanoVi')
    requisitos_de_ingreso = RichTextUploadingField(blank=True, null=True,config_name='textoPlanoVi')
    contenido_didactico = RichTextUploadingField(blank=True, null=True,config_name='archivos')
    calendario = RichTextUploadingField(blank=True,null=True,config_name='cal')
    correo_personalizado = RichTextUploadingField(blank=True, null=True, config_name='correo')

    tutor_1 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_1= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_1 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_2 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_2= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_2 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_3 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_3= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_3 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_4 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_4= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_4 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_5 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_5= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_5 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_6 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_6= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_6 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_7 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_7= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_7 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_8 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_8= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_8 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_9 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_9= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_9 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_10 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_10= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_10 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_11 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_11= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_11 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_12 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_12= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_12 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_13 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_13= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_13 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_14 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_14= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_14 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_15 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_15= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_15 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_16 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_16= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_16 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_17 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_17= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_17 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_18 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_18= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_18 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)
  
    tutor_19 = models.CharField(max_length=100, default='', null=True,blank=True)
    descripcion_tutor_19= RichTextUploadingField(blank=True, null=True, default='')
    imagen_tutor_19 = models.ImageField(upload_to='tutores/imagenes',blank=True, null=True)

    destacado = models.BooleanField(default=False,blank=True)

    detalle_btn_1 = models.ForeignKey(Detalles_botones, on_delete=models.CASCADE, default=None, blank=True, null=True,
                                      related_name="detalle_btn_1")
    detalle_btn_2 = models.ForeignKey(Detalles_botones, on_delete=models.CASCADE, default=None, blank=True, null=True,
                                      related_name="detalle_btn_2")
    detalle_btn_3 = models.ForeignKey(Detalles_botones, on_delete=models.CASCADE, default=None, blank=True, null=True,
                                      related_name="detalle_btn_3")
    detalle_btn_4 = models.ForeignKey(Detalles_botones, on_delete=models.CASCADE, default=None, blank=True, null=True,
                                      related_name="detalle_btn_4")

    eje_tematico = models.ForeignKey(Ejes_tematicos, on_delete=models.CASCADE, default=None,blank=True)
    modalidad = models.ForeignKey(Modalidades, on_delete=models.CASCADE, default=None,blank=True)
    nivel = models.ForeignKey(Niveles, on_delete=models.CASCADE, default=None,blank=True)

    pregunta_1 = models.ForeignKey(PreguntasFrecuentes, on_delete=models.CASCADE, default=None, blank=True, null=True,
                                      related_name="pregunta_1")
    pregunta_2 = models.ForeignKey(PreguntasFrecuentes, on_delete=models.CASCADE, default=None, blank=True, null=True,
                                      related_name="pregunta_2")
    pregunta_3 = models.ForeignKey(PreguntasFrecuentes, on_delete=models.CASCADE, default=None, blank=True, null=True,
                                      related_name="pregunta_3")
    pregunta_4 = models.ForeignKey(PreguntasFrecuentes, on_delete=models.CASCADE, default=None, blank=True, null=True,
                                      related_name="pregunta_4")
    pregunta_5 = models.ForeignKey(PreguntasFrecuentes, on_delete=models.CASCADE, default=None, blank=True, null=True,
                                      related_name="pregunta_5")
    pregunta_6 = models.ForeignKey(PreguntasFrecuentes, on_delete=models.CASCADE, default=None, blank=True, null=True,
                                      related_name="pregunta_6")


    tipo = models.ForeignKey(Tipos, on_delete=models.CASCADE, default=None,blank=True, null=True)
    #campos nuevos ------------------------------------------------------------------------------------------
    tipo_cupo = models.ForeignKey(Tipo_de_cupo, on_delete=models.CASCADE,default=None,blank=True,null=True)
    asunto_correo_personalizado = models.CharField(max_length=250,default=None,null=True,blank=True)
    id_dependencia=models.CharField(max_length=10,default="",blank=True)
    titulo_id= models.CharField(max_length=10,default="",blank=True)

    #--------------------------------------------------------------------------------------------------------
    #campos mapa lugar o sede --------------------------------------------------------------------------------------------
    lugar_o_sede = models.CharField(max_length=255,default=None,null=True,blank=True)
    #--------------------------------------------------------------------------------------------------------
    #nuevas secciones----------------------------------------------------------------------------------------

    #--------------------------------------------------------------------------------------------------------
    #agregar otro campo que diga tipo de lugar o sede 
    #aagregar checkbox a idioma para seleccionar varios idiomas


    mas_implementaciones = models.BooleanField(default=False,blank=True, null=True)
    bloqueo_registro_IMP_P = models.BooleanField(default=False,blank=True, null=True)
    masde18 = models.BooleanField(default=False,blank=True)
    abreviatura = models.TextField(blank=True, null=True)
    seguimiento_de_captacion = models.BooleanField(default=True,blank=True)
    titulo_equivalente = models.CharField(max_length=165,blank=True,default='')
    plantel = models.CharField(max_length=180,default="",null=True,blank=True)
    plantel_id = models.IntegerField(null=True,blank=True)

    grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE, default=None, blank=True, null=True)

    autogestivo = models.BooleanField(default=False,blank=True, null=True)
    semanas = models.CharField(max_length=180,default="",null=True,blank=True)
    sesiones_por_semanas = models.CharField(max_length=180,default="",null=True,blank=True)
    hora_por_sesion = models.CharField(max_length=180,default="",null=True,blank=True)
    dias_semana = models.CharField(max_length=180,default="",null=True,blank=True)
    grupo_academic = models.IntegerField(null=True,blank=True,default=0)
    class Meta:
        managed = False
        db_table = 'panelDeControl_programas'

    def save(self, *args, **kwargs):
        if not self.titulo_equivalente:
            self.titulo_equivalente = self.titulo
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo + ",  Dependencia: "+ str(self.get_dependencia_display())

class Inscripciones(models.Model):
    curso = models.ForeignKey(Programas,on_delete=models.CASCADE,default = None, blank = True,null= True)
    usuario = models.ForeignKey(UserProfile,on_delete=models.CASCADE,default = None, blank = True,null= True)
    fecha_inscripcion = models.DateTimeField(default=None, null=True,blank=True)
    implementacion = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'usuarios_inscripciones'

    def __str__(self):
        return "Usuario: " + self.usuario.user.email + " Curso: " + self.curso.titulo

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

class ConfigApisMoodle(models.Model):
    nombre_moodle = models.CharField(max_length=50,null= True,blank=True)
    endpoint = models.TextField(blank=True,null= True)
    token = models.TextField(blank=True,null= True)
